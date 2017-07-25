$(document).ready(function(){
	$("#signupbtn").click(function(){
    console.log("HERE");
		var fname = $("#inputFName").val();
        var lname = $("#inputLName").val();
        var email = $("#inputEmail").val();
		var psswrd = $("#inputPassword").val();
		console.log(fname);
        console.log(lname);
        console.log(email);
		console.log(psswrd);
        var fullname = fname+lname;
        console.log(fullname);
        var newUser = {name:fullname, email: email, password:psswrd};
        console.log(newUser);
        var valid = true;
        // TODO: sanitize strings and check for characters/numbers in names
        for (var key in newUser){
            if (newUser[key] == undefined || newUser[key] == ""){
                valid = false;
            }
        }
        if (valid == false){
            alert("Please fill in each section of the form");
        } else{
            $.ajax({
                type: 'POST',
                url: '/register',
                data: newUser,
                // headers: {
                //     'Cache-Control':'max-age=500'
                // },
                success: function(result) {
                    if(result[0].status == 200){
                        console.log("YOU LOGGED IN")
                window.location.href = "/reserve"
                    }
                    else if (result[0].status == 400){
                        alert("Oops something went wrong! We could not make you an account.");
                        // TODO: get message from backend about why we couldn't add user
                    }
                }
            });
		}
    });
});