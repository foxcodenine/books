new Vue({
    el: '#app',
    data: {
        submissions: Seed.submissions
    },
    methods: {
        testVue: function() {
            console.log(this.submissions);
        }
    }
})