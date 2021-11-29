import keyboard
from pushover import Client  # For sending alert
import time
import pygame  # For playing sound
pygame.init() # Load pygame - no gui

client = Client("USER_HERE", api_token="TOKEN_HERE")

while True:
    localtime = time.asctime( time.localtime(time.time()) )
    if keyboard.is_pressed('q'):
        print(localtime+" Bathroom!")
        my_sound = pygame.mixer.Sound('sounds/bathroom.mp3')
        my_sound.play()
        client.send_message("Bathroom!", title="Dog Pushbuttons")
        time.sleep(0.5)
    if keyboard.is_pressed('w'):
        print(localtime+" Outside!")
        my_sound = pygame.mixer.Sound('sounds/outside.mp3')
        my_sound.play()
        client.send_message("Outside!", title="Dog Pushbuttons")
        time.sleep(0.5)
    if keyboard.is_pressed('e')
        print(localtime+" Water!")
        my_sound = pygame.mixer.Sound('sounds/water.mp3')
        my_sound.play()
        client.send_message("Water!", title="Dog Pushbuttons")
        time.sleep(0.5)
    if keyboard.is_pressed('a'):
        print(localtime+" Food!")
        my_sound = pygame.mixer.Sound('sounds/food.mp3')
        my_sound.play()
        client.send_message("Food!", title="Dog Pushbuttons")
        time.sleep(0.5)
    if keyboard.is_pressed('w'):
        print(localtime+" Play!")
        my_sound = pygame.mixer.Sound('sounds/play.mp3')
        my_sound.play()
        client.send_message("Play!", title="Dog Pushbuttons")
        time.sleep(0.5)
