<template>
    <div class="signup-page">
        <div class="container">
            <form class="interface" @submit.prevent="submitForm">
                <Back />
                <h1>Faça seu sign up</h1>
                <div class="input-name">
                    <h3>Nome</h3>
                    <input class="name" type="text" placeholder="Insira seu nome de usuário" v-model="name">
                </div>
                <div v-if="errorName" class="error">
                    {{ errorName }}
                </div>
                <div v-if="errorMessage && !errorName" class="error">
                    {{ errorMessage }}
                </div>
                <div class="input-password">
                    <h3>Senha</h3>
                    <input class="password" type="password" placeholder="Insira sua senha" v-model="password">
                </div>
                <div v-if="errorPassword" class="error">
                    {{ errorPassword }}
                </div>
                <div class="input-confirm-password">
                    <h3>Confirmar senha</h3>
                    <input class="confirm-password" type="password" placeholder="Insira sua senha novamente" v-model="confirmPassword">
                </div>
                <div class="input-submit">
                    <input class="submit" type="submit" value="Fazer Sign up">
                </div>
            </form>
        </div>
    </div>
</template>

<script>
import Back from '../components/Back.vue';

export default {
    name: "Signup",
    components: {
        Back
    },
    data() {
        return {
            name: "",
            password: "",
            confirmPassword: "",
            errorName: "",
            errorPassword: "",
            errorMessage: ""
        };
    },
    methods: {
        async submitForm() {
            this.errorName = !this.name ? "Seu nome de usuário deve ter pelo menos uma letra" : "";
            this.errorPassword = !this.password ? "Sua senha deve ter pelo menos digito" : 
                                (this.password !== this.confirmPassword ? "As senhas não são as mesmas" : "");

            if (this.errorName || this.errorPassword) {
                return;
            }

            const formLoginJson = JSON.stringify({
                name: this.name,
                password: this.password
            });

            try {
                const response = await fetch('https://api-fad.onrender.com/register', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: formLoginJson
                });

                if (response.ok) {
                    const data = await response.json();
                    this.errorMessage = "";
                    this.$router.push('/login');
                } else {
                    const errorData = await response.json();
                    this.errorMessage = errorData.error || "Erro ao registrar usuário.";
                }
            } catch (error) {
                this.errorMessage = "Erro na comunicação com o servidor.";
                console.error("Erro:", error);
            }
        }
    }
}
</script>

<style scoped>

.signup-page {
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
