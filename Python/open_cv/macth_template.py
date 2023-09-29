import cv2,time
import numpy as np
import uiautomation as auto
def match_template(img_rgb,template,threshold):
    # img_rgb = cv2.imread('/Users/mac/PycharmProjects/pythonProject1/2.jpg')
    img_gray = cv2.cvtColor(img_rgb,cv2.COLOR_BGR2GRAY)

    # template = cv2.imread('/Users/mac/PycharmProjects/pythonProject1/2的副本.png')
    h,w = template.shape[:-1]

    img_gray = cv2.cvtColor(img_gray, cv2.COLOR_BGR2RGB)
    res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)

    # threshold = 0.8
    loc = np.where(res >= threshold)

    for pt in zip(*loc[::-1]):
        cv2.rectangle(img_rgb,pt,(pt[0]+w,pt[1]+h),(48,8,8),2)
        print(pt)
    cv2.imshow('in',img_rgb)
    cv2.waitKey(0)

# img_rgb = cv2.imread('/Users/mac/PycharmProjects/pythonProject1/2.jpg')
# template = cv2.imread('/Users/mac/PycharmProjects/pythonProject1/2的副本.png')
# match_template(img_rgb,template,0.8)


