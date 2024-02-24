import math

def isLightOrDark(rgbColor):
    [r,g,b]=rgbColor
    hsp = math.sqrt(0.299 * (r * r) + 0.587 * (g * g) + 0.114 * (b * b))
    if hsp > 10 and hsp < 20:
        return 'mid'
    elif hsp > 20:
        return "light"
    else:
        return 'dark'