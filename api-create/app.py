from flask import Flask, jsonify, request, send_file, after_this_request
from flask_pymongo import MongoClient
from flask_cors import CORS
from werkzeug.security import generate_password_hash
import io
import yaml

app = Flask(__name__)
CORS(app)

app.config["MONGO_URI"] = "mongodb+srv://otaviofetterg:XK3vyzB91lTOPrTS@fad.vikvn.mongodb.net/fad?retryWrites=true&w=majority&appName=fad"

# Testa a conexão com o banco MongoDB
try:
    client = MongoClient(app.config["MONGO_URI"])
    mongo = client["fad"]
    print("Conectado ao banco MongoDB")
except Exception as e:
    print(f"Erro ao conectar ao MongoDB: {e}")

@app.route('/createDockerfile', methods=['POST'])
def createDockerfile():
    form_dockerfile = request.get_json()

    # Recebe os valores do JSON
    base_image = form_dockerfile.get('baseImage')
    framework = form_dockerfile.get('framework', '').strip()
    dependencies = form_dockerfile.get('dependencies', '').strip()
    gpu_support = form_dockerfile.get('gpuSupport', False)
    env_vars = form_dockerfile.get('envVars', '').strip()
    ports = form_dockerfile.get('ports', '').strip()
    startup_script = form_dockerfile.get('startupScript', '').strip()
    use_requirements = form_dockerfile.get('useRequirements', False)

    # Função auxiliar para adicionar variáveis de ambiente
    def add_env_vars(env_vars):
        return "\n".join([f"ENV {env.strip()}" for env in env_vars.split(',') if env.strip()])

    # Função auxiliar para expor portas
    def add_ports(ports):
        return "\n".join([f"EXPOSE {port.strip()}" for port in ports.split(',') if port.strip()])

    # Inicia o conteúdo do Dockerfile
    dockerfile_content = f"# Dockerfile Gerado\n\nFROM {base_image}\n\n"

    # Instalação do framework de IA, se necessário
    if framework:
        dockerfile_content += f"# Instalar framework de IA\nRUN pip install {framework}\n\n"

    # Instalação de dependências adicionais, se houver
    if dependencies:
        dockerfile_content += f"# Instalar dependências adicionais\nRUN pip install {dependencies}\n\n"

    # Instalação de dependências a partir do requirements.txt, se especificado
    if use_requirements:
        dockerfile_content += "COPY requirements.txt .\n\nRUN pip install --no-cache-dir -r requirements.txt\n\n"

    # Suporte para GPU
    if gpu_support and "cuda" in base_image:
        dockerfile_content += "RUN apt-get update && apt-get install -y cuda\n\n"

    # Variáveis de ambiente
    if env_vars:
        dockerfile_content += "# Variáveis de Ambiente\n" + add_env_vars(env_vars) + "\n\n"

    # Exposição de portas
    if ports:
        dockerfile_content += "# Expor portas\n" + add_ports(ports) + "\n\n"

    # Script de inicialização
    if startup_script:
        # Divide o script de inicialização em uma lista de strings para o CMD, usando aspas duplas
        startup_command = '["' + '", "'.join(startup_script.split()) + '"]'
        dockerfile_content += f'CMD {startup_command}\n'
    
    # Usar o contexto de memória para gerar o Dockerfile sem criar arquivos temporários no disco
    dockerfile_bytes = io.BytesIO(dockerfile_content.encode('utf-8'))

    # Enviar o arquivo para o usuário baixar sem necessidade de apagar arquivos temporários
    return send_file(dockerfile_bytes, as_attachment=True, download_name="Dockerfile", mimetype="text/plain")

@app.route('/createDockerCompose', methods=['POST'])
def createDockerCompose():
    form_dockercompose = request.get_json()

    # Recebe os valores do JSON
    service_name = form_dockercompose.get('service')
    base_image = form_dockercompose.get('baseImage')
    framework = form_dockercompose.get('framework', '').strip()
    dependencies = form_dockercompose.get('dependencies', '').strip()
    gpu_support = form_dockercompose.get('gpuSupport', False)
    env_vars = form_dockercompose.get('envVars', '').strip()
    ports = form_dockercompose.get('ports', '').strip()
    startup_script = form_dockercompose.get('startupScript', '').strip()
    use_requirements = form_dockercompose.get('useRequirements', False)

    # Função auxiliar para configurar variáveis de ambiente
    def add_env_vars(env_vars):
        return {env.split('=')[0].strip(): env.split('=')[1].strip() for env in env_vars.split(',') if '=' in env}

    # Função auxiliar para configurar portas
    def add_ports(ports):
        return [port.strip() for port in ports.split(',') if port.strip()]

    # Cria o conteúdo do docker-compose.yml
    docker_compose_content = {
        'version': '3.8',
        'services': {
            service_name: {
                'image': base_image
            }
        }
    }

    # Adiciona as configurações apenas se houverem valores válidos
    if ports:
        docker_compose_content['services'][service_name]['ports'] = add_ports(ports)
    if env_vars:
        docker_compose_content['services'][service_name]['environment'] = add_env_vars(env_vars)
    if startup_script:
        docker_compose_content['services'][service_name]['command'] = startup_script.split()

    # Adiciona a seção de build apenas se for necessário
    if framework or dependencies or use_requirements:
        docker_compose_content['services'][service_name]['build'] = {
            'context': '.',
            'dockerfile': 'Dockerfile'
        }
        if use_requirements:
            docker_compose_content['services'][service_name].setdefault('volumes', []).append('./requirements.txt:/app/requirements.txt')

    # Adiciona suporte a GPU apenas se necessário
    if gpu_support:
        docker_compose_content['services'][service_name]['runtime'] = 'nvidia'

    # Gera o arquivo docker-compose.yml em memória
    docker_compose_yaml = yaml.dump(docker_compose_content, default_flow_style=False)
    docker_compose_bytes = io.BytesIO(docker_compose_yaml.encode('utf-8'))

    # Envia o arquivo para download
    return send_file(docker_compose_bytes, as_attachment=True, download_name="docker-compose.yml", mimetype="text/plain")

@app.route('/register', methods=['POST'])
def register_user():
    # Recebe os valores do JSON
    data = request.get_json()
    name = data.get("name")
    password = data.get("password")

    # Procura se já existe um usuário com o mesmo nome cadastrado
    if mongo["user"].find_one({"name": name}):
        return jsonify({"error": "Esse nome de usuário já está cadastrado"}), 409

    # Criptografa a senha
    hashed_password = generate_password_hash(password)

    # Salva o usuário e a senha criptografada no banco
    user_id = mongo["user"].insert_one({
        "name": name,
        "password": hashed_password
    }).inserted_id

    return jsonify({"message": "Usuário cadastrado com sucesso", "user_id": str(user_id)}), 201

if __name__ == '__main__':
    app.run(port=5000, debug=True)
