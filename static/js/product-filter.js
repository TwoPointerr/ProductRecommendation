$(document).ready(function(){
    $(".ajaxLoader").hide();
    $("#gender_cat, #sub_cat, #article_type, #sort_by,#color_filter, #priceFilterBtn").on('click', function(){
        var _filterObj={};
        var _minPrice=$('#minPrice').val();
        var _maxPrice=$('#maxPrice').val();
        _filterObj.minPrice= _minPrice;
        _filterObj.maxPrice= _maxPrice;
        $("#gender_cat").each(function(index, ele){
            var _filterVal=$(this).val();
            var _filterKey=$(this).data('filter');
            _filterObj[_filterKey]=Array.from(document.querySelectorAll('input[data-filter='+_filterKey+']:checked')).map(function(el){
                return el.value;
            });
        });

        $("#sub_cat").each(function(index, ele){
            var _filterVal=$(this).val();
            var _filterKey=$(this).data('filter');
            _filterObj[_filterKey]=Array.from(document.querySelectorAll('input[data-filter='+_filterKey+']:checked')).map(function(el){
                return el.value;
            });
        });

        $("#article_type").each(function(index, ele){
            var _filterVal=$(this).val();
            var _filterKey=$(this).data('filter');
            _filterObj[_filterKey]=Array.from(document.querySelectorAll('input[data-filter='+_filterKey+']:checked')).map(function(el){
                return el.value;
            });
        });

        $("#sort_by").each(function(index, ele){
            console.log("this is the list");
            var _filterVal=$(this).val();
            var _filterKey=$(this).data('filter');
            _filterObj[_filterKey]=Array.from(document.querySelectorAll('input[data-filter='+_filterKey+']:checked')).map(function(el){
                return el.value;
            });
        });

        $("#color_filter").each(function(index, ele){
            console.log("this is the list");
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
