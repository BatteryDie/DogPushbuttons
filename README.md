# DogPushbuttons
Welcome to Dog Pushbutton from Capstone Fall 2021 Team. This is repository contains designed piece of software for Dog pushbuttons.

![image](https://user-images.githubusercontent.com/13942195/151671405-c9f3733e-e4a4-4155-93ae-dae64eb865e1.png)


## Features 
- Receive command from pushbutton though Raspberry Pi GPIO
- Send alert to mobile and computer via [Pushover](https://pushover.net/)
- Play sound though Raspberry Pi output headphone port

## Pushover on iOS and watchOS 

![image](https://user-images.githubusercontent.com/13942195/151671487-fd559d3c-c28f-4d1a-984e-66ece1a4cc75.png) ![image](https://user-images.githubusercontent.com/13942195/151671482-972cbfe7-3cfe-4c15-9c3d-d7531e199de4.png)

## Team
Client: **Professor Karen Beiter**

Lead Technician: **Sahand Nowshiravani**

Assistant Technician: **Luca Jones**

## Diagram
![Screenshot 2021-11-15 231714](https://user-images.githubusercontent.com/13942195/141911259-a4ff4fc9-f957-4ac4-a3b7-12223d736c2f.png)

![image](https://user-images.githubusercontent.com/13942195/151671380-f9e13919-49eb-4c2b-bd02-201a0560aefd.png)

## Setup
1. Update Raspberry Pi OS and Python
```shell
sudo apt update && sudo apt upgrade
```
2. Install Pushover for Python, gpiozero and PyGame modules from Python package manager:
```shell
python -m pip install -U python-pushover gpiozero pygame
```
3. To create startup in GUI. Add line on /etc/xdg/lxsession/LXDE-pi/autostart: 
```shell
@lxterminal -e /home/pi/DogPushbuttons-main/startup.sh
```
![2021-11-29-164412_655x417_scrot](https://user-images.githubusercontent.com/13942195/143947869-1445eee0-b3c8-4882-b927-442ee33d1fec.png)

If you preferred startup in headless or commandline intead of GUI: [Click here](https://www.makeuseof.com/how-to-run-a-raspberry-pi-program-script-at-startup/).

4. Sign up [Pushover](https://pushover.net/) and create application for API token and User token.

5. Download zip of this repo for Raspberry Pi:

![Download zip](https://user-images.githubusercontent.com/13942195/142032300-4aa0cc3d-84c8-4ba0-962f-1a33072dd566.png)

6. Edit the script with new API token and User token. Example:
```python
client = Client("us7vsksv12zazdf6hwu2dt8a4wy743f", api_token="afdsfsdfwzxczt1426xjnp1waj4")
```

## Manually run the script
On Raspberry Pi with pushbutton switches
```shell
python main_pi.py
```
On PC with keyboard
```shell
python main_pc.py
```

## Troubleshooting
If you got Pygame error such as "No Mixer module found". Try this:
```shell
sudo apt-get install git curl libsdl2-mixer-2.0-0 libsdl2-image-2.0-0 libsdl2-2.0-0
```
