from playsound import playsound
import assets

# audio
assets.load_audio()
playsound(assets.get_audio("backgroundMusic"), False)