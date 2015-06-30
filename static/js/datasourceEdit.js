function datasource_update(){
	jQuery(':button[id="datasource_update"]').click(function(){
		//alert(window.location.pathname);
		//xmlName =update_form.XmlName.value;  获取input value值的另外两种写法
		//xmlName=document.getElementById("XmlName").value;
		pathname = window.location.pathname;
		

		xmlName = $("#XmlName").val();
		xmlContent = $("#XmlContent").val();
		xmlType =2;
		error_message =null;
		if (document.getElementById("XmlType_1").checked) {
			xmlType = 1;
		}
		else
			xmlType =0;

		if (!xmlName) {
			//error_message = "XmlName不能为空！";
			alert("XmlName不能为空！");
		}
		else if(!xmlContent){
			//error_message = "XmlContent不能为空！";
			alert("XmlContent不能为空！");
		}
		else if(xmlType==2){
			//error_message = "选择一种XmlType！";
			alert("选择一种XmlType！");
		}
		else{
			jQuery.ajax({
				type:"post",
                datatype:"json",
                url:"/save_update/",
                data:{'pathname':pathname,'xmlName':xmlName,'xmlContent':xmlContent,'xmlType':xmlType},
                error:function(ex){alert(ex.status);},
                success:function(data){                
                           if (data.status=="success") {
                           		alert("保存成功！");
                           		 //history.go(-1);
                           		var url = window.location.toString();
                           		reg = /\/{2}(.*?\/)/;//坑爹js正则不支持(?<= exp)
                           		var host = reg.exec(url)[1];
                           		//alert(host);
                           		window.location.href="http://"+host+"datasource_info";
                           		//alert("step1");
                           		refreshInfo(data.platformId);
                           }        
                }

			});
		}
/*
		if (error_message!=null) {
			//alert(error_message);
			$("#errorInfo").show();
		}
*/

	});
	
}

function datasource_delete_yes(){

	jQuery(':button[id="delete_yes"]').click(function(){
		pathname = window.location.pathname;
		//alert(pathname);
		//alert("123");
		jQuery.ajax({
				type:"post",
                datatype:"json",
                url:"/delete_yes/",
                data:{'pathname':pathname},
                error:function(ex){alert(ex.status);},
                success:function(data){
                	if (data.status=="success") {
                		alert("删除成功");
                		window.location.href="http://127.0.0.1:8000/datasource_info";
                		refreshInfo(data.platformId);
                	}
                }
            });
	});

}

/*
function checkbox_checked(){
	
	$("#toggle-all").click(function(){

		//alert($("#toggle-all").prop("checked"));
		//alert("123");
		if ($("#toggle-all").prop("checked")==true) {
			$('input[type="checkbox"]').prop('checked', true);
		}
		else
			$('input[type="checkbox"]').prop('checked', false);

	});

}
*/
function checkAll(obj){
	if ($(obj).prop("checked")==true) {
			$('input[type="checkbox"]').prop('checked', true);
		}
		else
			$('input[type="checkbox"]').prop('checked', false);

	var selectedIds =0;
	var n =1;
	$(":checkbox").each(function(i){
		if ($(this).prop("checked")==true) {
			selectedIds =selectedIds+","+$(this).prop("value") ;
			n++;
		}
	});

	alert(selectedIds);
}


function delete_selected(){
	var selectedIds =0;
	var n =1;
	$(":checkbox").each(function(i){
		if ($(this).prop("checked")==true) {
			selectedIds =selectedIds+","+$(this).prop("value") ;
			n++;
		}
	});

	alert(selectedIds);
	if (selectedIds!=0) {

		jQuery.ajax({
			type:"post",
            datatype:"json",
            url:"/delete_selected/",
            data:{'selectedIds':selectedIds},
            error:function(ex){alert(ex);},
            success:function(data){
              	if (data.status=="success") {
                	//alert(data.num);
                	//window.location.href="http://127.0.0.1:8000/datasource_info";
                	//refreshInfo();
                	refreshInfo(data.platformId);
                }
            }
        });
	}
	
	
}

function export_excel(){
	var selectedIds =0;
	var selected_Ids = new Array();
	var n =1;
	$(":checkbox").each(function(i){
		if ($(this).prop("checked")==true) {
//			selectedIds =selectedIds+","+$(this).prop("value") ;
			selected_Ids[n]=$(this).prop("value");
			alert(selected_Ids[n]);
			var downloadUrl ='download/'+selected_Ids[n];
			if (selected_Ids[n]!=-1) {
				//alert(downloadUrl);
				window.open(downloadUrl);
			}

			
			n++;
			
		}
	});
	//alert(n);


//	var downloadUrl ='download/'+selectedIds;
//	window.open(downloadUrl);
	//window.location.reload();

}

function upload_xml(){
	
}

function refreshInfo(platformId){
	//alert("step2");
	$("[href='#dataSourceTab'][name='platformId']").click()
	//alert("step3");
	$.get("../datasource_info",
        {
           platformId:channel
        },
       function(data){
           $("div#dataTable").html(data)
           $("div#myTab").hide()
           
       }

        );
}

function sDataSource() {
    $("[href='#dataSourceTab']").click(function(){
        channel = $(this).attr("name")
        //alert(channel)
        $.get("../datasource_info",
        { 
           platformId:channel
        },
       function(data){
           $("div#dataTable").html(data)
           $("div#myTab").hide()
           
       }

        );//end of post

    })
}
function data_toggle(){
/*
	$('a[data-toggle="tab"]').on('show', function (e) {
        log(e)
    });
    $('a[data-toggle="tab"]').on('shown', function (e) {
        log(e.target) // activated tab
        log(e.relatedTarget) // previous tab
    });
*/
    $('.selectpicker').selectpicker();

    $( ".box" )
    .find( ".box-title" )
    .prepend( "<i class='icon icon-chevron-up chevron'></i>")
    .end()
    .find( ".box-content" );

    $( ".box-title .icon.chevron" ).click(function() {
        $( this ).toggleClass( "icon-chevron-up" ).toggleClass( "icon-chevron-down" );
        $( this ).parents( ".box:first" ).find( ".box-content" ).toggle('fast');
    });
    
    $( ".column" ).disableSelection();

}


$(document).ready(function(){

	datasource_update();
	data_toggle();
	datasource_delete_yes();
	sDataSource();
	upload_xml();
	//checkbox_checked();
	//datasource_delete_no();
	$('#file_upload').uploadify({
    'uploader'  : '/uploadify/uploadify.swf',
    'script'    : '/uploadify/uploadify.php',
    'cancelImg' : '/uploadify/cancel.png',
    'folder'    : '/uploads',
    'auto'      : true
  });




})
