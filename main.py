from fastapi import FastAPI

app = FastAPI()

@app.get("/about")
def about_me():
    return {
        "name": "EDMUND",
        "username": "ELOGIC360",
        "background": "Software developer with a passion for building innovative solutions.",
        "projects": ["Project 1", "Project 2"],
        "current_focus": "building innovative solutions."
    }