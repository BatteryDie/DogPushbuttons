import keyboard
from pushover import Client  # For sending alert
import time
import pygame  # For playing sound
pygame.init() # Load pygame - no gui

client = Client("ur7vskev12zazdf6twu9dt5a4wy7pf", api_token="aqdqexpqcpagiazt1a386xjnp4mgw4")

bath_button = Button(17)
out_button = Button(27)
water_button = Button(22)
food_button = Button(23)
play_button = Button(24)

while True:
    localtime = time.asctime( time.localtime(time.time()) )
    if keyboard.is_pressed('q'):
        try:
            print(localtime+" Bathroom!")
            my_sound = pygame.mixer.Sound('sounds/bathroom.mp3')
            my_sound.play()
            client.send_message("Bathroom!", title="Dog Pushbuttons")
            time.sleep(0.5)
        except:
            print("Bathroom: Error. Please check internet connection or sound files.")
    if keyboard.is_pressed('w'):
        try:
            print(localtime+" Outside!")
            my_sound = pygame.mixer.Sound('sounds/outside.mp3')
            my_sound.play()
            client.send_message("Outside!", title="Dog Pushbuttons")
            time.sleep(0.5)
        except:
            print("Outside: Error. Please check internet connection or sound files.")
    if keyboard.is_pressed('e'):
        try:
            print(localtime+" Water!")
            my_sound = pygame.mixer.Sound('sounds/water.mp3')
            my_sound.play()
            client.send_message("Water!", title="Dog Pushbuttons")
            time.sleep(0.5)
        except:
            print("Water: Error. Please check internet connection or sound files.")
    if keyboard.is_pressed('a'):
        try:
            print(localtime+" Food!")
            my_sound = pygame.mixer.Sound('sounds/food.mp3')
            my_sound.play()
            client.send_message("Food!", title="Dog Pushbuttons")
            time.sleep(0.5)
        except:
            print("Food: Error. Please check internet connection or sound files.")
    if keyboard.is_pressed('s'):
        try:
            print(localtime+" Play!")
            my_sound = pygame.mixer.Sound('sounds/play.mp3')
            my_sound.play()
            client.send_message("Play!", title="Dog Pushbuttons")
            time.sleep(0.5)
        except:
            print("Play: Error. Please check internet connection or sound files.")

