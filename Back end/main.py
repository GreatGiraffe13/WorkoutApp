from pydantic import BaseModel
from typing import List, Literal, Annotated
import random

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
            "None": [
                {"name": "Reverse Snow Angels", "sets": 3, "reps": 15, "rest_seconds": 45},
                {"name": "Prone Y-T-I Raises", "sets": 3, "reps": 12, "rest_seconds": 45},
                {"name": "Back Widows", "sets": 3, "reps": 12, "rest_seconds": 45},
                {"name": "Superman Pulls", "sets": 3, "reps": 15, "rest_seconds": 45},
                {"name": "Doorway Rows (Towel Row)", "sets": 3, "reps": 10, "rest_seconds": 60}
            ],
            "Dumbbells": [
                {"name": "Dumbbell Rows", "sets": 4, "reps": 10, "rest_seconds": 60}
            ],
            "Barbells": [
                {"name": "Barbell Rows", "sets": 4, "reps": 8, "rest_seconds": 90}
            ],
            "Resistance Bands": [
                {"name": "Band Face Pulls", "sets": 3, "reps": 15, "rest_seconds": 45}
            ],
            "Kettlebells": [
                {"name": "Kettlebell High Pulls", "sets": 3, "reps": 12, "rest_seconds": 60}
            ],
            "Full Gym": [
                {"name": "Lat Pulldown", "sets": 4, "reps": 10, "rest_seconds": 75},
                {"name": "Seated Row", "sets": 4, "reps": 10, "rest_seconds": 75}
            ]
        },
        "lower": {
            "None": [
                {"name": "Supermans", "sets": 3, "reps": 20, "rest_seconds": 30},
                {"name": "Alternating Superman", "sets": 3, "reps": 16, "rest_seconds": 30},
                {"name": "Reverse Hyperextensions (on floor)", "sets": 3, "reps": 15, "rest_seconds": 30},
                {"name": "Glute Bridge March", "sets": 3, "reps": 16, "rest_seconds": 30}
            ],
            "Dumbbells": [
                {"name": "Dumbbell Deadlifts", "sets": 4, "reps": 12, "rest_seconds": 90}
            ],
            "Barbells": [
                {"name": "Barbell Deadlifts", "sets": 4, "reps": 6, "rest_seconds": 120}
            ],
            "Resistance Bands": [
                {"name": "Band Good Mornings", "sets": 3, "reps": 15, "rest_seconds": 45}
            ],
            "Kettlebells": [
                {"name": "Kettlebell Swings", "sets": 4, "reps": 15, "rest_seconds": 60}
            ],
            "Full Gym": [
                {"name": "Back Extension", "sets": 3, "reps": 15, "rest_seconds": 60}
            ]
        }
    },
    "chest": {
        "upper": {
            "None": [
                {"name": "Incline Push-ups", "sets": 3, "reps": 12, "rest_seconds": 45}
            ],
            "Dumbbells": [
                {"name": "Incline Dumbbell Press", "sets": 4, "reps": 10, "rest_seconds": 75}
            ],
            "Barbells": [
                {"name": "Incline Barbell Press", "sets": 4, "reps": 8, "rest_seconds": 90}
            ],
            "Resistance Bands": [
                {"name": "Band Chest Press (Incline)", "sets": 3, "reps": 15, "rest_seconds": 60}
            ],
            "Kettlebells": [
                {"name": "Incline Kettlebell Press", "sets": 3, "reps": 10, "rest_seconds": 60}
            ],
            "Full Gym": [
                {"name": "Incline Bench Press", "sets": 4, "reps": 8, "rest_seconds": 90}
            ]
        },
        "lower": {
            "None": [
                {"name": "Decline Push-ups", "sets": 3, "reps": 12, "rest_seconds": 45}
            ],
            "Dumbbells": [
                {"name": "Decline Dumbbell Press", "sets": 4, "reps": 10, "rest_seconds": 75}
            ],
            "Barbells": [
                {"name": "Decline Barbell Press", "sets": 4, "reps": 8, "rest_seconds": 90}
            ],
            "Resistance Bands": [
                {"name": "Band Chest Press (Decline)", "sets": 3, "reps": 15, "rest_seconds": 60}
            ],
            "Kettlebells": [
                {"name": "Decline Kettlebell Press", "sets": 3, "reps": 10, "rest_seconds": 60}
            ],
            "Full Gym": [
                {"name": "Decline Bench Press", "sets": 4, "reps": 8, "rest_seconds": 90}
            ]
        },
        "mid": {
            "None": [
                {"name": "Push-ups", "sets": 3, "reps": 15, "rest_seconds": 45}
            ],
            "Dumbbells": [
                {"name": "Dumbbell Bench Press", "sets": 4, "reps": 10, "rest_seconds": 75},
                {"name": "Dumbbell Flyes", "sets": 3, "reps": 12, "rest_seconds": 60},
                {"name": "Dumbbell Floor Press", "sets": 3, "reps": 10, "rest_seconds": 60},
                {"name": "Dumbbell Squeeze Press", "sets": 3, "reps": 12, "rest_seconds": 60},
                {"name": "Dumbbell Pullover", "sets": 3, "reps": 12, "rest_seconds": 60}
            ],
            "Barbells": [
                {"name": "Barbell Bench Press", "sets": 4, "reps": 8, "rest_seconds": 90},
                {"name": "Barbell Close-Grip Bench Press", "sets": 3, "reps": 10, "rest_seconds": 75},
                {"name": "Barbell Floor Press", "sets": 3, "reps": 8, "rest_seconds": 75},
                {"name": "Barbell Pin Press", "sets": 3, "reps": 8, "rest_seconds": 75}
            ],
            "Resistance Bands": [
                {"name": "Band Chest Press", "sets": 3, "reps": 15, "rest_seconds": 60},
                {"name": "Band Flyes", "sets": 3, "reps": 15, "rest_seconds": 60},
                {"name": "Band Push-ups", "sets": 3, "reps": 12, "rest_seconds": 45},
                {"name": "Band Squeeze Press", "sets": 3, "reps": 12, "rest_seconds": 60}
            ],
            "Kettlebells": [
                {"name": "Kettlebell Floor Press", "sets": 3, "reps": 12, "rest_seconds": 60},
                {"name": "Kettlebell Squeeze Press", "sets": 3, "reps": 12, "rest_seconds": 60},
                {"name": "Kettlebell Flyes", "sets": 3, "reps": 10, "rest_seconds": 60}
            ],
            "Full Gym": [
                {"name": "Chest Press Machine", "sets": 4, "reps": 10, "rest_seconds": 75},
                {"name": "Bench Press", "sets": 4, "reps": 8, "rest_seconds": 90},
                {"name": "Pec Deck Machine", "sets": 3, "reps": 12, "rest_seconds": 60},
                {"name": "Cable Flyes", "sets": 3, "reps": 15, "rest_seconds": 60},
                {"name": "Incline Chest Press Machine", "sets": 3, "reps": 10, "rest_seconds": 75}
            ]
        }
    },
    "legs": {
        "quads": {
            "None": [
                {"name": "Bodyweight Squats", "sets": 4, "reps": 15, "rest_seconds": 60},
                {"name": "Split Squats", "sets": 3, "reps": 12, "rest_seconds": 60},
                {"name": "Wall Sit", "sets": 3, "reps": 45, "rest_seconds": 45},  # seconds hold
                {"name": "Step-Ups (on chair/step)", "sets": 3, "reps": 12, "rest_seconds": 60},
                {"name": "Reverse Lunges", "sets": 3, "reps": 12, "rest_seconds": 60}
            ],
            "Dumbbells": [
                {"name": "Dumbbell Lunges", "sets": 3, "reps": 12, "rest_seconds": 60}
            ],
            "Barbells": [
                {"name": "Barbell Squats", "sets": 4, "reps": 8, "rest_seconds": 120}
            ],
            "Resistance Bands": [
                {"name": "Band Squats", "sets": 4, "reps": 15, "rest_seconds": 60}
            ],
            "Kettlebells": [
                {"name": "Goblet Squats", "sets": 4, "reps": 12, "rest_seconds": 75}
            ],
            "Full Gym": [
                {"name": "Leg Press", "sets": 4, "reps": 10, "rest_seconds": 90}
            ]
        },
        "hamstrings": {
            "None": [
                {"name": "Glute Bridge", "sets": 3, "reps": 20, "rest_seconds": 45},
                {"name": "Single-Leg Glute Bridge", "sets": 3, "reps": 12, "rest_seconds": 45},
                {"name": "Sliding Leg Curl (on towel)", "sets": 3, "reps": 12, "rest_seconds": 45},
                {"name": "Hip Thrust (bodyweight)", "sets": 3, "reps": 15, "rest_seconds": 45}
            ],
            "Dumbbells": [
                {"name": "Dumbbell Romanian Deadlift", "sets": 4, "reps": 12, "rest_seconds": 75}
            ],
            "Barbells": [
                {"name": "Barbell Romanian Deadlift", "sets": 4, "reps": 10, "rest_seconds": 90}
            ],
            "Resistance Bands": [
                {"name": "Band Leg Curl", "sets": 3, "reps": 15, "rest_seconds": 60}
            ],
            "Kettlebells": [
                {"name": "Kettlebell Swings", "sets": 4, "reps": 15, "rest_seconds": 60}
            ],
            "Full Gym": [
                {"name": "Leg Curl Machine", "sets": 4, "reps": 12, "rest_seconds": 75}
            ]
        },
        "calves": {
            "None": [
                {"name": "Standing Calf Raises", "sets": 4, "reps": 20, "rest_seconds": 45},
                {"name": "Single-Leg Calf Raise", "sets": 3, "reps": 15, "rest_seconds": 45},
                {"name": "Seated Calf Raise (bodyweight)", "sets": 3, "reps": 20, "rest_seconds": 45},
                {"name": "Calf Raise Hold (isometric)", "sets": 3, "reps": 30, "rest_seconds": 30}  # seconds hold
            ],
            "Dumbbells": [
                {"name": "Dumbbell Calf Raises", "sets": 4, "reps": 20, "rest_seconds": 45}
            ],
            "Barbells": [
                {"name": "Barbell Calf Raises", "sets": 4, "reps": 20, "rest_seconds": 60}
            ],
            "Resistance Bands": [
                {"name": "Band Calf Raises", "sets": 4, "reps": 20, "rest_seconds": 45}
            ],
            "Kettlebells": [
                {"name": "Kettlebell Calf Raises", "sets": 4, "reps": 20, "rest_seconds": 45}
            ],
            "Full Gym": [
                {"name": "Calf Raise Machine", "sets": 4, "reps": 20, "rest_seconds": 60}
            ]
        }
    },
    "core": {
        "upper": {
            "None": [
                {"name": "Crunches", "sets": 3, "reps": 20, "rest_seconds": 30}
            ],
            "Dumbbells": [
                {"name": "Weighted Crunches", "sets": 3, "reps": 15, "rest_seconds": 45}
            ],
            "Barbells": [],
            "Resistance Bands": [
                {"name": "Band Crunches", "sets": 3, "reps": 20, "rest_seconds": 30}
            ],
            "Kettlebells": [],
            "Full Gym": [
                {"name": "Cable Crunch", "sets": 3, "reps": 15, "rest_seconds": 45}
            ]
        },
        "lower": {
            "None": [
                {"name": "Leg Raises", "sets": 3, "reps": 15, "rest_seconds": 30}
            ],
            "Dumbbells": [
                {"name": "Weighted Leg Raises", "sets": 3, "reps": 12, "rest_seconds": 45}
            ],
            "Barbells": [],
            "Resistance Bands": [
                {"name": "Band Leg Raises", "sets": 3, "reps": 15, "rest_seconds": 30}
            ],
            "Kettlebells": [],
            "Full Gym": [
                {"name": "Hanging Leg Raise", "sets": 3, "reps": 10, "rest_seconds": 60}
            ]
        },
        "obliques": {
            "None": [
                {"name": "Russian Twists", "sets": 3, "reps": 20, "rest_seconds": 30}
            ],
            "Dumbbells": [
                {"name": "Dumbbell Side Bend", "sets": 3, "reps": 15, "rest_seconds": 30}
            ],
            "Barbells": [
                {"name": "Landmine Twists", "sets": 3, "reps": 12, "rest_seconds": 45}
            ],
            "Resistance Bands": [
                {"name": "Band Woodchoppers", "sets": 3, "reps": 15, "rest_seconds": 45}
            ],
            "Kettlebells": [
                {"name": "Kettlebell Russian Twists", "sets": 3, "reps": 20, "rest_seconds": 30}
            ],
            "Full Gym": [
                {"name": "Cable Woodchopper", "sets": 3, "reps": 15, "rest_seconds": 45}
            ]
        }
    },
    "arms": {
        "biceps": {
            "None": [
                {"name": "Isometric Curl Hold", "sets": 3, "reps": 30, "rest_seconds": 30}  # seconds hold
            ],
            "Dumbbells": [
                {"name": "Dumbbell Bicep Curl", "sets": 4, "reps": 12, "rest_seconds": 45}
            ],
            "Barbells": [
                {"name": "Barbell Curl", "sets": 4, "reps": 10, "rest_seconds": 60}
            ],
            "Resistance Bands": [
                {"name": "Band Curl", "sets": 4, "reps": 15, "rest_seconds": 45}
            ],
            "Kettlebells": [
                {"name": "Kettlebell Curl", "sets": 4, "reps": 12, "rest_seconds": 45}
            ],
            "Full Gym": [
                {"name": "Cable Curl", "sets": 4, "reps": 12, "rest_seconds": 45}
            ]
        },
        "triceps": {
            "None": [
                {"name": "Diamond Push-ups", "sets": 3, "reps": 12, "rest_seconds": 45}
            ],
            "Dumbbells": [
                {"name": "Dumbbell Tricep Extension", "sets": 3, "reps": 12, "rest_seconds": 45}
            ],
            "Barbells": [
                {"name": "Barbell Skullcrusher", "sets": 3, "reps": 10, "rest_seconds": 60}
            ],
            "Resistance Bands": [
                {"name": "Band Tricep Extension", "sets": 3, "reps": 15, "rest_seconds": 45}
            ],
            "Kettlebells": [
                {"name": "Kettlebell Tricep Extension", "sets": 3, "reps": 12, "rest_seconds": 45}
            ],
            "Full Gym": [
                {"name": "Cable Tricep Pushdown", "sets": 3, "reps": 15, "rest_seconds": 45}
            ]
        },
        "forearms": {
            "None": [
                {"name": "Reverse Push-ups", "sets": 3, "reps": 15, "rest_seconds": 30}
            ],
            "Dumbbells": [
                {"name": "Dumbbell Wrist Curl", "sets": 3, "reps": 20, "rest_seconds": 30}
            ],
            "Barbells": [
                {"name": "Barbell Wrist Curl", "sets": 3, "reps": 20, "rest_seconds": 30}
            ],
            "Resistance Bands": [
                {"name": "Band Wrist Curl", "sets": 3, "reps": 20, "rest_seconds": 30}
            ],
            "Kettlebells": [
                {"name": "Kettlebell Wrist Curl", "sets": 3, "reps": 20, "rest_seconds": 30}
            ],
            "Full Gym": [
                {"name": "Forearm Machine", "sets": 3, "reps": 20, "rest_seconds": 30}
            ]
        }
    },
    "shoulders": {
        "front": {
            "None": [
                {"name": "Pike Push-ups", "sets": 3, "reps": 10, "rest_seconds": 45}
            ],
            "Dumbbells": [
                {"name": "Dumbbell Front Raise", "sets": 3, "reps": 12, "rest_seconds": 45}
            ],
            "Barbells": [
                {"name": "Barbell Front Raise", "sets": 3, "reps": 12, "rest_seconds": 45}
            ],
            "Resistance Bands": [
                {"name": "Band Front Raise", "sets": 3, "reps": 15, "rest_seconds": 45}
            ],
            "Kettlebells": [
                {"name": "Kettlebell Front Raise", "sets": 3, "reps": 12, "rest_seconds": 45}
            ],
            "Full Gym": [
                {"name": "Shoulder Press Machine", "sets": 4, "reps": 10, "rest_seconds": 75}
            ]
        },
        "side": {
            "None": [
                {"name": "Plank to Push-up", "sets": 3, "reps": 10, "rest_seconds": 45}
            ],
            "Dumbbells": [
                {"name": "Dumbbell Lateral Raise", "sets": 3, "reps": 12, "rest_seconds": 45}
            ],
            "Barbells": [
                {"name": "Barbell Upright Row", "sets": 3, "reps": 10, "rest_seconds": 60}
            ],
            "Resistance Bands": [
                {"name": "Band Lateral Raise", "sets": 3, "reps": 15, "rest_seconds": 45}
            ],
            "Kettlebells": [
                {"name": "Kettlebell Lateral Raise", "sets": 3, "reps": 12, "rest_seconds": 45}
            ],
            "Full Gym": [
                {"name": "Lateral Raise Machine", "sets": 3, "reps": 12, "rest_seconds": 45}
            ]
        },
        "rear": {
            "None": [
                {"name": "Reverse Snow Angels", "sets": 3, "reps": 15, "rest_seconds": 45}
            ],
            "Dumbbells": [
                {"name": "Dumbbell Reverse Fly", "sets": 3, "reps": 12, "rest_seconds": 45}
            ],
            "Barbells": [
                {"name": "Barbell Reverse Fly", "sets": 3, "reps": 12, "rest_seconds": 45}
            ],
            "Resistance Bands": [
                {"name": "Band Reverse Fly", "sets": 3, "reps": 15, "rest_seconds": 45}
            ],
            "Kettlebells": [
                {"name": "Kettlebell Reverse Fly", "sets": 3, "reps": 12, "rest_seconds": 45}
            ],
            "Full Gym": [
                {"name": "Reverse Pec Deck", "sets": 3, "reps": 12, "rest_seconds": 45}
            ]
        }
    }
}

# Cardio and plyometric exercises for each equipment type
CARDIO_PLYO_EXERCISES = {
    "None": [
        {"name": "Jumping Jacks", "time_seconds": 45, "rest_seconds": 15},
        {"name": "Mountain Climbers", "time_seconds": 40, "rest_seconds": 20},
        {"name": "Burpees", "time_seconds": 30, "rest_seconds": 30},
        {"name": "High Knees", "time_seconds": 40, "rest_seconds": 20},
        {"name": "Bodyweight Lateral Hops", "time_seconds": 30, "rest_seconds": 20},
        {"name": "Skater Jumps", "time_seconds": 30, "rest_seconds": 20},
        {"name": "Plank Jacks", "time_seconds": 40, "rest_seconds": 20},
        {"name": "Tuck Jumps", "time_seconds": 20, "rest_seconds": 30},
        {"name": "Shadow Boxing", "time_seconds": 60, "rest_seconds": 15},
        {"name": "Stair Runs", "time_seconds": 60, "rest_seconds": 30},
    ],
    "Dumbbells": [
        {"name": "Dumbbell Thrusters", "time_seconds": 30, "rest_seconds": 30},
        {"name": "Dumbbell Snatch", "time_seconds": 30, "rest_seconds": 30},
        {"name": "Dumbbell Swings", "time_seconds": 30, "rest_seconds": 30},
        {"name": "Dumbbell Lateral Shuffle Press", "time_seconds": 30, "rest_seconds": 30},
    ],
    "Barbells": [
        {"name": "Barbell Complex (Deadlift, Row, Clean, Press)", "time_seconds": 60, "rest_seconds": 60},
        {"name": "Barbell Push Press", "time_seconds": 30, "rest_seconds": 30},
    ],
    "Resistance Bands": [
        {"name": "Band Sprints (anchor band and run in place)", "time_seconds": 30, "rest_seconds": 30},
        {"name": "Band Jump Squats", "time_seconds": 30, "rest_seconds": 30},
        {"name": "Band High Knees", "time_seconds": 30, "rest_seconds": 30},
    ],
    "Kettlebells": [
        {"name": "Kettlebell Swings", "time_seconds": 30, "rest_seconds": 30},
        {"name": "Kettlebell Snatch", "time_seconds": 30, "rest_seconds": 30},
        {"name": "Kettlebell Clean and Press", "time_seconds": 30, "rest_seconds": 30},
    ],
    "Full Gym": [
        {"name": "Treadmill Run", "time_seconds": 300, "rest_seconds": 60},
        {"name": "Rowing Machine", "time_seconds": 180, "rest_seconds": 60},
        {"name": "Battle Ropes", "time_seconds": 30, "rest_seconds": 30},
        {"name": "Box Jumps", "time_seconds": 30, "rest_seconds": 30},
        {"name": "Assault Bike", "time_seconds": 120, "rest_seconds": 60},
    ]
}

def get_exercises_for_muscle(muscle, user_equipment, min_per_muscle=2, force_all_subgroups=False):
    muscle_dict = EXERCISES.get(muscle, {})
    day_exercises = []
    for subgroup, eq_dict in muscle_dict.items():
        possible = []
        for eq in user_equipment:
            possible += eq_dict.get(eq, [])
        if possible:
            n = min_per_muscle
            if force_all_subgroups:
                n = max(1, min_per_muscle)  # Always at least 1 per subgroup
            n = min(n, len(possible))
            day_exercises.extend(random.sample(possible, k=n))
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
    "legs": ["legs", "core"],
    "upper body": ["chest", "back", "shoulders", "biceps", "triceps", "forearms"],
    "lower body": ["legs", "core"],
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
    "Walking",
]

def generate_workout(days_per_week, equipment, goal):
    workout_plan = []
    min_exercises_per_day = 5
    if goal == "Build Muscle":
        splits = MUSCLE_SPLITS.get(days_per_week, ["full body"])
        for day, split in enumerate(splits):
            if split == "active recovery":
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
            force_all_subgroups = split in ["pull", "legs", "lower body"]
            for muscle in muscles:
                min_per = 2 if not force_all_subgroups else 1
                day_exercises.extend(get_exercises_for_muscle(muscle, equipment, min_per_muscle=min_per, force_all_subgroups=force_all_subgroups))
            # Remove duplicates by exercise name
            seen = set()
            unique_exercises = []
            for ex in day_exercises:
                if ex['name'] not in seen:
                    unique_exercises.append(ex)
                    seen.add(ex['name'])
            # If less than min_exercises_per_day, fill with more from all muscles
            if len(unique_exercises) < min_exercises_per_day:
                all_possible = []
                for muscle in muscles:
                    all_possible += get_exercises_for_muscle(muscle, equipment, min_per_muscle=2, force_all_subgroups=force_all_subgroups)
                random.shuffle(all_possible)
                for ex in all_possible:
                    if ex['name'] not in seen and len(unique_exercises) < min_exercises_per_day:
                        unique_exercises.append(ex)
                        seen.add(ex['name'])
            workout_plan.append({
                "day": day + 1,
                "split": split.title(),
                "exercises": unique_exercises[:min_exercises_per_day],
                "rest_between_exercises_seconds": 90
            })
    elif goal == "General Fitness":
        splits = MUSCLE_SPLITS.get(days_per_week, ["full body"])
        num_days = days_per_week
        if num_days <= 4:
            for day in range(num_days):
                if day == num_days - 1:
                    cardio_exercises = []
                    for eq in equipment:
                        cardio_exercises += random.sample(
                            CARDIO_PLYO_EXERCISES.get(eq, []),
                            k=min(3, len(CARDIO_PLYO_EXERCISES.get(eq, [])))
                        )
                    if not cardio_exercises:
                        cardio_exercises = random.sample(CARDIO_PLYO_EXERCISES["None"], k=3)
                    workout_plan.append({
                        "day": day + 1,
                        "split": "Cardio/Plyometric",
                        "exercises": cardio_exercises,
                        "rest_between_exercises_seconds": 45
                    })
                else:
                    split = splits[day % len(splits)]
                    muscles = SPLIT_MUSCLES[split]
                    day_exercises = []
                    for muscle in muscles:
                        for ex in get_exercises_for_muscle(muscle, equipment, min_per_muscle=2):
                            ex_copy = ex.copy()
                            if "sets" in ex_copy and ex_copy["sets"] > 2:
                                ex_copy["sets"] = max(2, ex_copy["sets"] - 1)
                            if "reps" in ex_copy and ex_copy["reps"] > 8:
                                ex_copy["reps"] = max(8, ex_copy["reps"] - 2)
                            if "rest_seconds" in ex_copy and ex_copy["rest_seconds"] > 30:
                                ex_copy["rest_seconds"] = max(30, ex_copy["rest_seconds"] - 15)
                            day_exercises.append(ex_copy)
                    # Remove duplicates
                    seen = set()
                    unique_exercises = []
                    for ex in day_exercises:
                        if ex['name'] not in seen:
                            unique_exercises.append(ex)
                            seen.add(ex['name'])
                    # Fill if needed
                    if len(unique_exercises) < min_exercises_per_day:
                        all_possible = []
                        for muscle in muscles:
                            all_possible += get_exercises_for_muscle(muscle, equipment, min_per_muscle=3)
                        random.shuffle(all_possible)
                        for ex in all_possible:
                            if ex['name'] not in seen and len(unique_exercises) < min_exercises_per_day:
                                unique_exercises.append(ex)
                                seen.add(ex['name'])
                    workout_plan.append({
                        "day": day + 1,
                        "split": split.title(),
                        "exercises": unique_exercises[:min_exercises_per_day],
                        "rest_between_exercises_seconds": 75
                    })
        elif num_days in [5, 6]:
            cardio_days = [num_days - 2, num_days - 1]
            for day in range(num_days):
                if day in cardio_days:
                    cardio_exercises = []
                    for eq in equipment:
                        cardio_exercises += random.sample(
                            CARDIO_PLYO_EXERCISES.get(eq, []),
                            k=min(3, len(CARDIO_PLYO_EXERCISES.get(eq, [])))
                        )
                    if not cardio_exercises:
                        cardio_exercises = random.sample(CARDIO_PLYO_EXERCISES["None"], k=3)
                    workout_plan.append({
                        "day": day + 1,
                        "split": "Cardio/Plyometric",
                        "exercises": cardio_exercises,
                        "rest_between_exercises_seconds": 45
                    })
                else:
                    split = splits[day % len(splits)]
                    muscles = SPLIT_MUSCLES[split]
                    day_exercises = []
                    for muscle in muscles:
                        for ex in get_exercises_for_muscle(muscle, equipment, min_per_muscle=2):
                            ex_copy = ex.copy()
                            if "sets" in ex_copy and ex_copy["sets"] > 2:
                                ex_copy["sets"] = max(2, ex_copy["sets"] - 1)
                            if "reps" in ex_copy and ex_copy["reps"] > 8:
                                ex_copy["reps"] = max(8, ex_copy["reps"] - 2)
                            if "rest_seconds" in ex_copy and ex_copy["rest_seconds"] > 30:
                                ex_copy["rest_seconds"] = max(30, ex_copy["rest_seconds"] - 15)
                            day_exercises.append(ex_copy)
                    seen = set()
                    unique_exercises = []
                    for ex in day_exercises:
                        if ex['name'] not in seen:
                            unique_exercises.append(ex)
                            seen.add(ex['name'])
                    if len(unique_exercises) < min_exercises_per_day:
                        all_possible = []
                        for muscle in muscles:
                            all_possible += get_exercises_for_muscle(muscle, equipment, min_per_muscle=3)
                        random.shuffle(all_possible)
                        for ex in all_possible:
                            if ex['name'] not in seen and len(unique_exercises) < min_exercises_per_day:
                                unique_exercises.append(ex)
                                seen.add(ex['name'])
                    workout_plan.append({
                        "day": day + 1,
                        "split": split.title(),
                        "exercises": unique_exercises[:min_exercises_per_day],
                        "rest_between_exercises_seconds": 75
                    })
        elif num_days == 7:
            for day, split in enumerate(splits):
                if split == "active recovery":
                    exercises = [
                        {"name": ex, "time_seconds": 60, "rest_seconds": 15}
                        for ex in random.sample(ACTIVE_RECOVERY, k=min(2, len(ACTIVE_RECOVERY)))
                    ]
                    workout_plan.append({
                        "day": day + 1,
                        "split": split.title(),
                        "exercises": exercises
                    })
                elif split == "full body":
                    cardio_exercises = []
                    for eq in equipment:
                        cardio_exercises += random.sample(
                            CARDIO_PLYO_EXERCISES.get(eq, []),
                            k=min(3, len(CARDIO_PLYO_EXERCISES.get(eq, [])))
                        )
                    if not cardio_exercises:
                        cardio_exercises = random.sample(CARDIO_PLYO_EXERCISES["None"], k=3)
                    workout_plan.append({
                        "day": day + 1,
                        "split": "Cardio/Plyometric",
                        "exercises": cardio_exercises,
                        "rest_between_exercises_seconds": 45
                    })
                else:
                    muscles = SPLIT_MUSCLES[split]
                    day_exercises = []
                    for muscle in muscles:
                        for ex in get_exercises_for_muscle(muscle, equipment, min_per_muscle=2):
                            ex_copy = ex.copy()
                            if "sets" in ex_copy and ex_copy["sets"] > 2:
                                ex_copy["sets"] = max(2, ex_copy["sets"] - 1)
                            if "reps" in ex_copy and ex_copy["reps"] > 8:
                                ex_copy["reps"] = max(8, ex_copy["reps"] - 2)
                            if "rest_seconds" in ex_copy and ex_copy["rest_seconds"] > 30:
                                ex_copy["rest_seconds"] = max(30, ex_copy["rest_seconds"] - 15)
                            day_exercises.append(ex_copy)
                    seen = set()
                    unique_exercises = []
                    for ex in day_exercises:
                        if ex['name'] not in seen:
                            unique_exercises.append(ex)
                            seen.add(ex['name'])
                    if len(unique_exercises) < min_exercises_per_day:
                        all_possible = []
                        for muscle in muscles:
                            all_possible += get_exercises_for_muscle(muscle, equipment, min_per_muscle=3)
                        random.shuffle(all_possible)
                        for ex in all_possible:
                            if ex['name'] not in seen and len(unique_exercises) < min_exercises_per_day:
                                unique_exercises.append(ex)
                                seen.add(ex['name'])
                    workout_plan.append({
                        "day": day + 1,
                        "split": split.title(),
                        "exercises": unique_exercises[:min_exercises_per_day],
                        "rest_between_exercises_seconds": 75
                    })
    else:
        for day in range(days_per_week):
            workout_plan.append({
                "day": day + 1,
                "split": "Full Body",
                "exercises": [
                    {"name": "Jumping Jacks", "time_seconds": 45, "rest_seconds": 15},
                    {"name": "Bodyweight Squats", "sets": 3, "reps": 15, "rest_seconds": 45}
                ],
                "rest_between_exercises_seconds": 60
            })
    return workout_plan

if __name__ == "__main__":
    print("Welcome to the Workout Generator!\n")
    days = int(input("How many days per week do you want to work out? (1-7): "))
    print("Available equipment options:")
    for i, eq in enumerate(EQUIPMENT_OPTIONS):
        print(f"{i+1}. {eq}")
    eq_input = input("Enter the numbers of your available equipment, separated by commas (e.g. 1,3): ")
    eq_indices = [int(x.strip())-1 for x in eq_input.split(",") if x.strip().isdigit() and 0 < int(x.strip()) <= len(EQUIPMENT_OPTIONS)]
    user_equipment = [EQUIPMENT_OPTIONS[i] for i in eq_indices]
    print("Available goals:")
    for i, g in enumerate(GOAL_OPTIONS):
        print(f"{i+1}. {g}")
    goal_idx = int(input("Enter the number of your goal: ")) - 1
    user_goal = GOAL_OPTIONS[goal_idx]
    plan = generate_workout(days, user_equipment, user_goal)
    print(f"\nGenerated {user_goal} Workout Plan ({days} days/week):\n")
    for day in plan:
        print(f"Day {day['day']} - {day['split']}")
        for ex in day['exercises']:
            details = ', '.join(f"{k}: {v}" for k, v in ex.items() if k != 'name')
            print(f"  - {ex['name']} ({details})")
        print()