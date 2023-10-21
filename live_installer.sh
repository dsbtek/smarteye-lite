#!/bin/bash

# Get the directory where the script is located
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Define the name of the tar file
TAR_FILE="smarteye-lite.tar"
# Define the directory where you want to install the app
INSTALL_DIR="$SCRIPT_DIR"
# Define the FastAPI app directory name
APP_DIR="backend"

# Function to create a systemd service unit file
create_systemd_service() {
  cat > /etc/systemd/system/smarteyelite.service <<EOF
[Unit]
Description=My Smarteye-Lite Application

[Service]
ExecStart=/usr/bin/python $INSTALL_DIR/$APP_DIR/main.py  # Update with your backend executable path
WorkingDirectory=$INSTALL_DIR/$APP_DIR
Restart=always
User=pi  # Change this to the appropriate user

[Install]
WantedBy=multi-user.target
EOF
}

# Function to enable and start the systemd service
enable_and_start_service() {
  systemctl enable smarteyelite.service
  systemctl start smarteyelite.service
}

# Function to install the app
install_app() {
  # Extract the tar file
  tar -xvf "$TAR_FILE" -C "$INSTALL_DIR"
  # Navigate to the app directory
  cd "$INSTALL_DIR/$APP_DIR"
  python3 -m venv venv
  source venv/bin/activate
  # Install FastAPI dependencies
  pip install -r requirements.txt
  # Run the FastAPI server
  #   uvicorn main:app --host 0.0.0.0 --port 8000 --reload &
  # Create a systemd service unit file
  create_systemd_service
  
  # Enable and start the systemd service
  enable_and_start_service

  # Open the default browser with index.html
  sleep 10 # Wait for the server to start (adjust the delay as needed)
  # Open the default web browser with the specified URL
  if [[ "$OSTYPE" == "darwin"* ]]; then
      open "http://localhost:8000/"
  elif [[ "$OSTYPE" == "linux-gnu"* ]]; then
      xdg-open "http://localhost:8000/"
  else
      echo "Unsupported operating system"
  fi

  
}

# Main installation process
install_app
