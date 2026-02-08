from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# ⚠️ CRITICAL: You need this for the HTML file to be allowed to talk to the Python server
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # In production, change this to your GitHub URL
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/hello-world")
async def root():
    return {"message": "Hello world"} # Dictionary format is better