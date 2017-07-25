$(document).ready(function(){
    console.log("YO YO YO");
	$("#reserve").click(function(){
        console.log("HELLO");
		var pcampus = $("#pcampus option:selected").val();
        var scampus = $("#scampus option:selected").val();
        var ptime = $("#ptime option:selected").val();
		var stime = $("#stime option:selected").val();
        var date = $("#date").val();
		console.log(pcampus);
        console.log(scampus);
        console.log(ptime);
		console.log(stime);
        console.log(date);
        var newReservation = {pcampus: pcampus, scampus: scampus, ptime:ptime, stime:stime, date:date};
        // TODO: check that primary and secondary choices are different and that date is a valid date
        $.ajax({
                type: 'POST',
                url: '/reserve',
                data: newReservation,
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
    });
});