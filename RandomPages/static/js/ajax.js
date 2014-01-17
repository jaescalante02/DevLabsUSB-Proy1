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

    $('#toolbar-like').click( function () {
        $.get("/discover/"+this.id+"/", function(data) {

              $("#tb-stumble-frame").attr("src",data[0]);

        });
    });

    $('#toolbar-dislike').click( function () {
        $.get("/discover/"+this.id+"/", function(data) {

              $("#tb-stumble-frame").attr("src",data[0]);

        });
    });

});
