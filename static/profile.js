$(document).ready(function(){
	var name = user.name.split('_');
	console.log(name);
	var personalInfo = "<h3>Name:</h3><br/><p>"+name[0]+" "+name[1]+"</p><br/><h3>Email:</h3><br/><p>"+user.email+"</p>";
	var reservationInfo = "";
	var text = personalInfo+reservationInfo;
	$(function () {
  		$(text).appendTo('#profilediv');
	});

});