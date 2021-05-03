$(document).ready(function(){
    $(".ajaxLoader").hide();
    $(".form-check-input").on('click', function(){
        var _filterObj={};
        $(".form-check-input").each(function(index, ele){
            var _filterVal=$(this).val();
            var _filterKey=$(this).data('filter');
            _filterObj[_filterKey]=Array.from(document.querySelectorAll('input[data-filter='+_filterKey+']:checked')).map(function(el){
                return el.value;
            });
        });
        console.log(_filterObj)
        //Ajax Functionality
        $.ajax({
            url: '/filter-data',
            data: _filterObj,
            dataType:'json',
            beforeSend:function(){
                $(".ajaxLoader").show();
            },
            success:function(res){
                console.log(res);
                $("#filteredProducts").html(res.data);
                $(".ajaxLoader").hide();
            }
        });

    });
});