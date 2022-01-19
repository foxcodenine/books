<?php

// ---------------------------------------------------------------------

/** The assert function
 * 
 * The assert function is used in debuging to check a condition 
 * and generate an error if a  * condition is not true 
 * 
 *       php> assert(expression, 'Error message that is display);
 * 
 * zend.assertions need to be set to 1 in php.ini
 * zend.assertions = 1
 *  */ 
$mass= '1'; // if changed to 'a' it will gerarate an error
assert( is_numeric($mass), 'Input arument must be a number');


// ---------------------------------------------------------------------
// ---------------------------------------------------------------------


/** eval — Evaluate a string as PHP code
 * 
 * Caution Code Injection
 */

eval("echo '<br>This string is echoed through eval function.<br>';");


// ---------------------------------------------------------------------
// ---------------------------------------------------------------------

/** unset() destroys the specified variables. */

function checkVariable($v) {
    if(isset($v)){
        echo '<br> Variable Exists! <br>';
    } else {
        echo '<br> Variable Does Not Exists! <br>';
    }

}

$var = 'Testing testing 123';

error_reporting(0); // <- this will switch OFF all error
                    //    (E_ERROR | E_WARNING | E_PARSE | E_NOTICE)

checkVariable($var);

unset($var);        // <-<   

checkVariable($var);

error_reporting(E_ALL); // <- this will turn everything ON

// Not to be confused with unlink();
// Deletes filename. An E_WARNING level error will be generated on failure.


// ---------------------------------------------------------------------
// ---------------------------------------------------------------------

/** The list() function is used to assign values to a list of variables 
    in one operation. */

$info = array('coffee', 'brown', 'caffeine');

// Listing all the variables
list($drink, $color, $power) = $info;
echo "<br>$drink is $color and $power makes it special.<br>";

// Listing some of them
list($drink, , $power) = $info;
echo "<br>$drink has $power.<br>";

// Or let's skip to only the third one
list( , , $power) = $info;
echo "<br>I need $power!<br>";

// ---------------------------------------------------------------------
// ---------------------------------------------------------------------
?>