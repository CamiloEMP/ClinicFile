$(document).ready(function(){
    var popover = new bootstrap.Popover(document.querySelector('.navbar'), {
        container: 'body'
      })
    const fechaInput =  $("#FechaInput");
    const selectMedico = $("#selectMedico");
    const inputFiltrar = $("#inputFiltrar");
    fechaInput.hide();
    selectMedico.hide();
    inputFiltrar.hide();

    $(".form-check-input").change(function() {
        if ($(this).attr("id") === 'FechaLabel') {
            fechaInput.show();
        } else {
            fechaInput.hide();
        }
        if ($(this).attr("id") === "medico"){
            selectMedico.show();
        } else{
            selectMedico.hide();
        }
        if (["paciente", "idPaciente"].includes($(this).attr("id"))) {
            inputFiltrar.show();
        } else{
            inputFiltrar.hide();
        }
    });
});

$(function() {
    $("#flexCheckDefault").click(function(){
        let isEnabled = $("#flexCheckDefault").is(":checked");
        if (isEnabled) {
            $("#buttonEnviar").prop("disabled", null ); 
        } else {
            $("#buttonEnviar").prop("disabled", "disabled" );
        }
        
    });
  });
