// function isInputCharacter(event){

//     var patt = /^[a-zA-Z][a-zA-Z\s]+$/;
//     if (a.value.test(patt) == false) {
//         document.getElementById('sp1').innerHTML = "Please enter name in proper format";
//     return false;
// }

// }

function validName() {
  var namevalidation = /^[a-zA-Z][a-zA-Z\s]+$/;
  var emailvalidation = /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/;
  var firstname = document.forms["signupForm"]["firstname"].value;
  var lastname = document.forms["signupForm"]["lastname"].value;
  var username = document.forms["signupForm"]["username"].value;
  var email = document.forms["signupForm"]["email"].value;
  var error = 0;
  var pw = document.getElementsByClassName("unique_password")[0].value;
  var confirm_pw = document.getElementsByClassName("cfpassword")[0].value;

  //firstname validation
  if(firstname == ""){
      document.getElementById("message-firstname").innerHTML =
      "The field is empty"; 
      error = error + 1;  
  }
  else if(namevalidation.test(firstname) == false) {
    document.getElementById("message-firstname").innerHTML =
      "Please enter name in proper format";
      error = error + 1;   
  }
  //lastname validation
  if(lastname == ""){
      document.getElementById("message-lastname").innerHTML =
      "This field cannot be left empty"
      error = error + 1
  }

  else if (namevalidation.test(lastname) == false) {
    document.getElementById("message-lastname").innerHTML =
      "Please enter name in proper format";
      error = error + 1;
  }
  //username validation
  if(username == ""){
      document.getElementById("message-username").innerHTML =
      "This field cannot be left empty"
      error = error + 1;  
  }
  //email validation
  if(email == ""){
      document.getElementById("message-email").innerHTML =
      "This field cannot be left empty"
      error = error + 1;  
  }
  else if (emailvalidation.test(email) == false) {
    document.getElementById("message-email").innerHTML =
      "Please enter email in proper format eg: abcd@email.com";
      error = error + 1;
  }
  //password validation
  if(pw == ""){
      document.getElementById("message-password").innerHTML =
      "This field cannot be left empty"
      error = error + 1;  
  }
  else if(pw.length < 8){
      document.getElementById("message-password").innerHTML =
      "Password length must be atleast 8 characters"
      error = error + 1;  
  }
  else if(pw.length > 15){
      document.getElementById("message-password").innerHTML =
      "Password length must not exceed 15 characters" 
      error = error + 1;  
  }
  else if (pw !== confirm_pw) {
    document.getElementById("message-password").innerHTML = "Passwords don't match";
    error = error + 1;
  }

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
