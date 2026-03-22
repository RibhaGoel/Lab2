# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a REST API for managing a simple todo application using the FastAPI framework. You'll learn how to create API endpoints, handle HTTP requests, define data models with validation, and structure a modern Python web service. By completing this assignment, you'll understand the fundamentals of API design and how to use FastAPI's powerful features for rapid development.

## 📝 Tasks

### 🛠️ Set Up FastAPI Application and Create Basic Endpoints

#### Description
Create a new FastAPI application with a basic project structure. Set up GET, POST, PUT, and DELETE endpoints to manage a todo list. You'll need to define your data models and implement route handlers for all CRUD operations.

#### Requirements
Completed program should:

- Initialize FastAPI application with proper imports and configuration
- Define a Pydantic model for Todo items (with fields: id, title, description, completed)
- Create GET endpoint to retrieve all todos
- Create POST endpoint to create a new todo
- Create PUT endpoint to update an existing todo
- Create DELETE endpoint to remove a todo by id
- Include appropriate HTTP status codes for responses

### 🛠️ Add Data Validation and Error Handling

#### Description
Enhance your API with input validation and error handling. Implement proper validation for todo data, validate request parameters, and return meaningful error messages when operations fail.

#### Requirements
Completed program should:

- Use Pydantic validators to ensure todo data is valid (e.g., title is not empty)
- Validate todo IDs and handle cases where a todo doesn't exist
- Return appropriate HTTP error responses (400, 404, 500)
- Include error messages that help clients understand what went wrong
- Test all endpoints with various valid and invalid inputs
