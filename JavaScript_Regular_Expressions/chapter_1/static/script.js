function ppp(i) {
    console.log('');
    console.log(`------------ ${i} ------------`);
}

// _____________________________________________________________________

ppp('The RegExp constructor'); 

let rgx1 = new RegExp("hello");
let rgx2 = /hello/;

console.log(rgx1);
console.log(rgx2);

// _____________________________________________________________________

ppp('Using pattern flags'); 


console.log('ignore case or i flag');

console.log('multiline or m flag');

console.log('global or g flag');

// _____________________________________________________________________

ppp('Using the rgx.test method'); 

let rgx3 = /hello/;
console.log(rgx3.test("hello"));
console.log(rgx3.test("Hello"));

let rgx4 = /hello/i;
console.log(rgx4.test("hEllo"));

// _____________________________________________________________________

ppp('Using the rgx.exec method'); 

console.log(rgx3.exec("hello"));
console.log(rgx3.exec("Hello"));
console.log(rgx4.exec("hi hEllo"));

// _____________________________________________________________________

ppp('Using the String.replace method'); 

str1 = 'foo foo';

console.log(str1);

console.log(str1.replace(/foo/, 'qux'))
console.log(str1.replace(/foo/g, 'qux'))

str2 = 'foo Foo';

console.log(str2.replace(/foo/g, 'qux'))
console.log(str2.replace(/foo/ig, 'qux'))

// _____________________________________________________________________

ppp('Using the String.search method'); 

let str3 = "hello world!"

console.log(str3.search(/world/));

// _____________________________________________________________________

ppp('Using the String.match method'); 

let str4 = "abcabc";
console.log(str4.match(/b/));
console.log(str4.match(/b/g));

console.dir(str4.match(/b/g));

// The console method log() displays the toString representation of any
// object passed to it.

// The Console method dir() displays an interactive list of the
// properties of the specified JavaScript object. The output is
// presented as a hierarchical listing with disclosure triangles that
// let you see the contents of child objects.