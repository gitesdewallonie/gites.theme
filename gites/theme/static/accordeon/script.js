jQuery(document).ready(function($) {

	$('#descriptif-accordeon').accordionza({
		autoPlay: false,
	});
	$("#accordeon-spin").hide();
	$("#descriptif-accordeon").show();

	$("#description-photo-heb img").bind("click", function() {
        $("#descriptif-accordeon li.slide4").trigger('slide');
        return false;
	});

});
