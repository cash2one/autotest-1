$(document).ready(function(){
    var taskid;
    var tag;
    var interval;
    var cbT;
    var line_begin=1;
    var lastlogtime =0;
    var button_excute;
    var log = function(s){
        window.console && console.log(s)
    };

    $('.selectpicker').selectpicker();


//右上角收起按钮


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

    jQuery(':button[group="newtest"]').click(function(){
        button_excute = this;
        tag=$(this).attr('tag');
        svnaddr = jQuery.trim(jQuery(jQuery.format('#txt{0}ImprSvn',tag)).val() || "");
        resinsvnaddr =jQuery.trim(jQuery(jQuery.format('#txt{0}ResinSvn',tag)).val() || "");
        testsuit =jQuery.trim(jQuery(jQuery.format('#txt{0}Testsuit',tag)).val() || "");
        status = true;

        if (tag != "Dspbs" && tag != "Convtrack") {
            if (!svnaddr) {
                $("#NewUnionErrorInfo").show();
                //alert("请输入展示服务地址！");
            }
            else if (!resinsvnaddr) {
                alert("请输入resin地址！");
            }
            else if (!testsuit||testsuit=="无测试用例"){
                alert("无测试用例！无法创建任务！");
            }
            else{
                $(this).button('loading');
                jQuery.ajax({
                type:"post",
                datatype:"json",
                url:"/start_task/",
                data:{'item1':svnaddr,"item2":resinsvnaddr ,'item3':testsuit,'tag':tag},
                error:function(ex){alert(ex.statusTest);},
                success:function(data){
                    //alert(data.status);
                    //alert(data.taskid);
                    taskid = data.taskid;
                    cbT = jQuery(jQuery.format('#txt{0}StartNewTestLog',tag));
                    startLogging();
                    /*
                    $("#union1").bind('click',function(){
                        window.open('../task_report?taskId='+data.taskid,'_blank');
                        
                    })
                    */
                    jQuery(jQuery.format('#New{0}Result',tag)).bind('click',function(){
                        window.open('../task_report?taskId='+data.taskid,'_blank');
                    }
                        )


                    
                    
                    

                }
                });
            }


        }
        else if (tag=="Dspbs"&&!svnaddr) {
            alert("请输入dsp服务地址！");
        }
        else if (tag=="Dspbs"&&(!testsuit||testsuit=="无测试用例")) {
            alert("无测试用例！无法创建任务！");
        }else if(tag=="Convtrack"&&!svnaddr){
            alert("请输入convtrack服务地址！");
        }else if (tag=="Convtrack"&&(!testsuit||testsuit=="无测试用例")){
            alert("无测试用例！无法创建任务！");
        }
        else{
            jQuery.ajax({
            type:"post",
            datatype:"json",
            url:"/start_task/",
            data:{'item1':svnaddr,"item2":resinsvnaddr ,'item3':testsuit,'tag':tag},
            error:function(ex){alert(ex.statusTest);},
            success:function(data){  
                    taskid = data.taskid;
                    cbT = jQuery(jQuery.format('#txt{0}StartNewTestLog',tag));
                    startLogging();
                    jQuery(jQuery.format('#New{0}Result',tag)).bind('click',function(){
                        window.open('../task_report?taskId='+data.taskid,'_blank');
                    }
                    )
            }
            });
        }

        
    });

    jQuery(':button[group="oldtest"]').click(function(){
        tag=$(this).attr('tag');
        env = jQuery.trim(jQuery(jQuery.format('#txt{0}Env',tag)).val() || "");
        testsuit =jQuery.trim(jQuery(jQuery.format('#txt{0}Testsuit2',tag)).val() || "");
        //alert(env);
        //alert(testsuit);
        //alert(tag)
        jQuery.ajax({
            type:"post",
            datatype:"json",
            url:"/restart_task/",
            data:{'item1':env,"item2":testsuit,'tag':tag},
            error:function(ex){alert(ex.statusTest);},
            success:function(data){
                    taskid = data.taskid;
                    cbT = jQuery(jQuery.format('#txt{0}StartOldTestLog',tag));
                    startLogging();
                    jQuery(jQuery.format('#Old{0}Result',tag)).bind('click',function(){
                        window.open('../task_report?taskId='+data.taskid,'_blank');
                    }
                        )              

            }
        })
        

    });

function startLogging(){

    qinglog();
    getLog();

}


function getLog(){
    jQuery.ajax({
            type:"post",
            datatype:"json",
            url:"/read_log/",
            data:{'taskid':taskid,'line_begin':line_begin,'lastlogtime':lastlogtime},
            error:function(ex){alert(ex.status);},
            success:function(data){
                //alert(data.status);
                //alert(data.line_begin);
                //alert(data.line_end);
                //alert(data.result);
                if (data.status == 2) {
                    $(button_excute).button('complete');
                    stopLogging();
                    return;
                }
                else if (data.status == 1) {
                    //alert("step0+++++data.logstatus:"+data.logstatus+"++++data.status:"+data.status)
                    lastlogtime = data["lastlogtime"];
                }
                else if (data.status == 0&&data.logstatus == 0) {
                    line_begin =data["line_begin"];
                    lastlogtime = data["lastlogtime"];
                    //alert(lastlogtime)
                    cbT.val(cbT.val()+data.result+"\r");
                    cbT.scrollTop(cbT.height()+cbT.scrollTop());

                }
                else if (data.status == 0&&data.logstatus == 1) {
                    lastlogtime = data["lastlogtime"];
                    //alert("step1+++++data.logstatus:"+data.logstatus+"++++data.status:"+data.status)
                }
                else{
                    //alert("step2+++++data.logstatus:"+data.logstatus+"++++data.status:"+data.status)
                    $(button_excute).button('complete');
                    stopLogging();
                    return;
                }

                interval = setTimeout(getLog,1000);
                                           
            }

        })

}

function stopLogging(){
        
        clearTimeout(interval);
       }

function qinglog(){
        cbT.val("");
       }


function delete_product(){
    
        tag=$(this).attr('tag');
        env = jQuery.trim(jQuery(jQuery.format('#txt{0}Env',tag)).val() || "");
        testsuit =jQuery.trim(jQuery(jQuery.format('#txt{0}Testsuit2',tag)).val() || "");
        //alert(env);
        //alert(testsuit);
        //alert(tag)
        jQuery.ajax({
            type:"post",
            datatype:"json",
            url:"/restart_task/",
            data:{'item1':env,"item2":testsuit,'tag':tag},
            error:function(ex){alert(ex.statusTest);},
            success:function(data){
                    taskid = data.taskid;
                    cbT = jQuery(jQuery.format('#txt{0}StartOldTestLog',tag));
                    startLogging();
                    jQuery(jQuery.format('#Old{0}Result',tag)).bind('click',function(){
                        window.open('../task_report?taskId='+data.taskid,'_blank');
                    }
                        )              

            }
        })
}


});


