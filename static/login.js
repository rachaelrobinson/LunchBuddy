$(document).ready(function(){
	$("#loginbtn").click(function(){
    console.log("HERE");
		var email = $("#inputEmail").val();
		var psswrd = $("#inputPassword").val();
		console.log(email);
		console.log(psswrd);
		if (email == "" || psswrd == "" || email == undefined || psswrd == undefined){
			alert("Please login with your email and password");
		} else {
			$.ajax({
        		type: 'POST',
        		url: '/login',
        		data: {username: email, password: psswrd},
        		// headers: {
        		//     'Cache-Control':'max-age=500'
        		// },
        		success: function(result) {
        			if(result[0].status == 200){
        				console.log("YOU LOGGED IN")
                window.location.href = "/reserve"
        			}
        			else if (result[0].status == 400){
        				alert("YOU DIDN'T LOG IN");
        			}
        		  
        		}
      		});
		}
    });
});