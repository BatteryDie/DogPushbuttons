from gpiozero import Button
from pushover import Client  # For sending alert
import time
import pygame  # For playing sound
pygame.init() # Load pygame - no gui

client = Client("USER_HERE", api_token="TOKEN_HERE")

bath_button = Button(17)
out_button = Button(27)
water_button = Button(22)
food_button = Button(23)
play_button = Button(24)

while True:
    localtime = time.asctime( time.localtime(time.time()) )
    if bath_button.is_pressed:
        print(localtime+" Bathroom!")
        my_sound = pygame.mixer.Sound('sounds/bathroom.mp3')
        my_sound.play()
        client.send_message("Bathroom!", title="Dog Pushbuttons")
        time.sleep(0.5)
    if out_button.is_pressed:
        print(localtime+" Outside!")
        my_sound = pygame.mixer.Sound('sounds/outside.mp3')
        my_sound.play()
        client.send_message("Outside!", title="Dog Pushbuttons")
        time.sleep(0.5)
    if water_button.is_pressed:
        print(localtime+" Water!")
        my_sound = pygame.mixer.Sound('sounds/water.mp3')
        my_sound.play()
        client.send_message("Water!", title="Dog Pushbuttons")
        time.sleep(0.5)
    if food_button.is_pressed:
        print(localtime+" Food!")
        my_sound = pygame.mixer.Sound('sounds/food.mp3')
        my_sound.play()
        client.send_message("Food!", title="Dog Pushbuttons")
        time.sleep(0.5)
    if play_button.is_pressed:
        print(localtime+" Play!")
        my_sound = pygame.mixer.Sound('sounds/play.mp3')
        my_sound.play()
        client.send_message("Play!", title="Dog Pushbuttons")
        time.sleep(0.5)
