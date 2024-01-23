WIDTH = 1600 # Δ
HEIGHT = 900 # Δ
FULLSCREEN = False # Δ

SFX_VOLUME = 1.0 # Δ
MUSIC_VOLUME = 1.0 # Δ i don't think we'll need this

FPS = 60 # Δ set to None for uncapped FPS - use at your own risk!


JOYSTICK_THRESHOLD = 0.5 # Δ maybe?

BULLET_HELL_BOTTOM_RIGHT = True # Δ give it a shot :)

CB_COLOR_OVERRIDE = 0 # Δ 
# 0: no colorblindness
# 1: protanopia
# 2: deuteranopia
# 3: tritanopia

CONSTANT_SEED = False

# -----
# everything above this line is just a placeholder
# the real settings are found in settings.json

import os
base = os.path.dirname(os.path.abspath(__file__))
import json
with open(os.path.join(base, "settings.json")) as f:
    SETTINGS_JSON = json.load(f)

def reload_vars():
    for key, value in SETTINGS_JSON.items():
        exec(f"global {key}\n{key} = {value}")

def save_vars():
    with open(os.path.join(base, "settings.json"), "w") as f:
        json.dump(SETTINGS_JSON, f)

reload_vars()

if FPS and not(20 <= FPS):
    raise ValueError("The minimum FPS cap must be set to at least 20")
