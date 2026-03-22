"""
FastAPI Todo Application

Build a REST API for managing todos with FastAPI.
This starter code provides the basic structure to get you started.

TODO: Complete the implementation by adding endpoints and handlers.
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

# Initialize FastAPI application
app = FastAPI(title="Todo API", version="1.0.0")

# Define the Todo data model
class Todo(BaseModel):
    """
    Represents a todo item in our application.
    
    Attributes:
        id: Unique identifier for the todo
        title: Short title of the todo
        description: Detailed description of the task
        completed: Whether the todo is completed
    """
    id: int
    title: str
    description: Optional[str] = None
    completed: bool = False


# In-memory storage for todos (for simplicity)
# In a real application, you would use a database
todos_db: List[Todo] = [
    Todo(id=1, title="Learn FastAPI", description="Understand FastAPI basics", completed=False),
    Todo(id=2, title="Build an API", description="Create a REST API with FastAPI", completed=False),
]

# TODO: Implement these endpoints

# @app.get("/todos", response_model=List[Todo])
# async def get_todos():
#     """Retrieve all todos"""
#     pass


# @app.get("/todos/{todo_id}", response_model=Todo)
# async def get_todo(todo_id: int):
#     """Retrieve a specific todo by ID"""
#     pass


# @app.post("/todos", response_model=Todo, status_code=201)
# async def create_todo(todo: Todo):
#     """Create a new todo"""
#     pass


# @app.put("/todos/{todo_id}", response_model=Todo)
# async def update_todo(todo_id: int, todo: Todo):
#     """Update an existing todo"""
#     pass


# @app.delete("/todos/{todo_id}", status_code=204)
# async def delete_todo(todo_id: int):
#     """Delete a todo"""
#     pass


# Example of a basic endpoint (already implemented)
@app.get("/")
async def root():
    """Root endpoint - returns a welcome message"""
    return {"message": "Welcome to the Todo API"}


if __name__ == "__main__":
    import uvicorn
    # Run the server with: uvicorn starter-code:app --reload
    uvicorn.run(app, host="0.0.0.0", port=8000)
