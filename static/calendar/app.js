document.addEventListener('DOMContentLoaded', function () {

    var calendarEl = document.getElementById('calendar');

    var calendar = new FullCalendar.Calendar(calendarEl, {
        
        initialView: 'dayGridMonth',
        events: '/get-events/',
        eventClick: function(info) {
            var eventId = info.event.id;
            window.location.href = '/detail/' + eventId;
        },
        locale: 'ja',
        headerToolbar: {
          left: 'prev,today',
          center: 'title,dayGridMonth,timeGridWeek,timeGridDay',
          right: 'next',
        },
        buttonText: {
            today: '今月',
            month: '月',
            week: '週',
            day: '日',
        },
        buttonHints: {
		prev: '前の$0',
		next: '次の$0',
	    },
        
        navLinks: true, // can click day/week names to navigate views
        businessHours: true, // display business hours
        editable: true,
        selectable: true,
        
        
        // googleApi連携
        googleCalendarApiKey: "AIzaSyCj0vHldOkkJ9s1dELuw1FEKBLoDOCZL7E",
	    eventSources: [
    		//自分のカレンダー
    		{
    		    googleCalendarId: 'aws.n.kato@gmail.com'
    		},
    		//祝日カレンダー
    		{
    			googleCalendarId: 'ja.japanese#holiday@group.v.calendar.google.com'
    		}
	    ],
	    
    });
    
    calendar.render();
});
