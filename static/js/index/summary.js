$(function(){
	$.ajax({
       url : '/summary'+$(this).val(),
       type : 'POST',
       processData: false,  // tell jQuery not to process the data
       contentType: false,  // tell jQuery not to set contentType
       dataType:'json',
       success : (data) => {
	        console.log(data);
			$('.number#summary-new').text('<strong>'+data.new+'</strong>');
			$('.number#summary-positive').text('<strong>'+data.positive+'</strong>');
			$('.number#summary-negative').text('<strong>'+data.negative+'</strong>');
			$('.number#summary-archived').text('<strong>'+data.archived+'</strong>');
       }
	}).fail(()=> {
		alert('summary update error');
	});
});