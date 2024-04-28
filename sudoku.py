import pygame, sys
# from board import *
# from constant import *


beige = (209, 170, 86)
background_color = (255,255,255)
width = 600
height = 600


def start_screen(screen):
    pygame.init()

    screen.fill(background_color)

    title_font = pygame.font.SysFont("AovelSansRounded-rdDL.ttf", 100)
    buttons_font = pygame.font.SysFont("AovelSansRounded-rdDL.ttf", 75)

    opening_screen = title_font.render("Sudoku Game", 0, (200, 230, 230))
    title_box = opening_screen.get_rect(center=(width//2 + 38, height//2 - 150))
    screen.blit(opening_screen, title_box)

    easy_button, medium_button, hard_button = buttons_font.render("EASY", 0, (255, 255, 255)), buttons_font.render("MEDIUM", 0, (255, 255, 255)), buttons_font.render("HARD", 0, (255, 255, 255))
    easy_button_placement = pygame.Surface((easy_button.get_size()[0] + 20, easy_button.get_size()[1] + 20))
    easy_button_placement.fill(beige)
    easy_button_placement.blit(easy_button, (10, 10))
    easy_button_rectangle = easy_button_placement.get_rect(center=(width - 460, height//2 + 150))
    screen.blit(easy_button_placement, easy_button_rectangle)
    
    medium_button_placement = pygame.Surface((medium_button.get_size()[0] + 20, medium_button.get_size()[1] + 20))
    medium_button_placement.fill(beige)
    medium_button_placement.blit(medium_button, (10, 10))
    medium_button_rectangle = medium_button_placement.get_rect(center=(width - 280, height // 2 + 250))
    screen.blit(medium_button_placement, medium_button_rectangle)

    hard_button_placement = pygame.Surface((hard_button.get_size()[0] + 20, hard_button.get_size()[1] + 20))
    hard_button_placement.fill(beige)
    hard_button_placement.blit(hard_button, (10, 10))
    hard_button_rectangle = hard_button_placement.get_rect(center=(width - 100, height // 2 + 350))
    screen.blit(hard_button_placement, hard_button_rectangle)

   

    pygame.display.update()
    
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if easy_button_rectangle.collidepoint(event.pos):
                    return "Easy"
                if medium_button_rectangle.collidepoint(event.pos):
                    return "Medium"
                if hard_button_rectangle.collidepoint(event.pos):
                    return "Hard"
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            pygame.display.update()

def sudo_buttons(screen):
    reset_button_font = pygame.font.SysFont("AovelSansRounded-rdDL.ttf", 20)
    restart_button_font = pygame.font.SysFont("AovelSansRounded-rdDL.ttf", 20)
    exit_button_font = pygame.font.SysFont("AovelSansRounded-rdDL.ttf", 20)

    reset_button = reset_button_font.render("RESET", 0, (255, 255, 255))
    restart_button = restart_button_font.render("RESTART", 0, (255, 255, 255))
    exit_button = exit_button_font.render("EXIT", 0, (255, 255, 255))

    reset_button_position = pygame.Surface((reset_button.get_size()[0] + 20, reset_button.get_size()[1] + 20))
    reset_button_position.fill(beige)
    reset_button_position.blit(reset_button, (10, 10))
    reset_button_rectangle = reset_button_position.get_rect(center=(width - 250, height + 115))
    screen.blit(reset_button_position, reset_button_rectangle)

    restart_button_position = pygame.Surface((restart_button.get_size()[0] + 20, restart_button.get_size()[1] + 20))
    restart_button_position.fill(beige)
    restart_button_position.blit(restart_button, (10, 10))
    restart_button_rectangle = restart_button_position.get_rect(center=(width - 425, height + 115))
    screen.blit(restart_button_position, restart_button_rectangle)

    exit_button_position = pygame.Surface((exit_button.get_size()[0] + 20, exit_button.get_size()[1] + 20))
    exit_button_position.fill(beige)
    exit_button_position.blit(exit_button, (10, 10))
    exit_button_rectangle = exit_button_position.get_rect(center=(width - 100, height + 115))
    screen.blit(exit_button_position, exit_button_rectangle)

    pygame.display.update()

    return restart_button_rectangle, reset_button_rectangle, exit_button_rectangle

def winner_screen(screen):
    pygame.init()

    screen.fill(beige)

    winner_font = pygame.font.SysFont("AovelSansRounded-rdDL.ttf", 100)
    button_font = pygame.font.SysFont("AovelSansRounded-rdDL.ttf", 50)

    win_surf = winner_font.render("You Win!", True, beige)
    win_rect = win_surf.get_rect(center=(width//2 + 38, height//2 - 150))
    screen.blt(win_surf, win_rect)

    exit_text = button_font.render("EXIT", True, (255, 255, 255))
    exit_surf = pygame.Surface((exit_text.get_size()[0] + 20, exit_text.get_size()[1] + 20))
    exit_surf.fill(beige)
    exit_surf.blit(exit_text, (10, 10))
    exit_rect = exit_surf.get_rect(center=(width - 280, height // 2 + 250))
    screen.blit(exit_surf, exit_rect)

    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if exit_rect.collidepoint(event.pos):
                    return

        pygame.display.update()


def loser_screen(screen):
    screen.fill(beige)
    loser_font = pygame.font.SysFont("AovelSansRounded-rdDL.ttf", 100)
    button_font = pygame.font.SysFont("AovelSansRounded-rdDL.ttf", 50)

    lose_surf = loser_font.render("GAME OVER", True, (255, 0, 0))
    lose_rect = lose_surf.get_rect(center=(width//2 + 38, height//2 - 150))
    screen.blit(lose_rect, lose_rect)

    restart_text = button_font.render("RESENT", True, (255, 255, 255))
    restart_surf = pygame.Surface((restart_text.get_size()[0] + 20, restart_text.get_size()[1] + 20))
    restart_surf.fill(beige)
    restart_surf.blit(restart_text, (10, 10))
    restart_rect = restart_surf.get_rect(center=(width - 280, height // 2 + 250))
    screen.blit(restart_surf, restart_rect)
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if restart_rect.collidepoint(event.pos):
                    return

def main():
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Sudoku Game")

    difficulty = start_screen(screen)


