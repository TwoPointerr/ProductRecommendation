// function isInputCharacter(event){

//     var patt = /^[a-zA-Z][a-zA-Z\s]+$/;
//     if (a.value.test(patt) == false) {
//         document.getElementById('sp1').innerHTML = "Please enter name in proper format";
//     return false;
// }

// }

function validSeller() {
    // var namevalidation = /^[a-zA-Z][a-zA-Z\s]+$/;
    var emailvalidation = /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/;
    var phonenumbervalidation = /^(\+\d{1,3}[- ]?)?\d{10}$/;
    var companyname = document.forms["companydetailForm"]["companyname"].value;
    var description = document.forms["companydetailForm"]["description"].value;
    var companynumber = document.forms["companydetailForm"]["companynumber"].value;
    var companyemail = document.forms["companydetailForm"]["companyemail"].value;
    console.log(companynumber)
    console.log("Prem Mevada")
    var error = 0;
    // var pw = document.getElementsByClassName("unique_password")[0].value;
    // var confirm_pw = document.getElementsByClassName("cfpassword")[0].value;
  
    //firstname validation
    if(companyname == ""){
        document.getElementById("message-companyname").innerHTML =
        "The field is empty"; 
        error = error + 1;  
    }
    // else if(namevalidation.test(firstname) == false) {
    //   document.getElementById("message-firstname").innerHTML =
    //     "Please enter name in proper format";
    //     error = error + 1;   
    // }
    //lastname validation
    if(description == ""){
        document.getElementById("message-description").innerHTML =
        "This field cannot be left empty"
        error = error + 1
    }
  
    // else if (namevalidation.test(lastname) == false) {
    //   document.getElementById("message-lastname").innerHTML =
    //     "Please enter name in proper format";
    //     error = error + 1;
    // }
    //username validation
    if(companynumber == ""){
        document.getElementById("message-companynumber").innerHTML =
        "This field cannot be left empty"
        error = error + 1;  
    }
    else if(phonenumbervalidation.test(companynumber) == false){
        document.getElementById("message-companynumber").innerHTML =
        "Please enter the phonenumber in correct format"
        error = error + 1;
    }
    //email validation
    if(companyemail == ""){
        document.getElementById("message-email").innerHTML =
        "This field cannot be left empty"
        error = error + 1;  
    }
    else if (emailvalidation.test(companyemail) == false) {
      document.getElementById("message-email").innerHTML =
        "Please enter email in proper format eg: abcd@email.com";
        error = error + 1;
    }
    //password validation
    // if(pw == ""){
    //     document.getElementById("message-password").innerHTML =
    //     "This field cannot be left empty"
    //     error = error + 1;  
    // }
    // else if(pw.length < 8){
    //     document.getElementById("message-password").innerHTML =
    //     "Password length must be atleast 8 characters"
    //     error = error + 1;  
    // }
    // else if(pw.length > 15){
    //     document.getElementById("message-password").innerHTML =
    //     "Password length must not exceed 15 characters" 
    //     error = error + 1;  
    // }
    // else if (pw !== confirm_pw) {
    //   document.getElementById("message-password").innerHTML = "Passwords don't match";
    //   error = error + 1;
    // }
  
    if(error !=0){       
        return false;
    }
  }
  
  // function verifyPassword() {
  //   var pw = document.getElementById("password").value;
  //   var confirm_pw = document.getElementById("cfpassword").value;
  //   //to check empty password field
  //   if (pw !== confirm_pw) {
  //     document.getElementById("message").innerHTML = "Passwords don't match";
  //     return false;
  //   }
  // }
  