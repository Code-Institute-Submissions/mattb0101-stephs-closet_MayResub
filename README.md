# Stéph's Closet

Stéph's Closet is an e-commerce store built for my 4th Milestone project with the Code Institue Web and Software Development course. This is a full stack project using Django for complete control of front and back-end.

Shopping online is a huge thing these days, and with the last year of the COVID pandemic, people have had to be at home so online shopping has become evern more prevelant. My girlfriend Steph is an avid online shopper so having someone nearby to be able to give advice about what a shopper, and what someone who owned the shop, would like to see. 

# UX

## Project Goals

I want to be able to explore both sides of the shop and have created a functional site that I hope users enjoy using and find it easy to use and will return to shop at. It is also a site where the shop owners have full control and visibility of their sales and how their shop is doing. 

Because of shopping being such a massive thing these days, I would like to be able to stand out a bit, give users a good memory of the site and think about coming back to search for things they want to buy again. 

## User Stories

As a user of this site I would like:

1. To be able to easily look at products and move back and forth between pages.
2. To be able to filter the products I'm looking at so I'm not just searching through a long list.
3. To be able to search for products when I know what I'm looking for.
4. To be able to add products to a cart and be able to easily view and edit the cart.
5. To be able to easily create/register for an account. 
6. To be able to save my delivery information for future easy entry on future orders.
7. To be able to contact the store if there are any issues or questions.
8. To be able to see my past orders and easily keep track of them. 

As A Store Owner I would like:

1. To be able to see an overview of the stores performance.
2. To be able to see daily sales.
3. To be able to easily see what products need re-stocking.
4. To be able to manually adjust and manage stock, editing prices and descriptions.
5. To be able to add new products to the store.

As an administrator for the site I would like:

1. To be able to easily view information related to the store.
2. To be able to override information and easily update if a user is having an issue with verification or part of their account
3. To be able to look at the full order history and easily identify orders if they want changing.
4. To be able to....
 - NEEED A FEW MORE THINGS IN HERE

## Design Choices

A lot of the design inspiration came from my girlfriend Stéph as treating the store like her own, she has given the initial way she would like it to look, drawings and colour. I have taken these things and then added a coding element to adapt and try make it as user friendly and feasible as possible. 

### Icons

* With this site been mainly around shoppers, and across all devices, sometimes an icon to give display rather than lots of text makes things easier to look at. When icons are used it would be ideal for the user to know what they are pressing easily rather than having to guess or figure it out, I have tried to stick to this as much as possible using simple font awesome icons. 

### Colours

* The colours used came from Stéph, as white, black and a bright pink to give simplicity, clarity and also stand out. We went through some colour palletes to choose the colours that worked best for the store owner, and when these decided on, I put them in as root variables to make sure that colours were kept the same throughout.

### Styling and background

* The store owner wanted a wardrobe/closet as the background as the home page. This would be used across the site, but with different overlays giving it a very light background effect on most of the site, but keeping the theme throughout the site. 


## Wireframes

 
[Use this section to provide insight into your UX process, focusing on who this website is for, what it is that they want to achieve and how your project is the best way to help them achieve these things.

In particular, as part of this section we recommend that you provide a list of User Stories, with the following general structure:
- As a user type, I want to perform an action, so that I can achieve a goal.]


# Features
 
## Existing Features

#### Register

#### Login / Logout

#### User Account

#### Home

#### Products

#### Cart

#### Checkout

#### Store Admin

#### Stock

#### Static and Media Files?
 


## Features Left to Implement

#### Store Owner making Sale

#### Product Reviews

#### Ordering stock in


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

#### [Kaggle](https://www.kaggle.com/)
- Kaggle is a Data Science community with people uploading large sets of data free to use for testing. I have taken a large dataset from [here](https://www.kaggle.com/paramaggarwal/fashion-product-images-dataset) that contained images as well as a large number of products. I have cut this down from 45000 lines to just over 1000 for this project and had to make some amends. but this saved a lot of time creating test data for an e-commerce shop.

#### [Convertcsv.com](www.convertcsv.com)
- Convertcsv is a website that I used to be able to convert csv files into JSON files. This was used for creating and importing the data, from an excel spreadsheet into a JSON file to be used as a fixture. 

#### [Mockaroo](https://www.mockaroo.com/)
- Mockaroo is a random data generator tool. This can be used to generate a large amount of random data with lots of parameters. I have used this for adding data to the dataset I got from kaggle, such as prices and stock levels.

#### [Chrome Developer Tools](https://developers.google.com/web/tools/chrome-devtools)
 - A set of Web developer tools built into Google Chrome that allows you to make changes to a website on the fly for testing purposes and be able to diagnose issues. I used this for the console, to be able to view results as changes were made during gameplay. This also allowed me to issue commands to the game to carry on if there was a bug while testing rather than having to start the whole game again. 

#### [Django](https://www.djangoproject.com/)
- 'Django is a high-level Python Web framework that encourages rapid development and clean, pragmatic design' - Taken from the website. Django is a full stack framework that I have used to create apps and easily manage them with front end and backend capabilities.

##### [Django REST framework](https://www.django-rest-framework.org/)
- Django Rest framework is a toolkit made for building Web API's. I have used this in conjunction with Chartjs to easily query the data and display it, with options for authentication and user checking. 

##### [Django Crispy Forms]
- 'Forms have never been this crispy' - From the site. Django crispy forms allows very easily control how your forms render and can make sure that forms across the site stay uniform. With the amount of forms on the site, crispy forms was a great way to easily handle them all.

##### [Django Allauth](https://django-allauth.readthedocs.io/en/latest/#)
- A pre-built integrated set od Djano applications, allauth allows for easy use of them for user control and registration. Allauth handles all the user creation and validation to make sure standards are upheld.

##### [Django Storages](https://django-storages.readthedocs.io/en/latest/)
- Storages is a collection fo storage backends that will work with external storage sites and apps. This creates storages at a backend level to be able to deal with AWS and collect and transfer data effectively.

#### [gunicorn](https://gunicorn.org/)
- Gunicorn is a Python WSGI HTTP server and I have used it as a simple and speedy way to join all the frameworks together upon deployment. 

#### [Bootstrap](https://getbootstrap.com/)
- Bootstrap is a front-end open source toolkit that gives extensive prebuilt components and a responsive grid system. I have used bootstrap to help with the basic design of the site and be able to used pre-built classes rather than having to create a lot of css code for all the content involved.

#### [jQuery](https://jquery.com/)
- jQuery is a framework that enables easier manipulation of the DOM and i have used this to simplifiy the code from standard JavaScript.

#### [Font Awesome](https://fontawesome.com/)
- A font and icon based toolkit based on CSS - Wikipedia. I used font awesome icons to give a more visual appearance to the Happiness and Followers, it also gave the user a quick viewing of what was being affected.

#### [Chartjs](https://www.chartjs.org/)
- Chartjs provides simple and flexible JavaScript charts. This framework provides lots of pre-built, and easy to build in, charts and graphs. As a business owner of an e-commerce store, I think they would want to easily be able to see how business is going and how it is performing on a day to day basis. 

#### [Stripe](https://stripe.com/en-gb)
-  Stripe is a fully integrated suite of payment products which join to a website to accept be able to accept payments. I have used this as part of the full stack, and able to accept test payments with the correct checks.

#### [Amazon Web Services](https://aws.amazon.com/)
- Amazon Web services offers a wide range of cloud based solutions for web design, including, storage, analytics, mobile and management tools. I have used this to store static and media files, as with an e-commerce site, there is a lot of products and storing this on the site would make the site run a lot slower.

#### [Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)
- Boto3 is the AWS SDK for Python. This is an APi that provides object oriente connecting with AWS services. This has been used as the connection between Django and the AWS. 

#### [DB Browser for SQLite](https://sqlitebrowser.org/)
- DB Browser is a way of querying an SQLite database. With the use of SQLite to test and lots of data going in from the Django app, a way of querying the database to quickly build SQL queries that had the correct syntax to put into the website where queries are needed. I used this when building queries for the Charts

#### [Heroku](https://www.heroku.com/)
- Heroku is a fully managed platform that allows designers and developers to easily host projects in a live app. Heroku is a platform that can link to github for ease of deploying throughout the process and can be managed well in a live environment. 

#### [Github](https://github.com/)
- A software development sharing platform used for hosting and sharing projects for open source, or team based projects. I was using github so other people can see, its easily hostable and can deploy easily.

#### [Gitpod](https://www.gitpod.io/)
- An IDE (Integrated Development Environment) for GitHub that lets you quickly launch your projects in a ready-to-code environment.

#### [Git](https://git-scm.com/)
- A free and open source version control system that handles all projects and keeps version history in check.



# Testing

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


Talk about changing delivery to standard price and having to make sure changes were put in model.py and contexts.py and if, elif, else. delivery coming through as a flaot and total as a decimal, need to make delivery an int


## Deployment

I have depolyed this to heroku taking the following steps:

1. On the [Heroku Wesbite](https://dashboard.heroku.com), clikcing on "New" on the dashboard. Name the app and select the Europe region.

2. When the app has been created, click on the "Deploy" tab, and under the section for "Deployment method", click GitHub.

3. Confirm this link to GitHub, which will update the app based on commits and pushes to GitHub.

4. In the code for the project in Gitpod (or your IDE), create a `<requirements.txt>` file, which stores all the things we are using on the site. Do this by typing `<pip3 freeze --local > requirements.txt>` into your CLI.

5. As well as a requirments files, a `<Procfile>` is also needed to deploy. Create this by typing `<echo web: python app.py>` into your CLI. (`app.py` can be exchanged for the name of your python file, if you have named it `run.py` for example.)

6. Make sure to `<git add .>` and `<git commit -m "...">` these files, then `<git push>`. This will push everything to GitHub which will sync up with heroku. 

7. Back in Heroku under the "Settings" tab, there is a section called "Config Vars", click to reveal these and set the following vars:

Key | Value
----| ----
I.P | 0.0.0.0
MONGO_DBNAME | lakes_walks
MONGO_URI | mongodb+srv://<your_username>:<your_password>@myfirstcluster.0i01h.mongodb.net/<your_db_name>?retryWrites=true&w=majority"
PORT | 5000
SECRET_KEY | <your_secret_key>

8. From your app dahsboard, under "Deploy", make sure Automatic deploys are Enabled, and under "Manual Deploys", the correct branch you want to deploy is selected i.e. master.

9. The site is now successfully deployed. 




## Credits

### Content
- All the product information and images came from a dataset on [kaggle](https://www.kaggle.com/paramaggarwal/fashion-product-images-dataset).
- [Django documentation]
- [Crispy forms Documentation]
- [Product Variations](https://www.youtube.com/watch?v=cRbU7OH1RaQ) was used to help me understand a bit about how to incorpate sizes when the same product had multiple sizes.
- [Pagination](https://www.youtube.com/watch?v=acOktTcTVEQ). This helped me get the basic and then using the [django documentation](https://docs.djangoproject.com/en/3.1/topics/pagination/) to split products into pages, with a view function, not a ListView.
- [Chartjs](https://www.youtube.com/watch?v=B4Vmm3yZPgc) was a simple tutorial how to firstly incorporate chartjs into django, this helped build the basic that I could then take further. 
- [Stock Management](https://www.youtube.com/playlist?list=PL6RgKo1nB4TlJDfWz3czfXHkg8wSn8THV) -  Gave me an understanding of a simple way to control stock in a store. 
- [Contact form](https://hellowebbooks.com/news/tutorial-setting-up-a-contact-form-with-django/). Having used contact forms before, but this time actually sending emails and messages, learning how to incorporate these into Django. 



##### [w3schools](https://www.w3schools.com/)
- [Toasts](https://www.w3schools.com/bootstrap4/bootstrap_toast.asp) - very simple thing needed checking here with the document ready needed to make toasts show. 
- [Root Variable](https://www.w3schools.com/css/css3_variables.asp) is something i have seen on numerous research videos and used this to give me full understanding. 
- [Colspan](https://www.w3schools.com/tags/att_td_colspan.asp) to understand colspans and how they worked.

##### Stack Overflow
- [CSS Offset background](https://stackoverflow.com/questions/35505528/offset-background-behind-html-element-tag) for the free delivery tag on the homepage, helped my fully understand this.
- Django returning to previous page. [Previous URL](https://stackoverflow.com/questions/35894990/django-how-to-return-to-previous-url) and [back button](https://stackoverflow.com/questions/51776862/django-2-0-back-button-redirecting-to-different-pages-based-on-where-you-came-f). These were both explored for going back with filters and pagination were involved. Eventually using the back button to make sure the full url matched.
-Django template language ['and'](https://stackoverflow.com/questions/14957564/django-if-and-template/14957680) and ['or'](https://stackoverflow.com/questions/19284270/django-template-if-or-statement). These helped make sure i got the syntax right when putting multiple parameters in an if statement.
- [Nested if else in templates](https://stackoverflow.com/questions/36528958/django-nested-if-else-in-templates/36529093). This helped with making sure I had the correct terminolgy for nested if statements and if/else if/else statements.
- [Pagination appending url](https://stackoverflow.com/questions/64630914/django-pagination-filters-appending-to-url-rather-than-replacing). This was an issue that came up mutliple times that when changing to page 2, it would remove any other filters, this helped me understand and fix that issue.
- [Joining list](https://stackoverflow.com/questions/1236593/comma-separated-lists-in-django-templates). Sometimes when there was multiple categories or articles in the filter and I wanted these in the title, this showed how to put the list into one tag.
- [Date time functions in SQLite](https://stackoverflow.com/questions/3014667/how-can-i-convert-datetime-to-date-format-in-sqlite). Knowing standard SQL for my queries, this showed the SQLite counterparts for use in development.
- [Putting field names to raw SQL](https://stackoverflow.com/questions/60744714/get-associative-array-from-raw-sql-query-in-django). This page lead me to the area of the Django documentation that i needed to help me be able to display raw SQL results properly. 
- [Post Save signal](https://stackoverflow.com/questions/13014411/django-post-save-signal-implementation). This helped being able to reformat how my stock was being handled so that it would adjust when a sale is done using a post_save signal. 





### Media
- Main background image got from [pixabay](https://pixabay.com/photos/closet-clothing-walk-in-3615613/)

### Acknowledgements

- I received inspiration for this from my girlfriend Steph who is a keen and avid shopper, so she had good ideas for what shoppers would want to see. 