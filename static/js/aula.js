$(function () {
    $('#frm_objeto').formValidation({
        message: 'This value is not valid',
        icon: {
            valid: 'glyphicon glyphicon-ok',
            invalid: 'glyphicon glyphicon-remove',
            validating: 'glyphicon glyphicon-refresh'
        },
        fields: {
            numero: {
                 validators: {
                    notEmpty: {
                        message: 'Este campo es obligatorio'
                    },
                    stringLength: {
                        min: 1,
                    },
                    regexp: {
                        regexp: /^[0-9]/i,
                        message: 'Solo introduzca numeros'
                    },
                }
            }
        }
    }).on('success.form.fv', function(e) {
    });

});