#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# MIT License
#
# Copyright (c) 2019 Iván de Paz Centeno
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import cv2
from mtcnn import MTCNN
import glob

file = open("landmarks_realface96.txt", "w")

detector = MTCNN()


for filename in glob.glob('real_faces96/*.jpg'): #assuming jpg
    print (filename)

    image = cv2.cvtColor(cv2.imread(filename), cv2.COLOR_BGR2RGB)
    result = detector.detect_faces(image)

    # Result is an array with all the bounding boxes detected. We know that for 'ivan.jpg' there is only one.
    if not result:
        print("no result detected")
        continue
    bounding_box = result[0]['box']
    keypoints = result[0]['keypoints']

    file.write (filename)
    file.write(" " + str(keypoints['left_eye'][0]) +" "+ str(keypoints['left_eye'][1]))
    file.write(" " + str(keypoints['right_eye'][0]) +" "+ str(keypoints['right_eye'][1]))
    file.write(" " + str(keypoints['nose'][0]) +" "+ str(keypoints['nose'][1]))
    file.write(" " + str(keypoints['mouth_left'][0]) +" "+ str(keypoints['mouth_left'][1]))
    file.write(" " + str(keypoints['mouth_right'][0]) +" "+ str(keypoints['mouth_right'][1]))
    file.write("\n")



file.close()
