/*
 * mockup7.js
 */

// Returns the base URL of the API, onto which endpoint components can be appended.
function getAPIBaseURL() {
    var baseURL = window.location.protocol + '//' + window.location.hostname + ':' + window.location.port + '/api';
    return baseURL;
}

function initialize() {
    loadPage()
}

function getParameters() {
    url = window.location.search
    urlParams = new URLSearchParams(url)
    if (urlParams.has('id')) {
        console.log(urlParams.has('id'))
        newUrl = urlParams.get('id')
        newUrl = "/id/" + newUrl
        console.log(newUrl)
    } else {
        newUrl = ""
    }

    return newUrl
}

function loadPage() {

    var url = getAPIBaseURL() + '/artist' + getParameters();

    // send request to our api
    fetch(url, {method: 'GET'})

    // get info back convert to json
    .then((response) => response.json())

    // now build html page body
    .then(function(artist_data) {
        var artist_name = '';
        var artist_info_div = '';

        
        artist_name = "Artist name: " + artist_data[0]['artist_firstname'] + ' ' + artist_data[0]['artist_surname'];

        artist_info_div = '<div class = "image-detail"> Artist Biography: ' + artist_data[0]['artist_bio'] + '</div> <div class = "image-detail"> Artist Years: ' + artist_data[0]['artist_birthyear'] + '-' + artist_data[0]['artist_deathyear'] + '</div> <div class = "image-detail"> </div>';

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