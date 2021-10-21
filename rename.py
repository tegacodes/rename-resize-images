import os
from PIL import Image
import glob

def rename_image(_collection):
    print("Renaming images")
    for i, filename in enumerate(os.listdir(_collection)):
        i=str(i).zfill(5)
        os.rename(_collection + filename, _collection + str(i) + ".jpg")


def resize_image(file):
    print("Resizing images")
    thumbs="thumbs"

    print(thumbs)
    if not os.path.exists(thumbs):
        os.mkdir(thumbs)
    im = Image.open(file)
    print(im.size)
    im.thumbnail((400,400)) #set image size you want
    thumbpath = thumbs + "/" + os.path.basename(file)

    im.save(thumbpath, quality=50) #set image quality

if __name__ == "__main__":
    collection = "/Users/tegabrain/Documents/08-teaching/2021-DPN/images/imgs/"

    #rename images
    rename_image(collection)


    #resize images ending in 
    for image_file in glob.iglob(collection+'*.jpg'): 
        resize_image(image_file)