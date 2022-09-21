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
