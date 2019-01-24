var app=new Vue({
    el: '#app',
    delimiters: ['[[', ']]'],
    data: function(){
        return {
            info:null
        }
    },
    mounted() {
        axios
            .get('https://www.googleapis.com/books/v1/volumes?q=嫌われる勇気')
            .then(response => {this.info = response})
    },
});