#coding=utf8

import pygame
import sys
import config as c
from button import Button

from collections import defaultdict

pause = True

class Game:
    
    def __init__(self, caption, width, height, back_image_filename, frame_rate):
        # фоновое изображение
        self.background_image = pygame.image.load(back_image_filename)
        
        # фоновое изображение
        self.frame_rate = frame_rate
        
        # игра окончена
        self.game_over = False
        
        # объекты
        self.objects = []
        
        # настройка параметров звука
        pygame.mixer.pre_init(44100, 16, 2, 4096)
        
        # инициализация звука
        pygame.init()
        
        # выбор звуковой дорожки
        pygame.mixer.music.load('sound_effects/music2.mp3')
        pygame.mixer.music.play(-1)
        
        # инициализация звука
        pygame.font.init()
        
        # инициализация окна
        self.surface = pygame.display.set_mode((width, height))
        
        # название окна
        pygame.display.set_caption(caption)
        
        # инициализация времени
        self.clock = pygame.time.Clock()
        
        self.keydown_handlers = defaultdict(list)
        
        self.keyup_handlers = defaultdict(list)
        
        self.mouse_handlers = []
        
    def update(self):
        for o in self.objects:
            o.update()

    def draw(self):
        for o in self.objects:
            o.draw(self.surface)
            
    # пауза
    def create_pause(self):
        # запуск игры
        def on_play(button):
            for b in self.menu_buttons:
                self.objects.remove(b)

            self.is_game_running = True
            #self.start_level = True
        # выход из игры
        def on_quit(button):
            self.game_over = True
            self.is_game_running = False
            self.game_over = True
        
        while pause:
            for i, (text, click_handler) in enumerate((('PLAY', on_play), ('QUIT', on_quit))):
                b = Button(c.menu_offset_x,
                           c.menu_offset_y + (c.menu_button_h + 5) * i,
                           c.menu_button_w,
                           c.menu_button_h,
                           text,
                           click_handler,
                           padding=5)   
                self.objects.append(b)
                self.menu_buttons.append(b)
                self.mouse_handlers.append(b.handle_mouse_event)
        
            
    # поведение во время паузы
    def paused(self):
    
        largeText = pygame.font.SysFont("comicsansms",115)
        #TextSurf, TextRect = text_objects("Paused", largeText)
        #TextRect.center = ((c.screen_width/2),(c.screen_height/2))
        #gameDisplay.blit(TextSurf, TextRect)
        
    
        while pause:
            for event in pygame.event.get():
    
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                    
            #gameDisplay.fill(white)
            
    
            #button("Continue",150,450,100,50,green,bright_green,unpause)
            #button("Quit",550,450,100,50,red,bright_red,quitgame)
    
            pygame.display.update()
            #clock.tick(15)      

    # обработка событий
    def handle_events(self):
        for event in pygame.event.get():
            
            # выход
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            # нажатие клавиш
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    pause = True
                    self.create_pause()
                for handler in self.keydown_handlers[event.key]:
                    handler(event.key)
            
            # отпускание клавиш
            elif event.type == pygame.KEYUP:
                for handler in self.keydown_handlers[event.key]:
                    handler(event.key)
            
            # действия с мышью
            elif event.type in (pygame.MOUSEBUTTONDOWN, pygame.MOUSEBUTTONUP, pygame.MOUSEMOTION):
                for handler in self.mouse_handlers:
                    handler(event.type, event.pos)
    
    # запуск игры
    def run(self):
        while not self.game_over:
            self.surface.blit(self.background_image, (0, 0))

            self.handle_events()
            self.update()
            self.draw()

            pygame.display.update()
            self.clock.tick(self.frame_rate)
            
    
    # окончание игры
    def crash():
        
        
        largeText = pygame.font.SysFont("comicsansms",115)
        TextSurf, TextRect = text_objects("You Crashed", largeText)
        TextRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf, TextRect)
        
    
        while True:
            for event in pygame.event.get():
                #print(event)
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                    
            #gameDisplay.fill(white)
            
    
            button("Play Again",150,450,100,50,green,bright_green,game_loop)
            button("Quit",550,450,100,50,red,bright_red,quitgame)
    
            pygame.display.update()
            clock.tick(15) 
