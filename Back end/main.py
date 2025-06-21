from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Literal, Annotated
import random

app = FastAPI()

# Define possible options
EQUIPMENT_OPTIONS = [
    "None", "Dumbbells", "Barbells", "Resistance Bands", "Kettlebells", "Full Gym"
]
GOAL_OPTIONS = [
    "Lose Fat", "Build Muscle", "Increase Endurance", "General Fitness"
]

class WorkoutRequest(BaseModel):
    days_per_week: Annotated[int, (3, 7)]  # Accepts int, must be between 3 and 7
    equipment: List[Literal[
        "None", "Dumbbells", "Barbells", "Resistance Bands", "Kettlebells", "Full Gym"
    ]]
    goal: Literal[
        "Lose Fat", "Build Muscle", "Increase Endurance", "General Fitness"
    ]

# Example exercise dictionary with subgroups for 'back'
EXERCISES = {
    "back": {
        "upper": {
            "None": ["Reverse Snow Angels"],
            "Dumbbells": ["Dumbbell Rows"],
            "Barbells": ["Barbell Rows"],
            "Resistance Bands": ["Band Face Pulls"],
            "Kettlebells": ["Kettlebell High Pulls"],
            "Full Gym": ["Lat Pulldown", "Seated Row"]
        },
        "lower": {
            "None": ["Supermans"],
            "Dumbbells": ["Dumbbell Deadlifts"],
            "Barbells": ["Barbell Deadlifts"],
            "Resistance Bands": ["Band Good Mornings"],
            "Kettlebells": ["Kettlebell Swings"],
            "Full Gym": ["Back Extension"]
        }
    },
    "chest": {
        "upper": {
            "None": ["Incline Push-ups"],
            "Dumbbells": ["Incline Dumbbell Press"],
            "Barbells": ["Incline Barbell Press"],
            "Resistance Bands": ["Band Chest Press (Incline)"],
            "Kettlebells": ["Incline Kettlebell Press"],
            "Full Gym": ["Incline Bench Press"]
        },
        "lower": {
            "None": ["Decline Push-ups"],
            "Dumbbells": ["Decline Dumbbell Press"],
            "Barbells": ["Decline Barbell Press"],
            "Resistance Bands": ["Band Chest Press (Decline)"],
            "Kettlebells": ["Decline Kettlebell Press"],
            "Full Gym": ["Decline Bench Press"]
        },
        "mid": {
            "None": ["Push-ups"],
            "Dumbbells": ["Dumbbell Bench Press"],
            "Barbells": ["Barbell Bench Press"],
            "Resistance Bands": ["Band Chest Press"],
            "Kettlebells": ["Kettlebell Floor Press"],
            "Full Gym": ["Chest Press Machine", "Bench Press"]
        }
    },
    "legs": {
        "quads": {
            "None": ["Bodyweight Squats"],
            "Dumbbells": ["Dumbbell Lunges"],
            "Barbells": ["Barbell Squats"],
            "Resistance Bands": ["Band Squats"],
            "Kettlebells": ["Goblet Squats"],
            "Full Gym": ["Leg Press"]
        },
        "hamstrings": {
            "None": ["Glute Bridge"],
            "Dumbbells": ["Dumbbell Romanian Deadlift"],
            "Barbells": ["Barbell Romanian Deadlift"],
            "Resistance Bands": ["Band Leg Curl"],
            "Kettlebells": ["Kettlebell Swings"],
            "Full Gym": ["Leg Curl Machine"]
        },
        "calves": {
            "None": ["Standing Calf Raises"],
            "Dumbbells": ["Dumbbell Calf Raises"],
            "Barbells": ["Barbell Calf Raises"],
            "Resistance Bands": ["Band Calf Raises"],
            "Kettlebells": ["Kettlebell Calf Raises"],
            "Full Gym": ["Calf Raise Machine"]
        }
    },
    "core": {
        "upper": {
            "None": ["Crunches"],
            "Dumbbells": ["Weighted Crunches"],
            "Barbells": [],
            "Resistance Bands": ["Band Crunches"],
            "Kettlebells": [],
            "Full Gym": ["Cable Crunch"]
        },
        "lower": {
            "None": ["Leg Raises"],
            "Dumbbells": ["Weighted Leg Raises"],
            "Barbells": [],
            "Resistance Bands": ["Band Leg Raises"],
            "Kettlebells": [],
            "Full Gym": ["Hanging Leg Raise"]
        },
        "obliques": {
            "None": ["Russian Twists"],
            "Dumbbells": ["Dumbbell Side Bend"],
            "Barbells": ["Landmine Twists"],
            "Resistance Bands": ["Band Woodchoppers"],
            "Kettlebells": ["Kettlebell Russian Twists"],
            "Full Gym": ["Cable Woodchopper"]
        }
    },
    "arms": {
        "biceps": {
            "None": ["Isometric Curl Hold"],
            "Dumbbells": ["Dumbbell Bicep Curl"],
            "Barbells": ["Barbell Curl"],
            "Resistance Bands": ["Band Curl"],
            "Kettlebells": ["Kettlebell Curl"],
            "Full Gym": ["Cable Curl"]
        },
        "triceps": {
            "None": ["Diamond Push-ups"],
            "Dumbbells": ["Dumbbell Tricep Extension"],
            "Barbells": ["Barbell Skullcrusher"],
            "Resistance Bands": ["Band Tricep Extension"],
            "Kettlebells": ["Kettlebell Tricep Extension"],
            "Full Gym": ["Cable Tricep Pushdown"]
        },
        "forearms": {
            "None": ["Reverse Push-ups"],
            "Dumbbells": ["Dumbbell Wrist Curl"],
            "Barbells": ["Barbell Wrist Curl"],
            "Resistance Bands": ["Band Wrist Curl"],
            "Kettlebells": ["Kettlebell Wrist Curl"],
            "Full Gym": ["Forearm Machine"]
        }
    },
    "shoulders": {
        "front": {
            "None": ["Pike Push-ups"],
            "Dumbbells": ["Dumbbell Front Raise"],
            "Barbells": ["Barbell Front Raise"],
            "Resistance Bands": ["Band Front Raise"],
            "Kettlebells": ["Kettlebell Front Raise"],
            "Full Gym": ["Shoulder Press Machine"]
        },
        "side": {
            "None": ["Plank to Push-up"],
            "Dumbbells": ["Dumbbell Lateral Raise"],
            "Barbells": ["Barbell Upright Row"],
            "Resistance Bands": ["Band Lateral Raise"],
            "Kettlebells": ["Kettlebell Lateral Raise"],
            "Full Gym": ["Lateral Raise Machine"]
        },
        "rear": {
            "None": ["Reverse Snow Angels"],
            "Dumbbells": ["Dumbbell Reverse Fly"],
            "Barbells": ["Barbell Reverse Fly"],
            "Resistance Bands": ["Band Reverse Fly"],
            "Kettlebells": ["Kettlebell Reverse Fly"],
            "Full Gym": ["Reverse Pec Deck"]
        }
    }
}

def get_exercises_for_muscle(muscle, user_equipment):
    muscle_dict = EXERCISES.get(muscle, {})
    day_exercises = []
    for subgroup, eq_dict in muscle_dict.items():
        # Gather all possible exercises for user's equipment for this subgroup
        possible = []
        for eq in user_equipment:
            possible += eq_dict.get(eq, [])
        if possible:
            day_exercises.append(random.choice(possible))
    return day_exercises

@app.post("/generate-workout")
def generate_workout(req: WorkoutRequest):
    # Example: Day 1 is back day, select exercises from each back subgroup
    workout_plan = []
    if req.goal in ["Build Muscle", "General Fitness"]:
        # For demo, just do 'back' for Day 1
        for day in range(req.days_per_week):
            exercises = get_exercises_for_muscle("back", req.equipment)
            workout_plan.append({
                "day": day + 1,
                "muscle_group": "Back",
                "exercises": exercises
            })
    else:
        # Placeholder for other goals
        for day in range(req.days_per_week):
            workout_plan.append({
                "day": day + 1,
                "muscle_group": "Full Body",
                "exercises": ["Jumping Jacks", "Bodyweight Squats"]
            })
    plan = {
        "days": req.days_per_week,
        "equipment": req.equipment,
        "goal": req.goal,
        "workout_plan": workout_plan
    }
    return plan