
$(function () {
    $('#frm_objeto').formValidation({
        message: 'Esto no es un valor valido',
        icon: {
            valid: 'glyphicon glyphicon-ok',
            invalid: 'glyphicon glyphicon-remove',
            validating: 'glyphicon glyphicon-refresh'
        },
        fields: {
            nombres: {
                validators: {
                    notEmpty: {
                        message: 'Este campo debe ser obligatorio'
                    },
                    stringLength: {
                        min: 10,
                    },
                    regexp: {
                        regexp: /^[A-ZáéíóúÁÉÍÓÚñÑ\s]+$/i,
                        message: 'Solo introduzca letras'
                    },
                }
            },
            apellidos: {
                validators: {
                    notEmpty: {
                        message: 'Este campo es obligatorio'
                    },
                    stringLength: {
                        min: 5,
                    },
                    regexp: {
                        regexp: /^[A-ZáéíóúÁÉÍÓÚñÑ\s]+$/i,
                        message: 'Solo introduzca letras'
                    },
                }
            },
             cedula: {
                 validators: {
                    notEmpty: {
                        message: 'Este campo es obligatorio'
                    },
                    stringLength: {
                        min: 10,
                    },
                    regexp: {
                        regexp: /^[0-9]/i,
                        message: 'Solo introduzca numeros'
                    },
                }
            }
        }
    });

});
