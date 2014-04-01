/* Javascript for HelloWorldXBlock. */



function HelloWorldXBlock(runtime, element) {

    function updateCount(result) {
        $('.count', element).text(result.count);
        $('.user_count').text(JSON.stringify(result.studentIdCount));
        
        var display_text = "   "
        $.each(result.studentIdCount, function(index, val){
        	var temp_text = JSON.stringify(val['student_id']) + ":" + JSON.stringify(val['count']);
        	display_text = display_text + " " + temp_text;
        	$('.user_count').text(display_text)
        	
        	
        });
        
    }

    var handlerUrl = runtime.handlerUrl(element, 'increment_count');

    $('#C4', element).click(function(eventObject) {
    	console.log(getUrlVars()["student_id"]);
    	var student_id = getUrlVars()["student_id"];
        $.ajax({
            type: "POST",
            url: handlerUrl,
            data: JSON.stringify({"hello": "world", "student_id": student_id}),
            success: updateCount
        });
    });

    $(function ($) {
        /* Here's where you'd do things on page load. */
    });
    
    function getUrlVars()
    {
        var vars = [], hash;
        var hashes = window.location.href.slice(window.location.href.indexOf('?') + 1).split('&');
        for(var i = 0; i < hashes.length; i++)
        {
            hash = hashes[i].split('=');
            vars.push(hash[0]);
            vars[hash[0]] = hash[1];
        }
        return vars;
    }
}