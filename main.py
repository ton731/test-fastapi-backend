import json
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel


app = FastAPI()


# Configure CORS settings
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace with the origin of your frontend app
    allow_credentials=True,
    allow_methods=["GET", "POST"],  # Add other HTTP methods you need
    allow_headers=["*"],  # You can restrict this to specific headers if needed
)


@app.get("/")
def root():
    return {"description": "This is a fake backend server."}


class InputData(BaseModel):
    data: str


user_data = {
    "user1": {
        "name": "jithqeighqeg",
        "password": "falihgalghe",
    },
    "user2": {
        "name": "eqqytqoeiy",
        "password": "wruqrqur",
    },
}


@app.get("/users")
def get_user():
    print("[GET] users endpoint reached...")

    return user_data


@app.post("/users")
def post_user(input_data: InputData):
    print("[POST] users endpoint reached...")
    message = input_data.data

    if message is None:
        raise HTTPException(status_code=400, detail="data field is required")

    return_data = {"status": "success", "message": f"received: {message}"}

    return return_data


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8080)
