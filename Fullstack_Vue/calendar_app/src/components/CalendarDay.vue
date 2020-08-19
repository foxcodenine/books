<template>
  <!--  <div class="day column">
          <div class="day-banner has-text-white has-text-centered">Mon</div>
          <div class="day-details">
            <div class="day-number">1</div>
            <div class="day-event" style="background-color: rgb(153, 255, 153)">
              <div>
                <span class="has-text-centered details">Get Groceries</span> 
                <div class="has-text-centered icons"><i class="fa fa-pencil-square edit-icon"></i> 
                  <i class="fa fa-trash-o delete-icon"></i>
                </div>
              </div>
            </div>
          </div>
        </div> -->

        <div class="day column" v-on:click=" setActiveDay(day.id) ">
          <div class="day-banner has-text-white has-text-centered">{{day.abbvTitle}}</div>
          <div class="day-details">
            <div class="day-number">{{day.id}}</div>

                <app-calendar-event v-for="(event, index) in day.events" v-bind:key="index" v-bind:event="event" v-bind:day="day">

                </app-calendar-event>
          </div>
        </div>


</template>


<script>

    import CalendarEvent from './CalendarEvent'
    import { store } from '../store.js';

    export default {
        name: 'CalendarDay',
        props: ['day'],

        methods: {
          setActiveDay(dayId) {
            store.setActiveDay(dayId);
          },
        },

        components: {
            AppCalendarEvent: CalendarEvent
        }
    }
</script>




<style lang="scss" scoped>

    .day {
    background-color: #4A4A4A;
    color: #FFF;
    border-left: 1px solid #8F8F8F;
    border-bottom: 1px solid #8F8F8F;
    font-size: 12px;
    cursor: pointer;

    &:hover {
      background: darken(#4A4A4A,3%);
    }

    .day-banner {
      background-color: #333333;
      color: #FFF;
      padding: 10px;
      text-transform: uppercase;
      letter-spacing: 1px;
      font-size: 12px;
      font-weight: 600;
    }

    .day-details {
      padding: 10px;

      
    }

    &:last-child {
      border-right: 1px solid #8F8F8F;
    }
  }
</style>
