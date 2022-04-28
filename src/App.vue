<template>
    <div id="app">
        <div class="navbar">
             <Navbar :title="title"/>          
        </div>
        <div class="map">
            <MapContainer />
        </div>
    </div>
</template>

<script>
import Navbar from './components/Navbar.vue'
import MapContainer from './components/MapContainer.vue'

export default {
    name: 'App',
    components: {
        Navbar,
        MapContainer
    },
    data() {
        return {
            title: 'Cities Wishlist',
            date_set: 'when its done'
        }
    }
}
</script>

<style scoped>
html, body {
    height: fit-content;
    margin: 0;
}
#app {
    font-family:'Trebuchet MS', 'Lucida Sans Unicode', 'Lucida Grande', 'Lucida Sans', Arial, sans-serif;
    height: 100%;
    width: 100%;
}
.navbar {
    width: 100%;
    height: 40px;
    color: white;
    background-color: green;
    font-size: larger
}
.map {
    width: 100%;
    height: 80%;
    position:fixed;
}
</style>