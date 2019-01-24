Vue.component("cover", {
    props: ["init"],
    template: '<img :src="info.data.items[0].volumeInfo.imageLinks.thumbnail">',
    data: function(){
        return {
            info:null,
        };
    },
    mounted() {
        axios
            .get('https://www.googleapis.com/books/v1/volumes?q='+this.init)
            .then(response => {this.info = response})
    },
});

new Vue({
    el: "#app",
    delimiters: ['[[', ']]'],
});