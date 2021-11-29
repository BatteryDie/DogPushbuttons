# DogPushbuttons
Welcome to Dog Pushbutton from Capstone Fall 2021 Team. This is repository contains designed piece of software for Dog pushbuttons.

## Features 
- Receive command from pushbutton though Raspberry Pi GPIO
- Send alert to mobile and computer via [Pushover](https://pushover.net/)
- Play sound though Raspberry Pi output headphone port

## Team
Client: **Professor Karen Beiter**

Lead Technician: **Sahand Nowshiravani**

Assistant Technician: **Luca Jones**

## Diagram
![Screenshot 2021-11-15 231714](https://user-images.githubusercontent.com/13942195/141911259-a4ff4fc9-f957-4ac4-a3b7-12223d736c2f.png)

## Setup
1. Install Pushover for Python, gpiozero and PyGame modules from Python package manager:
```shell
python -m pip install -U python-pushover gpiozero pygame
```
2. To create startup in GUI. Edit and add line on /etc/xdg/lxsession/LXDE-pi/autostart: 
```shell
@lxterminal -e python /home/pi/DogPushbuttons-main/main_pi.py
```

3. Sign up [Pushover](https://pushover.net/) and create application for API token and User token.

4. Download zip of this repo for Raspberry Pi:

![Download zip](https://user-images.githubusercontent.com/13942195/142032300-4aa0cc3d-84c8-4ba0-962f-1a33072dd566.png)

5. Edit the script with new API token and User token. Example:
```python
client = Client("ur7vskev12zazdf6twu9dt5a4wy7pf", api_token="aqdqexpqcpagiazt1a386xjnp4mgw4")
```

## Manually run the script on Raspberry Pi
```shell
python main_pi.py
```

## Troubleshooting
If you got Pygame error such as "No Mixer module found". Try this:
```shell
apt-get install git curl libsdl2-mixer-2.0-0 libsdl2-image-2.0-0 libsdl2-2.0-0
```
