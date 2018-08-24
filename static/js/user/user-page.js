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
	//click on page number
	$(".page-control .page-link").click(function(){
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
	
	//click on upload button
	$(".btn[type='file']").change((e) => {
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
	$("select#status-filter").change((e)=>{
		filterValue = $("select option:selected").val()
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
	})

	$(".btn#status-filter-btn").click(function(){
		createModal();
	});

	$("input#allow-change-input").click(function(){
		toggleReadonly();
	})

	/*
	UI update methods
	*/
	var appendUser = (users) => {
		let body = $('#js-tbody').empty();
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
	/*
	Utility Functions
	*/

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

});