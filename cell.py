import pygame

pygame.font.init()

class Cell:
    def __init__(self, value, row, col, cell_size, screen):
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen
        self.cell_size = cell_size
        self.selected = False
        self.can_edit = False
        self.font = pygame.font.SysFont(None, 40)
        self.x = col * self.cell_size
        self.y = row * self.cell_size
        self.sketched = 0

    def set_cell_value(self, value):
        self.value = value

    def set_sketched(self, value):
        self.sketched = value

    def draw(self):
        cell_color = (255, 255, 255)
        pygame.draw.rect(self.screen, cell_color, (self.x, self.y, self.cell_size, self.cell_size))

        if self.selected:
            border_color = (255, 0, 0)
            border_thickness = 3
            pygame.draw.rect(self.screen, border_color, (self.x, self.y, self.cell_size, self.cell_size), border_thickness)

        if self.sketched != 0:
            sketch_color = (128, 128, 128)
            sketch_text = str(self.sketched)
            text_surface = self.font.render(sketch_text, True, sketch_color)
            text_rect = text_surface.get_rect(center=(self.x + self.cell_size // 2, self.y + self.cell_size // 2))
            self.screen.blit(text_surface, text_rect)

        if self.value != 0:
            value_color = (0, 0, 0)
            value_text = str(self.value)
            text_surface = self.font.render(value_text, True, value_color)
            text_rect = text_surface.get_rect(center=(self.x + self.cell_size // 2, self.y + self.cell_size // 2))
            self.screen.blit(text_surface, text_rect)

        pygame.display.update()

