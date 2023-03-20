function create_table(category,e){
    $.ajax({
        type: 'GET',
        url: `table_${category}/`,
        success: function (json) {
            const table_data = JSON.stringify(json['rendered_table']).replaceAll(/\\n|"/g,"");
            if($(`#ret_${category}`).children().length == 0)
                $(`#ret_${category}`).append(table_data);
            console.log("data pass success", json);
        },
        error: function (xhr, errmsg, err) {
            console.log(xhr.status + ": " + xhr.responseText);
        }
    });
}