function login() {
    $("[id$='login']").bind("click",function(){
        usr=$("[name='userName']").eq(0).val().length==0 ? $("[name='userName']").eq(1).val():$("[name='userName']").eq(0).val()
        pwd=$("[name$='passwd']").eq(0).val().length==0 ? $("[name$='passwd']").eq(1).val() : $("[name$='passwd']").eq(0).val()
        $.get("../login",
        {
           userName:usr,
           passwd:pwd
        },
        function(data){
            if(data==0) {
                alert("用户名或密码错误!")
            } else {
                $("#login-panel").hide();
                $("#loginOk").html("<strong>Welcome! "+usr+"</strong>");
                $("#loginLink").hide();
                location.href="../index"
            } 
        }
            
        );//end of post

    })
}

function logout() {
    $("#logoutLink").click(function() {
        $.get("../logout",function(){
            $("#loginOk").hide();
            $("#logoutLink").html("<p></p>");
            location.href="../index" 
    }


    );//end of get()
  

    }//end function
    );//end click
}


function sTestCase() {
     $("[href='#caseInfoTab']").click(function(){
         channel = $(this).attr("name");
         $.get("../case_info",
         { 
            platformId:channel,
            part:1
         },
         function(data){
             $("div#myTabContent").remove();
             $("div#caseTable").html(data);
         }
 
         );//end of post
 
     })
 }



function sTaskHistory() {
     $("[href='#taskHistoryTab']").click(function(){
         channel = $(this).attr("name")
         $.get("../task_history",
         { 
            platformId:channel
         },
         function(data){
             $("div#taskTable").html(data)
             $("div#myTabContent").remove()
         }
 
         );//end of post
 
     })
 }



function sEnv() {
     $("[href='#envTab']").click(function(){
         channel = $(this).attr("name")
         $.get("../env_check",
         { 
            platformId:channel
         },
         function(data){
             $("div#envTable").html(data)
             $("div#myTabContent").remove()
         }
 
         );//end of post
 
     })
 }

function sModifyEnv() {
     $("[href='#deleteEnv']").click(function(){
          envId = $(this).attr("name")
          $.get("../env_check",
          {
              modify:1,
              envId:envId,
              op:"7"
              
          },
          function(data){
             $("div#envTable").html(data)
             $("div#myTabContent").remove()
          }// end of getFunction

          );//end of get
       } // end of function
     ) //end of click
     
     $("[href='#startEnv']").click(function(){
          envId = $(this).attr("name")
          $.get("../env_check",
          {
              modify:1,
              envId:envId,
              op:"1"
              
          },
          function(data){
             $("div#envTable").html(data)
             $("div#myTabContent").remove()
          }// end of getFunction

          );//end of get
       } // end of function
     ) //end of click
     
     $("[href='#stopEnv']").click(function(){
          envId = $(this).attr("name")
          $.get("../env_check",
          {
              modify:1,
              envId:envId,
              op:"4"
              
          },
          function(data){
             $("div#envTable").html(data)
             $("div#myTabContent").remove()
          }// end of getFunction

          );//end of get
       } // end of function
     ) //end of click
}

//////////////////////////////////////
$(function(){
    login();
    logout();
    sTestCase();
    sTaskHistory();
    sEnv();
    sModifyEnv();
    //sDataSource();
});
