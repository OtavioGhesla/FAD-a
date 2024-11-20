<template>
  <body>
    <div class="home-page">
      <Header />
      <div class="container">
        <h1>Seja bem-vindo ao FAD!</h1>
      </div>
      <div class="content">
        <h2>O que é o FAD?</h2>
        <p>O FAD é uma ferramenta que serve como uma interface para criação de dockerfiles voltados a modelos de inteligência artificial. Aqui está uma lista de imagens base que o FAD oferece para facilitar a criação do seu modelo de inteligência artificial!</p>
        <h2>Lista de imagens base disponíveis: </h2>
        <div class="base-images">
          <div class="top">
            <img class="icon" src="../assets/img/python-icon.svg">
            <span class="icon-p">Python</span>
          </div>
          <div class="mid">
            <img class="icon" src="../assets/img/ubuntu-icon.svg">
            <span class="icon-p">Ubuntu</span>
          </div>
          <div class="mid">
            <img class="icon" src="../assets/img/debian-icon.svg">
            <span class="icon-p">Debian</span>
          </div>
          <div class="bottom">
            <img class="icon" src="../assets/img/nvidia-icon.svg">
            <span class="icon-p">Nvidia CUDA</span>
          </div>
        </div>
      </div>
    </div>
  </body>
</template>

<style scoped>

.container{
  padding: 5%;
  height: 800px;
  background-color: #1245A8;
  border-radius: 0 0 50px 50px;
}

.content{
  padding-top: 20px;
  padding: 5%;
}

.icon{
  height: 50px;
  width: 50px;
}

.top{
  margin-top: 40px;
  height: 80px;
  width: 100%;
  background-color: #1245A8;
  border-radius: 50px 50px 0 0;
  padding-left: 2%;
  padding-right: 2%;
  border-bottom: 2px solid;
  border-color: #fff;
  display: flex;
  align-items: center;
}

.mid{
  height: 80px;
  width: 100%;
  background-color: #1245A8;
  padding-left: 2%;
  padding-right: 2%;
  border-bottom: 2px solid;
  border-color: #fff;
  display: flex;
  align-items: center;
}

.bottom{
  height: 80px;
  width: 100%;
  background-color: #1245A8;
  border-radius: 0 0 50px 50px;
  padding-left: 2%;
  padding-right: 2%;
  display: flex;
  align-items: center;
}

.top:hover{
    background-color: #2662db;
}

.mid:hover{
    background-color: #2662db;
}

.bottom:hover{
    background-color: #2662db;
}

.icon-p{
  color: #fff;
  margin-left: 2.5%;
  font-size: 18px;
}

p{
  padding-top: 40px;
  font-size: 18px;
  color: #111;
}

h2{
  font-size: 22px;
  color: #000;
  padding-top: 40px;
}

h1{
  text-align: center;
  font-size: 40px;
  margin-bottom: 300px;
  color: #fff;
}

@media screen and (max-width: 767px){
  .container{
    padding: 5%;
    height: 600px;
    background-color: #1245A8;
    border-radius: 0 0 40px 40px;
  }

  .content{
    padding-top: 20px;
    padding: 5%;
  }

  .icon{
    height: 40px;
    width: 40px;
  }

  .top{
    margin-top: 35px;
    height: 75px;
    width: 100%;
    background-color: #1245A8;
    border-radius: 40px 40px 0 0;
    padding-left: 2%;
    padding-right: 2%;
    border-bottom: 1px solid;
    border-color: #fff;
    display: flex;
    align-items: center;
  }

  .mid{
    height: 75px;
    width: 100%;
    background-color: #1245A8;
    padding-left: 2%;
    padding-right: 2%;
    border-bottom: 1px solid;
    border-color: #fff;
    display: flex;
    align-items: center;
  }

  .bottom{
    height: 75px;
    width: 100%;
    background-color: #1245A8;
    border-radius: 0 0 40px 40px;
    padding-left: 2%;
    padding-right: 1%;
    display: flex;
    align-items: center;
  }

  .icon-p{
    color: #fff;
    margin-left: 2.5%;
    font-size: 14px;
  }

  p{
    padding-top: 40px;
    font-size: 14px;
    color: #111;
  }

  h2{
    font-size: 18px;
    color: #000;
    padding-top: 40px;
  }

  h1{
    text-align: center;
    font-size: 35px;
    margin-bottom: 250px;
    color: #fff;
  }
}

</style>

<script>
import Header from '../components/Header.vue';

export default{
  name: "Home",
  components: {
    Header
  }
}

</script>
