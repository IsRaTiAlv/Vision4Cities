#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import print_function


import numpy as np
import cv2

count = 0

def draw_hsv(flow):
    (h, w) = flow.shape[:2]
    (fx, fy) = (flow[:, :, 0], flow[:, :, 1])
    ang = np.arctan2(fy, fx) + np.pi
    v = np.sqrt(fx * fx + fy * fy)
    hsv = np.zeros((h, w, 3), np.uint8)
    hsv[..., 0] = ang * (180 / np.pi / 2)
    hsv[..., 1] = 0xFF
    hsv[..., 2] = np.minimum(v * 4, 0xFF)
    bgr = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
    cv2.imshow('hsv', bgr)
    return bgr

if __name__ == '__main__':

    cam = cv2.VideoCapture(0)
    (ret, prev) = cam.read()
    prevgray = cv2.cvtColor(prev, cv2.COLOR_BGR2GRAY)
    show_hsv = True
    while True:
        (ret, img) = cam.read()
        vis = img.copy()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        flow = cv2.calcOpticalFlowFarneback(prevgray,gray,None,0.5,5,15,3,5,1.1,cv2.OPTFLOW_FARNEBACK_GAUSSIAN)
        prevgray = gray

        if show_hsv:
            gray1 = cv2.cvtColor(draw_hsv(flow), cv2.COLOR_BGR2GRAY)
            thresh = cv2.threshold(gray1, 25, 0xFF,cv2.THRESH_BINARY)[1]
            thresh = cv2.dilate(thresh, None, iterations=2)

            gray2, cnts, hierarchy = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

            for c in cnts:
                (x, y, w, h) = cv2.boundingRect(c)
                if w > 100 and h > 100 and w < 900 and h < 680:
                    cv2.rectangle(vis, (x, y), (x + w, y + h), (0, 0xFF, 0), 4)
            cv2.imshow('Image', vis)

        ch = 0xFF & cv2.waitKey(5)
        if ch == 27:
            break

    cv2.destroyAllWindows()
