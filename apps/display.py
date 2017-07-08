def print_display(window, pygame, json_obj, ui, myfont, numchar):
    # Refilling to empty current space
    window.fill(pygame.Color("white"))

    # Background first
    bg = pygame.image.load("media/background/" + json_obj['background'])
    window.blit(bg, (0, 0))

    # Then comes the character
    character = pygame.image.load("media/characters/" + json_obj['character'])
    window.blit(character, (400, 0))

    # The UI is the last fo be blitz
    window.blit(ui, (5, 420))

    score = json_obj['text'][0:numchar]
    label = myfont.render(score, 1, (0, 0, 0))
    window.blit(label, (100, 560))
    # Refreshing the display with all the layers set
    pygame.display.flip()
