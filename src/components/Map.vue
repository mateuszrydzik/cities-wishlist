<template>
    <div id="map">
        <h2>Release date: {{date}}</h2>
        <input v-model="place">
        <button @click="pushArray">Add to list</button>
        <ul>
            <li v-for="place in placeList" :key="place.city">
                {{ place.city }}
                <button  @click="delFromArray"> X </button>
            </li>
        </ul>
    </div>
    
</template>

<script>
export default{
    name: 'Map',
    props: {
        date: String
    },
    data() {
        return {
            place: '',
            placeList: [
                {city: 'Madryt'},
                {city: 'Amsterdam'}
            ],
            placeArr: ['Poznan', 'Bialystok']
        }
    },
    methods: {
        pushList() {
            this.placeList.push({city: this.place})
        },
        pushArray() {
            this.placeArr.push(place)
        },
        logArray() {
            console.log(this.placeArr)
        },
        delFromList(place) { //usuwa ostatnie a nie to co chce sprawdz to
            this.placeList.splice(this.placeList.indexOf(place), 1);
        },
        delFromArr(place) {
            this.placeArr.splice(placeArr.indexOf(place), 1)
        }
    }
}
</script>
