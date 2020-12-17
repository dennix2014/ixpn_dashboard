$(document).ready(function() {
    $('.dateinput').attr('type', 'date');      
});

$('.reset-button').on('click', function(){
    $("select").each(function() { this.selectedIndex = 0 });
    $(".numberinput").val("");
    $(".dateinput").val("");
});
