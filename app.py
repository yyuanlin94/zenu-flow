from fastapi import FastAPI
import random

app = FastAPI()

mindfulness_exercises = {
    "stressed": ["Take a deep breath for 4 seconds, hold for 4 seconds, and exhale for 4 seconds.",
                 "Try a quick 5-minute meditation focusing on your breath."],
    "anxious": ["Close your eyes and count 5 things you hear.",
                "Hold something soft in your hands and focus on its texture."],
    "overwhelmed": ["Write down 3 things you’re grateful for.",
                    "Stretch for a few minutes and roll your shoulders back."]
}

@app.get("/")
def home():
    return {"message": "ZenU Flow API is running!"}

@app.get("/zenuflow")
def get_mindfulness(mood: str):
    exercise = random.choice(mindfulness_exercises.get(mood, ["Take a moment to breathe and center yourself."]))
    return {"mood": mood, "exercise": exercise}




