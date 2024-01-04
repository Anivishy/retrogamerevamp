DEFAULT_BLUE = (33, 33, 222)

FOREST = (30, 220, 50)
ICE = (75, 150, 230)
LAVA = (240, 30, 40)
SHADOW = (120, 50, 120)

GREY = (190, 190, 190)


from user_settings import CB_COLOR_OVERRIDE
if CB_COLOR_OVERRIDE == 1:
    FOREST = (220, 108, 30)
    ICE = (75, 175, 230)
    LAVA = (221, 240, 30)
    SHADOW = (159, 70, 202)
elif CB_COLOR_OVERRIDE == 2:
    FOREST = (255, 72, 72)
    ICE = (75, 22, 230)
    LAVA = (190, 208, 13)
    SHADOW = (159, 70, 202)
elif CB_COLOR_OVERRIDE == 3:
    FOREST = (75, 230, 203)
    ICE = (0, 145, 255)
    LAVA = (208, 167, 13)
    SHADOW = (173, 106, 255)