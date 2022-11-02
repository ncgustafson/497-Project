$(document).ready( function() {
    laundry_amount = $('#full');
    console.log("script loaded");
    $('.add').on('click', add_percent);
    $('.subtract').on('click', subtract_percent);
})

function add_percent() {
    temp = parseInt(laundry_amount[0].innerHTML) + 1;
    laundry_amount[0].innerHTML = temp + '%';
}

function subtract_percent() {
    temp = parseInt(laundry_amount[0].innerHTML) - 1;
    laundry_amount[0].innerHTML = temp + '%';
}

function allowDrop(ev) {
    ev.preventDefault();
}

function drag(ev) {
    ev.dataTransfer.setData("text", ev.target.id);
}

function drop(ev) {
    ev.preventDefault();
    var data = ev.dataTransfer.getData("text");
    if (ev.target.localName == 'img')
    {
        ev.target.parentElement.appendChild(document.getElementById(data));
    }
    else
    {
        ev.target.appendChild(document.getElementById(data));
    }
}

function insertCategory() {
    var x = document.getElementById("clothing_type");
    var option = document.createElement("option");
    var y = document.getElementById("new_category").value;
    if (y == 'New Category') {
        alert("Please enter a new category");
    }
    else {
        option.value = y;
        option.text = y;
        x.add(option);
    }
}

function make_laundry() {
    console.log("penis")
}