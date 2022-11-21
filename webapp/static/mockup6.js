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

    // http://127.0.0.1:5000/api/artwork/id/17

    let url = getAPIBaseURL() + "/artwork" + getParameters() ;
    console.log(url)
    // send request to our api
    fetch(url, {method: 'GET'})

    // get info back convert to json
    .then((response) => response.json())

    // now build html page body
    .then(function(artwork_data) {
        //build

        artwork_info = null

        console.log(artwork_data)
        artwork_info_div = ""

        // if (artwork_data[0]['artist_surname'] == "" & artwork_data[0]['artists_firstname' == ""]){
        //     var first_name = "No artist"
        //     var surname = "name"
        // }
        // else{
        //     first_name = artwork_data[0]['artist_firstname']
        //     surname = artwork_data[0]['artist_surname']
            
        // }

        
        artwork_info_div += '<div style = "color: #723D46; " class = "image-title">Title: ' + artwork_data[0]['artwork'] + ' </div><div class = "image-detail">Artwork Date: ' + artwork_data[0]['art_date'] +'</div> <div class = "image-detail">Artist Name: '+artwork_data[0]['artist_firstname'] + artwork_data[0]['artist_surname'] +' </div> <div class = "image-detail">Medium: '+artwork_data[0]['medium'] +'</div> <div class = "image-detail">Collection: '+artwork_data[0]['collection'] +'</div> <div class = "image-detail">Place of Origin: '+artwork_data[0]['country'] +'</div> <p></p><div class = "image-detail">Link to artwork: <a href='+artwork_data[0]['link_resource'] +'>' + artwork_data[0]['link_resource']  + '</a></div>'

        // if (typeof artwork_data[0] == "undefined") {
        //     artwork_info_1 = null
        // } else {
        //     console.log(artwork_data[0]['artwork'])
        //     artwork_info_1 = "<li><h3>" + artwork_data[0]['artist_surname'] + "</h3></li> " 
        // }

        var artwork_info_element = document.getElementById('artwork_info');
        artwork_info_element.innerHTML = artwork_info_div;
    })

}

window.onload = initialize;