Testing the User Stories that were previsouly defined in the UX section of the README:

Key: 
- E - Expected
- T - Testing
- R - Results
- F - Fixes

As A User of the site

1. To be able to easily look at products and move back and forth between pages.

    E. Going to all products, changing, clicking on a product to go to it and then pressing keep shopping to go back to the page I was on.
    T. Fresh site, not logged in, responsive laptop, table and mobile size, pressing all products, clicking an item then clicking keep shopping.
    R. Navigation worked as expected, but viewing on ipad size devices wasnt right.
    F. Resizing navbar and products per row for display at tablet size

2. To be able to filter the products I'm looking at so I'm not just searching through a long list.

    E. Using the dropdown menus in the nav bar to look at different product groups with only the results showing. 
    T. Select a group from one of the four dropdown menus and look at the products on the page to see if they matched what group I was looking for. Used some of the dropdown submenus to check display. Did this on all device sizes.
    R. Results were as expected the correct type of products showed up with correct titles and still able to move to new ones from that page.    

3. To be able to search for products when I know what I'm looking for.

    E. From the all products page type something in the search box at the top and the products filtering to include that search term.
    T. From products on all device sizes, type 'bag' in the search bar and press search. Only products with bag in their name or category to show.
    R. Only 2 items showed up both with bag in the name. One showed up with incorrect category (see Store Owner - 6 for fix)

4. To be able to add products to a cart and be able to easily view and edit the cart.

    E. On adding a product to the cart being able to see that it has been added and be able to click on the cart. From the cart be able to change the quantity or remove the item. No being able to add or update the product further then the in stock value. 
    T. On all devices, adding a quantity of the product to the cart that is more than in stock, then an allowed quantity, going to the cart, changing the quantity and pressing update. Trying to update the quantity to more than is in stock. Pressing remove to remove the item from the cart. 
    R. Adding more than in stock gave the user an error message, stayed on the same page and didnt add it to the cart. Adding an allowed qty notified the user that it has been added and gave a quick link to the cart. Updating the qty to more than in stock gave an error message and returned to the cart page. Updating an allowed qty was successful and updated the qty and prices. Removing the product from the cart worked and ended with no items in the cart.

5. To be able to checkout an order easily and get a confirmation email. 

    E. Easily able to get to the checkout from the cart, know what information to fill in. Make sure that I know what ive ordered and then get a success message and a confirmation email.
    T. From the cart (after adding an item) , clicking secure checkout and then filling in the form with shipping information. Using a test card number and details from Stripe, pressing complete order and being shown the success message. Checking the email from the email account entered to see if I have a confirmation email. Trying on all devices and pressing complete order before any information was filled in.  
    R. Pressing complete order resulted in a pop up for complete a field and no information was posted. Filling in all the information gave me a success screen with a review of the order details including the shipping details and items. Email was received to the email address given with all the details on it.

6. To be able to easily create/register for an account.

    E. Knowing how to register for an account, easily been able to fill in and verify my information, knowing if I am logged in and being able to log in and log out successfully.
    T. Pressing Register at the top of the screen to bring up the registrations form. Using temp-mail.org, taking an email address and using it to create an account. Firstly, trying to register with a username that I know already exists and a 2 letter password. Then trying a new username and 8 charcater password. Checking for a verification email then verifying the address. After verifying, logging in as the newly created user.
    R. All results as expected, email was received, signed in easily and shows me the user I am logged in as at the top. 

7. To be able to save my delivery information for future easy entry on future orders.

    E. Updating some delivery information in the user profile and then when going to checkout, the information to be pre-populated in the form. When some of this information is changed, for it to update my profile. 
    T. Enter some information in the form for this user on the profile then updating it. From there, adding some items to the cart and checking out. Checking the information has populated. Changing a few of the details on the delivery information and making sure the 'Save this info' box is checked. Going back to the profile to check if the information had been updated. 
    R. All as expected, exact information saved and then populated through the checkout page. Returning to profile showed the new information used as the new default.  

8. To be able to see my past orders and easily keep track of them.

    E. To be able to see a list of orders on my profile and click them to see the order summary.
    T. Click on the profile and if there is an order in the order history section, click the order number.
    R. There was an order in the history, and clicking the order number took me to the checkout success page, but with an information popup and a message on the screen telling me it was a historical order. the keep shopping button was now a back to profile button and took me back to my profile. 

9. To be able to contact the store if there are any issues or questions.

    E. To be able to contact the store with a message and make sure it gets to them
    T. From the user profile, pressing the mail button at the bottom, filling out a message with contact details and sending it. Checking the stores email account to see if the message was successfull
    R. Results were all as expected. Message with contact information was sent to the stores email. 

As A Store Owner I would like:

1. To be able to see an overview of the stores performance.

    E. When logged in as a user with staff or superuser status, being able to see some figures or orders in the store.
    T. Logging in as a user with superuser status, making sure the store management icon appears and been able to see the graphs of number of orders and average order value and easily understand what is said. Testing this across all devices. 
    R.Graphs are visible and its easy to understand what it going on. The dates are not in the correct order though on the Heroku App.
    F. Updated the postgres SQL queries to have an ORDER BY in. Refreshed the page

2. To be able to see daily sales.

    This was covered in the story above so is working fine.

3. To be able to easily see what products need re-stocking.

    E. Being able to see a list of what products are out of stock and be able to re-order them.  
    T. Check the store admin page to see the Out of stock list.
    R. There is a list of what items are out of stock, but there is no extra functionality. With a deadline, this is been added to the list of features still to implement. 

4. To be able to manually adjust and manage stock.

    E. 
    T.
    R.

5. To be able to add new products to the store.

    E. From the Store admin page, be able to add a new product, able to add all the information and then be able to see it on the products pages
    T. From store admin, clicking Product Management and then Add a product. trying to add the product with no name in. Filling in a name and then numerous other fields, adding an image and then adding the product and being able to see that product. 
    R. New product would not add with no name, adding the product takes me to the product info page, the image has uploaded and there is no stock so this cant be bought yet. All a success.

6. To be able to edit existing products in the store.

    E. To be able to edit a product field and then save the product.
    T. Using the product found in User - 3: going to the store management module, clicking product management nd then product list. Searching 'bag' in the search and then pressing Edit in the table. Updating the category to accessories and Article type to Handbags then pressing 'Confirm Edit' for this to change and take me back to the list of products.
    R. this took me onto a product information screen with no image and had created a new product. The action was incorrect in product edit and was looking at product add.
    F. Changed the action to the correct url path and tried again. Updating the item changed the fields and saving took me to the edit page, with the changed fields. Tried looking at handbags and the item was now there. 

As an administrator for the site I would like:

1. To be able to easily view information related to the store.
2. To be able to override information and easily update if a user is having an issue with verification or part of their account
3. To be able to look at the full order history and easily identify orders if they want changing.
4. To be able to....
 - NEEED A FEW MORE THINGS IN HERE


## External User Testing

With this being a shop and a lot of code, it was a good idea to get as much testing done as possible. I sent the site out at various stages of development to all my friends and all my family too, gave them instructions about the payment details and asked them to treat it like a store and create a user account and buy things. This also helped with my store admin section and the ability to monitor orders from the store.

Below is a list of issues that were brought up by external users and the fixes I put in to amend the issues:

    I. pagination buttons were not working on product pages.
    F. Upon looking this was a row at the bottom containing the back to top button that was obscuring the next page button. I added a margin to bottom of the pages section so that it would sit above the back to top row.

    I. On mobiles the toasts are appearing half off the screen.
    F. Added a media query in to give a max-width and different positioning at mobile size. 

    I. Profile links not working at mobile size and clicking the register button would take you back to home.
    F. I streamline the button process. I used to have dropdown menus for all the headings when only 1 option was often needed, so a lot of the buttons now function depending on the user and the state they are in, logged in or not.

    I. Issues with phone size display, certain fields like quantity were overrunning the row and splitting onto two.
    F. Through the testing of the operations and user stories, any minor changes to display have been fixed with bootstrap classes. 

    I. Some information on items is wrong, or they have a size option when they are a bag so are not supposed to. 
    F. Using the admin portal, these items have been adjusted so that sizes are taken off when not needed. Editing items has been built into the store admin, so that any member of staff can easily edit things on an item. 

    I. Name was not a field on the default delivery information so didnt pull through to delivery info at checkout.
    F. This is not yet fixed, the name comes from the user account but with the allauth form, these are not fields present on the signup. I had a look into adding them into it, but did not get time. This would be nice to have so has gone down as a feature left to implement. 