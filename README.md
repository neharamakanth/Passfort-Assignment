# Passfort-Assignment

Run the pure_rest_api.py in scripts folder to view the results using Python request:

-------To achieve POST /documents/<title>----------------------------------------------------------------------------------------------------------------------------------------
1.Uncomment print(create_document()) 
2.Enter the necessary details(author,title and content) of your document in first three lines of def create_document() function.
3.If the title doesnot exists, a new document with version 1 will be created.
4.If the title already exists, a document will be created with the next version.


 

-------To achieve GET /documents------------------------------------------------------------------------------------------------------------------------------------------------
1.Uncomment print(get_list_of_documents())
2.All the available documents will be listed.

------------GET /documents/<title>----------------------------------------------------------------------------------------------------------------------------------------------
1.Uncomment and send the title as parameter in---> print(get_list_of_documents('Name of your title'))
2.All the available documents of that title will be listed.

-----------GET /documents/<title>/latest----------------------------------------------------------------------------------------------------------------------------------------
1.Uncomment and send the title and True as parameters in---> print(get_list_of_documents('Name of your title',True))
2.Latest document of that title will be listed.


