$(function() {

    let box = $('#box');
    let para = $('p');
    let i = 0;

    para.text(i);

    function toggleBox(i) {
        box.fadeToggle(500, function() {
            i = i++;
            if(i < 10) {
                para.text(i);
                toggleBox(i);
            }
        })
    }

    toggleBox(i);
})