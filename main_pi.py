from gpiozero import Button
from pushover import Client  # For sending alert
import time
import pygame  # For playing sound
pygame.init()

client = Client("ur7vskev12zazdf6twu9dt5a4wy7pf", api_token="aqdqexpqcpagiazt1a386xjnp4mgw4")

bath_button = Button(14,None,True)
out_button = Button(15,None,True)
water_button = Button(16,None,True)
food_button = Button(17,None,True)

while True:
    if bath_button.is_pressed:
        print("Bathroom!")
        my_sound = pygame.mixer.Sound('sounds/bathroom.mp3')
        my_sound.play()
        client.send_message("Bathroom!", title="Dog Pushbuttons")
    if out_button.is_pressed:
        print("Outside!")
        my_sound = pygame.mixer.Sound('sounds/outside.mp3')
        my_sound.play()
        client.send_message("Outside!", title="Dog Pushbuttons")
    if water_button.is_pressed:
        print("Water!")
        my_sound = pygame.mixer.Sound('sounds/water.mp3')
        my_sound.play()
        client.send_message("Water!", title="Dog Pushbuttons")
    if food_button.is_pressed:
        print("Food!")
        my_sound = pygame.mixer.Sound('sounds/food.mp3')
        my_sound.play()
        client.send_message("Food!", title="Dog Pushbuttons")
    time.sleep(0.1)