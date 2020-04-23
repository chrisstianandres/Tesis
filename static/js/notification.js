function message(texto) {
    $.isLoading({
         text: "<strong>"+texto+"</strong>",
         tpl: '<span class="isloading-wrapper %wrapper%"><i class="fa fa-spin fa-spinner fa-2x fa-spin"></i><br>%text%</span>',
     });
    setTimeout( function(){
       $.isLoading("hide");
    },1000);
}