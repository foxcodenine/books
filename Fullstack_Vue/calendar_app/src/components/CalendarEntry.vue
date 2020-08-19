<template>
    <div id="calendar-entry">
      <div class="calendar-entry-note">
        <input type="text" placeholder="New Event"  v-model.lazy="newEvent" />
        <p class="calendar-entry-day">Day of event: <span class="bold">{{ titleOfActiveDay }}</span></p>
        <a class="button is-primary is-small is-outlined" v-on:click="submitEvent()">Submit</a>

        <p class="error" v-if="error">
          You must type something first!
        </p>
      </div>
    </div>
</template>

<script>
  import { store } from '../store'
  export default {

    name: 'CalendarEntry',

    data() {
      return {
        newEvent: '',
        error: false
      }
    },

    computed: {
      titleOfActiveDay() {
        // console.log(store.getActiveDay().fullTitle)
        return store.getActiveDay().fullTitle;
      }
    },

    methods: {
      // submitEvent() {
        
      //   if (this.newEvent.trim()) {
      //     const activeDay = store.getActiveDay();
      //     activeDay.events.push({details: this.newEvent, edit: false})
      //     this.newEvent = '';
      //   }
      // }, // <- this will work also

      submitEvent() {

        if (this.newEvent.trim()) {          
          store.addEvent(this.newEvent);
          this.newEvent = '';
        } 
        else {
          this.error = true;
          setTimeout(()=>{this.error = false;}, 4000);
        }
      }
      
    },
  }

</script>



<style lang="scss" scoped>

    #calendar-entry {
  background: #FFF;
  border: 1px solid #42b883;
  border-radius: 10px;
  max-width: 300px;
  margin: 0 auto;
  padding: 20px;

  .calendar-entry-note {
    input {
      width: 200px;
      font-weight: 600;
      border: 0;
      border-bottom: 1px solid #CCC;
      font-size: 15px;
      height: 30px;
      margin-bottom: 10px;

      &:focus {
        outline: none;
      }
    }

    .calendar-entry-day {
      color: #42b883;
      font-size: 12px;
      margin-bottom: 10px;
      padding-bottom: 5px;

      .bold {
        font-weight: 600;
      }
    }

    .submit {
      display: block;
      margin: 0 auto;
    }

    .error {
      color: orangered;
      font-size: 13px;
    }
  }
}

</style>

