from pushover import Client  # For sending alert
import pygame  # For playing sound
pygame.init()

client = Client("ur7vskev12zazdf6twu9dt5a4wy7pf", api_token="aqdqexpqcpagiazt1a386xjnp4mgw4")


while True:
    text = input("Debug Command:")
    if text == "bathroom":
        print("Bathroom!")
        my_sound = pygame.mixer.Sound('sound/bathroom.mp3')
        my_sound.play()
        client.send_message("Bathroom!", title="Dog Pushbuttons")
    if text == "outside":
        print("Outside!")
        my_sound = pygame.mixer.Sound('sound/outside.mp3')
        my_sound.play()
        client.send_message("Outside!", title="Dog Pushbuttons")
    if text == "water":
        print("Water!")
        my_sound = pygame.mixer.Sound('sound/water.mp3')
        my_sound.play()
        client.send_message("Water!", title="Dog Pushbuttons")
    if text == "food":
        print("Food!")
        my_sound = pygame.mixer.Sound('sound/food.mp3')
        my_sound.play()
        client.send_message("Food!", title="Dog Pushbuttons")
    if text == "testsound":
        print("Testing sound...")
        my_sound = pygame.mixer.Sound('sound/test.mp3')
        my_sound.play()
    if text == "testalert":
        print("Testing alert...")
        client.send_message("Testing alert from debug command", title="Dog Pushbuttons")
    if text == "help":
        print("Commands: quit, testsound, testalert, bathroom outside, water, food")
    if text == "quit":
        break
