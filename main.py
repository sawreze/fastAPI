from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

<<<<<<< HEAD
from domain.question import question_router

=======
>>>>>>> e0386be075e27750059fc84ad9f9fdc4df450f00
app = FastAPI()

origins = [
    "http://127.0.0.1:5173",
    "http://localhost:5173",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

<<<<<<< HEAD
app.include_router(question_router.router)
=======
@app.get("/hello")
def hello():
    return {"message": "안녕하세요    파이보"}
>>>>>>> e0386be075e27750059fc84ad9f9fdc4df450f00
