var app = new Vue({
    el:'#app',
    delimiters: ['[[', ']]'],
    data:{
        duration:0
    },
    computed:{
        minute: function () {
            if (this.duration<=50){
                return this.duration + "分"
            }
            else{
                return String(parseInt(this.duration / 60)) + "時間" + String(parseInt(this.duration % 60)) + "分"
            }
        }
    }
})