from PIL import Image
import numpy as np
import sys
import os
import csv


# default format can be changed as needed
def createFileList(myDir, format='.png'):
    fileList = []
    print(myDir)
    labels = []
    names = []
    keywords = {"duck": "1", "raccoon": "0", }  # keys and values to be changed as needed

    for root, dirs, files in os.walk(myDir, topdown=True):
        for name in files:
            if name.endswith(format):
                fullName = os.path.join(root, name)
                fileList.append(fullName)
            for keyword in keywords:
                if keyword in name:
                    labels.append(keywords[keyword])
                else:
                    continue
            names.append(name)
    return fileList, labels, names


# load the original image
myFileList, labels, names = createFileList('./content/')
i = 0
for file in myFileList:
    print(file)
    img_file = Image.open(file)
    # img_file.show()

    # get original image parameters...
    width, height = img_file.size
    format = img_file.format
    mode = img_file.mode

    # Make image Greyscale
    img_rgb = img_file.convert('RGB')
    img_rgb.save('result.png')
    # img_rgb.show()

    # Save Greyscale values
    value = np.asarray(img_rgb.getdata(), dtype=np.int_).reshape((width, height, 3))
    value = value.flatten()

    value = np.append(value, labels[i])
    i += 1

    print(value)
    with open("my_dataset.csv", 'a') as f:
        writer = csv.writer(f)
        writer.writerow(value)