from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routers import users, quests

# Create the main application instance, our "General Manager"
app = FastAPI(
    title="Aletheia Project API",
    description="The backend for the Aletheia MVP.",
    version="0.1.0",
)

# --- Security: CORS Middleware ---
# This is a security permit that allows our frontend website to send
# requests to this backend. Without it, web browsers would block it.
origins = [
    "http://localhost",
    "http://localhost:3000", # A common port for React development
    "http://localhost:5173", # The default port for Vite/React
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# --- Hiring the Waitstaff (Including Routers) ---
# The General Manager officially hires the routers we created.
app.include_router(users.router, prefix="/api")
app.include_router(quests.router, prefix="/api")


# --- The "Front Door" ---
# A simple welcome message when someone visits the main backend URL.
# This is useful for testing if the server is running.
@app.get("/")
async def root():
    return {"message": "Welcome to the Aletheia Forge Backend"}