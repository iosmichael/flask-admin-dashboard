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

	$("input[type='text']#searchInput").change(function(){
		if ($(this).val() == "") return;
		$.ajax({
	       url : '/search/'+$(this).val(),
	       type : 'POST',
	       processData: false,  // tell jQuery not to process the data
	       contentType: false,  // tell jQuery not to set contentType
	       dataType:'json',
	       success : (data) => {
		        console.log(data);
				appendUser(data.items);
				page = 1;
				updatePage(page);
	       }
		}).fail(()=> {
			alert('search error');
		});
	});

	//click on page number
	$("a.page-link").click(function(){
		let pageNumber = $(this).data('page');
		if (pageNumber == null){
			return
		}
		var formData = new FormData();
		formData.append(filterKey, filterValue);
		$.ajax({
			url: '/page/User/' + pageNumber,
			method: 'POST',
			data: formData,
			processData: false,  // tell jQuery not to process the data
	       	contentType: false,  // tell jQuery not to set contentType
			dataType: 'json'
		}).done(data => {
			console.log(data);
			appendUser(data.items);
			page = pageNumber;
			updatePage(page);
		}).fail(()=> {
			alert('error');
		});
	});
	
	//click on update button
	$('tr').click(function(){
		let uid = $(this).data('id');
		if (uid == null){
			return;
		}
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

	$('input#user-update').click(function(){
		var uid = $("#detail-form").data('id');
		var url = '/update/User/' + uid;
		var formData = fetchData();
		$.ajax({
			url: url,
			method: 'POST',
			processData: false,  // tell jQuery not to process the data
	       	contentType: false,  // tell jQuery not to set contentType
			data: formData
		}).done(data => {
			$("#detail-form").modal('hide');
			refresh();
		}).fail(()=>{
			alert('fail to update');
		})
	});

	$('input#user-delete').click(function(){
		var uid = $("#detail-form").data('id');
		$.ajax({
			url: '/delete/User/' + uid,
			method: 'POST'
		}).done(data => {
			$("#detail-form").modal('hide');
			refresh();
		});
	})

	$('input#send-message').click(function(){
		let message = $('textarea#new-message').val();	
		let phone = $('input#phone-detail').val();
		var formData = new FormData();
		formData.append('phone',phone);
		formData.append('message',message);
		$.ajax({
			url: '/twilio/send',
			method: 'POST',
			data: formData,
			processData: false,
			contentType: false,
			success: (data) => {
				$('textarea#new-message').val('');
				refreshRecords();
			}
		});
	});

	//click on upload button

	$("#fileInput").change((e) => {
		//spinner run
		var formData = new FormData();
		formData.append('file', e.target.files[0]);
		$.ajax({
	       url : '/upload',
	       type : 'POST',
	       data : formData,
	       processData: false,  // tell jQuery not to process the data
	       contentType: false,  // tell jQuery not to set contentType
	       success : (data) => {
	           alert(data);
	       }
		}).fail(()=> {
			alert('upload error');
		});
	});

	//click on filter status button
	$("div#CREATED").click(()=>{
		filterValue = "CREATED";
		filterSearch();
	})
	//click on filter status button
	$("div#POSITIVE").click(()=>{
		filterValue = "POSITIVE";
		filterSearch();
	})
	//click on filter status button
	$("div#NEGATIVE").click(()=>{
		filterValue = "NEGATIVE";
		filterSearch();
	})
	//click on filter status button
	$("div#ARCHIVED").click(()=>{
		filterValue = "ARCHIVED";
		filterSearch();
	})

	$('#enable-change').click(function(){ 
		toggleReadonly();
		console.log("enable change button pressed.") 
	});

	$('input#register-new-user').click(function(){
		console.log('register new user');
		var formData = new FormData();
		let first_name = $('input#register-first-name').val();
		let last_name = $('input#register-last-name').val();
		let phone = $('input#register-phone').val();
		formData.append('first_name', first_name);
		formData.append('last_name', last_name);
		formData.append('phone', phone);
		$.ajax({
			url : '/add/User',
			type : 'POST',
			data : formData,
			processData: false,  // tell jQuery not to process the data
			contentType: false,  // tell jQuery not to set contentType
			success : (data) => {
			    console.log(data);
			    $('.modal#new-form').modal('hide');
			}
		}).fail(() => {
			alert('add user error');
		});
	});

	/*
	UI update methods
	*/
	var filterSearch = () => {
		console.log(filterValue);
		var formData = new FormData();
		formData.append(filterKey, filterValue);
		$.ajax({
	       url : '/page/User/1',
	       type : 'POST',
	       data : formData,
	       processData: false,  // tell jQuery not to process the data
	       contentType: false,  // tell jQuery not to set contentType
	       dataType:'json',
	       success : (data) => {
		        console.log(data);
				appendUser(data.items);
				page = 1;
				updatePage(page);
	       }
		}).fail(()=> {
			alert('search error');
		});
	};

	var appendUser = (users) => {
		let body = $('#table-body').empty();
		if (users == null) {
			return;
		}
		let jusers = users.map((user)=>{
			var row = $("<tr></tr>").data('id', user.id).click(function(){
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
			row.append($("<th scope='row'></th>").text(user.id));
			row.append($("<td></td>").text(user.first_name + " " + user.last_name));
			row.append($("<td></td>").text(user.state));
			row.append($("<td></td>").text(user.zipcode));
			row.append($("<td></td>").text(user.dob));
			row.append($("<td></td>").text(user.sex));
			row.append($("<td></td>").text(user.phone));
			return row
		});
		jusers.forEach(juser => {
			body.append(juser);
		});
	};

	var appendRecord = (records) => {
		$('form.chat .messages').empty();
		if (records == null){
			return;
		}
		let jrecords = records.map((record) => {
			//record.delivered
			console.log(record);
			responsiveChatPush('form.chat', record.is_delivered, record.is_client, record.time, record.content);
		})
	}

	var updateModal = function (data){
		if (allowChange) {
			toggleReadonly();
		}
		$("#detail-form").data("id", data.id);
		$("#detail-form .card").show();
		$("#firstname-detail").val(data.first_name);
		$("#lastname-detail").val(data.last_name);
		$("#phone-detail").val(data.phone);
		$("#state-detail").val(data.state);
		$("#zipcode-detail").val(data.zipcode);
		$("#tag-detail").val(data.tag);
		$("#last-detail").val(data.last_response);
		console.log('/all/'+data.phone);
		$.ajax({
		   url : '/all/' + data.phone,
	       dataType:'json',
	       success : (data) => {
		        appendRecord(data);
	       }
		});
		$("#detail-form").modal('show');
	};


	var updatePage = (page) =>{
		var pageList = [];
		if(page <= 3){
			pageList = [1, 2, 3, 4, 5];
		}else{
			pageList=[page-2, page-1, page, page+1, page+2];
		}
		var links = $(".page-item.number > a.page-link");
		links.each(function(index, link){
			$.data(link, 'page', pageList[index]);
			$(link).text(pageList[index]);
		})
	};

	/*
	Utility Functions
	*/
	var fetchData = () => {
		var formData = new FormData();
		formData.append('first_name', $("input#firstname-detail").val());
		formData.append('last_name', $("input#lastname-detail").val());
		formData.append('phone', $("input#phone-detail").val());
		formData.append('state', $("input#state-detail").val());
		formData.append('zipcode', $("input#zipcode-detail").val());
		formData.append('tag', $("select#tag-detail option:selected").val());
		return formData;
	};

	var refresh = () => {
		var formData = new FormData();
		formData.append(filterKey, filterValue);
		$.ajax({
			url: '/page/User/' + page,
			method: 'POST',
			data: formData,
			processData: false,  // tell jQuery not to process the data
	       	contentType: false,  // tell jQuery not to set contentType
			dataType: 'json'
		}).done(data => {
			console.log(data);
			appendUser(data.items);
			updatePage(page);
		}).fail(()=> {
			alert('error');
		});
	}

	var refreshRecords = () => {
		let phone = $('input#phone-detail').val();
		$.ajax({
		   url : '/all/' + phone,
	       dataType:'json',
	       success : (data) => {
		        console.log(data);
		        appendRecord(data);
	       }
		});
	}

	var toggleReadonly = () => {
		$("#phone-detail").attr('readonly', allowChange);
		$("#tag-detail").attr('disabled', allowChange);
		$("#firstname-detail").attr('readonly', allowChange);
		$("#lastname-detail").attr('readonly', allowChange);
		$("#state-detail").attr('readonly', allowChange);
		$("#zipcode-detail").attr('readonly', allowChange);
		$("input#user-update").attr('disabled', allowChange);
		$("input#user-delete").attr('disabled', allowChange);
		allowChange = !allowChange;
	}

	var responsiveChatPush = (element, is_delivered, is_client, date, message) => {
	    var originClass;
	    if (is_client == false) {
	        originClass = 'myMessage';
	    } else {
	        originClass = 'fromThem';
	    }
	    var deliver = is_delivered ? 'delivered' : 'pending';
	    if (is_client) {
	    	deliver = "";
	    }
    	$(element + ' .messages').append('<div class="message"><div class="' + originClass + '"><p>' + 
    		message + '</p><date><b>' + deliver + '</b> ' + date + '</date></div></div>');
	};

});