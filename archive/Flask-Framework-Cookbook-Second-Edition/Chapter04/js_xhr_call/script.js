fetch('http://127.0.0.1:5000/catalog/', {
    method: 'GET',
    headers: {
        'X-Requested-With': 'XMLHttpRequest'
    }
})
.then(function(respons) {
    return respons.json()
})
.then(function(data) {
    console.log('>>',data)
    let markup = '<li class="list-group-item">' + 'count: ' + data.count + '</li>';
    document.querySelector('#homepage-list').innerHTML = markup;

})


// _____________________________________________________________________

fetch('http://127.0.0.1:5000/catalog/products/', {
    method: 'GET',
    headers: {
        'X-Requested-With': 'XMLHttpRequest'
    }
})
.then(function(respons) {
    return respons.json()
})
.then(function(data) {
    console.log('>>',data)
    let markup = '';

    for(const [key, value] of Object.entries(data)){
        markup += `<li class='list-group-item'>id: 
                                        ${key} - ${value.category} - 
                                        ${value.name} - 
                                        ${value.price}</li>`
    }

    document.querySelector('#products-list').innerHTML = markup;
})


