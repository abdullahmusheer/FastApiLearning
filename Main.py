from enum import Enum

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def get():
    return {"message" : "this is my first get page"}

@app.post("/")
async def post():
    return {"message: this is a post api link"}

@app.put("/")
async def put():
    return {"Hi this is the PUT api to modiy a record"}

##In this case we created a PATH PARAMETER {itemnumber}
@app.get("/list_items/{itemnumber}")   
async def grabbing_an_item(itemnumber: int):
    return {"Abdullah entered this item number" : itemnumber}

class foodEnum(str, Enum):
    vegetable = "lettuce"
    fruit = "banana"
dairy = ("milk","yogurt","ice-cream","dairy")

@app.get("/lifestyle/{enteredvalue}")
async def enter_food(enteredvalue):
    if enteredvalue == foodEnum.vegetable:
        return{"food name" : enteredvalue, "message": "that is a vegie u mentioned"}
    if enteredvalue == foodEnum.fruit:
        return{"food_name": enteredvalue, "message" : "good choice of fruit"}
    if enteredvalue in dairy:
        return{"food name":enteredvalue,"abdullah_says": "oh no I am lactose intolerant"}
    return  {"food name": enteredvalue, "message" :
     "any other food is good as long as moderately eaten"}

## Creating Query Parameters (here the endpoint is not defined)
## like its simply like localhost/endpoint
## but below i am going to incorporate both path parameter and query parameter

@app.get("/{item_id}/AlphaEndPoint")
async def item_id(item_id: str, query: str | None = None):
    if query:
        return{"item_code":item_id, "Query_input":query}
    return{"item_id": item_id, "query_info":"no query added"}