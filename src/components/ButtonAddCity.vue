<template>
    <div id="button">
        <button @click="logMessage">+</button>
    </div>
</template>

<script>
export default{
    name: 'ButtonAddCity',
    methods: {
        logMessage() {
            console.log('Gratulacje uzytkowniku')
        }
    }
}
</script>

<style scoped>
button {
  background-color: #4CAF50;
  font-size: 30px;
  border: none;
  color: white;
  cursor: pointer;
  height: 75px;
  width: 75px;
  border-radius: 50%;
}
</style>