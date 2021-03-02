# Stéph's Closet

A fabulous thing for Stéph to sell clothes - basic README in here to start and need to make sure i stay on top of this!

What apps do I need to make?!
 - Home (this holds the index - does it want to store things that will be available on all apps - navbars etc)
 - Register/Logon (Think this is handled by allauth!)
 - Products
 - Shopping Cart
 - Checkout
 - User Profile
 - Store Owner Trends / Sale monitoring
 - Stock?!
 - Store owner making a sale
 - Static files (CSS and JS)
 - Media (Images)


 Talk about changing delivery to standard price and having to make sure changes were put in model.py and contexts.py and if, elif, else. delivery coming through as a flaot and total as a decimal, need to make delivery an int

## UX
 
Use this section to provide insight into your UX process, focusing on who this website is for, what it is that they want to achieve and how your project is the best way to help them achieve these things.

In particular, as part of this section we recommend that you provide a list of User Stories, with the following general structure:
- As a user type, I want to perform an action, so that I can achieve a goal.

This section is also where you would share links to any wireframes, mockups, diagrams etc. that you created as part of the design process. These files should themselves either be included as a pdf file in the project itself (in an separate directory), or just hosted elsewhere online and can be in any format that is viewable inside the browser.

## Features

In this section, you should go over the different parts of your project, and describe each in a sentence or so.
 
### Existing Features
- Feature 1 - allows users X to achieve Y, by having them fill out Z
- ...

For some/all of your features, you may choose to reference the specific project files that implement them, although this is entirely optional.

In addition, you may also use this section to discuss plans for additional features to be implemented in the future:

### Features Left to Implement
- Another feature idea

# Technologies Used

#### [HTML (Hypertext Markup Language)](https://www.w3schools.com/html/)
- HTML is the standard markup language for programmers to use to display content on a webpage.

#### [CSS (Cascading Style Sheets)](https://www.w3schools.com/css/)
- CSS works alongside HTML to add style and effects to the website.

#### [JavaScript](https://www.w3schools.com/js/default.asp)
- JavaScript enables Interactive web pages and is an essential part of web applications.

#### [Python](https://www.python.org/)
- Python is a programming language similar to javascript but trying to make code more readble and trying to help programmers with clear and logical code. Python is the programming language of the django framework used for this project.

#### [jQuery](https://jquery.com/)
- jQuery is a framework that enables easier manipulation of the DOM and i have used this to simplifiy the code from standard JavaScript.

#### [Convertcsv.com](www.convertcsv.com)
- Convertcsv is a website that I used to be able to convert csv files into JSON files. This was used for creating and importing the data, from an excel spreadsheet into a JSON file to be used as a fixture. 

#### [Mockaroo](https://www.mockaroo.com/)
- Mockaroo is a random data generator tool. This can be used to generate a large amount of random data with lots of parameters. I have used this for adding data to the dataset I got from kaggle, such as prices and stock levels.

#### [Chrome Developer Tools](https://developers.google.com/web/tools/chrome-devtools)
 - A set of Web developer tools built into Google Chrome that allows you to make changes to a website on the fly for testing purposes and be able to diagnose issues. I used this for the console, to be able to view results as changes were made during gameplay. This also allowed me to issue commands to the game to carry on if there was a bug while testing rather than having to start the whole game again. 

#### [Django](https://www.djangoproject.com/)

##### [Django REST framework](https://www.django-rest-framework.org/)

##### [Django Crispy Forms]

##### [Django Allauth](https://django-allauth.readthedocs.io/en/latest/#)

##### [Django Storages](https://django-storages.readthedocs.io/en/latest/)

#### [gunicorn](https://gunicorn.org/)

#### [Bootstrap](https://getbootstrap.com/)
- Bootstrap is a front-end open source toolkit that gives extensive prebuilt components and a responsive grid system. I have used bootstrap to help with the basic design of the site and be able to used pre-built classes rather than having to create a lot of css code for all the content involved.

#### [jQuery](https://jquery.com/)
- jQuery is a framework that enables easier manipulation of the DOM and i have used this to simplifiy the code from standard JavaScript.

#### [Font Awesome](https://fontawesome.com/)
- A font and icon based toolkit based on CSS - Wikipedia. I used font awesome icons to give a more visual appearance to the Happiness and Followers, it also gave the user a quick viewing of what was being affected.

#### [Chartjs](https://www.chartjs.org/)

#### [Stripe](https://stripe.com/en-gb)

#### [Amazon Web Services](https://aws.amazon.com/)

#### [Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)

#### [DB Browser for SQLite](https://sqlitebrowser.org/)

#### [Heroku](https://www.heroku.com/)

#### [Github](https://github.com/)
- A software development sharing platform used for hosting and sharing projects for open source, or team based projects. I was using github so other people can see, its easily hostable and can deploy easily.

#### [Gitpod](https://www.gitpod.io/)
- An IDE (Integrated Development Environment) for GitHub that lets you quickly launch your projects in a ready-to-code environment.

#### [Git](https://git-scm.com/)
- A free and open source version control system that handles all projects and keeps version history in check.


## Testing

In this section, you need to convince the assessor that you have conducted enough testing to legitimately believe that the site works well. Essentially, in this part you will want to go over all of your user stories from the UX section and ensure that they all work as intended, with the project providing an easy and straightforward way for the users to achieve their goals.

Whenever it is feasible, prefer to automate your tests, and if you've done so, provide a brief explanation of your approach, link to the test file(s) and explain how to run them.

For any scenarios that have not been automated, test the user stories manually and provide as much detail as is relevant. A particularly useful form for describing your testing process is via scenarios, such as:

1. Contact form:
    1. Go to the "Contact Us" page
    2. Try to submit the empty form and verify that an error message about the required fields appears
    3. Try to submit the form with an invalid email address and verify that a relevant error message appears
    4. Try to submit the form with all inputs valid and verify that a success message appears.

In addition, you should mention in this section how your project looks and works on different browsers and screen sizes.

You should also mention in this section any interesting bugs or problems you discovered during your testing, even if you haven't addressed them yet.

If this section grows too long, you may want to split it off into a separate file and link to it from here.

## Deployment

This section should describe the process you went through to deploy the project to a hosting platform (e.g. GitHub Pages or Heroku).

In particular, you should provide all details of the differences between the deployed version and the development version, if any, including:
- Different values for environment variables (Heroku Config Vars)?
- Different configuration files?
- Separate git branch?

In addition, if it is not obvious, you should also describe how to run your code locally.


## Credits

### Content
- The text for section Y was copied from the [Wikipedia article Z](https://en.wikipedia.org/wiki/Z)

### Media
- Main background image got from [pixabay](https://pixabay.com/photos/closet-clothing-walk-in-3615613/)

### Acknowledgements

- I received inspiration for this from my girlfriend Steph who is a keen and avid shopper, so she had good ideas for what shoppers would want to see. 