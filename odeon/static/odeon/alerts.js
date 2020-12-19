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
  var oldpassword = document.forms["password"]["oldpassword"].value;
  var newpassword = document.forms["password"]["newpassword"].value;
  var newpasswordcon = document.forms["password"]["newpasswordcon"].value;
  if (oldpassword == "") {
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
  var subject = document.forms["tutor"]["t_subject"].value;
  var title = document.forms["tutor"]["t_title"].value;
  var body = document.forms["tutor"]["t_body"].value;
  var price = document.forms["tutor"]["t_price"].value;
  var phone = document.forms["tutor"]["t_phone"].value;
  var email = document.forms["tutor"]["t_email"].value;

  if(subject == "empty" || title == "" || body == "" || price == "" || phone == "" || email == ""){
    swal({
      title: "Complete everything!",
      text: "Every field is important. Please don't leave any blank field"
    });
    return false;
  }
}

function validate_student() {
  var subject = document.forms["student"]["s_subject"].value;
  var title = document.forms["student"]["s_title"].value;
  var body = document.forms["student"]["s_body"].value;
  var phone = document.forms["student"]["s_phone"].value;
  var email = document.forms["student"]["s_email"].value;

  if(subject == "empty" || title == "" || body == "" || phone == "" || email == ""){
    swal({
      title: "Complete everything!",
      text: "Every field is important. Please don't leav any blank field"
    });
    return false;
  }
}

function confirm_deletion(id) {
  var form = document.querySelector(`#deleteform-${id}`)

  swal({
    title: "Confirm deletion",
    text: "Are you sure you want to delete this announcement?",
    icon: "warning",
    buttons: true,
    dangerMode: true,
  })
  .then((willDelete) => {
    if (willDelete) {
      swal("Announcement deleted", {
        icon: "success",
      })
      .then(function() {
        form.submit();
      });
    } else {
      return false;
    }
    })
}

function confirm_unbookmark(id) {
  var form = document.querySelector(`#unbookmarkform-${id}`)

  swal({
    title: "Are your sure?",
    text: "You are about to unbookmark this announcement",
    icon: "warning",
    buttons: true,
    dangerMode: true,
  })
  .then((willDelete) => {
    if (willDelete) {
      swal("Announcement unbookmarked", {
        icon: "success",
      })
      .then(function() {
        form.submit();
      });
    } else {
      return false;
    }
    })
}