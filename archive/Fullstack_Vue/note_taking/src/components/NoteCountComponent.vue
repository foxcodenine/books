<template>
  <div class="note-count">
      Note count: <strong>{{ noteCount }}</strong>
  </div>
</template>

<script>

    export default {
        computed: {
            noteCount() {
                return this.$store.getters.getNoteCount;
            }
        }
    }
    
</script>

<style>

</style>