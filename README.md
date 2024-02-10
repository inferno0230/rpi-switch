# Project Overview: rpi-switch

## Introduction

This project is designed to control a relay switch which emulates a power switch of a computer to turn it on or off, using a Raspberry Pi through MQTT communication. It consists of several modules, including MqttService, PowerSwitch, and the main execution script, main.py.

## Project Structure

```plaintext
.
├── functions
│   ├── __init__.py
│   ├── MqttService.py
│   └── PowerSwitch.py
├── main.py
├── .env
├── README.md
└── requirements.txt
```
## Here
### init.py
```Empty initialization file to treat the directory as a Python package. ```
### MqttService.py
```Module handling MQTT communication and interaction with PowerSwitch. ```
### PowerSwitch.py
```Module defining the PowerSwitch class responsible for controlling the relay switch.```
### main.py
```The main execution script initializing and running the MQTT service.```

### Configuration for `.env`
```plaintext
MQTT_BROKER_PORT=<Port where mqtt server is listening>
MQTT_TOPIC=<topic to suscribe to>
MQTT_BROKER_ADDRESS=<IP address of mqtt server, or localhost if its on the raspberry pi itself>
MQTT_USERNAME=<username>
MQTT_PASSWORD=<password>
```

## Installation

To install the project, follow these steps:

```plaintext
# Clone the repository
git clone https://github.com/your-username/rpi-switch.git

# Navigate to the project directory
cd rpi-switch

# Install dependencies
pip install -r requirements.txt
```

## Setup systemd service to execute script at boot
``` $ sudo nano /etc/systemd/system/rpi_switch.service```

```plaintext
[Unit]
Description=Raspberry Pi Switch Service
After=network.target

[Service]
ExecStart=/usr/bin/python3 /path/to/rpi-switch/main.py
WorkingDirectory=/path/to/rpi-switch
Restart=always
User=root

[Install]
WantedBy=default.target
```

```$ sudo systemctl start rpi_switch ```

```$ sudo systemctl enable rpi_switch```
