<template>
    <div class="sidebar">
        <router-link to="/overview"><img class="logo" src="../assets/favicon.png"></router-link>
        <ul>
            <router-link to="/overview"><div class="icon">
                <l1><span class="material-symbols-outlined">home</span></l1>
            </div></router-link>
                <router-link to="/history"><div class="icon">
                <l1><span class="material-symbols-outlined">history</span></l1>
            </div></router-link>
        </ul>
    </div>
</template>

<script>
    export default{
        name: "Sidebar"
    }
</script>

<style scoped>

.logo{
    height: 40px;
    width: 50px;
}

.icon{
    height: 40px;
    width: 40px;
    align-items: center;
    justify-content: center;
    border-radius: 100%;    
    display: flex;
    align-items: center;
}

.icon:hover{
    background-color: #fff;
}

.icon:hover span{
    color: #1245A8;
}

.sidebar{
    display: flex;
    flex-direction: column;
    position: fixed;
    background-color: #1245A8;
    padding-top: 50px;
    width: 70px;
    height: 100vh;
    align-items: center;
    gap: 40px;
}

ul{
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 30px;
}

span{
    font-size: 30px;
}

@media screen and (max-width: 767px){

    .logo{
        height: 35px;
        width: 45px;
    }

    .icon{
        height: 35px;
        width: 35px;
    }

    .sidebar{
        padding-top: 45px;
        width: 60px;
        height: 100vh;
        gap: 35px;
    }

    ul{
        gap: 25px;
    }

    span{
        font-size: 25px;
    }

}

</style>
