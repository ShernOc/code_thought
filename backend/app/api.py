from fastapi import FastAPI,HTTPException, Depends, status
from fastapi.middleware.cors import CORSMiddleware # headers 
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer

app = FastAPI()

#Define the origin request 
#list of origin which 
origins = ["http://localhost:5173","localhost:5173"]

#handles the request
app.add_middleware(
    CORSMiddleware, 
    allow_origins = origins, #adds the fast api
    allow_credentials = True, # should allow credentials to be included in the request
    allow_methods = ["*"], # everything is allowed.
    allow_headers = ["*"]
)

# end points roots getting the ApI
@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI backend!"}

@app.get("api/data")
def get_data():
    return {"data": "Here is your API data"}



#Passwords: 
# Password Hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

hashed_password = pwd_context.hash("mysecretpassword")
print("Hashed password:", hashed_password)

# JWT Configuration
SECRET_KEY = "Shern_OC"
ALGORITHM = "SH2609"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/token")


