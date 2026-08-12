
* Array.prototype.sort()
https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/sort


* Array.prototype.find()
https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/find

* Vue Event Handling 
https://vuejs.org/v2/guide/events.html


<hr>

#####Use vm.$on to listen to event

    # If you are using single file components.

    window.bus = new Vue({});

    # Then in the receiver:

    bus.$on('myEvent',() => {
    // Do stuff
    });

    # And in the emitter:

    bus.$emit('myEvent',true);
