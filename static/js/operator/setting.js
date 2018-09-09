$(function(){
	var infoEditMode = false;
	var twilioEditMode = false;
	var profileEditMode = false;

	$('a#setting-info-edit').click(function(){
		toggleSystemSetting();
	});

	$('input#setting-info-update').click(function(){
		let formData = fetchSystemSetting();
		$.ajax({
			url: '/firebase/update/info',
			method: 'POST',
			data: formData,
			processData: false,  // tell jQuery not to process the data
	       	contentType: false,  // tell jQuery not to set contentType
			dataType: 'json'
		}).done(data => {
			console.log(data);
			refreshSystemSetting(data);
		}).fail((e)=> {
			alert(e);
		});
	});

	//twilio edit
	$('a#setting-twilio-edit').click(function(){
		toggleTwilioSetting();
	});
	//twilio update
	$('input.btn#setting-twilio-update').click(function(){
		let formData = fetchTwilioSetting();
		$.ajax({
			url: '/firebase/update/api',
			method: 'POST',
			data: formData,
			processData: false,  // tell jQuery not to process the data
	       	contentType: false,  // tell jQuery not to set contentType
			dataType: 'json'
		}).done(data => {
			refreshTwilioSetting(data);
		}).fail(()=> {
			alert('error');
		});
	})

	//profile edit
	$('a#setting-profile-edit').click(function(){
		toggleProfileSetting();
	});
	//profile update
	$('input.btn#setting-profile-update').click(function(){
		let formData = fetchProfileSetting();
		$.ajax({
			url: '/firebase/update/profile',
			method: 'POST',
			data: formData,
			processData: false,  // tell jQuery not to process the data
	       	contentType: false,  // tell jQuery not to set contentType
			dataType: 'json'
		}).done(data => {
			refreshProfileSetting(data);
		}).fail(()=> {
			alert('error');
		});
	});

	var fetchSystemSetting = () => {
		let autoMessage = $('textarea#setting-info-message').val();
		let replyIndicator = $('input#setting-info-indicator').val();
		let checkBox = $('input#setting-info-scheduler').val();
		let formData = new FormData();
		formData.append("autoMessage", autoMessage);
		formData.append("replyIndicator", replyIndicator);
		formData.append("enableScheduler", checkBox);
		return formData;
	}

	var refreshSystemSetting = (data) => {
		$('textarea#setting-info-message').val(data.autoMessage);
		$('input#setting-info-indicator').val(data.replyIndicator);
		$('input#setting-info-scheduler').val(data.enableScheduler);
	}

	var toggleSystemSetting = () => {
		$('textarea#setting-info-message').attr('readonly', infoEditMode);
		$('input#setting-info-indicator').attr('readonly', infoEditMode);
		$('input#setting-info-scheduler').attr('disabled', infoEditMode);
		$('input.btn#setting-info-update').attr('disabled', infoEditMode);
		infoEditMode != infoEditMode
	}

	var fetchTwilioSetting = () => {
		let twilioAccountSID = $('input#setting-twilio-accountSID').val();
		let twilioAuthToken = $('input#setting-twilio-authToken').val();
		let formData = new FormData();
		formData.append("twilioAccountSID", twilioAccountSID);
		formData.append("twilioAuthToken", twilioAuthToken);
		return formData;
	}

	var refreshTwilioSetting = (data) => {
		$('input#setting-twilio-accountSID').val(data.twilioAccountSID);
		$('input#setting-twilio-authToken').val(data.twilioAuthToken);
	}

	var toggleTwilioSetting = () => {
		$('input#setting-twilio-accountSID').attr('readonly', twilioEditMode);
		$('input#setting-twilio-authToken').attr('readonly', twilioEditMode);
		$('input.btn#setting-twilio-update').attr('disabled', twilioEditMode);
		twilioEditMode != twilioEditMode
	}

	var fetchProfileSetting = () => {
		let username = $('input#setting-profile-username').val();
		let title = $('input#setting-profile-title').val();
		let formData = new FormData();
		formData.append("username", username);
		formData.append("title", title);
		return formData;
	}

	var refreshProfileSetting = (data) => {
		$('input#setting-profile-username').val(data.username);
		$('input#setting-profile-title').val(data.title);
	}

	var toggleProfileSetting = () => {
		$('input#setting-profile-username').attr('readonly', profileEditMode);
		$('input#setting-profile-title').attr('readonly', profileEditMode);
		$('input.btn#setting-profile-update').attr('disabled', twilioEditMode);
		profileEditMode != profileEditMode
	}
});