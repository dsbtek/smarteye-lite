
# smarteye-lite Installation Guide

This guide will walk you through the process of installing and running the smarteye-lite on Raspberry Pi.

## Prerequisites

- Raspberry Pi 3 (or compatible) with Raspberry Pi OS (or a compatible Linux distribution) installed.
- Internet connection to download and install dependencies.

## Installation Steps

1. **Clone the repo:**
git clone https://github.com/dsbtek/smarteye-lite.git

2. **Open a Terminal:**

   Open a terminal on your Raspberry Pi. You can usually find the terminal application in the Raspberry Pi desktop environment.

3. **Navigate to the Clone folder/backend:**

   Use the `cd` command to navigate to the directory where you clone the project.

   
   cd /smarteye-lite/backend

4. **Activate the environment:**

    python3 -m venv venv
    source venv/bin/activate if you are on Ubintu or MacOs

6. **Install the dependencies:**

   pip3 install "fastapi[all]"
   pip3 install sqlalchemy
   pip3 install pandas
   pip3 install python-multipart

## How to send request to the app endpoint from the devices on the same network


**To call the endpoints of app from the other devices on the same wireless or locall network, you can follow the guide:**

    Get the IP Address of your Rasberry pie by running the command below on the terminal:
    enter "ifconfig" or "ip a" as appropriate. 
    Identify the IP address corresponding to your network interface (e.g., eth0, wlan0).
    Take note of this IP address, which will typically resemble "192.168.x.x" or "10.x.x.x." 
    You will use this address to send request to the app.
