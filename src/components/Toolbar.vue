<template>
    <v-toolbar
    app
    dark
    color="green"
    height="60px"
    >
      <v-toolbar-title>{{ title }}</v-toolbar-title>
    </v-toolbar>
</template>

<script>
export default{
    name: 'Toolbar',
    props: {
        title: String
    }
}
</script>
