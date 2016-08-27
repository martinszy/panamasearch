 $(function(){
//-------------------
var w1;
var h1;


$(document).ready(function() {
  
  loadMain();

});


function loadMain(){


        var form = $('#formulario');
        $("input[name='file']").on("change", function(){ event.preventDefault();  form_code(); });
        $(form).submit(function(event) { event.preventDefault(); form_code();  });

       
        //--------------------
        function form_code(){

            var formData = new FormData($("#formulario")[0]);
            var formData2 = $(form).serialize();

            var ruta = "#";
            $.ajax({
                url: ruta,
                type: "POST",
                data: formData2,
                contentType: false,
                processData: false,
                beforeSend: function() {
                    // setting a timeout
                    $("#loading_cont").show(500);
                },
                error : function(xhr, status) {
                    $("#loading_cont").hide(500);
                    $("#resultado ul").html("<li>.no carga file.</li>");
                },               
                success: function(datos){
                   //$("#respuesta").html(datos);
                   $("#loading_cont").hide(500);
                   $("#resultado ul").append("<li>.cargando file.</li>");
                },
                complete:function(data){ 
                    $("#loading_cont").hide(500);
                    $("#resultado ul").append("<li>"+formData+formData2+"</li>");
                   
                }
            });


        }
        //--------Form Code------------    
      

   

}//-------------loadMain-----------------





//------------------
});