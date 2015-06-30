function deleteCase() { 
     $("[href='#deleteCase']").live("click",function(){ 
     var datas=[]; 
     $("#caseInfoTable tbody tr").each(function() { 
         checked = $(this).children().eq(0).children().prop("checked") 
         if(checked){  
              id = $(this).attr("name"), 
              datas.push(id)
         } 
     });//end of each
     if(datas.length==0) {
         alert("请选择需要删除的用例！")
         return;
     } 
     var platformId = $("#platformId").val()  
     if(confirm("确定要删除吗？")){ 
          var cases = JSON.stringify(datas) 
          $.get("../case_edit", 
                 { 
                     deleted:1, 
                     cases:cases 
                 }, 
                 function(data){ 
                     if(data==1) {
                         self.location="case_info?platformId=" + platformId;
                     }
                 }//end of post function  
          ); //end of post 
      } //end of if 
      } //end of click func
     ); 
 }

function addCase() {
   $("[href='#addCase']").click(function() {
     platformId = $("#platformId").val()
     $.get("../case_edit",
         {
            add:1,
            platformId:platformId
         },
         function(data){
            if(data==1){
                self.location="case_info?platformId=" + platformId;
            }
         }
     )//end of get
     }//end of funcion
   );//end of click
}
function copyCase() {
    $("[href='#copyCases']").live("click",function(){
            var datas=[];
            var id=0; 
            $("#caseInfoTable tbody tr").each(function() {
                checked = $(this).children().eq(0).children().prop("checked");
                if(checked){ 
                    id = $(this).attr("name");
                }
             });//end of each
             datas.push(id)
             var platformId = $("#platformId").val() 
             var cases = JSON.stringify(datas)
             $.get("../case_edit",
                {
                    copy:1,
                    platformId:platformId,
                    cases:cases
                },
                function(data){
                    self.location="case_edit?id="+data;
                }//end of post function 
             ); //end of post
    });
}

function addFromFile() {
    $("#addFromFile").live("click",function(){
        platformId = $(this).attr("name")
        var filePath = prompt("请输入文件地址路径: 如qt103:/disk1/casefile","")
        if($.trim(filePath) == "") { 
           alert("请输入正确的用例路径！");
           return;
        }     
        platformId = $(this).attr("name")
        $.get("../case_edit",
        {
            file:filePath,
            platformId:platformId
        },
        function(data) {
            if(data==1) {
              alert("请先添加测试源文件！具体查看logs/all.log")
            } else {
              alert("操作成功！")
            }
            self.location="case_info?platformId="+platformId;
        }// end of get function
        )//end of get  
    }// end of click function

   
    );//end of click
}

function verify(row) {
   for(var i in row) {
      if($.trim(row[i])=="") //expect para could be null
          if (i =="expect" || i =="id"){
             continue;
          } else {
             alert(i +" can not be null")
             return false
          }
   }
   return true
}

function saveCaseTable() {
    $("#save").click(function() {
         var row = {
             id        : $("#CaseId").val(),
             name      : $("#CaseName").val(),
             suiteId   : $("#SuiteId").val(),
             suiteName : $("#SuiteName").val(),
             xml       : $("#XmlFile").find("option:selected").text(),
             command   : $("#CaseCommand").val(),
             param     : $("#CasePara").val(),
             matchType : $("#XmlName").find("option:selected").text(),
             expect    : $("#expect").val(),
             log       : $("#log").val(),
             platformId: $("#platformId").val(),
             detail: $("#CaseDetail").val()
         }// end of row
         if(!verify(row)) {
             alert("用例未填写完整!");
             return; 
         }
         var cases = JSON.stringify(row)
         var platId = row['platformId']
         $.get("../case_edit",
                {
                    save:1,
                    platformId:platId,
                    cases:cases
                },
                function(data){
                    //alert(data)
                    if(data==0) {
                      alert("失败！没有找到数据源文件");
                    } else {
                      self.location="case_info?platformId=" + platId;
                    }
                }//end of post function 
         ); //end of post
      }//endo of function

    )// end of click 

}


function CaseEditTab() { 
    $("[href='#caseEditTab']").click(function(){ 
      channel = $(this).attr("name") 
      $.get("../case_edit", 
      {  
        platformId:channel,
      }, 
      function(data){ 
        $("div#caseTable").html(data) 
        $("div#myTabContent").empty() 
        //$("div#bs-docs-example").empty() 
      } 
    );//end of post 
    }) 
} 

function searchBySuite() { 
    $("[href='#suiteNameS']").live("click",function(){ 
      platformId = $(this).attr("name")
      suiteName = $("#search").val() 
      $.get("../case_info", 
      {  
        platformId:platformId,
        searchText:suiteName,
        searchType:0,
        part:1
      }, 
      function(data){ 
        $("div#caseTable").html(data) 
        $("div#myTabContent").empty() 
        //$("div#bs-docs-example").empty() 
      } 
    );//end of post 
    }) 
} 
function searchByCaseName() { 
    $("[href='#caseNameS']").live("click",function(){ 
      platformId = $(this).attr("name")
      caseName = $(this).parent().parent().parent().find("input").val()
      $.get("../case_info", 
      {  
        platformId:platformId,
        searchText:caseName,
        searchType:1,
        part:1
      }, 
      function(data){ 
        $("div#caseTable").html(data); 
        $("div#myTabContent").empty();
        //$("div#bs-docs-example").empty() 
      } 
    );//end of post 
    }) 
} 
function saveXmlFile(){
    $("#saveXmlFile").click(function(){
      platformId = $("#platformId").val()
      content = $("#xmlContent").val()
      name = $("#xmlName").val()
      type = $('input[name="xmlType"]:checked').attr("id")
      $.get("../case_edit",
      {
        xml:1,
        name:name,
        platformId: platformId,
        content:content,
        type:type
      },function(data){
        alert("上传成功！")
        $("#addXmlFile").hide()
      }
      ) // end of get
    } //end of function
    );//end of click

}

function importXmlFile() {
   $("#addXmlFromFile").live("click",function() {
      platformId = $(this).attr("name");
      var filePath = prompt("请输入文件地址路径: 如qt103:/disk1/xmlFile。(多个用分号分隔)","");
      if($.trim(filePath) == "") { 
         alert("请输入正确的用例路径！");
         return;
      }     
      $.get("../case_edit",
      {
          importXml:1,
          platformId: platformId,
          filePath: filePath
      },
      function(data){
          if(data == 0) {
            alert("操作成功！")
          } else {
            alert("操作失败！")
          }
          self.location="case_info?platformId=" + platformId;     
      }// end of get function
      );//end of get
   }// end of click function
   );//end of click 

}

function editXmlFile() {
   $("[href='#editXmlFile']").live("click",function(){
        xmlName = $(this).parent().parent().find("td").eq(4).find("input").eq(0).attr("value")
        $("#editXmlName").html(xmlName)
        platformId = $("#platformId").val()
        $.get("../case_edit",
          {
             getXmlContent: 1,
             xmlName: xmlName,
             platformId: platformId
          },
          function(data){
             $("#editXmlContent").html(data); 
          });//end of get 
    }// end of click function

   )//end of live

   $("#editXmlSave").click(function() {
       xmlName = $("#editXmlName").html()
       content = $("#editXmlContent").val()
       platformId = $("#platformId").val()
       $.get("../case_edit",
        {
            saveXmlEdit:1,
            xmlName: xmlName,
            platformId: platformId,
            xmlContent: content
        },
        function(data) {
            alert("保存成功！")
        }// end of get function
       )//end of get
    }// end of clicl function
   )//end of click
}

function clickCb(){
  check =  $(this).prop("checked")
  if(check)
     $(this).prop("checked",false);
  else
     $(this).prop("checked",true);
}

function checkAll(){
  check = $(this).prop("checked");
  if(check){
     $(":checkbox").prop("checked",false);
     $(this).prop("checked",false);
  } else {
     $(":checkbox").prop("checked",true);
     $(this).prop("checked",true);
  }
}
//////////////////////////////////////
$(function(){
    addCase();
    copyCase();
    saveCaseTable();
    CaseEditTab();
    addFromFile();
    saveXmlFile();
    importXmlFile();
    editXmlFile();
    searchBySuite();
    searchByCaseName();
    clickCb();
    checkAll();
    deleteCase();
});
