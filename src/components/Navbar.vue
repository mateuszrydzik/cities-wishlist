<template>
    <v-app-bar>
        <v-toolbar-title>{{ title }}</v-toolbar-title>
    </v-app-bar>
</template>

<script>
export default{
    name: 'Navbar',
    props: {
        title: String
    }
}
</script>
