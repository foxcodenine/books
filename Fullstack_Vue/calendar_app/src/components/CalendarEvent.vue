<template>
            <div class="day-event"  :style="getEventBackgroudColor">

              <div v-if="!event.edit">
                <span class="has-text-centered details">{{ event.details }}</span> 
                <div class="has-text-centered icons">
                  <i class="fa fa-pencil-square edit-icon" v-on:click="editEvent()"></i> 
                  <i class="fa fa-trash-o delete-icon" v-on:click="deleteEvent()"></i>
                </div>
              </div>
              <div v-else>
                <span class="has-text-centered details">
                  <input type="text" v-bind:placeholder="event.details" v-model.lazy="newEventDetails">
                </span> 
                <div class="has-text-centered icons"><i class="fa fa-check" v-on:click="updateEvent()"></i></div>
              </div>

            </div>
</template>

<script>
import { store } from '../store'
    export default {
        props: ['event', 'day'],

        data() {
          return {
            newEventDetails: '',
          }
        },

        computed: {
          getEventBackgroudColor() {
            const color = ['#FF9999', '#85D6FF', '#99FF99']
            const randomColor = color[Math.floor(Math.random() * color.length)]
            return `background-color: ${randomColor};`
          }
        },

        methods: {
          editEvent() {
            store.resetAllEvent();          
            store.editEvent(this.day.id, this.event.details);
          },
          updateEvent() {

            if (!this.newEventDetails.trim()) {this.newEventDetails = this.event.details};

            store.updateEvent(this.day.id, this.event.details, this.newEventDetails);
            this.newEventDetails = '';            
          },
          deleteEvent() {
            store.deleteEvent(this.day.id, this.event.details);
          }
        }
    }
</script>





<style lang="scss" scoped>
    .day-event {
        margin-top: 6px;
        margin-bottom: 6px;
        display: block;
        color: #4C4C4C;
        padding: 5px;

        .details {
          display: block;
        }

        .icons .fa {
          padding: 0 2px;
        }

        input {
          background: none;
          border: 0;
          border-bottom: 1px solid #FFF;
          width: 100%;

          &:focus {
            outline: none;
          }
        }
      }
 
</style>