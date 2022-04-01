from pygame import mixer

file = '02 Galti Se Mistake - Jagga Jasoos (Arijit Singh) 190Kbps.mp3'
mixer.init()
mixer.music.load(file)
mixer.music.play()
