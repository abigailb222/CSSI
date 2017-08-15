function greeting() {
   var userName = $('#username').val();
   alert("Hi "  + userName + ", welcome to my page!");
 }

 function setup() {
   $("#ok_button").click(greeting);
 }

 $(document).ready(setup)
