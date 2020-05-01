$(function () {
    $('#frm_objeto').formValidation({
        message: 'Esto no es un valor valido',
        icon: {
            valid: 'glyphicon glyphicon-ok',
            invalid: 'glyphicon glyphicon-remove',
            validating: 'glyphicon glyphicon-refresh'
        },
        fields: {
            nombre: {
                validators: {
                    notEmpty: {
                        message: 'Este campo debe ser obligatorio'
                    },
                    stringLength: {
                        min: 3,
                    },
                    regexp: {
                        regexp: /^[A-ZáéíóúÁÉÍÓÚñÑ\s]+$/i,
                        message: 'Solo introduzca letras'
                    },
                }
            },
        }
    });
});
