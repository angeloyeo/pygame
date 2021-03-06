# -*- coding: utf-8 -*-
"""
Created on Sat Aug 22 09:20:58 2020

@author: icbab

출처 https://www.youtube.com/watch?v=Dkx8Pl6QKW0
"""

import pygame


pygame.init() # 초기화 (반드시 필요)

# 화면 크기 설정
screen_width = 480 # 가로크기
screen_height = 640 # 세로크기

screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 title 설정

pygame.display.set_caption("Nado Game") # 게임 이름

# 배경이미지 불러오기
background = pygame.image.load("background.png")

# 이벤트 루프
running = True # 게임이 진행중인가?

while running:
    for event in pygame.event.get(): # 어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생하였는가?
            running = False # 게임이 진행중이 아님.
            
    screen.blit(background, (0, 0)) # 배경 그리기
    # screen.fill((100, 100, 255)) # 컬러로 백그라운드 채우기
    
    pygame.display.update() # 게임 화면을 다시 그리기 (p5.js의 draw 같은 느)
    
            
# pygame 종료 처리
pygame.quit()

