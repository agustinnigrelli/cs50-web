Hi! My name is Agustin and my final project is named "ODEON: Academic Support".

It's about my personal entrepreneurship in real life. I've been doing tutorships for a while with students of several levels.
And i used a lot of platforms that allows the user to make an announcement offering courses or tutorships. But i always struggle with
the complexities and requirements of the sites. So i thought, "what if there is a site that only offer the users the opportunity of
make an announcement (offering tutorship or asking for help, as student) whitout making any kind of intervetion between the interested parts?"

So the idea of this project is to crate links between students and tutors in any subject. Just let them publish what they want to teach or learn, a couple of contact options, and thats it. Users will interact with each other outside the web once the contac is made.

I think this projects distincts because it takes every aspect of the course in consideration. I tried to integrate everything i've learned in a single project and added a bit of personal touch learning an extra couple of things as custom-interactive alerts and in-site search.
I would like to continue developing this project to make a real thing of it one day. Maybe a more complete plattform offering the same service not only to tutors and students, but to workers by trade and people looking for work/employees too.

Specification:

Publish:
Once an account is made, the user can publish an announcement in his own index. First choosing a role in a dropdown menu.
If the user chooses the option "Tutor", a form is displayed and the user must complete a few fields before submitting.
A script prevents the user to leave incomplete fields, or input incorrect data (for example: submitting non numerical characters in the 'price' field).
If the user chooses the option "Student", a different form is displayed.
Once the announcement is submitted, the user is redirected to index and shown a table wich shows all his announcements.
Information as 'title', 'role', and 'date' is displayed with a 'delete' button (wich delete the corresponding row in the database based on the user_id and the announcement_id). When clicked, a script will display an alert to the user to confirm the deletion.
If confirmed, the announcement will be deleted from the database.

Announcements tabs:
All announcements made are arranged in reverse cronological orden in two tabs. "Students" and "Tutors" and each one displays card-styled posts with every announcement made with the selected role.

Paginatcion:
I took the idea from Project 4 - Network. The announcements are displayed 10 on a page. If there are more, a "next" button appears at the bottom of the page. This button takes the user to the next page of announcements. If the user is not in the first page, a "previous" button appears at the bottom and takes the user to the previous page.

Bookmark:
Users are able to click on a "flag" icon in the announcement to bookmark it. When clicked, the announcement is added to the user's Bookmarks list using JavaScript (via a call to fetch), and the flag is coloured and the page is not reloaded in the process.
The same way works if the user wats to unbookmark a bookmarked announcement, returning the flag to its original state.
Also there is a tab "Bookmarks" where all announcements bookmarked are shown in reverse cronological order. In this tab, the announcements have it's flag replaced for an unbookmark button. Wich let the user to delet an announcement in particular from his Bookmarks list. The behaviour in the backend is the same. But in the front end the user is flashed with an alert that ask for a confirmation before deletion.

Search:
There is a search-box in the nav-bar. When submiting a string as a query (like in google), a new page is loaded with all the announcements that have at least one match in any substring. This is case-insensitive. For example, if the user submits the string 'cal' (without ''). Announcements with words like Calculus, calculator, Calvin, Caltech are displayed.
If the user submits an empty string, or there are no matching announcements. An according message of failure is shown.

Change Password:
Last but not least. Once registered, the user is allowed to change his password at any time. The submission of a new password requires the user to write the current password and two times the new desired one. If the current password is correct and the new password and its confirmation matches, the new password is set and the user is flashed with a success message. Otherwise the user is flashed with a failure message explaining what was the problem.



Hope you like the idea. I intend to continue developing and refining details to make this web project a real thing.
I can't thank you enough for al the knowledge i aquired throug the lectures and projects.
Best regards.
Agustin Nigrelli.