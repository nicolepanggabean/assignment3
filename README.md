# Assignment 3

Heroku Link: https://pbp-nicole-assignment3.herokuapp.com/mywatchlist/

1. Explain the difference between JSON, XML, and HTML!

HyperText Markup Language (HTML) is a formatting language built for the web. It provides structure to content so that it'll be displayed in an organized manner. It is typically written in pairs of tags that denote how a certain piece of information will be displayed. For example, the <p></p> tags denote paragraph text.

eXtensible Markup Language (XML), similar to HTML, is a markup language, and is written in pairs of tags. However, it is considered to be dynamic, because its main priority is transporting the data, as opposed to displaying it (the way HTML does).

JavaScript Object Notation (JSON) utilizes the same code used for creating JavaScript objects, which make it easy to convert said JSON data to objects. Though the syntax comes from JavaScript, the format is text-only, meaning that both programs used to generate and read JSON data can be coded in any language.


2. Explain why we need the data delivery when implementing on a platform!

Data delivery is essentially the way a client and server communicate with one another. The client requests data, and the server responds with data. For example, if the client (browser) requests an HTML page, then the server will respond with an HTML file. If the client (browser) requests raw data, the server will respond with an XML or JSON file.

Data delivery allows for this interaction to happen. Without data delivery, the platform would be one-sided and would not allow for productive communication between parties.


3. Explain how you completed the tasks in this assignment!

First off, I started by creating a new app and initializing that app in the django project settings. I also added the URL path so the user can access it. Then, I built the model that contains the required attributes.

After doing so, I migrated the models and created a views function that would be able to convert it to HTML format. I also created a JSON file with the raw data as well as an HTML template.

Then, I modified the views function accordingly, and also added more functions to allow the data to be displayed in XML and JSON format. After that, I implemented URL routing so each of this formats can be accessed by the user.

Finally, I deployed the app to Heroku.

---
## Postman screenshots
![](html_response.png)
![](xml_response.png)
![](json_response.png)

Sources:
https://www.geeksforgeeks.org/html-vs-xml/


# Assignment 4

Heroku Link: https://pbp-nicole-assignment3.herokuapp.com/todolist

1.  What does {% csrf_token %} do in the <form> element? What happens if there is no such "code snippet" in the <form> element?
  
  The csrf_token template tag is a protection of sorts from Cross Site Request Forgeries (CSRF). It protects any information submitted through forms via POST. If there is no CSRF token, then there is no way to authenticate credentials, and anyone with malicious intent could take advantage of unsuspecting users (in other words, they could conduct forgery).


2. Can we create the <form> element manually (without using a generator like {{ form.as_table }})? Explain generally how to create <form> manually.
  
  We can. However, we'd need to create tags for each field. Typically, we'd need to specify its input type, the label or name, its value, and more. However, this isn't very effective for making forms with a larger number of fields, as it may get repetitive, or when a more complex field is needed.


3. Describe the data flow process from the submission made by the user through the HTML form, data storage in the database, until the appearance of the data that has been stored in the HTML template.
  
  When the user enters information into the form, the entries are used as arguments that are handled by views.py, and the data is stored in the models. Then, depending on the code, the server sends another HTML page as a result. In this case, once the data is entered and stored, it is displayed back to the user.
  

4. Explain how you implement the checklist above.
  
  First, I ran a virtual environment and created a new Django app. Then, I handled the URL routing by adding the required paths to urls.py (both in project_django and in todolist).
  
  Once I did so, I created a Task model with the required attributes. I used models.ForeignKey as the field for user, DateTimeField() for date, CharField() for title, and TextField() for description.
  
  Then, I edited views.py and urls.py to accommodate the registration, login, and logout forms. I also edited the HTML templates to ensure that these were functioning correctly.
  
  I then created a new function that would create a new Task object whenever the user inputted information in the create-task form. By doing so, I essentially saved the data and displayed it back to the user afterwards. I also created the form page in HTML to ensure it achieved what I wanted. Once done, I added the new URL to the path as well.
  
  Lastly, I deployed to Heroku and created tester accounts.
