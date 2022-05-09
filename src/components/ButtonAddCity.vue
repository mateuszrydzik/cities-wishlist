<template>
    <div id="button">
        <button @click="enterEditMode">{{icon}}</button>
    </div>
</template>

<script>
export default{
    name: 'ButtonAddCity',
    data() {
        return {
            editModeIsActive: false,
            icon: '+'
        }
    },
    methods: {
        enterEditMode() {
            this.editModeIsActive = !this.editModeIsActive;
            this.icon = this.editModeIsActive ? 'edit' : '+';
            if (this.editModeIsActive === true) {
                this.icon = 'edit'
            } else {
                this.icon = '+'
            }
        }
    } 
}
</script>

<style>
button {
  background-color: green;
  font-size: 30px;
  border: none;
  color: white;
  cursor: pointer;
  height: 75px;
  width: 75px;
  border-radius: 50%;
}
</style>