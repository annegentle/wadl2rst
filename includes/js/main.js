$(document).ready(function() {
	
	// banner and associated localStorage
	
	var banner = localStorage.getItem('banner');

	if (banner == 'closed') {
        $('#banner-announcement-container').hide();
    }

	$(function() {
		$('.banner-announcement-close').click(function() {
			$('#banner-announcement-container').slideUp('fast');
			localStorage.setItem('banner', 'closed');
			return false;
		});
	});
  
	// feedback and associated localStorage
	
	var feedback = localStorage.getItem('feedback');

	if (feedback == 'yes') {
    $('.feedback-decision a.yes').addClass('active');
  }
  
	if (feedback == 'no') {
    $('.feedback-decision a.no').addClass('active');
  }
  
	$(function() {
		$('.feedback-decision a.yes').click(function() {
			$(this).addClass('active');
			$('.feedback-decision a.no').removeClass('active');
			localStorage.setItem('feedback', 'yes');
			return false;
		});
	});
  
	$(function() {
		$('.feedback-decision a.no').click(function() {
			$(this).addClass('active');
			$('.feedback-decision a.yes').removeClass('active');
			localStorage.setItem('feedback', 'no');
			return false;
		});
	});
    
	// tooltips
	
    $(function() {
		$('.tooltip').tooltip();
		return false;
	});
  
  $('.note p').before('<h4>Please note:</h4>');
			
});

