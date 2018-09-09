$(function(){

	$("input#new-twilio-add-btn").click(function(){
		let formData = fetchCreateForm();
		$.ajax({
			url: '/firebase/add/operator',
			method: 'POST',
			data: formData,
			processData: false,  // tell jQuery not to process the data
	       	contentType: false,  // tell jQuery not to set contentType
			dataType: 'json'
		}).done(data => {
			console.log("operators: " + data);
			appendOperator(data);
			$('#new-twilio-form').modal('hide');
		}).fail(()=> {
			alert('error');
		});
	});

	var appendOperator = (operators) => {
		let body = $('#table-body').empty();
		if (operators == null) {
			return;
		}
		let joperators = operators.map((operator)=>{
			var row = $("<tr></tr>").data('id', operator.id).click(function(){
				let uid = $(this).data('id');
				if (uid == null){
					return
				}
				//undefined
				console.log('clicked: '+ uid);
				// if (uid) {
				// 	$.ajax({
				// 		url: '/search/User/' + uid,
				// 		method: 'GET',
				// 		dataType: 'json'
				// 	}).done(data => {
				// 		updateModal(data);
				// 	}).fail(()=> {
				// 		alert('error');
				// 	});
				// }
			});
			row.append($("<th scope='row'></th>").text(operator.id));
			row.append($("<td></td>").text(operator.phone));
			return row
		});
		joperators.forEach(joperator => {
			body.append(joperator);
		});
	};

	var refreshCreateForm = () => {
		$("input#new-twilio-phone").val("");
	}

	//add operator, table & modal management
	var fetchCreateForm = () => {
		let formData = new FormData();
		let phone = $("input#new-twilio-phone").val();
		formData.append('phone', phone.toString());
		return formData;
	}

});