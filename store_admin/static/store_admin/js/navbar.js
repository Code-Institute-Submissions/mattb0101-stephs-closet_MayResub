$(document).ready(function(){
    $('#sidenavCollapse').on('click', function() {
        $('#sidenav, #admin-content').toggleClass('active');
    }); 
    

    $('#dismiss').on('click', function() {
        $('#sidenav').addClass('active');
    });
});
    
