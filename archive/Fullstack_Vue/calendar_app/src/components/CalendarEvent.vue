<template>
            <div class="day-event"  :style="getEventBackgroudColor">
              <div>
                <span class="has-text-centered details">{{ event.details }}</span> 
                <div class="has-text-centered icons"><i class="fa fa-pencil-square edit-icon"></i> 
                  <i class="fa fa-trash-o delete-icon"></i>
                </div>
              </div>
            </div>
</template>

<script>
    export default {
        props: ['event', 'day'],
        computed: {
          getEventBackgroudColor() {
            const color = ['#FF9999', '#85D6FF', '#99FF99']
            const randomColor = color[Math.floor(Math.random() * color.length)]
            return `background-color: ${randomColor};`
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