$(function(){
	$.ajax({
       url : '/summary'+$(this).val(),
       type : 'POST',
       processData: false,  // tell jQuery not to process the data
       contentType: false,  // tell jQuery not to set contentType
       dataType:'json',
       success : (data) => {
	        console.log(data);
	        $('.number#summary-new').empty();
			$('.number#summary-new').append($('<strong></strong>').text(data.new));
			$('.number#summary-positive').empty();
			$('.number#summary-positive').append($('<strong></strong>').text(data.positive));
			$('.number#summary-negative').empty();
			$('.number#summary-negative').append($('<strong></strong>').text(data.negative));
			$('.number#summary-archived').empty();
			$('.number#summary-archived').append($('<strong></strong>').text(data.archived));
       }
	}).fail(()=> {
		alert('summary update error');
	});
});