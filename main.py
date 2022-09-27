from fastapi import FastAPI, status, Request, Header, Depends 
from fastapi.responses import JSONResponse
from config import settings

app = FastAPI()

class AuthException(Exception):
        def __init__(self):
           pass

@app.exception_handler(AuthException)
async def token_exception (request: Request, exc: AuthException):
    return JSONResponse(
        status_code = status.HTTP_401_UNAUTHORIZED,
        content = {"errors": [{"message": "Unauthorized"}]}
    )

async def check_service_key(IFTTT_Service_Key: str = Header('IFTTT-Service-Key')):
    if IFTTT_Service_Key != settings.IFTTT_SERVICE_KEY:
        raise AuthException()

@app.get("/ifttt/v1/status", dependencies=[Depends(check_service_key)])
async def service_status():
    return {"message": "IFTTT API is up"}

class TestSetup:
    def __init__(self, name, data):
        self.name = name
        self.age = data

SetupTest = TestSetup("Bjorn", 45)


@app.post("/ifttt/v1/test/setup", dependencies=[Depends(check_service_key)])
async def service_setup():
    return {
        "data": {}
    }

@app.post("/ifttt/v1/triggers/new_thing_created", dependencies=[Depends(check_service_key)])
async def service_setup():
    return {
        "data": [0, 3, 4]
        
    }