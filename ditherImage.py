from PIL import Image, ImageOps

def dither(image, amountOfColors):
    amountOfColors -= 1
    image = ImageOps.grayscale(image)
    pixelList = list(image.getdata())
    x = image.size[0]
    y = image.size[1]
    ylimit = y*x-x
    xylimit = len(pixelList)-1

    for i, value in enumerate(pixelList):
        newValue = round(value/(255/amountOfColors))*(255/amountOfColors)
        quantError = value - newValue
        pixelList[i] = newValue
        if i < x:
            pixelList[i-x] += quantError*5/16
        if i < ylimit:
            pixelList[i+x] += quantError*3/16
        if i != 0:
            pixelList[i-1] += quantError*1/16
        if i != xylimit:
            pixelList[i+1] += quantError*7/16

    for i, value in enumerate(pixelList):
        pixelList[i] = round(value/(255/amountOfColors))*(255/amountOfColors)

    newImage = Image.new('L', (x, y))
    newImage.putdata(pixelList)
    return newImage

dither(Image.open(input('Image name here: ')), int(input('Amount of shades of gray: '))).show()

        