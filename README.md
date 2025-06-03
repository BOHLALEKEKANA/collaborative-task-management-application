# collaborative task management application

To set up and run this application:

Backend (Java/Spring Boot):

Ensure you have Java 17+ and Maven installed
Place all Java files in appropriate package structure under src/main/java/com/example/taskmanager
Place application.properties in src/main/resources
Run mvn spring-boot:run in the project directory
The backend will run on http://localhost:8080

Frontend (Python/Flask):

Install Python 3.8+
Create a virtual environment: python -m venv venv
Activate virtual environment and install requirements: pip install -r requirements.txt
Place app.py and templates/index.html in your project directory
Run python app.py
The frontend will run on http://localhost:5000

Features:

User authentication (basic HTTP authentication)
Real-time task creation, updates, and deletion
Task assignment to users
Status tracking (To Do, In Progress, Done)
Real-time updates across all connected clients using WebSockets

Notes:

The backend uses an in-memory H2 database for simplicity
Add proper security configuration (JWT, OAuth) for production
Create a templates folder for index.html
Ensure both backend and frontend are running simultaneously
Access the application at http://localhost:5000
