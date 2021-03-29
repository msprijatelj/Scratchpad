# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 15:58:34 2020

@author: Michael S. Prijatelj

Created to split Print & Play cards from a larger image into individual card
files. Splits all files in a input directory & outputs them to a target
directory.
"""


import os
import sys
from PIL import Image

def cardsplitter(inputDir, outputDir):
    fnames = os.listdir(inputDir)
    xPad = 100
    yPad = 150
    os.mkdir(outputDir)
    for fname in fnames:
        with Image.open(fname) as im:
            w, h = im.size
            cropIm = im.crop(box=(xPad, yPad, w-xPad, h-yPad))
            print(f"Filename {fname}")
            cropIm.save(outputDir + fname)




if __name__=="__main__":
    indir = sys.argv[1]
    outDir = sys.argv[2]
    cardsplitter(inDir, outDir)