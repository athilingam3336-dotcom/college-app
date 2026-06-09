from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

STUDENTS = [
    {"name": "Arun Kumar",  "roll_number": "CS2021001"},
    {"name": "Priya S",     "roll_number": "CS2021002"},
    {"name": "Karthik R",   "roll_number": "CS2021003"},
    {"name": "Divya M",     "roll_number": "CS2021004"},
    {"name": "Surya V",     "roll_number": "CS2021005"},
]

class LoginRequest(BaseModel):
    name: str
    roll_number: str

@app.post("/api/login")
def login(req: LoginRequest):
    student = next(
        (s for s in STUDENTS
         if s["name"].lower() == req.name.lower()
         and s["roll_number"].lower() == req.roll_number.lower()),
        None
    )
    if student:
        return {"message": f"Login successful! Welcome, {student['name']}."}
    raise HTTPException(status_code=401, detail="Invalid name or roll number.")

# Frontend HTML serve பண்ணு
app.mount("/", StaticFiles(directory="../frontend", html=True), name="frontend")
