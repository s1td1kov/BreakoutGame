import pygame

from game_object import GameObject
from text_object import TextObject
import config as c



class Button(GameObject):
    def __init__(self, x, y, w, h, text, on_click=lambda x: None, padding=0):
        super().__init__(x, y, w, h)
        self.state = 'normal'
        self.on_click = on_click
        self.text = TextObject(x + padding, y + padding, lambda: text, c.button_text_color, c.font_name, c.menu_font_size)
        

    @property
    
    def back_color(self):
    
        return dict(normal=c.button_normal_back_color,
    
                    hover=c.button_hover_back_color,
    
                    pressed=c.button_pressed_back_color)[self.state]



    def draw(self, surface):
        
        
        pygame.draw.rect(surface, self.back_color, self.bounds)
        
        
        self.text.draw(surface)
        
    
    
    def handle_mouse_event(self, type, pos):
        
    
        if type == pygame.MOUSEMOTION:
            self.handle_mouse_move(pos)
            
            
        elif type == pygame.MOUSEBUTTONDOWN:
            self.handle_mouse_down(pos)
            
         
        elif type == pygame.MOUSEBUTTONUP:
            self.handle_mouse_up(pos)
            


    def handle_mouse_move(self, pos):
        
        
        if self.bounds.collidepoint(pos):
            
            
            if self.state != 'pressed':
                self.state = 'hover'
        else:
            self.state = 'normal'
            


    def handle_mouse_down(self, pos):
        
        
        if self.bounds.collidepoint(pos):
            self.state = 'pressed'
            

    def handle_mouse_up(self, pos):
        
        
        if self.state == 'pressed':
            self.on_click(self)
            self.state = 'hover'
