$(function () {
    $('#frm_objeto').formValidation({
        message: 'This value is not valid',
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
    }).on('success.form.fv', function(e) {
        e.preventDefault();
    });

});