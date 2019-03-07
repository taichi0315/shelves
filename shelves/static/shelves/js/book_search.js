new Vue({
    el: "#app",
    delimiters: ['[[', ']]'],
    data: function(){
        return{
            name:'',
            books:[]
        }
    },
    methods:{
        getUrl(){
            axios
            .get('https://www.googleapis.com/books/v1/volumes?q='+this.name)
            .then(response => {this.books = response.data.items})
        }
    },
});