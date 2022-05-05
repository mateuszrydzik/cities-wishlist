<template>
    <div id="app">
        <div class="navbar">
             <Navbar :title="title"/>          
        </div>
        <div class="map">
            <MapContainer />
        </div>
        <div class="bt">
            <ButtonAddCity />
        </div>
    </div>
</template>

<script>
import Navbar from './components/Navbar.vue'
import ButtonAddCity from './components/ButtonAddCity.vue'
import MapContainer from './components/MapContainer.vue'

export default {
    name: 'App',
    components: {
        Navbar,
        ButtonAddCity,
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

<style>
html, body {
    height: 100%;
    margin: 0;
}
#app {
    font-family:'Trebuchet MS', 'Lucida Sans Unicode', 'Lucida Grande', 'Lucida Sans', Arial, sans-serif;
    height: 100%;
    width: 100%;
    top: 0;
    left: 0;
}
.navbar {
    width: 100%;
    height: 60px;
    color: white;
    background-color: green;
    font-size: larger
}
.bt {
    position: fixed;
    right: 5%;
    bottom: 5%;
    z-index: 1;
}
.map {
    width: 100%;
    height: calc(100% - 60px);
    position:fixed;
}
</style>