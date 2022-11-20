/*
 * mockup7.js
 */

// Returns the base URL of the API, onto which endpoint components can be appended.
function getAPIBaseURL() {
    var baseURL = window.location.protocol + '//' + window.location.hostname + ':' + window.location.port + '/api';
    return baseURL;
}

function initialize() {
    var url = getAPIBaseURL() + '/mockup7';

    // send request to our api
    fetch(url, {method: 'GET'})

    // get info back convert to json
    .then((response) => response.json())

    // now build html page body
    .then(function(artist_list) {
        var artist_name = '';
        var artist_info_div = '';

        // build 
        artist_name = artist_list[98]['artist_firstname'] + ' ' + artist_list[98]['artist_surname'];

        artist_info_div = '<div id = "image-page"> <div class="current-image"> <img src = "almond_blossom.jpg"  alt = "white flower buds with a teal background">  </div> <div class = "image-detail"> Artist Bio: ' + artist_list[98]['artist_bio'] + '</div> <div class = "image-detail">' + artist_list[98]['artist_birthyear'] + '-' + artist_list[98]['artist_deathyear'] + '</div> <div class = "image-detail"> # of works at the MET:</div> </div>';

        var artist_names_element = document.getElementById('artist_names');
        artist_names_element.innerHTML = artist_name;

        var artist_info_element = document.getElementById('artist_info_div');
        artist_info_element.innerHTML = artist_info_div;
    })

    .catch(function(error) {
        console.log(error);
    });

}

window.onload = initialize;