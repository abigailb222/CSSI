function showWhenClicked() {
    $("#pig").show();
}

function hideWhenClicked() {
    $("#pig").hide();
}
function flyWhenClicked() {
    $("#pig").animate({left: '1600px'}, "slow", flypignumber2);
}

function flypignumber2() {
    $("#pig2").animate({left: '1250px'},);
}

function setup() {
    $("#showPig").click(showWhenClicked);
    $("#hidePig").click(hideWhenClicked);
    $("#flypig").click(flyWhenClicked);
}

$(document).ready(setup);
