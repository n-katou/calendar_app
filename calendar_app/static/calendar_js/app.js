document.addEventListener('DOMContentLoaded', function () {

    var calendarEl = document.getElementById('calendar');

    var calendar = new FullCalendar.Calendar(calendarEl, {
        
        initialView: 'dayGridMonth',
        locale: 'ja',
        headerToolbar: {
          left: 'prev,next today',
          center: 'title',
          right: 'dayGridMonth,timeGridWeek,timeGridDay,listDay'
        },
        buttonText: {
            today: '今月',
            month: '月',
            week: '週',
            day: '日',
            list: 'リスト',
            
        },
        navLinks: true, // can click day/week names to navigate views
        businessHours: true, // display business hours
        editable: true,
        selectable: true,
        
        // googleApi連携
        googleCalendarApiKey: "AIzaSyAkL4UivND5nu3usAu3faTP1O-8YHxH9Uo",
	    eventSources: [
    		//自分のカレンダー
    		{
    		    //googleCalendarId: 'naoto.light@gmail.com'
    		},
    		//祝日カレンダー
    		{
    			googleCalendarId: 'ja.japanese#holiday@group.v.calendar.google.com'
    		}
	    ]
	    
    });
    
    calendar.render();
});
