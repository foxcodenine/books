<template>
  <div class="note-count">Note count: {{noteCount}}<strong></strong></div>
</template>

<script>
    export default {
        data() {
            return {
                noteCount: 0,
            }
        },

        created() {
            EventBus.$on('update-count', (e) => this.noteCount = e)
        }
    }

</script>

<style>

</style>