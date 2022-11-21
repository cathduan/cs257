/*
 * mockup2.js
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
    loadBrowseAll()
    // getImages()
    loadMenus()
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

    if (urlParams.has('collections')) {
        console.log(urlParams.has('collections'))
        newUrl = urlParams.get('collections')
        newUrl = "/collections/" + newUrl
    } else if (urlParams.has('geographic_locations')) {
        console.log(urlParams.has('geographic_locations'))
        newUrl = urlParams.get('geographic_locations')
        newUrl = "/geographic_locations/" + newUrl
    } else if (urlParams.has('materials')) {
        console.log(urlParams.has('materials'))
        newUrl = urlParams.get('materials')
        newUrl = "/materials/" + newUrl
    } else if (urlParams.has('q')) {
        console.log(urlParams.has('q'))
        newUrl = urlParams.get('q')
        newUrl = "/q/" + newUrl
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


function loadBrowseAll() {

    let url = getAPIBaseURL() + "/browse-all" + getParameters();

    console.log(url)

    // send request to our api
    fetch(url, {method: 'GET'})

    // get info back convert to json
    .then((response) => response.json())

    // now build html page body
    .then(function(browse_all_page) {

        current_browsing = browse_all_page['current_browsing']
        
        // main art page info
        var artwork_info_1 = '';
        var artwork_info_2 = '';
        var artwork_info_3 = '';
        var artwork_info_4 = '';

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

        fir_work = temp-4
        sec_work = temp-3
        thi_work = temp-2
        fou_work = temp-1

        // build 
        if (typeof current_browsing[fir_work] == "undefined") {
            artwork_info_1 = null
        } else {
            console.log(typeof current_browsing[fir_work])
            artwork_info_1 = "<li><h3>" + current_browsing[fir_work]['artist_firstname'] + " " + current_browsing[fir_work]['artist_surname'] + "</h3></li><li>" + current_browsing[fir_work]['art_date'] + "</li><li>" + current_browsing[fir_work]['artwork'] + "</li><li>" + current_browsing[fir_work]['material_type'] + "</li>"

            id_1=  current_browsing[fir_work]['artwork_id']
            document.getElementById("Img").onClick = function(){
                clickImage1Function()
            }
        }
        if (typeof current_browsing[sec_work] == "undefined") {
            artwork_info_2 = null
        } else {
            artwork_info_2 = "<li><h3>" + current_browsing[sec_work]['artist_firstname'] + " " + current_browsing[sec_work]['artist_surname'] + "</h3></li><li>" + current_browsing[sec_work]['art_date'] + "</li><li>" + current_browsing[sec_work]['artwork'] + "</li><li>" + current_browsing[sec_work]['material_type'] + "</li>"
           
            id_2=  current_browsing[sec_work]['artwork_id']
            document.getElementById("Img").onClick = function(){
                clickImage2Function()
            }
        }
        if (typeof current_browsing[thi_work] == "undefined") {
            artwork_info_3 = null
        } else { 
            artwork_info_3 = "<li><h3>" + current_browsing[thi_work]['artist_firstname'] + " " + current_browsing[thi_work]['artist_surname'] + "</h3></li><li>" + current_browsing[thi_work]['art_date'] + "</li><li>" + current_browsing[thi_work]['artwork'] + "</li><li>" + current_browsing[thi_work]['material_type'] + "</li>"

            id_3=  current_browsing[thi_work]['artwork_id']
            document.getElementById("Img").onClick = function(){
                clickImage3Function()
            }
        }
        if (typeof current_browsing[fou_work] == "undefined") {
            artwork_info_4 = null
        } else { 
            artwork_info_4 = "<li><h3>" + current_browsing[fou_work]['artist_firstname'] + " " + current_browsing[fou_work]['artist_surname'] + "</h3></li><li>" + current_browsing[fou_work]['art_date'] + "</li><li>" + current_browsing[fou_work]['artwork'] + "</li><li>" + current_browsing[fou_work]['material_type'] + "</li>"

            id_4=  current_browsing[fou_work]['artwork_id']
            document.getElementById("Img").onClick = function(){
                clickImage4Function()
            }
        }

        var artwork_info_1_element = document.getElementById('artwork_info_1');
        artwork_info_1_element.innerHTML = artwork_info_1;

        var artwork_info_2_element = document.getElementById('artwork_info_2');
        artwork_info_2_element.innerHTML = artwork_info_2;

        var artwork_info_3_element = document.getElementById('artwork_info_3');
        artwork_info_3_element.innerHTML = artwork_info_3;

        var artwork_info_4_element = document.getElementById('artwork_info_4');
        artwork_info_4_element.innerHTML = artwork_info_4;
    })

    .catch(function(error) {
        console.log(error);
    });

}

function loadMenus() {
    var url = getAPIBaseURL() + '/browse-all';

    // send request to our api
    fetch(url, {method: 'GET'})

    // get info back convert to json
    .then((response) => response.json())

    // now build html page body
    .then(function(browse_all_page) {

        collections_menu = browse_all_page['collections']
        geographic_locations_menu = browse_all_page['geographic_locations']
        materials_menu = browse_all_page['materials']

        // collections drop down info
        collections_dropdown = '<div class="dropdown-menu scrollable-menu" role="menu">'
        for (let collection = 0; collection < collections_menu.length; collection++) {

            collection_link = collections_menu[collection]['collection']
            collection_link = collection_link.toLowerCase()
            collection_link = collection_link.split(" ")
            collection_link_join = collection_link.join("-")

            collections_dropdown += '<a href='
            collections_dropdown += '"/browse-all?collections=' + collection_link_join + '"'
            collections_dropdown += '>'
            collections_dropdown += collections_menu[collection]['collection']
            collections_dropdown += '</a>'
        }
        collections_dropdown += '</div>'
        
        // geographic locations drop down info
        geographic_locations_dropdown = '<div class="dropdown-menu scrollable-menu" role="menu">'
        for (let location = 0; location < geographic_locations_menu.length; location++) {

            geographic_location_link = geographic_locations_menu[location]['country_name']
            geographic_location_link = geographic_location_link.toLowerCase()
            geographic_location_link = geographic_location_link.split(" ")
            geographic_location_link_join = geographic_location_link.join("-")

            geographic_locations_dropdown += '<a href='
            geographic_locations_dropdown += '"/browse-all?geographic_locations=' + geographic_location_link_join + '"'
            geographic_locations_dropdown += '>'
            geographic_locations_dropdown += geographic_locations_menu[location]['country_name']
            geographic_locations_dropdown += '</a>'
        }
        geographic_locations_dropdown += '</div>'

        // materials drop down info
        materials_dropdown = '<div class="dropdown-menu scrollable-menu" role="menu">'
        for (let material = 0; material < materials_menu.length; material++) {

            material_link = materials_menu[material]['material_type']
            material_link = material_link.toLowerCase()
            material_link = material_link.split(" ")
            material_link_join = material_link.join("-")

            materials_dropdown += '<a href='
            materials_dropdown += '"/browse-all?materials=' + material_link_join + '"'
            materials_dropdown += '>'
            materials_dropdown += materials_menu[material]['material_type']
            materials_dropdown += '</a>'
        }
        materials_dropdown += '</div>'

        // collections dropdown
        var collections_menu_element = document.getElementById('collections_dropdown');
        collections_menu_element.innerHTML = collections_dropdown;

        // geographic locations dropdown
        var geographic_locations_menu_element = document.getElementById('geographic_locations_dropdown');
        geographic_locations_menu_element.innerHTML = geographic_locations_dropdown;

        // materials dropdown
        var materials_menu_element = document.getElementById('materials_dropdown');
        materials_menu_element.innerHTML = materials_dropdown;

    })

    .catch(function(error) {
        console.log(error);
    });

}

function clickImage1Function(){
    redirected_url = window.location.protocol + '//' + window.location.hostname + ':' + window.location.port + "/artwork?id=" + id_1
    window.location.href = redirected_url
}
 
function clickImage2Function(){
    redirected_url = window.location.protocol + '//' + window.location.hostname + ':' + window.location.port + "/artwork?id=" + id_2
    window.location.href = redirected_url
}

function clickImage3Function(){
    redirected_url = window.location.protocol + '//' + window.location.hostname + ':' + window.location.port + "/artwork?id=" + id_3
    window.location.href = redirected_url
}
 
function clickImage4Function(){
    redirected_url = window.location.protocol + '//' + window.location.hostname + ':' + window.location.port + "/artwork?id=" + id_4
    window.location.href = redirected_url
}
 
 

window.onload = initialize;


