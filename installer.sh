#!/bin/bash

# Define paths to your FastAPI and Vue.js projects
FASTAPI_DIR="/path/to/fastapi_project"
VUEJS_DIR="/path/to/vuejs_project"

# Function to configure and run FastAPI
configure_and_run_fastapi() {
  # Navigate to the FastAPI directory
  cd "$FASTAPI_DIR"
  
  # Install FastAPI dependencies (assuming you use virtualenv)
  virtualenv venv
  source venv/bin/activate
  pip install -r requirements.txt
  
  # Run FastAPI server
  uvicorn main:app --host 0.0.0.0 --port 8000 --reload
}

# Function to configure and run Vue.js
configure_and_run_vuejs() {
  # Navigate to the Vue.js directory
  cd "$VUEJS_DIR"
  
  # Install Vue.js dependencies
  npm install
  
  # Build Vue.js application
  npm run build
  
  # Run Vue.js development server
  npm run serve
}

# Function to run both FastAPI and Vue.js
run_app() {
  configure_and_run_fastapi &
  configure_and_run_vuejs &
  
  # Wait for both processes to finish
  wait
}

# Run the whole application
run_app
