from fastapi import FastAPI, HTTPException


app = FastAPI()


activities = {
   "Chess Club": {
      "description": "Learn strategies and compete in chess tournaments",
      "schedule": "Fridays, 3:30 PM - 5:00 PM",
      "max_participants": 12,
      "participants": ["michael@mergington.edu", "daniel@mergington.edu"]
   },
   "Programming Class": {
      "description": "Learn programming fundamentals and build software projects",
      "schedule": "Tuesdays and Thursdays, 3:30 PM - 4:30 PM",
      "max_participants": 20,
      "participants": ["emma@mergington.edu", "sophia@mergington.edu"]
   },
   "Gym Class": {
      "description": "Physical education and sports activities",
      "schedule": "Mondays, Wednesdays, Fridays, 2:00 PM - 3:00 PM",
      "max_participants": 30,
      "participants": ["john@mergington.edu", "olivia@mergington.edu"]
   },
   "Basketball Team": {
      "description": "Competitive basketball training and games",
      "schedule": "Tuesdays and Thursdays, 4:00 PM - 6:00 PM",
      "max_participants": 15,
      "participants": []
   },
   "Swimming Club": {
      "description": "Swimming training and water sports",
      "schedule": "Mondays and Wednesdays, 3:30 PM - 5:00 PM",
      "max_participants": 20,
      "participants": []
   },
   "Art Studio": {
      "description": "Express creativity through painting and drawing",
      "schedule": "Wednesdays, 3:30 PM - 5:00 PM",
      "max_participants": 15,
      "participants": []
   },
   "Drama Club": {
      "description": "Theater arts and performance training",
      "schedule": "Tuesdays, 4:00 PM - 6:00 PM",
      "max_participants": 25,
      "participants": []
   },
   "Debate Team": {
      "description": "Learn public speaking and argumentation skills",
      "schedule": "Thursdays, 3:30 PM - 5:00 PM",
      "max_participants": 16,
      "participants": []
   },
   "Science Club": {
      "description": "Hands-on experiments and scientific exploration",
      "schedule": "Fridays, 3:30 PM - 5:00 PM",
      "max_participants": 20,
      "participants": []
   },
   # New sports activities
   "Soccer Team": {
      "description": "Competitive soccer training and matches",
      "schedule": "Mondays and Thursdays, 4:00 PM - 6:00 PM",
      "max_participants": 18,
      "participants": []
   },
   "Track and Field": {
      "description": "Running, jumping and throwing events practice",
      "schedule": "Tuesdays and Fridays, 3:30 PM - 5:00 PM",
      "max_participants": 25,
      "participants": []
   },
   # New artistic activities
   "Photography Club": {
      "description": "Learn photography, composition, and editing",
      "schedule": "Wednesdays, 4:00 PM - 5:30 PM",
      "max_participants": 20,
      "participants": []
   },
   "Ceramics Workshop": {
      "description": "Hand-building and wheel-throwing ceramics",
      "schedule": "Thursdays, 3:30 PM - 5:30 PM",
      "max_participants": 12,
      "participants": []
   },
   # New intellectual activities
   "Math Olympiad": {
      "description": "Advanced problem solving and competition prep",
      "schedule": "Wednesdays, 3:30 PM - 4:30 PM",
      "max_participants": 15,
      "participants": []
   },
   "Robotics Club": {
      "description": "Design and build robots for challenges",
      "schedule": "Tuesdays and Thursdays, 4:00 PM - 6:00 PM",
      "max_participants": 16,
      "participants": []
   }
}

@app.get("/activities")
def get_activities():
   """Return all activities and their details"""
   return activities

@app.post("/activities/{activity_name}/signup")
def signup_for_activity(activity_name: str, email: str):
   """Sign up a student for an activity"""
   # Validate activity exists
   if activity_name not in activities:
      raise HTTPException(status_code=404, detail="Activity not found")

   # Get the activity
   activity = activities[activity_name]

   # Validate student is not already signed up
   if email in activity["participants"]:
     raise HTTPException(status_code=400, detail="Student is already signed up")

   # Add student
   activity["participants"].append(email)
   return {"message": f"Signed up {email} for {activity_name}"}
