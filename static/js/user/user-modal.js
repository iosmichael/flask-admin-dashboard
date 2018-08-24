// setup call function when clicked

$(function () {
	var tagFilter = null;
	var page = 1;
	var allowChange = false;
	var filterKey = 'tag';
	var filterValue = 'CREATED';
	/*
	Click event methods
	*/
	//click on user info
	$('tr').click(function(){
		let uid = $(this).data('id');
		if (uid == null){
			return
		}
		//undefined
		console.log('clicked: '+ uid);
		if (uid) {
			$.ajax({
				url: '/search/User/' + uid,
				method: 'GET',
				dataType: 'json'
			}).done(data => {
				updateModal(data);
			}).fail(()=> {
				alert('error');
			});
		}
	});
	//click on update button
	$('.btn#user-update').click(function(){
		var uid = $("#detail").data('id');
		var url = '/update/User/' + uid;
		var formData = fetchData();
		if (uid == 0){
			console.log('add');
			url = '/add/User';
		}
		$.ajax({
			url: url,
			method: 'POST',
			processData: false,  // tell jQuery not to process the data
	       	contentType: false,  // tell jQuery not to set contentType
			data: formData
		}).done(data => {
			$(".modal").modal('hide');
			refresh();
		}).fail(()=>{
			alert('fail to update');
		})
	});

	$('.btn#user-delete').click(function(){
		var uid = $("#detail").data('id');
		$.ajax({
			url: '/delete/User/' + uid,
			method: 'POST'
		}).done(data => {
			$(".modal").modal('hide');
			refresh();
		});
	})

	$('button#send-message').click(function(){
		let message = $('textarea#message').val();	
		let phone = $('input#phone').val();
		var formData = new FormData();
		formData.append('phone',phone);
		formData.append('message',message);
		$.ajax({
			url: '/send',
			method: 'POST',
			data: formData,
			processData: false,
			contentType: false,
			success: (data) => {
				$('textarea#message').val('');
				refreshRecords();
			}
		});
	});

	$(".btn#status-filter-btn").click(function(){
		createModal();
	});

	$("input#allow-change-input").click(function(){
		toggleReadonly();
	})

	/*
	UI update methods
	*/
	var appendRecord = (records) => {
		let body = $('div#records').empty();
		if (records == null){
			return;
		}
		let jrecords = records.map((record) => {
			var row = $("<div class='record'></div>");
			if (!record.receive) {
				row.append($("<strong></strong>").text('caller texted:'));
			}else{
				row.append($("<strong></strong>").text('bot texted:'));
			}
			row.append($("<br/>"));
			row.append($("<span></span>").text(record.content));
			row.append($("<br/>"));
			// row.append($("<span></span>").text(record.time));
			return row;
		})
		jrecords.forEach(juser => {
			body.append(juser);
		});
	}

	var createModal = () => {
		if (!allowChange) {
			toggleReadonly();
			$("input#allow-change-input").prop('checked', true);
		}
		$("#detail").data('id', 0);
		$(".modal-title").text('Create User');
		$("div#records").empty();
		$("#firstname").val('');
		$("#lastname").val('');
		$("#phone").val('');
		$("#state").val('NA');
		$("#zipcode").val('NA');
		$("#tag").val('CREATED');
		$(".modal").modal('show');
	}

	var updateModal = (data) => {
		//modal show
		if (allowChange) {
			toggleReadonly();
			$("input#allow-change-input").prop('checked', false);
		}
		$("#firstname").val(data.first_name);
		$("#lastname").val(data.last_name);
		$("#phone").val(data.phone);
		$("#state").val(data.state);
		$("#zipcode").val(data.zipcode);
		$("#tag").val(data.tag);
		$("#last").val(data.last_response);
		$("#modalLabel").text('User ID:' + data.id);
		$("#detail").data('id', data.id);
		$.ajax({
		   url : '/all/' + data.phone,
	       dataType:'json',
	       success : (data) => {
		        console.log(data);
		        appendRecord(data);
	       }
		});
		$("#detail").modal('show');
	};

	var toggleReadonly = () => {
		$("#phone").attr('readonly', allowChange);
		$("#tag").attr('disabled', allowChange);
		$("#firstname").attr('readonly', allowChange);
		$("#lastname").attr('readonly', allowChange);
		$("button#user-update").attr('disabled', allowChange);
		$("button#user-delete").attr('disabled', allowChange);
		allowChange = !allowChange;
	}

	/*
	Utility Functions
	*/
	var fetchData = () => {
		var formData = new FormData();
		formData.append('first_name', $("input#firstname").val());
		formData.append('last_name', $("input#lastname").val());
		formData.append('phone', $("input#phone").val());
		// formData.append('state', $("input#state").val());
		// formData.append('zipcode', $("input#zipcode").val());
		formData.append('tag', $("select#tag option:selected").val());
		return formData;
	};

	var refreshRecords = () => {
		let phone = $('input#phone').val();
		$.ajax({
		   url : '/all/' + phone,
	       dataType:'json',
	       success : (data) => {
		        console.log(data);
		        appendRecord(data);
	       }
		});
	}

});