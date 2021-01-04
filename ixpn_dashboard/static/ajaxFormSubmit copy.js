
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


function resetColumns() {
    for (i = 0; i < classez.length; i++) {
        $(classez[i]).hide();
    }
};


var classez = ['.index', '.member', '.pop', '.portc', '.membership', '.status',
                    '.switch', '.switch_port', '.fees_anum', '.fees_qtr', '.fees_mon', '.date']
var mobile_screen_size = ['.member', '.pop', '.fees_anum', ];
var normal_screen_size = ['.index', '.member', '.pop', '.portc', '.membership', '.fees_anum', '.date' ]

var isMobile = window.matchMedia("only screen and (max-width: 760px)").matches;


$(document).ready(function () {
    resetColumns();
    
    var switchId = $('#id_switch').val();
    if (switchId) {
        loadSwitchPorts()
    }
    
    $('#id_switch_port option').prop('disabled', true);
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


function loadSwitchPorts () {
    var switchId = $('#id_switch').val();
    var urll = $("#Urll").attr("data-ports-url");
    
    var boundSwitchPortName = $("#swiname").attr("data-ports-name");
    var boundSwitchPortid = $("#swiid").attr("data-ports-id");

    $.ajax({ 
      url: urll,
      data: {
        'switch': switchId,
        'switch_port_id' : boundSwitchPortid,
        'switch_port_name' : boundSwitchPortName,
      },
      success: function (data) { 
        $("#id_switch_port").html(data.result);
      }
    });

}


$("#id_switch").on('change', function () {
    var switchId = $('#id_switch').val();
    if (switchId) {
        loadSwitchPorts()
    }
});