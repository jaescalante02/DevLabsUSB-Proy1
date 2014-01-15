$(document).ready(function() {
$('#toolbar-title').click( function () {
$.get("/test/"+this.id+"/", function(data) {

  $("#tb-stumble-frame").attr("src",data[0]);

});
});
});
