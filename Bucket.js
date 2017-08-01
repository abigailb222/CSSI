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
	names=document.getElementsByClassName("clearAll");
	for(i=0; i<names.length; i++)
	{
		names[i].style.textDecoration = "none";
	}
}
