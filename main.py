import pygame
import sys


pygame.init()  ## used to initialize all the required module
screen = pygame.display.set_mode((1000, 600))   ## set the window desired size
bg = pygame.transform.scale(pygame.image.load("images\wakadinali\main.jpg"), [1000,700] )

# background = pygame.image.load('images/img.jpg')
pygame.display.set_caption("RONG RENDE")
icon = pygame.image.load('images/wakadinali/rongrende_logo.jpg')
pygame.display.set_icon(icon)

left_nav = pygame.Surface([300,600])

done = True  
  
while True:  
    for event in pygame.event.get():   ## empty the event queue 
        pygame.draw.rect(screen, (255, 100, 0), pygame.Rect(250, 255, 0, 10)) 
    #load the fonts  
    font = pygame.font.SysFont("Aldo the Apache", 35)  
    rongrende_font = pygame.font.SysFont("Blogger Sans", 50)  
    font_caption = pygame.font.SysFont("D-din", 20)  
    font2 = pygame.font.SysFont("D-din condensed bold", 20) 

    # Render the text in new surface  
    main_text = font.render("Wakadinali", True, (255,165,0))
    rong = rongrende_font.render("RONG RENDE", True, (255,255,255))
    notice = pygame.font.SysFont("Century Gothic", 20).render("Sign Up", True, (255, 255, 255))
    notice_2 = pygame.font.SysFont("Century Gothic", 20).render("Log In", True, (255, 255, 255))
    copyright = font2.render("(v1.0). Techstacity, 2023", True, (255, 255, 255))


    # screen.blit(background, (0,0))
    screen.blit(bg, (0,0))
    screen.blit(left_nav, (10,0))
    screen.blit(rong, (30,50))
    screen.blit(main_text,(70-main_text.get_width() //10, 120-main_text.get_height()))
    screen.blit(notice,(100-main_text.get_width() //10, 550-main_text.get_height()))
    screen.blit(notice_2,(300-main_text.get_width() //10, 550-main_text.get_height()))
    screen.blit(copyright,(50-copyright.get_width() //10, 550+copyright.get_height()))

    if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()

        

    

    pygame.display.flip() ## make all the changes avalible for screen