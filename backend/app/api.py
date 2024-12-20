from fastapi import FastAPI,HTTPException, Depends, status
from fastapi.middleware.cors import CORSMiddleware # headers 


app = FastAPI()

#Define the origin request 
#list of origin which 
origins = ["http://localhost:5173","localhost:5173"]

#handles the request
app.add_middleware(
    CORSMiddleware, 
    allow_origin = origins, #adds the fast api
    allow_credentials = True, # should allow credentials to be included in the request
    allow_methods = ["*"], # everything is allowed.
    allow_headers = ["*"]
)


#Get Route 

@app.get("/", tags = ["root"]) # categorize tag.
async def read_root()->dict: # excuted will return dictionary 
    return {"message":"Welcome to FastApi!"} # converted to json 


#Get route for resting 
#@app.get(models)


@app.get("/models", tags = ["models"]) # categorize tag.
async def get_models()->dict: # excuted will return dictionary 
    return {"bloglist":"Welcome to FastApi!"} # converted to json 





