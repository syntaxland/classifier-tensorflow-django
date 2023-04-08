# Image Classifier Model | TensorFlow

## Classes | LABELS
Cat 0
Dog 1
Monkey 2
Parrot 3
Elephant 4
Bear 5

## Prepare Dataset
Building an Image classifier that can predict if the inputed 
image is a Cat, Dog, Monkey, Parrot, Elephant or Bear.
<!-- # Load the data -->
py CNN/load.py

## Train the model
Separating the dataset into train_set (90%) and 
test_set (10%) for training and validation respectively.
<!-- ### Run train.py -->
py CNN/train.py

# Predict usinga sample
py CNN/predict.py

## Setup Django API
django-admin startproject api .
python manage.py runserver
