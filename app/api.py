from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():

    return {
        "message": "Automated Resume Screening API Running"
    }


@app.get("/health")
def health():

    return {
        "status": "success"
    }