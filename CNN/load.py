import os
import cv2
from PIL import Image
import numpy as np

data=[]
labels=[]

# ----------------
# LABELS
# Cat 0
# Dog 1
# Monkey 2
# Parrot 3
# Elephant 4
# Bear 5
# ----------------

# Cat 0
cats = os.listdir(os.getcwd() + "/CNN/data/cat")
for cat in cats:
    imag=cv2.imread(os.getcwd() + "/CNN/data/cat/" + cat)
    img_from_ar = Image.fromarray(imag, 'RGB')
    resized_image = img_from_ar.resize((50, 50))
    data.append(np.array(resized_image))
    labels.append(0)

# Dog 1
dogs = os.listdir(os.getcwd() + "/CNN/data/dog/")
for dog in dogs:
    imag=cv2.imread(os.getcwd() + "/CNN/data/dog/" + dog)
    img_from_ar = Image.fromarray(imag, 'RGB')
    resized_image = img_from_ar.resize((50, 50))
    data.append(np.array(resized_image))
    labels.append(1)

# Monkey 2
monkeys = os.listdir(os.getcwd() + "/CNN/data/monkey/")
for monkey in monkeys:
    imag=cv2.imread(os.getcwd() + "/CNN/data/monkey/" + monkey)
    img_from_ar = Image.fromarray(imag, 'RGB')
    resized_image = img_from_ar.resize((50, 50))
    data.append(np.array(resized_image))
    labels.append(2)

# Parrot 3
parrots = os.listdir(os.getcwd() + "/CNN/data/parrot/")
for parrot in parrots:
    imag=cv2.imread(os.getcwd() + "/CNN/data/parrot/" + parrot)
    img_from_ar = Image.fromarray(imag, 'RGB')
    resized_image = img_from_ar.resize((50, 50))
    data.append(np.array(resized_image))
    labels.append(3)

# Elephant 4
elephants = os.listdir(os.getcwd() + "/CNN/data/elephant/")
for elephant in elephants:
    imag=cv2.imread(os.getcwd() + "/CNN/data/elephant/" + elephant)
    img_from_ar = Image.fromarray(imag, 'RGB')
    resized_image = img_from_ar.resize((50, 50))
    data.append(np.array(resized_image))
    labels.append(4)

# Bear 5
bears = os.listdir(os.getcwd() + "/CNN/data/bear/")
for bear in bears:
    imag=cv2.imread(os.getcwd() + "/CNN/data/bear/" + bear)
    img_from_ar = Image.fromarray(imag, 'RGB')
    resized_image = img_from_ar.resize((50, 50))
    data.append(np.array(resized_image))
    labels.append(5)

animals=np.array(data)
labels=np.array(labels)

np.save("animals",animals)
np.save("labels",labels)
