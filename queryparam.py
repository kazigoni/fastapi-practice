from fastapi import FastAPI

app = FastAPI()

# same way I can run this file as for 'main.py' by running this command
# in the terminal (bash or powershell)
# 'fastapi dev queryparam.py'

fake_items_db = [{"item_name": "foo"}, {
    "item_name": "Bar"}, {"item_name": "Baz"}]

# Query parameters are not fixed path so they are 'OPTIONAL'


@app.get("/items/")
async def read_items(skip: int = 0, limit: int = 10):
    return fake_items_db[skip: skip + limit]
"""
# So going to the /items and /items?skip=0&limit=10 are same default values are already set
# Query parameters value can be changed for example /items/?skip=0&items=1
# it will retrive one value from the list (fakeitems_db)
"""


######### OPTIONAL PARAMETERS ############
