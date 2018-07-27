// setup call function when clicked

$(function () {
	var appendUser = (users) => {
		let jusers = users.map( user =>{
			var row = $("<tr></tr>");
			row.append($("<th scope='row'></th>").text(user.id));
			row.append($("<td></td>").text(user.first_name + " " + user.last_name));
			row.append($("<td></td>").text(user.state));
			row.append($("<td></td>").text(user.zipcode));
			row.append($("<td></td>").text(user.dob));
			row.append($("<td></td>").text(user.sex));
			row.append($("<td></td>").text(user.phone));
			return row
		});
		let body = $('#js-tbody').empty();
		jusers.forEach(juser => {
			body.append(juser);
		});
	};

	var updateAlert = (alert) => {
		$('#jalert').text(alert);
	};

	//click event
	$("a.page-link").click(function(){
		console.log('click');
		let pageNumber = $(this).text();
		$.ajax({
			url: '/page/' + pageNumber,
			method: 'GET',
			dataType: 'json'
		}).done(data => {
			console.log('hello');
			appendUser(data);
		}).fail(()=> {
			alert('error');
		});
	});

});