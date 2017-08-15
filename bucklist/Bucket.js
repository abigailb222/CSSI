function Task1Done(amazingabigail)
{
	var bulletstyle = document.getElementById(amazingabigail).style.textDecoration;
  if (bulletstyle == "line-through")
		document.getElementById(amazingabigail).style.textDecoration='none';
  else
  	document.getElementById(amazingabigail).style.textDecoration='line-through';
}

function clearAll()
{
	names = $('.task');
	names.css("textDecoration", "none");
}

function addListItem(text){
  list = document.querySelector('ol');
  item = document.createElement('li');
  item.innerText = text;
  list.appendChild(item);
}
	function pop_up()
	{
	var i = prompt("Enter an item to add to list");
	addListItem (i);
}
