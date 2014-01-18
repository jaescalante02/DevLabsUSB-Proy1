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

            $("#random-page").hide();
            numtw = data.length/2;
            i=0;
            while(i<numtw){

              $('#tweet'+(i+1)).show();
              $('#tweet'+(i+1)).text(data[2*i]);
              //$('#tweet1')[0].innerHTML=data[0];
              $("#tweet"+(i+1)).attr("name",data[2*i+1]);
              i=i+1;
            }

        });
    });

    $('.tweet').click( function () {
        $.get("/add/"+$("#"+this.id).attr("name")+"/", function(data) {

              $("#tb-stumble-frame").attr("src",data);
              $("#random-page").show();

            

        });
    });


});


