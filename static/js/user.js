// // setup call function when clicked

// $(function () {
// 	var tagFilter = null;
// 	var page = 1;
// 	var allowChange = false;
// 	var filterKey = 'tag';
// 	var filterValue = 'CREATED';
// 	/*
// 	Click event methods
// 	*/
// 	//click on page number
// 	$(".page-control .page-link").click(function(){
// 		let pageNumber = $(this).data('page');
// 		if (pageNumber == null){
// 			return
// 		}
// 		var formData = new FormData();
// 		formData.append(filterKey, filterValue);
// 		$.ajax({
// 			url: '/page/User/' + pageNumber,
// 			method: 'POST',
// 			data: formData,
// 			processData: false,  // tell jQuery not to process the data
// 	       	contentType: false,  // tell jQuery not to set contentType
// 			dataType: 'json'
// 		}).done(data => {
// 			console.log(data);
// 			appendUser(data.items);
// 			page = pageNumber;
// 			updatePage(page);
// 		}).fail(()=> {
// 			alert('error');
// 		});
// 	});
// 	//click on user info
// 	$('tr').click(function(){
// 		let uid = $(this).data('id');
// 		if (uid == null){
// 			return
// 		}
// 		//undefined
// 		console.log('clicked: '+ uid);
// 		if (uid) {
// 			$.ajax({
// 				url: '/search/User/' + uid,
// 				method: 'GET',
// 				dataType: 'json'
// 			}).done(data => {
// 				updateModal(data);
// 			}).fail(()=> {
// 				alert('error');
// 			});
// 		}
// 	});
// 	//click on update button
// 	$('.btn#user-update').click(function(){
// 		var uid = $("#detail").data('id');
// 		var url = '/update/User/' + uid;
// 		var formData = fetchData();
// 		if (uid == 0){
// 			console.log('add');
// 			url = '/add/User';
// 		}
// 		$.ajax({
// 			url: url,
// 			method: 'POST',
// 			processData: false,  // tell jQuery not to process the data
// 	       	contentType: false,  // tell jQuery not to set contentType
// 			data: formData
// 		}).done(data => {
// 			$(".modal").modal('hide');
// 			refresh();
// 		}).fail(()=>{
// 			alert('fail to update');
// 		})
// 	});

// 	$('.btn#user-delete').click(function(){
// 		var uid = $("#detail").data('id');
// 		$.ajax({
// 			url: '/delete/User/' + uid,
// 			method: 'POST'
// 		}).done(data => {
// 			$(".modal").modal('hide');
// 			refresh();
// 		});
// 	})

// 	$('button#send-message').click(function(){
// 		let message = $('textarea#message').val();	
// 		let phone = $('input#phone').val();
// 		var formData = new FormData();
// 		formData.append('phone',phone);
// 		formData.append('message',message);
// 		$.ajax({
// 			url: '/send',
// 			method: 'POST',
// 			data: formData,
// 			processData: false,
// 			contentType: false,
// 			success: (data) => {
// 				$('textarea#message').val('');
// 				refreshRecords();
// 			}
// 		});
// 	});

// 	//click on upload button
// 	$(".btn[type='file']").change((e) => {
// 		//spinner run
// 		var formData = new FormData();
// 		formData.append('file', e.target.files[0]);
// 		$.ajax({
// 	       url : '/upload',
// 	       type : 'POST',
// 	       data : formData,
// 	       processData: false,  // tell jQuery not to process the data
// 	       contentType: false,  // tell jQuery not to set contentType
// 	       success : (data) => {
// 	           alert(data);
// 	       }
// 		}).fail(()=> {
// 			alert('upload error');
// 		});
// 	});
// 	//click on filter status button
// 	$("select#status-filter").change((e)=>{
// 		filterValue = $("select option:selected").val()
// 		var formData = new FormData();
// 		formData.append(filterKey, filterValue);
// 		$.ajax({
// 	       url : '/page/User/1',
// 	       type : 'POST',
// 	       data : formData,
// 	       processData: false,  // tell jQuery not to process the data
// 	       contentType: false,  // tell jQuery not to set contentType
// 	       dataType:'json',
// 	       success : (data) => {
// 		        console.log(data);
// 				appendUser(data.items);
// 				page = 1;
// 				updatePage(page);
// 	       }
// 		}).fail(()=> {
// 			alert('search error');
// 		});
// 	})

// 	$(".btn#status-filter-btn").click(function(){
// 		createModal();
// 	});

// 	$("input#allow-change-input").click(function(){
// 		toggleReadonly();
// 	})

// 	/*
// 	UI update methods
// 	*/
// 	var appendUser = (users) => {
// 		let body = $('#js-tbody').empty();
// 		if (users == null) {
// 			return;
// 		}
// 		let jusers = users.map((user)=>{
// 			var row = $("<tr></tr>").data('id', user.id).click(function(){
// 				let uid = $(this).data('id');
// 				if (uid == null){
// 					return
// 				}
// 				//undefined
// 				console.log('clicked: '+ uid);
// 				if (uid) {
// 					$.ajax({
// 						url: '/search/User/' + uid,
// 						method: 'GET',
// 						dataType: 'json'
// 					}).done(data => {
// 						updateModal(data);
// 					}).fail(()=> {
// 						alert('error');
// 					});
// 				}
// 			});
// 			row.append($("<th scope='row'></th>").text(user.id));
// 			row.append($("<td></td>").text(user.first_name + " " + user.last_name));
// 			row.append($("<td></td>").text(user.state));
// 			row.append($("<td></td>").text(user.zipcode));
// 			row.append($("<td></td>").text(user.dob));
// 			row.append($("<td></td>").text(user.sex));
// 			row.append($("<td></td>").text(user.phone));
// 			return row
// 		});
// 		jusers.forEach(juser => {
// 			body.append(juser);
// 		});
// 	};

// 	var appendRecord = (records) => {
// 		let body = $('div#records').empty();
// 		if (records == null){
// 			return;
// 		}
// 		let jrecords = records.map((record) => {
// 			var row = $("<div class='record'></div>");
// 			if (!record.receive) {
// 				row.append($("<strong></strong>").text('caller texted:'));
// 			}else{
// 				row.append($("<strong></strong>").text('bot texted:'));
// 			}
// 			row.append($("<br/>"));
// 			row.append($("<span></span>").text(record.content));
// 			row.append($("<br/>"));
// 			// row.append($("<span></span>").text(record.time));
// 			return row;
// 		})
// 		jrecords.forEach(juser => {
// 			body.append(juser);
// 		});
// 	}

// 	var createModal = () => {
// 		if (!allowChange) {
// 			toggleReadonly();
// 			$("input#allow-change-input").prop('checked', true);
// 		}
// 		$("#detail").data('id', 0);
// 		$(".modal-title").text('Create User');
// 		$("div#records").empty();
// 		$("#firstname").val('');
// 		$("#lastname").val('');
// 		$("#phone").val('');
// 		$("#state").val('NA');
// 		$("#zipcode").val('NA');
// 		$("#tag").val('CREATED');
// 		$(".modal").modal('show');
// 	}

// 	var updateModal = (data) => {
// 		//modal show
// 		if (allowChange) {
// 			toggleReadonly();
// 			$("input#allow-change-input").prop('checked', false);
// 		}
// 		$("#firstname").val(data.first_name);
// 		$("#lastname").val(data.last_name);
// 		$("#phone").val(data.phone);
// 		$("#state").val(data.state);
// 		$("#zipcode").val(data.zipcode);
// 		$("#tag").val(data.tag);
// 		$("#last").val(data.last_response);
// 		$("#modalLabel").text('User ID:' + data.id);
// 		$("#detail").data('id', data.id);
// 		$.ajax({
// 		   url : '/all/' + data.phone,
// 	       dataType:'json',
// 	       success : (data) => {
// 		        console.log(data);
// 		        appendRecord(data);
// 	       }
// 		});
// 		$("#detail").modal('show');
// 	};

// 	var updatePage = (page) =>{
// 		var pageList = [];
// 		if(page <= 3){
// 			pageList = [1, 2, 3, 4, 5];
// 		}else{
// 			pageList=[page-2, page-1, page, page+1, page+2];
// 		}
// 		var links = $(".page-item.number > a.page-link");
// 		links.each(function(index, link){
// 			$.data(link, 'page', pageList[index]);
// 			$(link).text(pageList[index]);
// 		})
// 	};

// 	var updateAlert = (alert) => {
// 		$('#jalert').text(alert);
// 	};

// 	var toggleReadonly = () => {
// 		$("#phone").attr('readonly', allowChange);
// 		$("#tag").attr('disabled', allowChange);
// 		$("#firstname").attr('readonly', allowChange);
// 		$("#lastname").attr('readonly', allowChange);
// 		$("button#user-update").attr('disabled', allowChange);
// 		$("button#user-delete").attr('disabled', allowChange);
// 		allowChange = !allowChange;
// 	}

// 	/*
// 	Utility Functions
// 	*/
// 	var fetchData = () => {
// 		var formData = new FormData();
// 		formData.append('first_name', $("input#firstname").val());
// 		formData.append('last_name', $("input#lastname").val());
// 		formData.append('phone', $("input#phone").val());
// 		// formData.append('state', $("input#state").val());
// 		// formData.append('zipcode', $("input#zipcode").val());
// 		formData.append('tag', $("select#tag option:selected").val());
// 		return formData;
// 	};

// 	var refresh = () => {
// 		var formData = new FormData();
// 		formData.append(filterKey, filterValue);
// 		$.ajax({
// 			url: '/page/User/' + page,
// 			method: 'POST',
// 			data: formData,
// 			processData: false,  // tell jQuery not to process the data
// 	       	contentType: false,  // tell jQuery not to set contentType
// 			dataType: 'json'
// 		}).done(data => {
// 			console.log(data);
// 			appendUser(data.items);
// 			updatePage(page);
// 		}).fail(()=> {
// 			alert('error');
// 		});
// 	}

// 	var refreshRecords = () => {
// 		let phone = $('input#phone').val();
// 		$.ajax({
// 		   url : '/all/' + phone,
// 	       dataType:'json',
// 	       success : (data) => {
// 		        console.log(data);
// 		        appendRecord(data);
// 	       }
// 		});
// 	}

// });