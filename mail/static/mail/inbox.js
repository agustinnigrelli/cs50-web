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
  document.querySelector('#view-email').style.display = 'none';

  // Clear out composition fields
  document.querySelector('#compose-recipients').value = '';
  document.querySelector('#compose-subject').value = '';
  document.querySelector('#compose-body').value = '';
  
}

function reply_email(recipient, response, body, date) {

  // Show compose view and hide other views
  document.querySelector('#emails-view').style.display = 'none';
  document.querySelector('#compose-view').style.display = 'block';
  document.querySelector('#view-email').style.display = 'none';

  // Fill the forms with the arguments
  document.querySelector('#compose-recipients').value = `${recipient}`;
  if(response.slice(0,3) === 'Re:') {
    document.querySelector('#compose-subject').value = `${response}`;
  } else {
    document.querySelector('#compose-subject').value = `Re: ${response}`;
  }

  document.querySelector('#compose-body').value = `\n\n________________\nIn response to:\nOn ${date}, ${recipient} wrote: ${body}`;

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
  document.querySelector('#view-email').style.display = 'none';

  // Show the mailbox name
  document.querySelector('#emails-view').innerHTML = `<h3>${mailbox.charAt(0).toUpperCase() + mailbox.slice(1)}</h3>`;

  // Load the inbox tab
  if (mailbox === 'inbox') {
  
    fetch('/emails/inbox')
    .then(response => response.json())
    .then(emails => {
      // Print emails in console
      console.log(emails);

      // Show emails
      emails.forEach(emails => {

        const div = document.createElement('div');
        if (emails.read === true) {
          div.style.background = 'lightgray';
        } else {
          div.style.background = 'white';
        }; 

        div.innerHTML = 
        `<p style="padding:8px; border:1px solid lightgray; margin:0px">
        <span style="float:left"><strong>${emails.sender}</strong></span>
        <span>${emails.subject}</span>
        <span style="float:right">${emails.timestamp}</span>
        </p>`;

        document.querySelector('#emails-view').append(div);
        
        div.addEventListener('click', function() {
          
          // Show the view of the email and hide the inbox
          document.querySelector('#emails-view').style.display = 'none';
          document.querySelector('#compose-view').style.display = 'none';
          document.querySelector('#view-email').style.display = 'block';

          document.querySelector('#view-email').innerHTML = '<h3>View email</h3>';

          // Show the clicked email
          fetch(`/emails/${emails.id}`)
          .then(response => response.json())
          .then(email => {
            // Print email in console
            console.log(email);
            
            // Create the HTML elements and append them to the view
            const header = document.createElement('ul');
            const sender = document.createElement('li');
            const recipients = document.createElement('li');
            const subject = document.createElement('li');
            const timestamp = document.createElement('li');
            const reply = document.createElement('button');
            const archive = document.createElement('button');
            const separator = document.createElement('hr');
            const body = document.createElement('p');
            
            header.style.listStyleType = 'none';
            header.style.margin = 0;
            header.style.padding = 0;
            
            sender.innerHTML = `<strong>From: </strong>${emails.sender}`;
            recipients.innerHTML = `<strong>To: </strong>${emails.recipients}`;
            subject.innerHTML = `<strong>Subject: </strong>${emails.subject}`;
            timestamp.innerHTML = `<strong>Date: </strong>${emails.timestamp}`;
            body.innerText = `${emails.body}`
            
            reply.className = 'btn btn-sm btn-outline-primary';
            reply.innerHTML = 'Reply';

            // Reply
            reply.addEventListener('click', function() {

              reply_email(`${emails.sender}`, `${emails.subject}`, `${emails.body}`, `${emails.timestamp}`)

            })

            archive.className = 'btn btn-sm btn-outline-secondary';
            archive.innerHTML = 'Archive';

            // Archive the viewed mail
            archive.addEventListener('click', function() {
              
              fetch(`/emails/${emails.id}`, {
                method: 'PUT',
                body: JSON.stringify({
                    archived: true
                })
              })
              // Load inbox tab when the mail is archived
              .then(() => {
                load_mailbox('inbox')
              })
            });
          
            header.append(sender);
            header.append(recipients);
            header.append(subject);
            header.append(timestamp);
            header.append(reply, ' ');
            header.append(archive);
            
            document.querySelector('#view-email').append(header);
            document.querySelector('#view-email').append(separator);
            document.querySelector('#view-email').append(body);

          });
          
          // Mark the viewed mail as read
          fetch(`/emails/${emails.id}`, {
            method: 'PUT',
            body: JSON.stringify({
                read: true
            })
          })
        });
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

      // Show emails
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

  // Load the archive tab
  if (mailbox === 'archive') {
  
    fetch('/emails/archive')
    .then(response => response.json())
    .then(emails => {
      // Print emails in console
      console.log(emails);

      // Show emails
      emails.forEach(emails => {

        const div = document.createElement('div');
        div.innerHTML = `<p style="padding:8px; border:1px solid lightgray; margin:0px">
                          <span style="float:left"><strong>${emails.sender}</strong></span>
                          <span>${emails.subject}</span>
                          <span style="float:right">${emails.timestamp}</span>
                        </p>`;

        div.addEventListener('click', function() {

          // Show the view of the archived email and hide the inbox
          document.querySelector('#emails-view').style.display = 'none';
          document.querySelector('#compose-view').style.display = 'none';
          document.querySelector('#view-email').style.display = 'block';

          document.querySelector('#view-email').innerHTML = '<h3>View archived email</h3>';

          // Show the clicked email
          fetch(`/emails/${emails.id}`)
          .then(response => response.json())
          .then(email => {
            // Print email in console
            console.log(email);
            
            // Create the HTML elements and append them to the view
            const header = document.createElement('ul');
            const sender = document.createElement('li');
            const recipients = document.createElement('li');
            const subject = document.createElement('li');
            const timestamp = document.createElement('li');
            const reply = document.createElement('button');
            const archive = document.createElement('button');
            const separator = document.createElement('hr');
            const body = document.createElement('p');
            
            header.style.listStyleType = 'none';
            header.style.margin = 0;
            header.style.padding = 0;
            
            sender.innerHTML = `<strong>From: </strong>${emails.sender}`;
            recipients.innerHTML = `<strong>To: </strong>${emails.recipients}`;
            subject.innerHTML = `<strong>Subject: </strong>${emails.subject}`;
            timestamp.innerHTML = `<strong>Date: </strong>${emails.timestamp}`;
            body.innerHTML = `${emails.body}`
            
            reply.className = 'btn btn-sm btn-outline-primary';
            reply.innerHTML = 'Reply';
            archive.className = 'btn btn-sm btn-secondary';
            archive.innerHTML = 'Archive';

            // Archive the viewed mail
            archive.addEventListener('click', function() {
              
              fetch(`/emails/${emails.id}`, {
                method: 'PUT',
                body: JSON.stringify({
                    archived: false
                })
              })
              // Load inbox tab when the mail is archived
              .then(() => {
                load_mailbox('inbox')
              })
            });
          
            header.append(sender);
            header.append(recipients);
            header.append(subject);
            header.append(timestamp);
            header.append(reply, ' ');
            header.append(archive);
            
            document.querySelector('#view-email').append(header);
            document.querySelector('#view-email').append(separator);
            document.querySelector('#view-email').append(body);

          });

        });
        document.querySelector('#emails-view').append(div);
        
      });
    });
    event.preventDefault();
  };
};