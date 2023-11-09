
from gtts import gTTS

import os

mytext = 'ye vedya rushya bat ka grip nikal  ke bat sidhi tere gand me dhalunga'


language = 'en'


myobj = gTTS(text=mytext, lang=language, slow=False)


myobj.save("welcome.mp3")



