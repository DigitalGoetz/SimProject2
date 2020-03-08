$(document).ready(function() {

	$("#start").click(function() {
		console.log("start recording");
		$.get("/event/start", function(data, status) {
			console.log(status);
			console.log(data);
		});
	});

	$("#end").click(function() {
		console.log("end recording");
		$.get("/event/end", function(data, status) {
			console.log(status);
			console.log(data);
		});
	});

	$("#arrival").click(function() {
		console.log("car arrival");
		$.get("/event/arrival", function(data, status) {
			console.log(status);
			console.log(data);
		});
	});

	$("#orderstart").click(function() {
		console.log("start order");
		$.get("/event/orderstart", function(data, status) {
			console.log(status);
			console.log(data);
		});
	});

	$("#orderend").click(function() {
		console.log("end order");
		$.get("/event/orderend", function(data, status) {
			console.log(status);
			console.log(data);
		});
	});

	$("#paymentstart").click(function() {
		console.log("start payment");
		$.get("/event/paymentstart", function(data, status) {
			console.log(status);
			console.log(data);
		});
	});

	$("#paymentend").click(function() {
		console.log("end payment");
		$.get("/event/paymentend", function(data, status) {
			console.log(status);
			console.log(data);
		});
	});
	
	$("#pickupend").click(function() {
		console.log("end pickup");
		$.get("/event/pickupend", function(data, status) {
			console.log(status);
			console.log(data);
		});
	});
	
	$("#pickupstart").click(function() {
		console.log("start pickup");
		$.get("/event/pickupstart", function(data, status) {
			console.log(status);
			console.log(data);
		});
	});
});