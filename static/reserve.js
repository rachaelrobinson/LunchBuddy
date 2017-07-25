$(document).ready(function(){
	$("#reserve").click(function(){
		var pcampus = $("#pcampus option:selected").val();
        var scampus = $("#scampus option:selected").val();
        var ptime = $("#ptime option:selected").val();
		var stime = $("#stime option:selected").val();
        var date = $("#date").val();
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
                        window.location.href = "/reserve"
                    }
                    else if (result[0].status == 400){
                        alert("Oops something went wrong! We could not find you a buddy.");
                        // TODO: get message from backend about why we couldn't add user
                    }
                }
        });
    });
});