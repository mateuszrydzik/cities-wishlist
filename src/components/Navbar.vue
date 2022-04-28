<template>
    <div id="navbar">
        {{ title }}
    </div>
</template>

<script>
export default{
    name: 'Navbar',
    props: {
        title: String
    }
}
</script>
