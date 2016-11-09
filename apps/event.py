from pygame.constants import QUIT

def event_handler(main_event):
    for event in main_event:
        if event.type == QUIT:
            return 'QUIT';