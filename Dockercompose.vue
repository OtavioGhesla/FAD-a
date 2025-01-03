<template>
    <div class="dockercompose-page">
        <Sidebar />
        <div class="container">
            <Back />
            <form class="interface" @submit.prevent="submitForm">
                <h1>Crie seu arquivo docker-compose.yml</h1>
                <h2>Escolha o nome do serviço</h2>
                <div class="input-service">
                    <input 
                        class="service" 
                        type="text" 
                        placeholder="Insira o nome do serviço" 
                        v-model="service" 
                    />
                    <div v-if="errorService" class="error-message">
                        {{ errorService }}
                    </div>
                </div>
                <div class="checkbox">
                    <input type="checkbox" id="gpuCheckbox" v-model="gpuSupport" />
                    <label class="labelCheckbox" for="gpuCheckbox">Você está utilizando GPU em seu modelo?</label>
                </div>
                <h2>Escolha a imagem base</h2>
                <div class="checkbox">
                    <input type="checkbox" id="gpuCheckbox" v-model="useDockerfile" />
                    <label class="labelCheckbox" for="gpuCheckbox">Deseja utilizar um Dockerfile como base para seu Docker Compose?</label>
                </div>
                <div class="input-base-image" v-if="!useDockerfile">
                    <div class="top">
                        <img class="base-logo" src="../assets/img/ubuntu-icon.svg">
                        <label for="rad4">Ubuntu</label>
                        <input type="radio" name="base-image" class="radio" id="rad2" value="ubuntu:latest" v-model="baseImage">
                    </div>
                    <div class="mid" v-if="!gpuSupport">
                        <img class="base-logo" src="../assets/img/nvidia-icon.svg">
                        <label for="rad4">Nvidia CUDA</label>
                        <input type="radio" name="base-image" class="radio" id="rad4" value="nvidia/cuda:11.8-cudnn8-devel-ubuntu20.04" v-model="baseImage">
                    </div>
                    <div class="mid" v-if="!gpuSupport">
                        <img class="base-logo" src="../assets/img/python-icon.svg">
                        <label for="rad1">Python</label>
                        <input type="radio" name="base-image" class="radio" id="rad1" value="python:latest" v-model="baseImage">
                    </div>
                    <div class="bottom">
                        <img class="base-logo" src="../assets/img/debian-icon.svg">
                        <label for="rad4">Debian</label>
                        <input type="radio" name="base-image" class="radio" id="rad3" value="debian:latest" v-model="baseImage">
                    </div>
                    <div v-if="errorImage" class="error-message">
                        {{ errorImage }}
                    </div>
                </div>
                <div class="input-context" v-if="useDockerfile">
                    <h2>Insira o diretório que você vai trabalhar</h2>
                    <input 
                        class="context" 
                        type="text" 
                        placeholder="Insira o caminho do seu Dockerfile" 
                        v-model="context"
                    />
                </div>
                <div class="input-workdir" v-if="!useDockerfile">
                    <h2>Insira o diretório que você vai trabalhar</h2>
                    <input 
                        class="workdir" 
                        type="text" 
                        placeholder="Insira o local do diretório (Exemplo: /app)" 
                        v-model="workdir" 
                    />
                </div>
                <h2>Insira as váriaveis de ambiente</h2>
                <div class="input-env">
                    <input 
                        class="envVars" 
                        type="text" 
                        placeholder="Insira as váriaveis de ambiente (Exemplo: MY_ENV_VAR=value1,ANOTHER_VAR=value2)" 
                        v-model="envVars" 
                    />
                </div>
                <h2>Insira a porta que seu modelo vai rodar</h2>
                <div class="input-ports">
                    <input 
                        class="ports" 
                        type="text" 
                        placeholder="Insira a porta que o container vai rodar (Exemplo: 8080:8080)" 
                        v-model="ports" 
                    />
                </div>
                <h2>Insira o comando para rodar seu modelo</h2>
                <div class="input-startup-script">
                    <input 
                        class="startupScript" 
                        type="text" 
                        placeholder="Insira o comando que vai rodar sua aplicação (Exemplo: python3 app.py)" 
                        v-model="startupScript" 
                    />
                </div>
                <div class="input-submit">
                    <input class="submit" type="submit" value="Criar arquivo docker-compose.yml">
                </div>
            </form>
        </div>
    </div>
</template>

<script>
import Sidebar from '../components/Sidebar.vue';
import Back from '../components/Back.vue';

export default{
  name: "Dockercompose",
  components: {
    Sidebar,
    Back
  },
  data(){
    return{
        service: "",
        baseImage: "",
        workdir: "",
        errorService: "",
        errorImage: "",
        gpuSupport: false,
        useDockerfile: false,
        context: "",
        envVars: "",
        ports: "",
        startupScript: ""
    };
  },
  methods: {
    async submitForm() {
        const token = localStorage.getItem('token');

        const dockerComposeData = {
            service: this.service,
            baseImage: this.baseImage,
            workdir: this.workdir,
            gpuSupport: this.gpuSupport,
            envVars: this.envVars,
            ports: this.ports,
            startupScript: this.startupScript,
            useDockerfile: this.useDockerfile,
            context: this.context
        };

        fetch('https://api-fad.onrender.com/createDockerCompose', {
            method: 'POST',
            headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${token}`
            },
            body: JSON.stringify(dockerComposeData)
        })
        .then(response => response.blob())
        .then(blob => {
            const link = document.createElement('a');
            link.href = URL.createObjectURL(blob);
            link.download = 'docker-compose.yml';
            link.click();
        })
        .catch(error => {
            console.error('Erro ao criar o docker-compose.yml:', error);
        });
        }
  },
}
</script>

<style scoped>

.dockercompose-page{
    display: flex;
}

h1{
    color: #000;
    font-size: 26px;
}

h2{
    color: #000;
    font-size: 22px;
    margin-top: 30px;
}

.error-message{
    color: #ff2c2c;
    width: 100%;
    font-size: 16px;
    text-align: center;
    margin-top: 15px;
}

::placeholder{
    color: #e7e7e7;
}

label{
    font-size: 18px;
}

.labelCheckbox{
    font-size: 18px;
    color: #000;
}

input[type=radio], input[type=flexbox]{
    transform: scale(1.5);
    float: right;
    margin-left: auto;
}

input[type=checkbox]{
    transform: scale(1.5);
    float: left;
    margin-right: auto;
}

input[type=text]{
    background-color: #1245A8;
    border: none;
    outline: none;
    width: 100%;
    height: 70px;
    border-radius: 50px;
    padding-left: 2.5%;
    padding-right: 2.5%;
    font-size: 18px;
    margin-top: 30px;
}

.submit{
    background-color: #148f60;
    border: none;
    outline: none;
    width: 100%;
    height: 70px;
    border-radius: 50px;
    font-size: 18px;
    margin-top: 80px;
    margin-bottom: 80px;
    cursor: pointer;
}

.submit:hover{
    background-color: #14af74;
}

.input-requeriments{
    margin-top: 60px;
}

.base-logo{
    height: 50px;
    width: 50px;
    margin-right: 5%;
}

.interface{
    width: 100%;
    height: 100%;
}

.container{
    width: 100%;
    padding-left: 120px;
    padding-right: 50px;
    padding-top: 2.5%;
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 30px;
    height: 1100px;
}

.top{
    margin-top: 20px;
    width: 100%;
    height: 80px;
    background-color: #1245A8;
    border-radius: 50px 50px 0 0;
    border-bottom: 2px solid #fff;
    display: flex;
    justify-content: flex-start;
    align-items: center;
    padding-left: 2.5%;
    padding-right: 2.5%;
}

.mid{
    width: 100%;
    height: 80px;
    background-color: #1245A8;
    border-bottom: 2px solid #fff;
    display: flex;
    justify-content: flex-start;
    align-items: center;
    padding-left: 2.5%;
    padding-right: 2.5%;
}

.unique{
    margin-top: 20px;
    width: 100%;
    height: 80px;
    background-color: #1245A8;
    border-radius: 50px;
    display: flex;
    justify-content: flex-start;
    align-items: center;
    padding-left: 2.5%;
    padding-right: 2.5%;
}

.checkbox{
    border: 2px solid #1245A8;
    border-radius: 50px;
    margin-top: 20px;
    width: 100%;
    height: 70px;
    padding-left: 2.5%;
    padding-right: 2.5%;
    display: flex;
    justify-content: flex-start;
    align-items: center;
}

.top:hover{
    background-color: #2662db;
}

.mid:hover{
    background-color: #2662db;
}

.unique:hover{
    background-color: #2662db;
}

.bottom:hover{
    background-color: #2662db;
}

.bottom{
    width: 100%;
    height: 80px;
    background-color: #1245A8;
    border-radius: 0 0 50px 50px;
    display: flex;
    justify-content: flex-start;
    align-items: center;
    padding-left: 2.5%;
    padding-right: 2.5%;
}

@media screen and (max-width: 767px){
    h1{
        font-size: 22px;
    }

    h2{
        color: #000;
        font-size: 18px;
        margin-top: 25px;
    }

    .error-message{
        color: #ff2c2c;
        font-size: 12px;
        margin-top: 10px;
    }

    label{
        font-size: 14px;
    }

    .labelCheckbox{
        font-size: 14px;
    }

    input[type=radio], input[type=flexbox]{
        transform: scale(1);
        float: right;
        margin-left: auto;
    }

    input[type=checkbox]{
        transform: scale(1);
        float: left;
        margin-right: auto;
    }

    input[type=text]{
        height: 65px;
        border-radius: 35px;
        padding-left: 5%;
        padding-right: 5%;
        font-size: 14px;
        margin-top: 25px;
    }

    .submit{
        height: 65px;
        border-radius: 35px;
        font-size: 14px;
        margin-top: 75px;
        cursor: pointer;
    }

    .input-requeriments{
        margin-top: 55px;
    }

    .base-logo{
        height: 35px;
        width: 35px;
    }

    .container{
        padding-left: 115px;
        padding-right: 45px;
        gap: 25px;
        height: 950px;
    }

    .sidebar{
        padding-top: 45px;
        width: 60px;
        height: 100vh;
        gap: 35px;
    }

    .top{
        margin-top: 15px;
        height: 75px;
        border-radius: 35px 35px 0 0;
    }

    .mid{
        height: 75px;
    }

    .bottom{
        height: 75px;
        border-radius: 0 0 35px 35px;
    }

    .checkbox{
        border-radius: 35px;
        margin-top: 20px;
        height: 65px;
    }
}

</style>
