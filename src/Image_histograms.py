# Importing packages
import os
import sys
sys.path.append(os.path.join(".."))
import cv2
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import argparse

# get target image and normalize
def target_image(image):
    filepath = os.path.join("..","in","flowers", image+".jpg")
    focus_image = cv2.imread(filepath)
    focus_image = cv2.cvtColor(focus_image, cv2.COLOR_BGR2RGB)
    focus_image_hist = cv2.calcHist([focus_image], [0,1,2], None, [8,8,8], [0,256, 0,256, 0,256])
    focus_image_norm = cv2.normalize(focus_image_hist, focus_image_hist, 0,255, cv2.NORM_MINMAX)
    
    return focus_image_norm, focus_image, filepath

# create list of images and their histogram compared to focus_image
def all_images(focus_image_norm, filepath):
    
    images = []
    
    for index, filename in enumerate(os.listdir(os.path.join("..","in","flowers"))):
        image_data = []
        img = cv2.imread(os.path.join("..","in", "flowers", filename))
        if not filename.endswith(".jpg"):
            pass
        else:
            if img is not None and os.path.join("..","in","flowers", filename) != filepath:
                img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                img_hist = cv2.calcHist([img], [0,1,2], None, [8,8,8], [0,256, 0,256, 0,256])
                img_norm = cv2.normalize(img_hist, img_hist, 0, 255, cv2.NORM_MINMAX)
                img_score = cv2.compareHist(focus_image_norm, img_norm, cv2.HISTCMP_CHISQR)
                image_data = [filename, img, img_score]
                images.insert(index, image_data)
            else:
                pass
    
    return images

# Sort images by score and print top 3
def image_sort(images):
    images = sorted(images, key=lambda x:x[2])
    
    print(f"The closest image is {images[0][0]}")
    print(f"The second closest image is {images[1][0]}")
    print(f"The third closest image is {images[2][0]}")

    return images

# Save as a .csv
def csv_dataframe(filepath, images, csv):
    image_df = list(zip([filepath], images[0], images[1], images[2]))
    
    df = pd.DataFrame(image_df, columns = ["Target image", "Closest image nr. 1","Closest image nr. 2","Closest image nr. 3"])
    
    outpath = os.path.join("..","out", csv+".csv")
    
    df.to_csv(outpath, index = False)
    
# saving plot of images
def save_plots(focus_image, images, plot):
    outpath = os.path.join("..","out", plot+".jpg")

    plt.figure(figsize=(18,12))

    plt.subplot(1,4,1)
    plt.imshow(focus_image)
    plt.title("Target image")
    plt.tight_layout()
    plt.axis('off')

    for ranking in range(0,3):
        plt.subplot(1,4,ranking+2)
        plt.imshow(images[ranking][1])
        plt.title(f"Closest image nr. {ranking+1}\n{images[ranking][0]}\nscore:{images[ranking][2]}")
        plt.tight_layout()
        plt.axis('off')

    plt.savefig(outpath)

    plt.show()

# args_parse
def parse_args():
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--image", required = True, help="The target image filename. Don't include '.jpg'")
    ap.add_argument("-c", "--csv", required = True, help="The name of the .csv file- Don't include '.csv'")
    ap.add_argument("-p", "--plot", required = True, help="The name of the image plot file.")
    args = vars(ap.parse_args())
    return args
    
# Defining main
def main():
    args = parse_args()
    focus_image_norm, focus_image, filepath = target_image(args["image"])
    images = all_images(focus_image_norm, filepath)
    images = image_sort(images)
    csv_dataframe(filepath, images, args["csv"])
    save_plots(focus_image, images, args["plot"])
                                     
# Running main
if __name__ == "__main__":
    main()
