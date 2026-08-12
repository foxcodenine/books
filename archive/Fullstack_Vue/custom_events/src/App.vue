<template>
    <div id="app">
    <div class="notes-section">
      <div class="columns">
        <div class="column has-text-centered">
          <strong>Notes</strong>
          
          <div class="notes" v-for="(note, index) in notes" :key="index">
              {{note}}
          </div>

        </div>
        <div class="column has-text-centered">
          <strong>Timestamp</strong>

          <div class="timestamps" v-for="(stamp, index) in timestamps" :key="index">
              {{stamp}}
          </div>

        </div>
      </div>

      <app-input-component :placeholder="placeholder" @add-note="addNote($event)">        
      </app-input-component>
    
    </div>
    <app-note-count></app-note-count>
  </div>
</template>

<script>
  import InputComponent from  './components/InputComponent'
  import NoteCount from "./components/NoteCount";

  export default {

    data() {
      return {
        notes: [],
        timestamps: [],
        placeholder: 'Enter a note...'
      }
    },

    components: {
      AppInputComponent: InputComponent,
      AppNoteCount : NoteCount
    },

    methods: {
      addNote(e) {
        
        this.notes.push(e.note);
        this.timestamps.push(e.timestamp)

      }
    }
    
  }
</script>

<style lang="scss">

</style>
