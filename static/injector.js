$(document).ready(function() {

    //document.getElementById("data").style.display = "none";
    $("#data").hide()

    $("#search").on('submit', function() { 
        //const input = document.getElementById("serial").value

        $.getJSON(
        // {
            '/find_serial',
            {serial: $('#serial').val()}
            // type: 'GET',
            // data: { serial: $('#serial').val() },
            // dataType: 'json',
            /*success:*/ function(data) {
            },
            // error: function(xhr, status, error) {
            //     // yes
            //     console.error('Error: ...')
            // }
        // }
        );

        //document.getElementById("data").style.display = "block";
        $("#data").show()
        
    });
});