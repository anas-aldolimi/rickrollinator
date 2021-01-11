import pyautogui
import time
import os

song = open("songs.txt")
i = input("press enter to start")
if i == "":
	time.sleep(2)
	for line in song:
		pyautogui.typewrite(line)
		time.sleep(1)
