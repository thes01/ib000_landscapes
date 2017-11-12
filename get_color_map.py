from PIL import Image, ImageColor

with open('hues.txt', 'w') as hues:
    for hue in range(200):
        hues.write(str(ImageColor.getrgb('hsl({},90%,50%)'.format(int(hue))))+",")