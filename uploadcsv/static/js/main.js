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
        //$(form).submit(function(event) { event.preventDefault(); form_code();  });


        //--------------------
        function form_code(){

            var formData = new FormData($("#formulario")[0]);
            var formData2 = $(form).serialize();

            var ruta = "/";
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





//-------------------------function ver csv desde link--------------------------------------
function verCSV(url_){         
  Papa.parse(url_, {
    download: true,
    complete: function(results){ 
        $("#resultadoCSV table").html('');  //para que no se acumulen vistas de CSV

        for(var i=0;i<results.data.length;i++){ 

               $("#resultadoCSV table").append(
                    "<tr>"+
                    "<td>"+results.data[i][0]+"</td>"+
                    "<td>"+results.data[i][1]+"</td>"+
                    "<td>"+results.data[i][2]+"</td>"+
                    "<td>"+results.data[i][3]+"</td>"+
                    "</tr>"
                );
        }                        
      }        
  });                 
   
}
//-------------------------------------------------------------------