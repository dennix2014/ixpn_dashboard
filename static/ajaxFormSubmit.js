$(document).ready(function() {
    $('.dateinput').attr('type', 'date');      
});

$('.reset-button').on('click', function(){
    $("select").each(function() { this.selectedIndex = 0 });
    $(".numberinput").val("");
    $(".dateinput").val("");
});
$(document).on('click', '.confirm-delete', function(){
    return confirm('Are you sure you want to delete this?');
})