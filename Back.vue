<template>
    <div class="back">
        <span @click="$router.back()" class="material-symbols-outlined" id="icon">arrow_back</span>
    </div>
</template>

<script>
    export default{
        name: "Back"
    }
</script>

<style scoped>

#icon{
    color: #000;
    cursor: pointer;
}

.back{
    width: 100%;
}

</style>
