import json
import time
import requests
import random
import pygame
import sys
import math

FOOD = []

GENERAL_ID = int(random.uniform(1000, 9999))

fruitsCount = 0
#C:\Users\Bogdan\Desktop\client.py
sizeController = 1
pygame.init()
x, y = 500, 500
screen = pygame.display.set_mode((x, y))
pygame.display.set_caption("Snake")

URL = "http://127.0.0.1:12345"

X_POS, Y_POS = 0, 0

def FoodGenerate(count):
	global fruitsCount
	fruitsCount = count
	for el in range(0, count):
		FOOD.append([int(random.uniform(10, 490)), int(random.uniform(10, 490))])

def FoodRender():
	if len(FOOD) > 0:
		for el in FOOD:
			pygame.draw.rect(screen, (0, 0, 0), (el[0], el[1], 5, 5), 0)

def CreateText(text):
	global screen
	font = pygame.font.Font(None, 36)
	text = font.render(text, 1, (74, 74, 74))
	screen.blit(text, (320, 450))

def GAME_UPDATE():
	Cr, Cg, Cb = 0, 0, 0

	Xp, Yp = 30, 30
	Sx, Sy = 10, 10

	def FoodRender():
		if len(FOOD) > 0:
			for el in FOOD:
				pygame.draw.rect(screen, (0, 143, 12), (el[0], el[1], 5, 5), 0)

	FoodGenerate(20)
	print (FOOD)

	while True:
		global sizeController, fruitsCount
		screen.fill((222, 222, 222))
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					Xp -= 10
				elif event.key == pygame.K_RIGHT:
					Xp += 10
				elif event.key == pygame.K_UP:
					Yp -= 10
				elif event.key == pygame.K_DOWN:
					Yp += 10
				elif event.key == pygame.K_r:
					Sx += 3
					Sy += 3

		FoodRender()

		if len(FOOD) > 0:
			for el in range(0, len(FOOD)):
				if math.dist(FOOD[el], [Xp, Yp]) < Sx:
					print(FOOD)
					FOOD.pop(el)
					print(FOOD)
					fruitsCount -= 1
					sizeController += 5
					Sx += 5
					Sy += 5
					break

		if fruitsCount <= 0:
			FoodGenerate(20)

		params = {"ID": GENERAL_ID, "X": Xp, "Y": Yp, "SX": Sx, "SY": Sy}
		data = requests.get(URL, params).json()["call"]
		for el in data:
			pygame.draw.rect(screen, (0, 0, 0), (int(el.split("=")[2].split("&")[0]), int(el.split("=")[3].split("&")[0]), int(el.split("=")[4].split("&")[0]), int(el.split("=")[5])), 0)
		print(data)
		#C:\Users\Bogdan\Desktop\client.py
		CreateText(f"SIZE: {sizeController}")
		pygame.display.update()
		pygame.time.delay(200)

GAME_UPDATE()