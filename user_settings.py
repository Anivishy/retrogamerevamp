WIDTH = 1600 # Δ
HEIGHT = 900 # Δ
FULLSCREEN = False # Δ

SFX_VOLUME = 1.0 # Δ
MUSIC_VOLUME = 1.0 # Δ i don't think we'll need this

FPS = 60 # Δ set to None for uncapped FPS - use at your own risk!

if FPS and not(20 <= FPS):
    raise ValueError("The minimum FPS cap must be set to at least 20")

JOYSTICK_THRESHOLD = 0.5 # Δ maybe?

BULLET_HELL_BOTTOM_RIGHT = True # Δ give it a shot :)

CB_COLOR_OVERRIDE = 0 # Δ 
# 0: no colorblindness
# 1: protanopia
# 2: deuteranopia
# 3: tritanopia