import pygame

class Button(pygame.sprite.Sprite):
   def __init__(self, size, position, color=(100, 100, 100), text=''):
       super().__init__()
       self.color = color
       self.hover_color = (0, 255, 0)
       self.rect = pygame.Rect(size, position)
       self.text = text
   def update(self, screen):
       pygame.draw.rect(screen, self.color, self.rect)
       screen.blit(pygame.font.Font('freesansbold.ttf', 18).render(self.text, True, (0, 0, 0)), (self.rect.x + 2, self.rect.y + 2))
       if self.rect.collidepoint(pygame.mouse.get_pos()):
           pygame.draw.rect(screen, (64, 224, 208), self.rect)
           screen.blit(pygame.font.Font('freesansbold.ttf', 18).render(self.text, True, (0, 0, 0)), (self.rect.x + 2, self.rect.y + 2))
           return True
       return False