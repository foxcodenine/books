function ppp(i) {
    console.log('');
    console.log(`------------ ${i} ------------`);
}

// _____________________________________________________________________

ppp('Matching a wild card character'); 

let str, rgx;


str = '123 1b3 1 3 133 321'

rgx = /1.3/g;

console.log(str.match(rgx));
// _____________________________________________________________________

ppp('Matching digits'); 


str = '123 1b3 1 3 133 321'

rgx = /1\d3/g;

console.log(str.match(rgx));


// _____________________________________________________________________

ppp('Matching alphanumeric chars'); 


str = '123 1b3 1 3 133 321'

rgx = /1\w3/g;

console.log(str.match(rgx));


// _____________________________________________________________________

ppp('Negating alphanumeric chars and digits'); 


str = '123 1b3 1 3 133 321'

rgx = /1\D3/g;

console.log(str.match(rgx));

rgx = /1\W3/g;

console.log(str.match(rgx));


// _____________________________________________________________________

ppp('Defining ranges in Regex'); 


str = 'bicycle'

rgx = /[abc]/g;

console.log(str.match(rgx));


str = 'Tim sam Bob maC Guy';

rgx = /[A-Z][a-z][a-z]/g;

console.log(str.match(rgx));

// _____________________________________________________________________


ppp('Matching the dash \- character and period \.'); 


str = 'hello world  hello-world,'

rgx = /hello[\- ]world/g;

console.log(str.match(rgx));


str = '123 2.4 .45'

rgx = /[\d.][\d.]\d/g;
console.log(str.match(rgx));

// _____________________________________________________________________


ppp('Defining negated ranges'); 


str = 'Tim sam Bob maC Guy,';

rgx = /[^ ^A-Z][a-z][a-zA-Z]/g;

console.log(str.match(rgx));


// _____________________________________________________________________
