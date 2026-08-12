<template>
  <div>
      <input 
        placeholder='Enter a note' class="input is-small" type="text" 
        v-model="input" @keyup.enter="monitorEntryKey"/>
  </div>
</template>

<script>

  export default {
    data() {
      return {
        input: '',
      }
    },
    methods: {
      monitorEntryKey() {
        this.$store.dispatch('addNote', this.input);
        this.$store.dispatch('addTimestamp', new Date().toLocaleString());
        this.input = '';
      }
    }
  }
</script>

<style>

</style>