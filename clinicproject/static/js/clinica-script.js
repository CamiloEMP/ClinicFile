$(document).ready(function(){
    var popover = new bootstrap.Popover(document.querySelector('.navbar'), {
        container: 'body'
      })
    $("#confirmar").prop("disabled", null ); 
    const filtroPaciente = $("#filtro");
    const filtroEstadoCita = $("#selectEstados");
    const filtroLabelEstadoCita = $("label[For=selectEstados]");
    const filtroFechaCita = $("#fecha");

    const fechaInput =  $("#FechaInput");
    const selectMedico = $("#selectMedico");
    const inputFiltrar = $("#inputFiltrar");
    filtroPaciente.hide();
    
    filtroEstadoCita.hide();
    filtroLabelEstadoCita.hide();

    filtroFechaCita.hide();
    

    fechaInput.hide();
    selectMedico.hide();
    inputFiltrar.hide();

    $(".filtrocitamedico li input").change(function() {
        if (["filtros-1", "filtros-2"].includes($(this).attr("id"))) {
            filtroPaciente.show();
        } else{
            filtroPaciente.hide();
        }    
        if ($(this).attr("id") === 'filtros-3') {
            filtroEstadoCita.show();
            filtroLabelEstadoCita.show();
        } else {
            filtroEstadoCita.hide();
            filtroLabelEstadoCita.hide();
        }
        if ($(this).attr("id") === 'filtros-4') {
            filtroFechaCita.show();
        } else {
            filtroFechaCita.hide();
        }
    });

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

    $("#terminos").click(function(){
        let isEnabled = $("#terminos").is(":checked");
        if (isEnabled) {
            $("#confirmar").prop("disabled", null ); 
        } else {
            $("#confirmar").prop("disabled", "disabled" );
        }
        
    });
});

$(function() {

  });
