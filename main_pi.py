from gpiozero import Button
from pushover import Client  # For sending alert
import time
import pygame  # For playing sound
pygame.init() # Load pygame - no gui

client = Client("ur7vskev12zazdf6twu9dt5a4wy7pf", api_token="aqdqexpqcpagiazt1a386xjnp4mgw4")

bath_button = Button(19,None,True)
out_button = Button(26,None,True)
water_button = Button(20,None,True)
food_button = Button(21,None,True)

while True:
    localtime = time.asctime( time.localtime(time.time()) )
    if bath_button.is_pressed:
        print(localtime+" Bathroom!")
        my_sound = pygame.mixer.Sound('sounds/bathroom.mp3')
        my_sound.play()
        client.send_message("Bathroom!", title="Dog Pushbuttons")
        time.sleep(1.0)
    if out_button.is_pressed:
        print(localtime+" Outside!")
        my_sound = pygame.mixer.Sound('sounds/outside.mp3')
        my_sound.play()
        client.send_message("Outside!", title="Dog Pushbuttons")
        time.sleep(1.0)
    if water_button.is_pressed:
        print(localtime+" Water!")
        my_sound = pygame.mixer.Sound('sounds/water.mp3')
        my_sound.play()
        client.send_message("Water!", title="Dog Pushbuttons")
        time.sleep(1.0)
    if food_button.is_pressed:
        print(localtime+" Food!")
        my_sound = pygame.mixer.Sound('sounds/food.mp3')
        my_sound.play()
        client.send_message("Food!", title="Dog Pushbuttons")
        time.sleep(1.0)


