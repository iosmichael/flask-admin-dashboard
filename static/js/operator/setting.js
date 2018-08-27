$(function(){


	

	//profile edit
	$('a#setting-profile-edit').click(function(){

	});
	//profile update
	$('input.btn#setting-profile-update').click(function(){

	});

	var fetchSystemSetting = () => {
		let autoMessage = $('textarea#setting-auto-message').val();
		let replyIndicator = $('input#setting-reply-indicator').val();
		let checkBox = $('input#setting-enable-scheduler').val();
		return {
			'autoMessage': autoMessage,
			'replyIndicator': replyIndicator,
			'enableScheduler': checkBox
		}
	}

	var fetchTwilioSetting = () => {

	}

	var fetchProfileSetting = () => {
		let username = $('input#setting-profile-username').val();
		let title = $('input#setting-profile-title');
		return {
			'username': username,
			'title': title
		}
	}

});