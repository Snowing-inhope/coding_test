$('.btn1').on('click', start_long_task);

function start_long_task() {
    var id={'id':$("#text1").val()};
    $.ajax({
        url:"/goodinfo/",
        data:id,
        dataType: 'json',
        success:function(result){
            addBox(result.goodinfo);
        }
    })
}
function addBox(data){
    $.each(data,function(i,item){
        $("#box").append("<tr class='product'>"+
        "<td>"+item[0]+"</td>"+
        "<td>"+item[1]+"</td>"+
        "<td>"+item[2]+"</td>"+
        "<td>"+item[3]+"</td>"+
        "<td>"+item[4]+"</td>"+
        "<td>"+item[5]+"</td>"+
        "<td>"+item[6]+"</td>"+
        "</tr>");
    });
}