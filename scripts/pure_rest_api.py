import requests
import json

BASE_URL='http://127.0.0.1:8000/'
END_POINT='documents/'

def get_list_of_documents(title=None,latest=False):
    data=json.dumps({})
    if title is not None :
            data=json.dumps({"title":title,"latest":latest})
    r=requests.get( BASE_URL + END_POINT ,data=data)
    print(r.status_code)
    status_code=r.status_code
    if status_code != 200:
        print('probably not good sign')
    data=r.json()
    return data

print(get_list_of_documents('Python Blog'))

def create_document():
    new_data={
    'author': 1,
    'title':'Python Blog',
    'content':'Python was introduced by Guido Van Rossum',
    }
    r=requests.post( BASE_URL + END_POINT,data=json.dumps(new_data))
    if r.status_code == requests.codes.ok:# status_code in the range (200,299)
        return r.text
    return r.json()
#print(create_document())

# Steps to run the above Python script:
#
# -------To achieve POST /documents/<title>-------
# 1.Uncomment print(create_document())
# 2.Enter the necessary details(author,title and content) of your document in first three lines of def create_document() function.
# 3.If the title doesnot exists, a new document with version 1 will be created.
# 4.If the title already exists, a document will be created with the next version.
#
#
#
#
# -------To achieve GET /documents-------
# 1.Uncomment print(get_list_of_documents())
# 2.All the available documents will be listed.
#
# ------------GET /documents/<title>-------------
# 1.Uncomment and send the title as parameter in---> print(get_list_of_documents('Name of your title'))
# 2.All the available documents of that title will be listed.
#
# -----------GET /documents/<title>/latest-----------
# 1.Uncomment and send the title and True as parameters in---> print(get_list_of_documents('Name of your title',True))
# 2.Latest document of that title will be listed.
# 
#
#
#
#
#
