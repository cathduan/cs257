/*
 * mockup5.js
 * 
 *
 * A little bit of Javascript showing one small example of AJAX
 * within the "books and authors" sample for Carleton CS257.
 *
 * This example uses a very simple-minded approach to Javascript
 * program structure. We'll talk more about this after you get
 * a feel for some Javascript basics.
 */

// Returns the base URL of the API, onto which endpoint components can be appended.

function getAPIBaseURL() {
    var baseURL = window.location.protocol + '//' + window.location.hostname + ':' + window.location.port + '/api';
    return baseURL;
}

function initialize() {
    loadArtists()
   
    // getImages()
    //loadMenus()
}
function previousPageEvent() {
    currUrl = location.href

    pageNum = getPageNumber()

    sliceLength = pageNum.length

    pageNum = parseInt(pageNum)

    if (pageNum-1 > 0) {
        pageNum = pageNum - 1
    }

    newUrl = currUrl.slice(0, -sliceLength) + pageNum;
    
    location.href = newUrl
}

function nextPageEvent () {
    currUrl = location.href

    pageNum = getPageNumber()

    sliceLength = pageNum.length

    pageNum = parseInt(pageNum)

    pageNum = pageNum + 1

    newUrl = currUrl.slice(0, -sliceLength) + pageNum

    location.href = newUrl
}

function getParameters() {
    // var url = document.URL
    url = window.location.search
    urlParams = new URLSearchParams(url)

    
    if (urlParams.has('q')) {
        console.log(urlParams.has('q'))
        newUrl = urlParams.get('q')
        newUrl = "/q/" + newUrl
        console.log(newUrl)
    } else {
        newUrl = ""
    }
    
    return newUrl
}

function getPageNumber() {
    url = window.location.search
    urlParams = new URLSearchParams(url)

    if (urlParams.has('page')) {
        console.log(urlParams.get('page'))
        return urlParams.get('page')
    } else {
        return 1
    }
}

function loadArtists() {

    let url = getAPIBaseURL() + "/artists" + getParameters();
    
    console.log(url)

    // send request to our api
    fetch(url, {method: 'GET'})

    // get info back convert to json
    .then((response) => response.json())

    // now build html page body
    .then(function(browse_artist_page) {

        // console.log(browse_all_page)
        current_browsing = browse_artist_page['artist_list']
        
        // main art page info
        var artist_info_1 = '';
        var artist_info_2 = '';
        var artist_info_3 = '';
        var artist_info_4 = '';
        

        if (urlParams.has('page') == false) {
            currUrl = location.href
            if (urlParams.has('q') == true || urlParams.has('collections') == true || urlParams.has('geographic_locations') == true || urlParams.has('materials') == true) {
                location.href = currUrl + "&page=1"
            } else {
                location.href = currUrl + "?page=1"
            }
        }

        pageNumber = getPageNumber()
        

        temp = pageNumber * 4

        fir_artist = temp-4
        sec_artist = temp-3
        thi_artist = temp-2
        fou_artist = temp-1

        // build 
        if (typeof current_browsing[fir_artist] == "undefined") {
            artist_info_1 = null
        } else {
            
            artist_info_1 = "<li><h3>" + current_browsing[fir_artist]['artist_firstname'] + " " + current_browsing[fir_artist]['artist_surname'] + "</h3></li><li>" + current_browsing[fir_artist]['artist_birthyear'] + "-" + current_browsing[fir_artist]['artist_deathyear'] + "</li>"

            id_1=  current_browsing[fir_artist]['artist_id']
            document.getElementById("Img").onClick = function(){
                clickImage1Function()
            }
            
        }

        if (typeof current_browsing[sec_artist] == "undefined") {
            artist_info_2 = null
        } else {
            artist_info_2 = "<li><h3>" + current_browsing[sec_artist]['artist_firstname'] + " " + current_browsing[sec_artist]['artist_surname'] + "</h3></li><li>" + current_browsing[sec_artist]['artist_birthyear'] + "-" + current_browsing[sec_artist]['artist_deathyear'] + "</li>"

            //new_url = "/artist?id=" + current_browsing[sec_artist]['artist_id']
            id_2 = current_browsing[sec_artist]['artist_id']
           
            document.getElementById("Img").onClick = function(){
                clickImage2Function()
                
            }
        }
        if (typeof current_browsing[thi_artist] == "undefined") {
            artist_info_3 = null
        } else { 
            artist_info_3 = "<li><h3>" + current_browsing[thi_artist]['artist_firstname'] + " " + current_browsing[thi_artist]['artist_surname'] + "</h3></li><li>" + current_browsing[thi_artist]['artist_birthyear']+ "-" + current_browsing[thi_artist]['artist_deathyear'] + "</li>"

            id_3 = current_browsing[thi_artist]['artist_id']
           
            document.getElementById("Img").onClick = function(){
                clickImage3Function()
            }

        }
        if (typeof current_browsing[fou_artist] == "undefined") {
            artist_info_4 = null
        } else { 
            artist_info_4 = "<li><h3>" + current_browsing[fou_artist]['artist_firstname'] + " " + current_browsing[fou_artist]['artist_surname'] + "</h3></li><li>" + current_browsing[fou_artist]['artist_birthyear'] + "-" + current_browsing[fou_artist]['artist_deathyear'] + "</li>"

            id_4 = current_browsing[fou_artist]['artist_id']
           
            document.getElementById("Img").onClick = function(){
                clickImage4Function()
            }
        }

        var artist_info_1_element = document.getElementById('artist_info_1');
        artist_info_1_element.innerHTML = artist_info_1;

        var artist_info_2_element = document.getElementById('artist_info_2');
        artist_info_2_element.innerHTML = artist_info_2;

        var artist_info_3_element = document.getElementById('artist_info_3');
        artist_info_3_element.innerHTML = artist_info_3;

        var artist_info_4_element = document.getElementById('artist_info_4');
        artist_info_4_element.innerHTML = artist_info_4;
    })

    .catch(function(error) {
        console.log(error);
    });

}

function clickImage1Function(){

    let beginning_url = String(window.location.href)
    let redirected_url = beginning_url.substring(0,-7)
    redirected_url += "/artist?id=" + id_1
    window.location.href = redirected_url
}
 
function clickImage2Function(){
    let beginning_url = String(window.location.href)
    let redirected_url = beginning_url.substring(0,-7)
    redirected_url += "/artist?id=" + id_2
    window.location.href = redirected_url
}

function clickImage3Function(){
    let beginning_url = String(window.location.href)
    let redirected_url = beginning_url.substring(0,-7)
    redirected_url += "/artist?id=" + id_3
    window.location.href = redirected_url
}
 
function clickImage4Function(){
    let beginning_url = String(window.location.href)
    let redirected_url = beginning_url.substring(0,-7)
    redirected_url += "/artist?id=" + id_4
    window.location.href = redirected_url
}
 
 

window.onload = initialize;


