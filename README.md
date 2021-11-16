# DogPushbuttons
Welcome to Dog Pushbutton from Capstone Fall 2021 Team. This is repository contains designed piece of software for Dog pushbuttons.

## Features 
- Receive command from pushbutton though Raspberry Pi GPIO
- Send alert to mobile and computer via [Pushover](https://pushover.net/)
- Play sound though Raspberry Pi output headphone port

## Team
Client: **Professor Karen Beiter**

Lead Technician: **Sahand Nowshiravani**

Assistant Technician: **Lucas Jones**

## Diagram
![Screenshot 2021-11-15 231714](https://user-images.githubusercontent.com/13942195/141911259-a4ff4fc9-f957-4ac4-a3b7-12223d736c2f.png)

## Setup
Install python-pushover and pygame library from Python package manager:
```shell
python -m pip install -U python-pushover pygame
```
or
```shell
pip install -r requirements.txt
```
Sign up [Pushover](https://pushover.net/) and create application for API token.
