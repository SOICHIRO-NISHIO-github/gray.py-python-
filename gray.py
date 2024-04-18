import cv2
import sys
import os
import tqdm

if __name__ == "__main__":
    arg = sys.argv
    inputdir = arg[1]
    outputdir = "result"

    if not os.path.exists(outputdir):
        os.makedirs(outputdir)
    
    files = os.listdir(inputdir)

    #tqdmあり
    for file in tqdm.tqdm(files):
        img = cv2.imread(os.path.join(inputdir, file))
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        outputimg = "gray_" + str(file) 
        cv2.imwrite(os.path.join(outputdir, outputimg), img_gray)
    
    #tqdmなし
    """
    for file in files:
        img = cv2.imread(os.path.join(inputdir, file))
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        outputimg = "gray_" + str(file) 
        cv2.imwrite(os.path.join(outputdir, outputimg), img_gray)
    """