jQuery(document).ready(function($) {

    var printing = ($('#javascript-print-detection').css('display') == 'block') ? true : false;

    if (!printing) {
    	$('#descriptif-accordeon').accordionza({
    		autoPlay: false
    	});
    }

	$("#accordeon-spin").hide();
	$("#descriptif-accordeon").show();

	$("#description-photo-heb img").bind("click", function() {
        $("#descriptif-accordeon li.slide4").trigger('slide');
        return false;
	});

});
