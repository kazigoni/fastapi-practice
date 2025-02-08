from enum import Enum
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Welcome to the site"}

"""  
run this command 'fastapi dev main.py' in the terminal to run the server.

install 'fastapi[standard]' to run the 'fastapi' command in the terminal
"""


"""@app.get("/user/{name}")
# : type annotaion. type can str, int, bool and more complex
async def user_name(name: str):
    return {"user": f"Hello {name.upper()}"}"""

# fastapi dev main.py


@app.get("/user/me")
async def user_profile():
    return {"user_id": "Current User_ID"}


@app.get("/user/{user_id}")
async def read_user(user_id):
    return {"user id": user_id}

# same path operation can't be redefined (dupliate path is not allowed), otherwise first path will be executed only.

##### PREDEFINED VALUES ########
####### ENUM CLASS ###############
# import 'enum' class. see above 'from enum import Enum'
"""
Import Enum and create a sub-class that inherits from 'str' and from 'Enum'.

By inheriting from 'str' the API docs will be able to know that the values must be of 
'type string' and will be able to render correctly.

Then create class attributes with fixed values, which will be the available valid values:
"""


class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}


# Practicing by creating my own class, and how to send multiple values in path parameters
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


@app.get("/myname/{myname: Person}")
async def show_name(myname):
    return {myname}


############## Path parameters containing paths ##############
"""
Let's say you have a path operation with a path '/files/{file_path}'.

But you need file_path itself to contain a path, like home/johndoe/myfile.txt.

So, the URL for that file would be something like: /files/home/johndoe/myfile.txt
"""
# Path convertor¶
# Using an option directly from Starlette you can declare a path parameter containing a path using a URL like:
# /files/{file_path:path}


@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}

"""
You could need the parameter to contain /home/johndoe/myfile.txt, with a leading slash (/).

In that case, the URL would be: 
/files//home/johndoe/myfile.txt, with a double slash (//) between files and home.
"""
