<template>
  <div id="app">
    
    <app-calendar-week></app-calendar-week>
    <app-calendar-entry></app-calendar-entry>


  </div>
</template>




<script>

  import CalendarWeek from './components/CalendarWeek';
  import CalendarEntry from './components/CalendarEntry';


  export default {
    name: 'App',

    components: {
      AppCalendarWeek: CalendarWeek,
      AppCalendarEntry: CalendarEntry,
    }
  }
</script>




<style lang="scss">
html, body {
  height: 100%;
}

#app {
  height: inherit;
  background: #6e6e6e;
  display: flex;
  flex-direction: column;
  align-items: center;
  -webkit-align-items: center;
  justify-content: center;
  -webkit-justify-content: center;
}


</style>
