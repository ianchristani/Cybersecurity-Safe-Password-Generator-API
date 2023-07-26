from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
import random
from mangum import Mangum

description = """
API created using FastAPI to generate safe passwords based on users' choice.

Stop using silly and obvious passwords, for your safety use something out of the box! 
Just make a request to the end point and get the generated password for your needs.

This API was builded thinking to be integrated with some application relalated with
user registration, or password changes.
"""


# creating the API instance
safepssw = FastAPI(
    title = "Safe Password",
    description = description,
    version = "1.0.0",
    contact = {
        "name": "Ian Christani",
        "url": "https://github.com/ianchristani",
        "email": "ianchristani@gmail.com",
    }
)

# adapting to AWS lambda
handler = Mangum(safepssw)

# collections to compose the password based on choice
numbers = ["0","1","2","3","4","5","6","7","8","9"]
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','x','y','w','z']
symbols = ['!','@','#','$','%','^','&','?','~']
signs = ['=','+','-','/','|','<','>']


# model to receive the choices
class Info(BaseModel):
    caracterlen: int
    havenumbers: bool = None
    haveletters: bool = None
    havesymbols: bool = None
    havesigns: bool = None
    havecapitalletters: bool = None

# get method
@safepssw.get('/', description = "Provides a general overview about the API and the Documentation link.")
def get_password():
    return {"message": "Welcome to Safe Password Generator",
        "instructions": "please check the endpoint and body request content to use th API",
        "doc link": "https://eer6p533griarwyetgzb5edmmu0bvdzr.lambda-url.eu-north-1.on.aws/docs"
    }


# get method to use the API
@safepssw.get('/safepassword', description = "Return the generated random password based on the user's parameters choice.")
def get_password(inf: Info):
    # centralizing the choices
    paramToBuild = []

    if inf.caracterlen < 8:
        raise HTTPException(detail = "the minimal length is 8", status_code = status.HTTP_411_LENGTH_REQUIRED)
    else:
        if inf.havenumbers == True:
            paramToBuild.extend(numbers)
        if inf.haveletters == True:
            paramToBuild.extend(letters)
        if inf.havesymbols == True:
            paramToBuild.extend(symbols)
        if inf.havesigns == True:
            paramToBuild.extend(signs)
        if inf.havecapitalletters == True:
            paramToBuild.extend([capLetter.upper() for capLetter in letters])

    counter = 1
    psswrd = []

    while counter <= inf.caracterlen:
        index = random.randint(0,len(paramToBuild)-1)
        psswrd.append(paramToBuild[index])
        counter += 1

    psswrd = ''.join(psswrd)
    return {"generated_password":psswrd}