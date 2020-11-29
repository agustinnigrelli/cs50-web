/*global swal*/

function validate_login() {
  var username = document.forms["login"]["username"].value;
  var password = document.forms["login"]["password"].value;
  if (username == "") {
    swal({
        title: "Who are you?",
        text: "It seems that you forgot to say your name"
        });
    return false;
  } else if (password ==""){
      swal({
          title: "Not so fast!",
          text: "It seems that you forgot to put your password"
          });
      return false;
  }
}

function validate_account() {
  var fname = document.forms["account"]["fname"].value;
  var lname = document.forms["account"]["lname"].value;
  var city = document.forms["account"]["city"].value;
  var state = document.forms["account"]["state"].value;
  if (fname == "" || lname == "" || city == "" || state =="") {
    swal({
        title: "Ups!",
        text: "You must not leave any blank fields"
        });
    return false;
  }
}

function validate_password() {
  var password = document.forms["password"]["password"].value;
  var newpassword = document.forms["password"]["newpassword"].value;
  var newpasswordcon = document.forms["password"]["newpasswordcon"].value;
  if (password == "") {
    swal({
        title: "Not so fast!",
        text: "Ir order to change your password, you must first provide it"
        });
    return false;
  } else if (newpassword =="" || newpasswordcon == ""){
      swal({
          title: "Pending confirmation",
          text: "You must provide the new password twice"
          });
      return false;
  }
}

function validate_register() {
  var regusername = document.forms["register"]["regusername"].value;
  var regemail = document.forms["register"]["regemail"].value;
  var regpassword = document.forms["register"]["regpassword"].value;
  var regpasswordcon = document.forms["register"]["regpasswordcon"].value;
  if (regusername == "") {
    swal({
        title: "Ups!",
        text: "You didn't put an username"
        });
    return false;
  } else if (regemail ==""){
      swal({
          title: "Ups!",
          text: "You must provide an e-mail"
          });
      return false;
  } else if (regpassword == "" || regpasswordcon == ""){
      swal({
          title: "Ups!",
          text: "Password and/or confirmation pending"
          });
          return false;
  }
}

function validate_tutor() {
  var subject = document.forms["tutor"]["subject"].value;
  var title = document.forms["tutor"]["title"].value;
  var body = document.forms["tutor"]["body"].value;
  var price = document.forms["tutor"]["price"].value;
  var phone = document.forms["tutor"]["phone"].value;
  var email = document.forms["tutor"]["email"].value;
  if(subject=="empty" || title == "" || body == "" || price == "" || phone == "" || email == ""){
    swal({
      title: "Complete everything!",
      text: "Every field is important. Please don't leave any blank field"
    });
    return false;
  }
}

function validate_student() {
  var subject = document.forms["student"]["subject"].value;
  var title = document.forms["student"]["title"].value;
  var body = document.forms["student"]["body"].value;
  var phone = document.forms["tutor"]["phone"].value;
  var email = document.forms["tutor"]["email"].value;
  if(subject == "" || title == "" || body == "" || phone == "" || email == ""){
    swal({
      title: "Complete everything!",
      text: "Every field is important. Please don't leavy any blank field"
    });
    return false;
  }
}