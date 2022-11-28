from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import datetime, os
from PIL.ExifTags import TAGS

def processImageLandscape(image, metadata,fname):
    time = datetime.datetime.strptime(metadata[306],"%Y:%m:%d %H:%M:%S").strftime("%H:%M %d %b, %Y")
    iD = ImageDraw.Draw(image)
    width,height = metadata[256],metadata[257]
    iD.text(
        (width - int((width*17)/100),height - int((height*5)/100)),
        text=time,fill=(255,255,255),
        font=ImageFont.truetype('arial.ttf',size=int((width*2/100 + height*2/100)/2))
    )
    image.save(fname,"JPEG")

def processImagePortrait(image, metadata,fname):
    
    time = datetime.datetime.strptime(metadata[306],"%Y:%m:%d %H:%M:%S").strftime("%H:%M %d %b, %Y")
    iD = ImageDraw.Draw(image)
    width,height = metadata[256],metadata[257]
    iD.text(
        (width - int((width*17)/100),height - int((height*5)/100)),
        text=time,fill=(255,255,255),
        font=ImageFont.truetype('arial.ttf',size=int((width*2/100 + height*2/100)/2))
    )
    image.save(fname,"JPEG")


# print("Enter Path of Folder: ")
# ip = input()


# Protrail = 6 Land = 1

def placeTimeStamp(inputFolder,outputFolder) -> tuple:
    all_photos = os.listdir(inputFolder)
    outputFolder += "\\"
    err = 0
    for i in all_photos:
        print(i)
        img = Image.open(inputFolder + "\\" + i)
        meta = img.getexif()
        ori = meta.get(274)

        if ori == 1:
            processImageLandscape(img, meta,outputFolder + i)
        elif ori == 6:
            processImagePortrait(img, meta, outputFolder + i)
        else:
            print("ERROR: orientation missmatch -> " + str(ori))
            err += 1

    return (len(all_photos),err)

        
    # print()



# print("Done!")