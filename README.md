# API_Testing
Testing a company's SKU API

Goals:

Test the GET, POST and DELETE methods of the API provided.

GET- Test if the items in inventory can be retrieved successfully:
test cases:
1. Can a valid SKU be retrieved successfully
2. Can non existant SKU attempted to be retrieved and return appropriate status code (204)
3. Does Malformed get request return a 400 or appropriate status code

POST- Test if items in inventory can be created and updated successfully.
test cases:
1. Can you create an item with new SKU successfully - result 200 OK, check if item has been added
2. Can you update a given item successfully- check by retrieving item and checking for updated value
3. Does a malformed request return appropriate error code

DELETE - Test if items can be deleted from inventory.
test cases:
1. Can you delete an existing SKU successfully
2. if you try to delete a non existant SKU, do you get appropriate error response
3. Are there appropriate safeguards against deleting all inventory

How to run:
1. Prerequisites: Need to install python, pip and pytest. Also would need requests library.
2. On the commandline: 

    py -3 -m pytest - will run all tests
    
    py -3 -m pytest [file_name] would run just the test whose file_name is specified



