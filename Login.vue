<template>
  <div class="login-page">
      <div class="container">
          <form class="interface" @submit.prevent="submitForm">
              <Back />
              <h1>Faça seu log in</h1>
              <div class="input-name">
                  <h3>Nome</h3>
                  <input class="name" type="text" placeholder="Insira seu nome de usuário" v-model="name">
              </div>
              <div v-if="errorName" class="error">
                  {{ errorName }}
              </div>
              <div class="input-password">
                  <h3>Senha</h3>
                  <input class="password" type="password" placeholder="Insira sua senha" v-model="password">
              </div>
              <div v-if="errorPassword" class="error">
                  {{ errorPassword }}
              </div>
              <div class="input-submit">
                  <input class="submit" type="submit" value="Fazer Log in">
              </div>
          </form>
      </div>
  </div>
</template>

<script>
import Back from '../components/Back.vue';

export default {
  name: "Login",
  components: {
    Back
  },
  data() {
    return {
      name: "",
      password: "",
      errorName: "",
      errorPassword: "",
      apiError: "",
    };
  },
  methods: {
    async submitForm() {
      this.errorName = !this.name ? "Seu nome de usuário deve ter pelo menos uma letra" : "";
      this.errorPassword = !this.password ? "Senha é obrigatória" : "";

      if (this.errorName || this.errorPassword) {
        return;
      }

      try {
        const response = await fetch('https://api-fad.onrender.com/login', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({
            name: this.name,
            password: this.password
          })
        });

        if (!response.ok) {
          const errorData = await response.json();
          throw new Error(errorData.error || "Erro ao fazer login");
        }

        const responseData = await response.json();
        console.log("Resposta da API:", responseData);

        localStorage.setItem('token', responseData.token);
        this.$router.push('/overview');
      } catch (error) {
        console.error("Erro na requisição:", error.message);
        this.apiError = error.message || "Erro ao fazer login. Tente novamente.";
      }
    }
  }
}
</script>

<style scoped>

.login-page {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  background-color: #f5f5f5;
}

.container {
  width: 100%;
  max-width: 400px;
  padding: 20px;
  background: #fff;
  border-radius: 8px;
}

.interface {
  display: flex;
  flex-direction: column;
  gap: 20px;
}

h1 {
  font-size: 24px;
  text-align: center;
  color: #000;
  margin-bottom: 20px;
}

h3 {
  font-size: 16px;
  color: #000;
  margin-bottom: 5px;
}

::placeholder{
    color: #111;
    font-size: 16px;
}

input[type="text"],
input[type="password"] {
  width: 100%;
  padding: 10px;
  font-size: 16px;
  border: 1px solid #ccc;
  border-radius: 18px;
  box-sizing: border-box;
  color: #000;
}

input[type="text"]:focus,
input[type="password"]:focus {
  outline: none;
  border-color: #1245A8;
}

.submit {
  width: 100%;
  padding: 12px;
  background-color: #1245A8;
  color: #fff;
  font-size: 16px;
  font-weight: bold;
  border: none;
  border-radius: 18px;
  cursor: pointer;
  transition: background-color 0.0s;
}

.submit:hover {
  background-color: #2662db;
}

.error {
  color: #ff2c2c;
  font-size: 14px;
}

@media (max-width: 768px) {
  .container {
    margin: 20px;
    padding: 15px;
  }

  h1 {
    font-size: 20px;
  }

  h3 {
    font-size: 14px;
  }
}
</style>
