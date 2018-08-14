$(function(){
	/*
	Click Event
	*/
	$('tr').click(function(){
		let uid = $(this).data('id');
		if (uid == null){
			return
		}
		//undefined
		console.log('clicked: '+ uid);
		if (uid) {
			$.ajax({
				url: '/search/Message/' + uid,
				method: 'GET',
				dataType: 'json'
			}).done(data => {
				showModal(data);
			}).fail(()=> {
				alert('error');
			});
		}
	})

	$('button#delete-tag').click(function(){
		uid = $('.modal').data('id');
		if (uid < 5) {
			return;
		}
		$.ajax({
			url:'/delete/Message/'+uid,
			success: function(data){
				alert(data);
			}
		});
	});

	$('button#create-btn').click(function(){
		createModal();	
	})

	$('#save-change').click(function(){
		var formData = new FormData();
		var dict = get_dict();
		url = "/add/Message"
		if ($('.modal').data('id') != 0) {
			url = "/update/Message/" + $('.modal').data('id');
		}
		console.log(dict);
		if (dict != null) {
			formData.append('tag', dict["tag"]);
			formData.append('tru_tag', dict["tru_tag"]);
			formData.append('tru_indicator', dict["tru_indicator"]);
			formData.append('fal_tag', dict["fal_tag"]);
			formData.append('fal_indicator', dict["fal_indicator"]);
			formData.append('el_tag', dict["el_tag"]);
			formData.append('content', dict["content"]);
			$.ajax({
				url : url,
				type : 'POST',
				data : formData,
				processData: false,  // tell jQuery not to process the data
				contentType: false,  // tell jQuery not to set contentType
				success : (data) => {
					$('.modal').modal('hide');
				}
			}).fail(() => {
				alert('upload error');
			}).complete(() => {
				$(".modal").modal('hide');
			});
		} else {
			alert('not complete');
		}
	});

	var createModal = () => {
		var defaultOption = "ACTION";
		$('.modal').data('id', 0);
		$('.modal-title').text('Create Tag');
		$("#tag[type='text']").val('');
		$("#tru_indicator[type='text']").val('');
		$("#tru_tag").val(defaultOption);
		$("#fal_indicator[type='text']").val('');
		$("#fal_tag").val(defaultOption);
		$("#el_indicator[type='text']").val('');
		$("#el_tag").val(defaultOption);
		$(".modal").modal('show');
	}

	var showModal = (data) => {
		if (data == null) {
			return;
		}
		$('.modal').data('id', data.id);
		$('.modal-title').text('Tag ID: '+data.id);
		$("#tag[type='text']").val(data.tag);
		selectOption('tru_tag', data.tru_tag);
		$("#tru_indicator[type='text']").val(data.tru_indicator);
		selectOption('fal_tag', data.fal_tag);
		$("#fal_indicator[type='text']").val(data.fal_indicator);
		selectOption('el_tag', data.el_tag);
		$("textarea#content").val(data.content);
		$(".modal").modal('show');
	}

	/*
	Utility Function
	*/
	var selectOption = (id, str) => {
		if (str == "NULL") {
			str = 'UNQUALIFIED';
		}
		$('#'+id).val(str).change()
	}

	var get_dict = () => {
		var dict = {};
		var tag = $("#tag[type='text']").val();
		var tru_tag = $("#tru_tag option:selected").val();
		var tru_indicator = $("#tru_indicator[type='text']").val();
		var fal_tag = $("#fal_tag option:selected").val();
		var fal_indicator = $("#fal_indicator[type='text']").val();
		var el_tag = $("#el_tag option:selected").val();
		var content = $("textarea#content").val();
		if (tag == null || tru_tag == null || tru_indicator == null
			|| fal_tag == null || fal_indicator == null ||
			el_tag == null || content == null) {
			return null;
		} else {
			dict["tag"] = tag;
			dict["tru_tag"] = tru_tag;
			dict["tru_indicator"] = tru_indicator;
			dict["fal_tag"] = fal_tag;
			dict["fal_indicator"] = fal_indicator;
			dict["el_tag"] = el_tag;
			dict["content"] = content;
			return dict;
		}
	};

});