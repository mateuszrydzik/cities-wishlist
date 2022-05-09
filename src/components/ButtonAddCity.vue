<template>
    <div id="button">
        <v-container>
            <v-btn 
            icon 
            elevation="10"
            color="secondary" 
            @click="enterEditMode"> 
                {{ icon }} 
            </v-btn>
        </v-container>
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
        }
    } 
}
</script>

<style scoped>

</style>