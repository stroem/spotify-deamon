import pygame.mixer as mixer

mixer.init(44100)
mixer.music.load("test.mp3")
mixer.music.play()
mixer.music.get_busy()

print "Press enter to quit."
raw_input()
