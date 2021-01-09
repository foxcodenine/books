<template>
  <div id="calendar-week" class="container">
      <div class="columns is-mobile">

        <app-calendary-day  v-for=" day in sharedState.seedData" 
                            v-bind:key="day.id"
                            v-bind:day="day"                            
        >  </app-calendary-day>
      </div>

    </div>
</template>


<script>

    import { store } from '../store';
    import CalendaryDay from './CalendarDay';

    export default {

        data() {
            return {
                sharedState: store.state,
            }
        },
        components: {
            AppCalendaryDay: CalendaryDay
        }
    }
</script>

<style lang="scss" scoped>

#calendar-week {
  margin-bottom: 50px;
  .column {
    padding: 0 0 0 0;
  }  
}
</style>