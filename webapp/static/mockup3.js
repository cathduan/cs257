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


        for (var collection = 0; collection < collections_list.length; collection++) { 
            var collection_link = '';
            var collection_link_info = '';
            collection_link_info = collections_list[collection]['department_name']
            collection_link_info = collection_link_info.toLowerCase()
            collection_link_info = collection_link_info.split(" ")
            collection_link_info_join = collection_link_info.join("-")

            collection_link += '<a style= "text-decoration:none;" color: black href='
            collection_link += '"/browse-all?collections=' + collection_link_info_join + '"'
            collection_link += '>'
            collection_link += collections_list[collection]['department_name']
            collection_link += '</a>'

            collection_info_div += '<p></p><div class="collection-image"> <div class = "collection-image-text">' + collection_link + '</div></div> <p></p';
        }
       
        // collection_info_div = '<div class="collection-image"><a href = "mockup2.html"><img src = "{{ url_for("static", filename= "almond_blossom.jpg")}"  alt = "white flower buds with a teal background"></a><div class = "collection-image-text">' + collections_list[1]['department_name'] + '</div></div><p>     </p';
        // collection_info_div =  collections_list[3]['department_name']

        var collection_names_element = document.getElementById('collection_names');
        collection_names_element.innerHTML = collection_info_div;

       
    })

    .catch(function(error) {
        console.log(error);
    });

}

window.onload = initialize;