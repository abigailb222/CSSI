// Paste the helpful function here:
function addListItem(text){
  list = document.querySelector('ul');
  item = document.createElement('li');
  item.innerText = text;
  list.appendChild(item);
}

// Now use the function to add elements to the list!
addListItem("Banana")
addListItem("Pear")
addListItem("Tamborine")
addListItem("Guinep")
addListItem("Guava")
