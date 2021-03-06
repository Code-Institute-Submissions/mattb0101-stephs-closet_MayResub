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

    E. 
    T.
    R.

7. To be able to save my delivery information for future easy entry on future orders.

    E. 
    T.
    R.

8. To be able to contact the store if there are any issues or questions.

    E. 
    T.
    R.

9. To be able to see my past orders and easily keep track of them.

    E. 
    T.
    R.

As A Store Owner I would like:

1. To be able to see an overview of the stores performance.

    E. 
    T.
    R.

2. To be able to see daily sales.

    E. 
    T.
    R.

3. To be able to easily see what products need re-stocking.

    E. 
    T.
    R.

4. To be able to manually adjust and manage stock, editing prices and descriptions.

    E. 
    T.
    R.

5. To be able to add new products to the store.

    E. 
    T.
    R.

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