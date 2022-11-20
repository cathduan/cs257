/*
 * mockup3.js
 */

// Returns the base URL of the API, onto which endpoint components can be appended.
function getAPIBaseURL() {
    var baseURL = window.location.protocol + '//' + window.location.hostname + ':' + window.location.port + '/api';
    return baseURL;
}

function initialize() {
    var url = getAPIBaseURL() + '/collections';

    // send request to our api
    fetch(url, {method: 'GET'})

    // get info back convert to json
    .then((response) => response.json())

    // now build html page body
    .then(function(collections_list) {
        
        // var collection_info_div = [];
        var collection_info_div = "";

        var collection_link = '';

        for (var i = 0; i < collections_list.length; i++) { 
            collection_link 
            collection_info_div += '<div class="collection-image"><a href = "mockup2.html"><img src = "almond_blossom.jpg""  alt = "white flower buds with a teal background"></a><div class = "collection-image-text">' + collections_list[i]['department_name'] + '</div></div> <p>     </p';
        }
        //collection_info_div = '{{ url_for("static", filename= "all_black.png")}} alt = "white flower buds with a teal background"></a><div class = "collection-image-text">'
        // collection_info_div = '<div class="collection-image"><a href = "mockup2.html"><img src = "{{ url_for("static", filename= "almond_blossom.jpg")}"  alt = "white flower buds with a teal background"></a><div class = "collection-image-text">' + collections_list[1]['department_name'] + '</div></div><p>     </p';
        // collection_info_div =  collections_list[3]['department_name']

        var collection_names_element = document.getElementById('collection_names');
        collection_names_element.innerHTML = collection_info_div;

       
    })

    .catch(function(error) {
        console.log(error);
    });

}


function getImage(){

}
window.onload = initialize;