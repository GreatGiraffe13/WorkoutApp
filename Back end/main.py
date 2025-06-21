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
    days_per_week: Annotated[int, (1, 7)]  # Accepts int, must be between 1 and 7
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
        possible = []
        for eq in user_equipment:
            possible += eq_dict.get(eq, [])
        if possible:
            exercise = random.choice(possible)
            # Add default sets/reps/time/rest for strength exercises
            day_exercises.append({
                "name": exercise,
                "sets": 3,
                "reps": 10,
                "rest_seconds": 60
            })
    return day_exercises

# Define splits for 'Build Muscle' goal
MUSCLE_SPLITS = {
    1: ["full body"],
    2: ["upper body", "lower body"],
    3: ["push", "pull", "legs"],
    4: ["upper body", "lower body", "push", "pull"],
    5: ["push", "pull", "legs", "upper body", "lower body"],
    6: ["push", "pull", "legs", "push", "pull", "legs"],
    7: ["push", "pull", "legs", "upper body", "lower body", "full body", "active recovery"]
}

# Map splits to muscle groups
SPLIT_MUSCLES = {
    "push": ["chest", "shoulders", "triceps"],
    "pull": ["back", "biceps", "forearms"],
    "legs": ["legs"],
    "upper body": ["chest", "back", "shoulders", "biceps", "triceps", "forearms"],
    "lower body": ["legs"],
    "full body": ["chest", "back", "shoulders", "biceps", "triceps", "forearms", "legs", "core"],
    "active recovery": []  # Could be stretching, yoga, etc.
}

# Helper for active recovery
ACTIVE_RECOVERY = [
    "Child's Pose",
    "Downward Dog",
    "Cat-Cow Stretch",
    "Seated Forward Fold",
    "Cobra Pose",
    "Thread the Needle",
    "Supine Twist",
    "Butterfly Stretch",
    "Pigeon Pose",
    "Foam Rolling",
    "Walking"
]

@app.post("/generate-workout")
def generate_workout(req: WorkoutRequest):
    workout_plan = []
    if req.goal == "Build Muscle":
        splits = MUSCLE_SPLITS.get(req.days_per_week, ["full body"])
        for day, split in enumerate(splits):
            if split == "active recovery":
                # Add time and rest for yoga/stretching
                exercises = [
                    {"name": ex, "time_seconds": 60, "rest_seconds": 15}
                    for ex in random.sample(ACTIVE_RECOVERY, k=min(2, len(ACTIVE_RECOVERY)))
                ]
                workout_plan.append({
                    "day": day + 1,
                    "split": split.title(),
                    "exercises": exercises
                })
                continue
            muscles = SPLIT_MUSCLES[split]
            day_exercises = []
            for muscle in muscles:
                day_exercises.extend(get_exercises_for_muscle(muscle, req.equipment))
            workout_plan.append({
                "day": day + 1,
                "split": split.title(),
                "exercises": day_exercises,
                "rest_between_exercises_seconds": 90
            })
    else:
        # Placeholder for other goals
        for day in range(req.days_per_week):
            workout_plan.append({
                "day": day + 1,
                "split": "Full Body",
                "exercises": [
                    {"name": "Jumping Jacks", "time_seconds": 45, "rest_seconds": 15},
                    {"name": "Bodyweight Squats", "sets": 3, "reps": 15, "rest_seconds": 45}
                ],
                "rest_between_exercises_seconds": 60
            })
    plan = {
        "days": req.days_per_week,
        "equipment": req.equipment,
        "goal": req.goal,
        "workout_plan": workout_plan
    }
    return plan