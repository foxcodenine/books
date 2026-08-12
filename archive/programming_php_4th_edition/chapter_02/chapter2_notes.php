<?php
# Lexical Structire

// Case Sensitivity

echo ("hello, world \n");
ECHO ("hello, world \n");
Echo ("hello, world \n");

$name = 1234;
$Name = 5467;
echo "{$name} {$Name} \n";

// _____________________________________________________________________

// Comments

# This is an inline comment.
// And this is another form of inline comment.

/*
This is a multy line comment.
*/

// _____________________________________________________________________

// Liiterals

// A literal is a data value as:

/*
123
'hello'
1.23
*/

// _____________________________________________________________________

// Functions and Classes

// function and classes name are not case sensitive as varables are:

function helloWorld() {
    echo "Hello php World \n";
}

HELLOworld();



// _____________________________________________________________________

// Constants

define('PUBLISHER', 'O\'Reilly Media');
echo PUBLISHER . "\n";

// _____________________________________________________________________

// Keywords

$keywords = array('__halt_compiler', 'abstract', 'and', 'array', 'as', 'break', 'callable', 'case', 
    'catch', 'class', 'clone', 'const', 'continue', 'declare', 'default', 'die', 'do', 'echo', 'else', 
    'elseif', 'empty', 'enddeclare', 'endfor', 'endforeach', 'endif', 'endswitch', 'endwhile', 'eval', 
    'exit', 'extends', 'final', 'for', 'foreach', 'function', 'global', 'goto', 'if', 'implements', 
    'include', 'include_once', 'instanceof', 'insteadof', 'interface', 'isset', 'list', 'namespace', 
    'new', 'or', 'print', 'private', 'protected', 'public', 'require', 'require_once', 'return', 
    'static', 'switch', 'throw', 'trait', 'try', 'unset', 'use', 'var', 'while', 'xor'); 


$predefined_constants = array('__CLASS__', '__DIR__', '__FILE__', '__FUNCTION__', '__LINE__', 
    '__METHOD__', '__NAMESPACE__', '__TRAIT__');


const FORBIDDEN_TYPES = [
    'null',

    'bool',
    'false',
    'true',

    'int',
    'float',

    'string',
];

// _____________________________________________________________________

// Data Types

// Single-value (scalar):
        /**
         * Integer
         * Floating-point
         * String
         * Booleans
         */

// Compoud (collection):
        /**
        * Array
        * Object
         */

// Special Types:
        /**
         * Numbers
         * Booleans
         * Resources
         * Null
         */



/*
    Integers

    Decimal
    0 - 9 

    Octal number
    0 to 7

    0755
    +010

    Hexadecimal

    0xFF
    0x10
    -0xDAD1

    Binary

    0b01110000
    -0b10

*/

echo is_int(888) . "\n";
echo decoct("36"). "\n";
echo is_int(0x88) . "\n";





// Floating-Point Numbers

echo 3.14 . "\n";
echo -7.1 . "\n";

// Scientific numbers
echo 0.314E1 . "\n";

?>



