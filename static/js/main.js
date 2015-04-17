window.onload= function(){
$.ajax({
	url: 'test/',
	type: 'get',
	dataType: 'json',
	success: function(data) {
		alert(data.test);
	},
	failure: function(data) {
		alert('error');
	}


});
};