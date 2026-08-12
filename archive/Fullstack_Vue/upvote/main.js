
``
const submissionComponent = {
    template: 
    `<div style="display: flex; width: 100%">
        <figure class="media-left">
            <img src="./public/images/submissions/image-yellow.png" class="image is-64x64"v-bind:src='submission.submissionImage'>
        </figure>
        <div class="media-content">
            <div class="content">
                <p>
                    <strong>
                        <a href="#" class="has-text-info" v-bind:href='submission.url'>Yellow Pail</a>
                        <span class="tag is-small">#{{ submission.id }}</span>
                    </strong>
                    <br>
                    On-demand sand castle construction expertise.
                    <br>
                    <small class="is-size-7">
                        Submitted by:
                        <img src="./public/images/avatars/daniel.jpg" class="image is-24x24" v-bind:src='submission.avatar'>
                    </small>
                </p>
            </div>
        </div>
        <div class="media-right">
            <span class="icon is-small" v-on:click='upvote(submission.id)'>
                <i class="fa fa-chevron-up">
                    <strong class="has-text-info">{{ submission.votes }}</strong>
                </i>
            </span>
        </div>
    </div>`,
    props: {
        submission: Object,
        submissions: Array
    },
    methods: {
        upvote: function(id){
            
            const mySubmition = this.submissions.find(function(sub) {
                return sub.id === id;
            });
            
            mySubmition.votes++;
        }
    },
}



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

        testVue: function() {
            console.log(this.submissions);
        }
    },
    components: {
        'submission-component': submissionComponent
    },
});