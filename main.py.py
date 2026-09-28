from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

from qna import answer_question
from quiz_module import generate_quiz

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


class QuestionRequest(BaseModel):
    question: str


@app.get("/")
def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"request": request}
    )


@app.post("/qa")
def qa(request: QuestionRequest):
    answer = answer_question(request.question)
    return {"answer": answer}
    class QuizRequest(BaseModel):
    topic: str


@app.post("/quiz")
def quiz(request: QuizRequest):
    quiz_data = generate_quiz(request.topic)
    return {"quiz": quiz_data}