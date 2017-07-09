import spritesheet
from random import randint
import time
myStruct = {'Jill': (51, 102, 153), 'Alma': (255, 153, 0)}


def print_display(window, pygame, json_obj, bg, ui, myfont, numchar, previousSprite=None):
    # Avoiding useless JSON repetition and making it clean
    if 'sprite' in json_obj:
        current_sprite = json_obj['sprite']
    else:
        current_sprite = previousSprite

    # Refilling to empty current space
    #window.fill(pygame.Color("white"))

    # Then comes the character
    character = pygame.image.load("media/characters/" + current_sprite + ".png")
    window.blit(bg, (10, 16))
    window.blit(character, (105, 57))
    window.blit(ui, (0, 0))

    name = json_obj['name']
    name_lb = myfont.render(name + ":", 1, myStruct[name])
    window.blit(name_lb, (40, 280))

    score = json_obj['text'][0:numchar]
    label = myfont.render(score, 1, (255, 255, 255))
    window.blit(label, (80, 280))
    # Refreshing the display with all the layers set
    # Making the character close his eyes randomly, because why not
    if randint(0, 30) == 5:
        closing_eyes(window, pygame, current_sprite)
    pygame.display.flip()
    return current_sprite


def closing_eyes(window, pygame, sprite):
    ss = spritesheet.spritesheet("media/characters/""e_"+sprite+".png")
    # Sprite is 16x16 pixels at location 0,0 in the file...
    images = [ss.image_at((0, 0, 61, 28)), ss.image_at((61, 0, 61, 28))]
    # Load two images into an array, their transparent bit is (255, 255, 255)
    i = 0
    while i < len(images):
        window.blit(images[i], (145, 130))
        pygame.display.flip()
        time.sleep(.0500)
        i += 1


def mouth_movement(window, pygame, sprite, i):
    ss = spritesheet.spritesheet("media/characters/""m_" + sprite + ".png")
    # Sprite is 16x16 pixels at location 0,0 in the file...
    images = [ss.image_at((0, 0, 42, 15)),
              ss.image_at((42, 0, 42, 15)),
              ss.image_at((84, 0, 42, 15)),
              ss.image_at((126, 0, 42, 15))]
    # Load two images into an array, their transparent bit is (255, 255, 255)
    window.blit(images[i], (152, 170))
    pygame.display.flip()
    i += 1
    if i >= 3:
        return 0
    else:
        return i
