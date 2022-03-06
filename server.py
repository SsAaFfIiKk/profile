import uvicorn
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.middleware.cors import CORSMiddleware


origins = [
    "http://127.1.0.0.1",
    "http://127.1.0.0.1:8000",
]

templates = Jinja2Templates(directory=".")
app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/cards", response_class=HTMLResponse)
def homepage(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/get_logo")
def logo():
    return  FileResponse("logo.jpg")


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=1990, ssl_keyfile="./certs/privkey.pem", ssl_certfile="./certs/cert.pem")
