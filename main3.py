# Classes in FastAPI. 
# We can define a class and instantiate an object from that class to
# use their attributes as parameters of the dictionaries. 
# The URL is: http://127.0.0.1:8000/models/{model_name}
# where the model is the name of one model from the class. 
# http://127.0.0.1:8000/models/alexnet

from enum import Enum

from fastapi import FastAPI


class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


app = FastAPI()


@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name == ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}