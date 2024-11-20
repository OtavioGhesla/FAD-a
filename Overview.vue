<template>
    <div class="overview-page">
        <Sidebar />
        <div class="container">
            <h1>O que deseja criar hoje?</h1>
            <div class="options">
                <div class="option">
                    <div class="content">
                        <h2>Dockerfile</h2>
                        <span>Crie instruções para criar suas imagens docker!</span>
                        <router-link to="/overview/dockerfile"><input class="submit" type="submit" value="Criar Dockerfile"></router-link>
                    </div>
                </div>
                <div class="option">
                    <div class="content">
                        <h2>Compose</h2>
                        <span>Crie instruções para orquestrar seus containers!</span>
                        <router-link to="/overview/dockercompose"><input class="submit" type="submit" value="Criar Compose"></router-link>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import Sidebar from '../components/Sidebar.vue';

export default{
  name: "Overview",
  components: {
    Sidebar
  }
}
</script>


<style scoped>

h1{
    color: #000;
    font-size: 22px;
}

h2{
    color: #000;
    font-size: 20px;
    margin-bottom: 30px;
}

span{
    color: #000;
    font-size: 18px;
    margin-bottom: 20px;
}

input[type=submit]{
    background-color: #1245A8;
    border: none;
    outline: none;
    width: 100%;
    height: 50px;
    border-radius: 50px;
    padding-left: 2.5%;
    padding-right: 2.5%;
    font-size: 18px;
    margin-top: 30px;
}

input[type=submit]:hover{
    background-color: #2662db;
    cursor: pointer;
}

.icon{
    height: 150px;
    width: 160px;
    margin: 30px;
}

.content{
    width: 100%;
    display: flex;
    flex-direction: column;
}

.options{
    width: 100%;
    height: 80px;
}

.option{
    border: 1px solid #ccc;
    padding: 1rem;
    margin-bottom: 8rem;
    border-radius: 8px;
    background-color: #f9f9f9;
}

.container{
    width: 100%;
    padding-left: 120px;
    padding-right: 50px;
    padding-top: 2.5%;
    display: flex;
    flex-direction: column;
    gap: 30px;
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
    margin-bottom: 25px;
  }

  h3{
    font-size: 16px;
  }

  span{
    font-size: 14px;
  }

  input[type=submit]{
    height: 40px;
    border-radius: 50px;
    font-size: 14px;
    margin-top: 25px;
  }
}

</style>
