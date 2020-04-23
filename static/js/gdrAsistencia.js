

var tabla =[
    {horarioin,listadoin,asistein}
    ];

window.onload = cargarEventos()

function cargarEventos() {
    document.getElementById("Guardar-Asist").addEventListener("submit", NuevaAsit,false)

}


function NuevaAsit(event) {
    alert("si");
    event.preventDefault();
    var horarioin= document.getElementById("horario").value
    var listadoin= document.getElementById("listado").value
    var asistein= document.getElementById("asiste").value

    var nuevaAsist = {Horario:horarioin,Listado:listadoin,Asistencia:asistein};
    tabla.push(nuevaAsist);


}