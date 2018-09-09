/*

Name    : Responsive HTML5 Chat

Responsive HTML5 Chat helps you to create useful chatbox on your website easly. 
You can change skin and sizes. You can read the installation and support documentation 
before you begin. If you do not find the answer, do not hesitate to send a message to me.

Owner   : Vatanay Ozbeyli
Web     : www.vatanay.com
Support : hi@vatanay.com

*/

function showLatestMessage() {
    $(element).find('.messages').scrollTop($(element).find('.messages').height());
}

// $(element + ' > span').addClass("spinner");
// $(element + ' > span').removeClass("spinner");

// function responsiveChatPush(element, is_client, date, message) {
//     var originClass;
//     if (is_client == false) {
//         originClass = 'myMessage';
//     } else {
//         originClass = 'fromThem';
//     }
//     $(element + ' .messages').append('<div class="message"><div class="' + originClass + '"><p>' + message + '</p><date> ' + date + '</date></div></div>');
// }
