new Vue({
    el: '#app',
    data: {
        submissions: Seed.submissions
    },
    computed: {
        sortedSubmissions: function(){
            return this.submissions.sort(function(a, b){
                return b.votes - a.votes
            })
        }
    },
    methods: {
        upvote: function(id){
            
            const mySubmition = this.submissions.find(function(sub) {
                return sub.id === id;
            });
            
            mySubmition.votes++;
        },
        testVue: function() {
            console.log(this.submissions);
        }

    }
});