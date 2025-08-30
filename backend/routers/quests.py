from fastapi import APIRouter, HTTPException
from google.cloud import firestore
import os

# Import the data templates we defined earlier
from ..models.schemas import QuestCreate, AARCreate

# --- Database Connection ---
# This is a more robust way to connect to Firestore, which works both
# locally (if you set it up) and automatically in Google Cloud Run.
try:
    if os.getenv("GCP_PROJECT"):
        # We're in the cloud
        db = firestore.Client()
    else:
        # We're running locally. This requires a special setup with a "service account file".
        # For our MVP, we'll focus on the cloud deployment.
        # To run locally, you'd need to set this path:
        # os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "path/to/your/credentials.json"
        db = firestore.Client()
except Exception as e:
    print(f"Could not connect to Firestore: {e}")
    db = None

# This is our Head Waiter's notepad
router = APIRouter()

@router.post("/quests", tags=["Quests"])
async def create_quest(quest_data: QuestCreate):
    """
    Takes an order for a new Quest and saves it to the database.
    """
    if not db:
        raise HTTPException(status_code=500, detail="Database not configured")

    try:
        # Create a new document in the "quests" collection
        quest_ref = db.collection("quests").document()

        # Save the main quest data
        quest_ref.set({
            "userId": quest_data.userId,
            "questStatement": quest_data.questStatement,
            "strengths": quest_data.strengths,
            "isActive": True,
            "createdAt": firestore.SERVER_TIMESTAMP
        })

        # If the user provided If-Then plans, save them too
        if quest_data.ifThenPlans:
            for plan in quest_data.ifThenPlans:
                plan_ref = quest_ref.collection("ifThenPlans").document()
                plan_ref.set({
                    "ifSituation": plan.ifSituation,
                    "thenAction": plan.thenAction,
                    "isCompletedToday": False
                })

        return {"questId": quest_ref.id, "message": "Quest created successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/quests/{quest_id}/aars", tags=["Quests"])
async def create_aar(quest_id: str, aar_data: AARCreate):
    """
    Takes an order for a new After-Action Review and saves it.
    """
    if not db:
        raise HTTPException(status_code=500, detail="Database not configured")

    try:
        # Find the correct quest to add the AAR to
        quest_ref = db.collection("quests").document(quest_id)

        # Create a new AAR document inside that quest
        aar_ref = quest_ref.collection("aars").document()
        aar_ref.set({
            "intendedOutcome": aar_data.intendedOutcome,
            "actualOutcome": aar_data.actualOutcome,
            "learnings": aar_data.learnings,
            "createdAt": firestore.SERVER_TIMESTAMP
        })

        return {"aarId": aar_ref.id, "message": "AAR submitted successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))