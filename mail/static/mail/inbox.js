document.addEventListener('DOMContentLoaded', function() {

  // Use buttons to toggle between views
  document.querySelector('#inbox').addEventListener('click', () => load_mailbox('inbox'));
  document.querySelector('#sent').addEventListener('click', () => load_mailbox('sent'));
  document.querySelector('#archived').addEventListener('click', () => load_mailbox('archive'));
  document.querySelector('#compose').addEventListener('click', compose_email);

  // By default, load the inbox
    load_mailbox('inbox');
});

function compose_email() {

  // Show compose view and hide other views
  document.querySelector('#emails-view').style.display = 'none';
  document.querySelector('#compose-view').style.display = 'block';

  // Clear out composition fields
  document.querySelector('#compose-recipients').value = '';
  document.querySelector('#compose-subject').value = '';
  document.querySelector('#compose-body').value = '';
}

// Submitting the form calls a function
document.addEventListener('DOMContentLoaded', function() {
  document.querySelector('#compose-form').onsubmit = function() {
  
    const recipients = document.querySelector('#compose-recipients').value;
    const subject = document.querySelector('#compose-subject').value;
    const body = document.querySelector('#compose-body').value;

    fetch('/emails', {
      method: 'POST',
      body: JSON.stringify({
          recipients: recipients,
          subject: subject,
          body: body
      })
    })
    .then(response => response.json())
    .then(result => {
        // Print result
        console.log(result);       
    })
    // Load sent tab when the mail is sent
    .then(load_mailbox('sent'))
  }
})

function load_mailbox(mailbox) {
  
  // Show the mailbox and hide other views
  document.querySelector('#emails-view').style.display = 'block';
  document.querySelector('#compose-view').style.display = 'none';

  // Show the mailbox name
  document.querySelector('#emails-view').innerHTML = `<h3>${mailbox.charAt(0).toUpperCase() + mailbox.slice(1)}</h3>`;

  // Load the inbox tab
  if (mailbox === 'inbox') {
  
    fetch('/emails/inbox')
    .then(response => response.json())
    .then(emails => {
      // Print emails in console
      console.log(emails);

      // Show emails in the inbox
      emails.forEach(emails => {

        const div = document.createElement('div');
        if (emails.read === true) {
          div.style.background = 'lightgray';
        } else {
          div.style.background = 'white';
        }; 

        div.innerHTML = `<p style="padding:8px; border:1px solid lightgray; margin:0px">
                          <span style="float:left"><strong>${emails.sender}</strong></span>
                          <span>${emails.subject}</span>
                          <span style="float:right">${emails.timestamp}</span>
                        </p>`;
        div.addEventListener('click', function() {
          console.log('This element has been clicked!')
        });
        document.querySelector('#emails-view').append(div);
        
      });
    });
  };

  // Load the sent tab
  if (mailbox === 'sent') {
    
    fetch('/emails/sent')
    .then(response => response.json())
    .then(emails => {
      // Print emails in console
      console.log(emails);

      // Show emails in the inbox
      emails.forEach(emails => {
        const div = document.createElement('div');

        div.innerHTML = `<p style="padding:8px; border:1px solid lightgray; margin:0px">
                          <span style="float:left"><strong>${emails.recipients}</strong></span>
                          <span>${emails.subject}</span>
                          <span style="float:right">${emails.timestamp}</span>
                        </p>`;
        div.addEventListener('click', function() {
          console.log('This element has been clicked!')
        });
        document.querySelector('#emails-view').append(div);
        
      });
    });
    event.preventDefault();
  };

};