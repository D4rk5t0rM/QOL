import pyttsx3

e = pyttsx3.init()

filename = "./transcript.speak"
f = open(filename,'r')

content  = f.read()

#lower speed a little
#e.setProperty('rate',e.getProperty('rate')-10)

# #voice:
# voices = e.getProperty('voices') 
# e.setProperty('voice', voices[1].id)

#say/save-to-file

# e.say(content)#use for debug so it doen't have to save
e.save_to_file(content, filename[:-6]+'.tts.mp3')


e.runAndWait()