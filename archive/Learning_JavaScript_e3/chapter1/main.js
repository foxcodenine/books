$(document).ready(function(){

    'use strict';
    console.log('main.js loaded');

    paper.install(window);
    paper.setup(document.getElementById('mainCanvas'));

    // TODO
    // 1st Exercise
    // var c  = Shape.Circle(200, 200, 50)
    // c.fillColor = 'green';

    // 2nd
    // var c;
    // for(var y=25; y<400; y+=50){
    //     for(var x=25; x<400; x+=50){
    //         c = Shape.Circle(x, y, 20);
    //         c.fillColor = 'green';
    //     };
    // };


    // 3rd
    var tool = new Tool();

    var c = Shape.Circle(200, 200, 80)
    c.fillColor = 'black';
    var text = new PointText(200, 205);
    text.justification = 'center';
    text.fillColor = 'white';
    text.fontSize = 20;
    text.content = 'hello world';

    tool.onMouseDown = function(event) {
        var c = Shape.Circle(event.point.x, event.point.y, 20);
        c.fillColor = 'brown';
    };

    paper.view.draw();

});