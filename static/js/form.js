$(document).ready(function() {

	$('form').on('submit', function(event) {
		var user = $('#user').val();
		var useDate = $('#useDate').val();
		// if(!user){
		// 	alert("请输入用户名");
		// 	return false;
		// }
		// if(!useDate){
		// 	alert("请选择日期");
		// 	return false;
		// }
		$.ajax({
			data : {
				grade: $('#select_grade').val(),
				class: $('#select_class').val(),
				course: $('#select_course').val(),
				useDate: useDate,
				subject: $('#subject').val(),
				is_normal:$('#is_normal').val(),
				description:$('#description').val(),
				user : user
			},
			type : 'POST',
			url : '/process'
		})
		.done(function(data) {
			if (data.error) {
				alert(data.error);
			}
			else {
				alert("您已成功登记！");
				location.reload();
				
			}

		});

		event.preventDefault();

	});

});