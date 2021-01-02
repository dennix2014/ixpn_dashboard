$('.reset-button').on('click', function(){
    $("select").each(function() { this.selectedIndex = 0 });
    $(".numberinput").val("");
    $(".dateinput").val("");
    var url = $("#Url").attr("data-url");
    window.location.href = url;
});

$(document).on('click', '.confirm-delete', function(){
    return confirm('Are you sure you want to delete this?');
})


 $(".hidden-filter-icon").click(function(){
    $(".tty").toggle();
  });


var classez = ['.index', '.member', '.pop', '.portc', '.membership', '.status',
                    '.no_of_ports', '.fees_anum', '.fees_qtr', '.fees_mon', '.date']
var mobile_screen_size = ['.member', '.pop', '.fees_anum', ];
var normal_screen_size = ['.index', '.member', '.pop', '.portc', '.membership', '.no_of_ports', '.fees_anum', ]
var isMobile = window.matchMedia("only screen and (max-width: 760px)").matches;

function resetColumns() {
    for (i = 0; i < classez.length; i++) {
        $(classez[i]).hide();
      }
};
$(document).ready(function () {
    resetColumns();
    $('#id_pot option').prop('disabled', true);
    $('.dateinput').attr('type', 'date');

    $('#filter-form select, #filter-form input').on('change', function() {
        $('#submitFilter').click();
      });

    if (isMobile) {
        for (i = 0; i < mobile_screen_size.length; i++) {
            $(mobile_screen_size[i]).show();
            var id = '#' + mobile_screen_size[i].substring(1);
            $(id).prop('checked', true).change();
          }
    }else {
        for (i = 0; i < normal_screen_size.length; i++) {
            $(normal_screen_size[i]).show();
            var id = '#' + normal_screen_size[i].substring(1);
            $(id).prop('checked', true).change();
          }
    }
    
    $(".submit-cols").click(function(){
        $("#dropdownMenuButton").click();
        resetColumns()
        
        var selectedColumn = new Array();
        $('input[name="port_connection_column"]:checked').each(function() {
        selectedColumn.push(this.value);
        for (j = 0; j < selectedColumn.length; j++) {
            $(selectedColumn[j]).show();
        }
    
        });
    });
});


var checks = document.querySelectorAll(".columns");

var max;
if (isMobile) {
    max = 4
}else {
    max = 8
}

for (var i = 0; i < checks.length; i++)
  checks[i].onclick = selectiveCheck;
function selectiveCheck (event) {
  var checkedChecks = document.querySelectorAll(".columns:checked");
  if (checkedChecks.length >= max + 1) {
    alert(`You can only select ${max} columns at a time`)
    return false;   
  }
  
};


$("#id_switch").on('change', function () {
    var urll = $("#Urll").attr("data-ports-url");
    var switchId = $(this).val();
    console.log(urll)
    console.log(switchId)

    $.ajax({ 
      url: urll,
      data: {
        'switch': switchId
      },
      success: function (data) { 
        $("#id_pot").html(data.result);
      }
    });

  });