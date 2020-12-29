$(document).ready(function() {
    $('.dateinput').attr('type', 'date');      
});

$('.reset-button').on('click', function(){
    $("select").each(function() { this.selectedIndex = 0 });
    $(".numberinput").val("");
    $(".dateinput").val("");
    let url = $("#Url").attr("data-url");
    window.location.href = url;
});

$(document).on('click', '.confirm-delete', function(){
    return confirm('Are you sure you want to delete this?');
})


$(document).ready(function() {
    $('form select').on('change', function() {
      $('#submitFilter').click();
 
    });
 });

 $(document).ready(function() {
    $('form input').on('change', function() {
      $('#submitFilter').click();
 
    });
 });

 $(".hidden-filter-icon").click(function(){
    $(".tty").toggle();
  });


  var expanded = false;

  function showCheckboxes() {
    var checkboxes = document.getElementById("checkboxes");
    if (!expanded) {
      checkboxes.style.display = "block";
      expanded = true;
    } else {
      checkboxes.style.display = "none";
      expanded = false;
    }
  }
$(document).ready(function () {
    let classes = ['.index', '.member', '.pop', '.portc', '.membership', '.status',
                    '.no_of_ports', '.fees_anum', '.fees_qtr', '.fees_mon', '.date']
    $(".submit-cols").click(function(){
        $("#dropdownMenuButton").click();
        $('.index').hide();
        for (i = 0; i < classes.length; i++) {
            $(classes[i]).hide();
          }
    var selectedLanguage = new Array();
    $('input[name="port_connection_column"]:checked').each(function() {
    selectedLanguage.push(this.value);
    for (j = 0; j < selectedLanguage.length; j++) {
        $(selectedLanguage[j]).show();
    }
    
    });
    });
    });


    var checks = document.querySelectorAll(".oggg");
    var max = 7;
    for (var i = 0; i < checks.length; i++)
      checks[i].onclick = selectiveCheck;
    function selectiveCheck (event) {
      var checkedChecks = document.querySelectorAll(".oggg:checked");
      if (checkedChecks.length >= max + 1) {
        alert('you can only select 7 columns at a time')
        return false;   
      }
      
    }


$(function() {      
    let isMobile = window.matchMedia("only screen and (max-width: 760px)").matches;

    if (isMobile) {
        alert('mobile')
    }
});