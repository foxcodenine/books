<template>

  <div id="app">
    <div class="notes-section">

      <div class="columns">

        <div class="column has-text-centered">
          <strong>Notes</strong>
          <div class="notes" v-for="(note, index) in notes" :key='index'>
            {{ note }}
          </div>
        </div>

        <div class="column has-text-centered">
          <strong>Timestamp</strong>
          <div class="timestamps" v-for="(stamp, index) in timestampes" :key='index'>
            {{ stamp }}
          </div>
        </div>

      </div>

      <app-input-component></app-input-component>      
    </div>
    <app-note-count-component></app-note-count-component>
  </div>

</template>

<script>

  import InputComponent from './components/InputComponent'
  import NoteCountComponent from "./components/NoteCountComponent";

  export default {
    name: 'app',
    components: {
      appInputComponent: InputComponent,
      appNoteCountComponent: NoteCountComponent,
    },
    computed: {
      notes() {
        return this.$store.getters.getNotes;
      },
      timestampes() {
        return this.$store.getters.getTimestamps;
      }
    }
  }

</script>

<style lang="scss">
</style>
