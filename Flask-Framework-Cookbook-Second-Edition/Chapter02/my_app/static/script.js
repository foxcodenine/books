// https://momentjs.com/

let moment_list = [
    moment().format('MMMM Do YYYY, h:mm:ss a'),
    moment().format('dddd'),
    moment().format("MMM Do YY"),
    moment().format('YYYY [escaped] YYYY'),
    moment().format()
]

let vm = new Vue({
    el: '#myapp',
    data: {
        timestamp: new Date().toLocaleString(),
        myMoment: moment_list,
    },
    delimiters: ['[[',']]']
    
})

console.log(moment().format('MMMM Do YYYY, h:mm:ss a'))

