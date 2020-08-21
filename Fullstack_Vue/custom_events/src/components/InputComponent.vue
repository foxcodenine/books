<template>
    <input 
        class="input is-small" 
        type="text" 
        :placeholder="placeholder" 
        v-model="input"
        @keyup.enter="monitorEnterKey()"
    />
</template>

<script>
    
    
    export default {
        props: ['placeholder'],

        data(){
            return {
                input: '',
                count: 0
            }
        },

        methods: {
            monitorEnterKey() {

                this.$emit('add-note', {
                    note: this.input,
                    timestamp: new Date().toLocaleString()
                });
                this.input = '';

                this.count++
                EventBus.updateCount(this.count);
            }
        },
    }
</script>

<style>

</style>