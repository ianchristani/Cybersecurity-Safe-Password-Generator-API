from fastapi import FastAPI, HTTPException, status
from typing import Optional
from pydantic import BaseModel
import random

# creating the API instance
safepssw = FastAPI()

# collections to compose the password based on choice
numbers=["0","1","2","3","4","5","6","7","8","9"]
letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','x','y','w','z']
symbols=['!','@','#','$','%','^','&','?','~']
signs=['=','+','-','/','|','<','>']


# model to receive the choices
class Info(BaseModel):
    caracterlen: int
    havenumbers: Optional[bool]=None
    haveletters: Optional[bool]=None
    havesymbols: Optional[bool]=None
    havesigns: Optional[bool]=None
    havecapitalletters: Optional[bool]=None


# get method
@safepssw.get('/')
def get_password():
    return {"message": "Welcome to Safe Password Generator",
        "instructions": "please check the endpoint and body request content to use th API",
        "doc link": "http:// /docs"
    }


# get method to use the API
@safepssw.get('/safepassword')
def get_password(inf: Info):
    # centralizing the choices
    paramToBuild=[]

    if inf.caracterlen<8:
        raise HTTPException(detail="the minimal length is 8", status_code=status.HTTP_411_LENGTH_REQUIRED)
    else:
        if inf.havenumbers==True:
            paramToBuild.extend(numbers)
        if inf.haveletters==True:
            paramToBuild.extend(letters)
        if inf.havesymbols==True:
            paramToBuild.extend(symbols)
        if inf.havesigns==True:
            paramToBuild.extend(signs)
        if inf.havecapitalletters==True:
            paramToBuild.extend([capLetter.upper() for capLetter in letters])

    counter=1
    psswrd=[]

    while counter<=inf.caracterlen:
        index=random.randint(0,len(paramToBuild)-1)
        psswrd.append(paramToBuild[index])
        counter+=1

    psswrd=''.join(psswrd)
    return {"generated_password":psswrd}       



# running the server
if __name__ == '__main__':
    import uvicorn

    uvicorn.run("main:safepssw", host="0.0.0.0", port=8000, reload=True)