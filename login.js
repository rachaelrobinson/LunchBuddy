$(document).ready(function(){
	$("#login").click(function(){
		var username = $("#email").val();
		var psswrd = $("#password").val();
		console.log(username);
		console.log(psswrd);
		if (username == "" || psswrd == "" || username == undefined || psswrd == undefined){
			alert("Please login with your email and password");
		} else {
			// $.ajax({
   //      		type: 'POST',
   //      		url: '/newhome',
   //      		data: {email: username, password: psswrd},
   //      		// headers: {
   //      		//     'Cache-Control':'max-age=500'
   //      		// },
   //      		success: function(result) {
   //      			if(result[0].status == 200){
   //      				console.log("YOU LOGGED IN")
   //      			}
   //      			else if (result[0].status == 400){
   //      				alert("YOU DIDN'T LOG IN");
   //      			}
        		  
        		// }
      		// });
		}
    });
});