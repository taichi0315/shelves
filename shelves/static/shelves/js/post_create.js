var app = new Vue({
    el:'#app',
    delimiters: ['[[', ']]'],
    data:{
        duration:600
    },
    computed:{
        minute: function () {
            if (this.duration<=3000){
                return String(parseInt(this.duration / 60)) + "分"
            }
            else{
                return String(parseInt(this.duration / 3600)) + "時間" + String(parseInt((this.duration % 3600)/60)) + "分"
            }
        }
    }
})