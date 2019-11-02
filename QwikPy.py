def PygameWindow(width, height, WindowCaption):
    import pygame

    pygame.init()
    pygame.display.set_caption(WindowCaption)


    #make the pygame window
    pygame.display.set_mode((width, height ) )

    running = True

    while (running):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False