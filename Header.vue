<template>
    <div id="navbar">
        <router-link to="/" id="logo-url">
            <img src="../assets/favicon.png" id="logo">
        </router-link>
        <div id="buttons">
            <router-link to="/login"><button id="login">Log in</button></router-link>
            <router-link to="/signup"><button id="signup">Sign up</button></router-link>
        </div>
    </div>
</template>

<script>
    export default{
        name: "Header"
    }
</script>

<style scoped>

* {
    font-family: 'Roboto';
    padding: 0;
    margin: 0;
    box-sizing: border-box;
    background-color: #1245A8;
  }

#navbar{
    padding: 15px 50px;
    display: flex;
    justify-content: flex-end;
    align-items: center;
}

#logo-url{
    margin: auto;
    margin-left: 0;
}

#logo{
    height: 50px;
    width: 60px;
}

#signup{
    background-color: transparent;
    border: 0.5px solid #fff;
}

#login{
    background-color: transparent;
}

button{
    color: #fff;
    font-size: 18px;
    height: 40px;
    width: 100px;
    margin: 12px;
    border: none;
    border-radius: 100px;
    cursor: pointer;
}

#signup:hover{
    background-color: #113781;
    cursor: pointer;
}

#login:hover{
    background-color: #113781;
}

@media screen and (max-width: 767px){
    
    #navbar{
        padding: 15px 50px;
        display: flex;
        justify-content: flex-end;
        align-items: center;
    }

    #logo-url{
        margin: auto;
        margin-left: 0;
    }

    #logo{
        height: 45px;
        width: 55px;
    }

    #signin{
        background-color: transparent;
        border: 0.5px solid #fff;
    }

    #login{
        background-color: transparent;
    }

    button{
        color: #fff;
        font-size: 14px;
        height: 35px;
        width: 95px;
        margin: 8px;
        border: none;
        border-radius: 95px;
        cursor: pointer;
    }
}
</style>
