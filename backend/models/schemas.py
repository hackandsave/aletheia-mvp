from pydantic import BaseModel
from typing import List, Optional

# Template for creating an If-Then Plan
class IfThenPlanCreate(BaseModel):
    ifSituation: str
    thenAction: str

# Template for creating a Quest
# It can optionally include a starting list of If-Then plans
class QuestCreate(BaseModel):
    userId: str
    questStatement: str
    strengths: List[str]
    ifThenPlans: Optional[List[IfThenPlanCreate]] = None

# Template for creating an After-Action Review (AAR)
class AARCreate(BaseModel):
    intendedOutcome: str
    actualOutcome: str
    learnings: str