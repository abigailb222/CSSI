function fadeImage() {
  $('img').fadeToggle();
}

function setupHandlers() {
  $('#android').on('click', fadeImage);
}

$(document).ready(setupHandlers);
