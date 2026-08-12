## Chapter2

jQuery website http://jquery.com

```js

    $(document).ready(function(){});
    $(function() {})

    $("body").css("background", "lightgreen");


    .text()
    .html()
    .val()


    .fadeIn( [duration ] [, complete ] )
    .fadeOut( [duration ] [, complete ] )
    .fadeToggle( [duration ] [, easing ] [, complete ] )


    // Adjust the opacity of the matched elements.
    .fadeTo( duration, opacity [, complete ] )


    // Display the matched elements with a sliding motion.
    .slideDown( [duration ] [, complete ] )
    // Hide the matched elements with a sliding motion.
    .slideUp( [duration ] [, complete ] )

```

________________________________________________________________________

## Chapter3

```js

    // Return the number of elements in the jQuery object.
    .size();

    .addClass();
    .removeClass();

    //  Reduce the set of matched elements to the one at the specified index.
    .eq( index );
    .last();
    .first();


    .find( selector )
    // Get the descendants of each element in the current set of matched elements, 
    // filtered by a selector, jQuery object, or element.


    .children( [selector ] )
    // Get the children of each element in the set of matched elements, 
    // optionally filtered by a selector.

    // The .children() method differs from .find() in that .children() only 
    // travels a single level down the DOM tree while .find() can traverse 
    // down multiple levels to select descendant elements (grandchildren, etc.) 


    .contents()
    // The .contents() and .children() methods are similar, except that the former 
    // includes text nodes and comment nodes as well as HTML elements in the 
    // resulting jQuery object. 

```