
def audio_handler(filename, pygame):
    pygame.mixer.music.load('media/music/'+filename)
    pygame.mixer.music.play()
