from gtts import gTTS
import os
tts = gTTS(text='la mucca muggisce', lang='it')
tts.save('test.mp3')
os.system('afplay test.mp3')
