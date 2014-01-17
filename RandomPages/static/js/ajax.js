$(document).ready(function() {
$('#toolbar-title').click( function () {
$.get("/test/"+this.id+"/", function(data) {

  $("#tb-stumble-frame").attr("src",data[0]);

});
});

$('#toolbar-buttons').click( function () {
    $.get("/discover/"+this.id+"/", function(data) {

          $("#tb-stumble-frame").attr("src",data[0]);

    });
});
});
