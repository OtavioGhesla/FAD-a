<template>
  <div id="history-page">
    <Sidebar />
    <div class="container">
      <h1>Histórico</h1>
      
      <div class="buttons">
        <button @click="fetchDockerfileHistory">Histórico de Dockerfiles</button>
        <button @click="fetchDockerComposeHistory">Histórico de Docker Compose</button>
      </div>
      
      <div v-if="loading">Carregando histórico...</div>
      <div v-else-if="error" class="error">{{ error }}</div>
      
      <div v-if="showDockerfileHistory">
        <h2>Histórico de Dockerfiles</h2>
        <div v-if="dockerfileHistory.length > 0">
          <div
            v-for="(dockerfile, index) in dockerfileHistory"
            :key="dockerfile._id"
            class="dockerfile-card"
          >
            <h3>Dockerfile #{{ index + 1 }}</h3>
            
            <p v-if="dockerfile.base_image"><strong>Imagem Base:</strong> {{ dockerfile.base_image }}</p>
            <p v-if="dockerfile.framework"><strong>Framework:</strong> {{ dockerfile.framework }}</p>
            <p v-if="dockerfile.dependencies"><strong>Dependências:</strong> {{ dockerfile.dependencies }}</p>
            <p v-if="dockerfile.gpu_support"><strong>Suporte a GPU:</strong> {{ dockerfile.gpu_support ? 'Sim' : 'Não' }}</p>
            <p v-if="dockerfile.env_vars"><strong>Variáveis de Ambiente:</strong> {{ dockerfile.env_vars }}</p>
            <p v-if="dockerfile.ports"><strong>Portas:</strong> {{ dockerfile.ports }}</p>
            <p v-if="dockerfile.startup_script"><strong>Script de Inicialização:</strong> {{ dockerfile.startup_script }}</p>
            <p v-if="dockerfile.use_requirements"><strong>Usar Requirements:</strong> {{ dockerfile.use_requirements ? 'Sim' : 'Não' }}</p>
            <p v-if="dockerfile.created_at"><strong>Criado em:</strong> {{ new Date(dockerfile.created_at).toLocaleString() }}</p>

            <pre>{{ dockerfile.content }}</pre>

            <form @submit.prevent="deleteDockerfile(dockerfile._id)">
              <button type="submit" class="button-delete">Excluir</button>
            </form>
            
            <form @submit.prevent="createDockerfile(dockerfile)">
              <button type="submit" class="button-create">Criar Dockerfile</button>
            </form>
          </div>
        </div>
        <div v-else>
          <p>Não há histórico de Dockerfiles para este usuário.</p>
        </div>
      </div>
      
      <div v-if="showDockerComposeHistory">
        <h2>Histórico de Docker Compose</h2>
        <div v-if="dockercomposeHistory.length > 0">
          <div
            v-for="(dockercompose, index) in dockercomposeHistory"
            :key="dockercompose._id"
            class="dockerfile-card"
          >
            <h3>Docker Compose #{{ index + 1 }}</h3>
            
            <p v-if="dockercompose.service_name"><strong>Nome do Serviço:</strong> {{ dockercompose.service_name }}</p>
            <p v-if="dockercompose.base_image"><strong>Imagem Base:</strong> {{ dockercompose.base_image }}</p>
            <p v-if="dockercompose.framework"><strong>Framework:</strong> {{ dockercompose.framework }}</p>
            <p v-if="dockercompose.dependencies"><strong>Dependências:</strong> {{ dockercompose.dependencies }}</p>
            <p v-if="dockercompose.gpu_support"><strong>Suporte a GPU:</strong> {{ dockercompose.gpu_support ? 'Sim' : 'Não' }}</p>
            <p v-if="dockercompose.env_vars"><strong>Variáveis de Ambiente:</strong> {{ dockercompose.env_vars }}</p>
            <p v-if="dockercompose.ports"><strong>Portas:</strong> {{ dockercompose.ports }}</p>
            <p v-if="dockercompose.startup_script"><strong>Script de Inicialização:</strong> {{ dockercompose.startup_script }}</p>
            <p v-if="dockercompose.use_requirements"><strong>Usar Requirements:</strong> {{ dockercompose.use_requirements ? 'Sim' : 'Não' }}</p>
            <p v-if="dockercompose.created_at"><strong>Criado em:</strong> {{ new Date(dockercompose.created_at).toLocaleString() }}</p>

            <pre>{{ dockercompose.content }}</pre>

            <form @submit.prevent="deleteDockerCompose(dockercompose._id)">
              <button type="submit" class="button-delete">Excluir</button>
            </form>
            
            <form @submit.prevent="createDockerCompose(dockercompose)">
              <button type="submit" class="button-create">Criar Docker Compose</button>
            </form>
          </div>
        </div>
        <div v-else>
          <p>Não há histórico de Docker Compose para este usuário.</p>
        </div>
      </div>
      
    </div>
  </div>
</template>

<script>
import Sidebar from '../components/Sidebar.vue';
import Back from '../components/Back.vue';

export default {
  name: "History",
  components: {
    Sidebar,
    Back,
  },
  data() {
    return {
      dockerfileHistory: [],
      dockercomposeHistory: [],
      loading: true,
      error: null,
      showDockerfileHistory: false,
      showDockerComposeHistory: false,
    };
  },
  methods: {
    async fetchDockerfileHistory() {
      const token = localStorage.getItem("token");

      if (!token) {
        this.error = "Token não encontrado. Faça login novamente.";
        this.loading = false;
        return;
      }

      try {
        const response = await fetch("https://api-fad.onrender.com/dockerfileHistory", {
          method: "GET",
          headers: {
            Authorization: `Bearer ${token}`,
            "Content-Type": "application/json",
          },
        });

        if (!response.ok) {
          throw new Error("Erro ao carregar o histórico de Dockerfiles.");
        }

        const data = await response.json();
        this.dockerfileHistory = data.history || [];
        this.showDockerfileHistory = true;
        this.showDockerComposeHistory = false;
      } catch (err) {
        console.error(err);
        this.error = err.message || "Erro ao carregar o histórico de Dockerfiles.";
      } finally {
        this.loading = false;
      }
    },

    async fetchDockerComposeHistory() {
      const token = localStorage.getItem("token");

      if (!token) {
        this.error = "Token não encontrado. Faça login novamente.";
        this.loading = false;
        return;
      }

      try {
        const response = await fetch("https://api-fad.onrender.com/dockerComposeHistory", {
          method: "GET",
          headers: {
            Authorization: `Bearer ${token}`,
            "Content-Type": "application/json",
          },
        });

        if (!response.ok) {
          throw new Error("Erro ao carregar o histórico de Docker Compose.");
        }

        const data = await response.json();
        this.dockercomposeHistory = data.history || [];
        this.showDockerfileHistory = false;
        this.showDockerComposeHistory = true;
      } catch (err) {
        console.error(err);
        this.error = err.message || "Erro ao carregar o histórico de Docker Compose.";
      } finally {
        this.loading = false;
      }
    },

    async deleteDockerfile(dockerfileId) {
      const token = localStorage.getItem("token");

      if (!token) {
        this.error = "Token não encontrado. Faça login novamente.";
        return;
      }

      try {
        const response = await fetch("https://api-fad.onrender.com/dockerfileHistoryDelete", {
          method: "DELETE",
          headers: {
            Authorization: `Bearer ${token}`,
            "Content-Type": "application/json",
          },
          body: JSON.stringify({ _id: dockerfileId }),
        });

        if (!response.ok) {
          throw new Error("Erro ao excluir o Dockerfile.");
        }

        this.dockerfileHistory = this.dockerfileHistory.filter(
          (dockerfile) => dockerfile._id !== dockerfileId
        );
      } catch (err) {
        console.error(err);
        this.error = err.message || "Erro ao excluir o Dockerfile.";
      }
    },

    async deleteDockerCompose(dockercomposeId) {
      const token = localStorage.getItem("token");

      if (!token) {
        this.error = "Token não encontrado. Faça login novamente.";
        return;
      }

      try {
        const response = await fetch("https://api-fad.onrender.com/dockerComposeHistoryDelete", {
          method: "DELETE",
          headers: {
            Authorization: `Bearer ${token}`,
            "Content-Type": "application/json",
          },
          body: JSON.stringify({ _id: dockercomposeId }),
        });

        if (!response.ok) {
          throw new Error("Erro ao excluir o Docker Compose.");
        }

        this.dockercomposeHistory = this.dockercomposeHistory.filter(
          (dockercompose) => dockercompose._id !== dockercomposeId
        );
      } catch (err) {
        console.error(err);
        this.error = err.message || "Erro ao excluir o Docker Compose.";
      }
    },

    async createDockerfile(dockerfile) {
      const token = localStorage.getItem("token");

      if (!token) {
        this.error = "Token não encontrado. Faça login novamente.";
        return;
      }

      const dockerfileData = {
        title: dockerfile.base_image,
        base_image: dockerfile.base_image,
        framework: dockerfile.framework,
        dependencies: dockerfile.dependencies,
        gpu_support: dockerfile.gpu_support,
        env_vars: dockerfile.env_vars,
        ports: dockerfile.ports,
        startup_script: dockerfile.startup_script,
        use_requirements: dockerfile.use_requirements,
      };

      try {
        const response = await fetch("https://api-fad.onrender.com/createDockerfileHistory", {
          method: "POST",
          headers: {
            Authorization: `Bearer ${token}`,
            "Content-Type": "application/json",
          },
          body: JSON.stringify(dockerfileData),
        });

        if (!response.ok) {
          throw new Error("Erro ao criar o Dockerfile.");
        }

        const blob = await response.blob();
        const link = document.createElement("a");
        link.href = URL.createObjectURL(blob);
        link.download = "Dockerfile";
        link.click();
      } catch (err) {
        console.error(err);
        this.error = err.message || "Erro ao criar o Dockerfile.";
      }
    },

    async createDockerCompose(dockercompose) {
      const token = localStorage.getItem("token");

      if (!token) {
        this.error = "Token não encontrado. Faça login novamente.";
        return;
      }

      const dockercomposeData = {
        title: dockercompose.base_image,
        base_image: dockercompose.base_image,
        framework: dockercompose.framework,
        dependencies: dockercompose.dependencies,
        gpu_support: dockercompose.gpu_support,
        env_vars: dockercompose.env_vars,
        ports: dockercompose.ports,
        startup_script: dockercompose.startup_script,
        use_requirements: dockercompose.use_requirements,
      };

      try {
        const response = await fetch("https://api-fad.onrender.com/createDockerComposeHistory", {
          method: "POST",
          headers: {
            Authorization: `Bearer ${token}`,
            "Content-Type": "application/json",
          },
          body: JSON.stringify(dockercomposeData),
        });

        if (!response.ok) {
          throw new Error("Erro ao criar o Docker Compose.");
        }

        const blob = await response.blob();
        const link = document.createElement("a");
        link.href = URL.createObjectURL(blob);
        link.download = "docker-compose.yml";
        link.click();
      } catch (err) {
        console.error(err);
        this.error = err.message || "Erro ao criar o Docker Compose.";
      }
    },
  },
};
</script>

<style scoped>

.history-page{
    display: flex;
}

.container{
    width: 100%;
    padding-left: 120px;
    padding-right: 50px;
    padding-top: 2.5%;
    display: flex;
    flex-direction: column;
    gap: 30px;
    height: 1100px;
}

.dockerfile-card {
  border: 1px solid #ccc;
  padding: 1rem;
  margin-bottom: 1rem;
  border-radius: 8px;
  background-color: #f9f9f9;
}

button {
  margin-top: 10px;
  padding: 10px 20px;
  border: none;
  background-color: #1245A8;
  color: white;
  cursor: pointer;
  border-radius: 5px;
  margin: 10px;
  font-size: 16px;
}

.button-delete{
  background-color: #ff2c2c;
}

.button-create{
  background-color: #148f60;
}

.button-delete:hover{
  background-color: #ff4d4d;
}

.button-create:hover{
  background-color: #14af74;
}

button:hover {
  background-color: #0056b3;
}

p{
  color: #000;
  font-size: 18px;
}

strong{
  color: #000;
}

h1{
  color: #000;
  font-size: 26px;
}

h2{
  color: #000;
  font-size: 22px;
}

h3{
  color: #000;
  font-size: 20px;
}

@media screen and (max-width: 767px){
  .container{
      padding-left: 115px;
      padding-right: 45px;
      gap: 25px;
      height: 950px;
  }

  h1{
    font-size: 22px;
  }

  h2{
    font-size: 18px;
  }

  h3{
    font-size: 16px;
  }

  p{
    font-size: 14px;
  }

  button{
    font-size: 14px;
  }
}

</style>
