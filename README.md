# Visual_analytics_Assignment_1
This repository contains a script that takes a user-defined image and findes the three closest images based on difference in histograms.

The model will:
- print the names of the three cloest images in the console.
- create a .csv with the image names of the three cloest images
- A .jpg plot of the target image and the three cloest images + their hist scores.

## ------ DATA ------
The data is a large collection of flower images provided through the course.

## ------ REPO STRUCTURE ------
"src" FOLDER:
- This folder contains the .py script to find the closest image based on histogram and create plot + .csv

"in" FOLDER:
- This is where the data used in the scripts should be placed. Ie. where the flowers should be placed in a folder called "flowers".

"out" FOLDER:
- This is where the .csv and image plot will be saved

"utils" FOLDER:
- This folder should include all utility scrips used by the main script.

## ------ SCRIPT ------
- The model_creation.py script requires you to give the arguments "-i" / "--image" (the name of the user-defined image. Don't include .jpg)

- The poster_prediction.py script requires you to give the argument "-c" / "--csv" (the name of the csv created by the script. Don't include .csv)

- The poster_prediction.py script requires you to give the argument "-p" / "--plot" (the name of the image plot file created by the script)
