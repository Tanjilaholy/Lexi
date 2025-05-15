from playsound import playsound

import eel

# Playing assistant sound function

@eel.expose
def playAssistantSound():
    music_dir ="Fronted\\assets\\vendore\\texllate\\audio\\www_assets_audio_start_sound.mp3"
    playsound(music_dir)