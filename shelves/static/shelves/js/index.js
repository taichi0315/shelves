Vue.component("cover", {
    props: ["init"],
    template: '<div><img :src="info"></div>',
    data: function(){
        return {
            info:null,
        };
    },
    mounted() {
        axios
            .get('https://www.googleapis.com/books/v1/volumes?q='+this.init)
            .then(response => {this.info = response.data.items[0].volumeInfo.imageLinks.thumbnail})
    },
});

new Vue({
    el: "#app",
    delimiters: ['[[', ']]'],
});