// function onReady() { 
//     alert('Ready to go')
// }
// $(document).ready(onReady);

// _____________________________________________________________________




$(function(){

    // Changing body background color
    $("body").css("background", "lightgreen");
    
    // Selecting box element
    var box = $('#box');

    // Declaring function fadeOut and FadeIn
    function boxOut() {
        box.fadeOut(1000, boxIn);
    }

    function boxIn() {
        box.fadeIn(1000, boxOut);
    }
    
    boxOut();    
})