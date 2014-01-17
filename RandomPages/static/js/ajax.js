$(document).ready(function() {
    $('#toolbar-title').click( function () {
        $.get("/test/"+this.id+"/", function(data) {

            $("#tb-stumble-frame").attr("src",data[0]);

        });
    });


    $('#toolbar-discover').click( function () {
        $.get("/discover/"+this.id+"/", function(data) {

              $("#tb-stumble-frame").attr("src",data[0]);

        });
    });

    /*$('#toolbar-like').click( function () {
       
        $.get("/like/"+this.id+"/");
        
    });

    $('#toolbar-dislike').click( function () {
       
        $.get("/dislike/"+this.id+"/);

    });*/

    $('#search-twitter').click( function () {
        
        $.get("/search/"+$("#search").val()+"/", function(data) {

            //alert(data[0]);
            $("#random-page").hide();
            $('#tweet1').text(data[0]);
            //$('#tweet1')[0].innerHTML=data[0];
            $("#tweet1").attr("href",data[1]);

        });
    });


});


