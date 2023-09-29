import cv2,numpy,time
from PIL import ImageGrab
image_path = 'images/example_1.jpg'
prototxt = 'model/MobileNetSSD_deploy.prototxt'
model = 'model/MobileNetSSD_deploy.caffemodel'

CLASSES = ('background','aerophone','bicylce','bird','boat','bottle','bus'
           ,'car','cat','chair','cow','diningtable','dog','horse','motorbike',
           'person','pottedplant','sheep','sofa','train','tvmonitor')
COLORS = numpy.random.uniform(0,255,size=(len(CLASSES),3))
FONT = cv2.FONT_HERSHEY_SIMPLEX

net = cv2.dnn.readNetFromCaffe(prototxt,model)



image  = cv2.imread(image_path)
vc = cv2.VideoCapture(0)
# vc = cv2.VideoCapture('C:\Users\\29115\\Documents\\ShareX\\Screenshots\\2023-07\\input.mp4')




while True:
    retval, image = vc.read()
    if not retval or cv2.waitKey(16) & 0xFF == ord('q'):
        break
    img = ImageGrab.grab((1820,60,2840,2250))
    # img = ImageGrab.grab((1650, 60, 3840, 1080))
    # image = cv2.cvtColor(numpy.asarray(img), cv2.COLOR_RGB2BGR)
    # if cv2.waitKey(16) & 0xFF == ord('q'):
    #     break
    (h,w) = image.shape[:2]
    blob_img = cv2.resize(image,(300,300))
    blob = cv2.dnn.blobFromImage(blob_img,0.007843,(300,300),127.5)

    net.setInput(blob)
    detections = net.forward()

    for i in numpy.arange(0, detections.shape[2]):
        idx = int(detections[0, 0, i, 1])
        confidence = detections[0, 0, i, 2]
        if confidence > 0.2:
            #画矩形框
            box = detections[0, 0, i, 3:7] * numpy.array([w, h, w, h])
            (x1, y1, x2, y2) = box.astype('int')
            cv2.rectangle(image, (x1, y1), (x2, y2), COLORS[idx], 2)
            #标注信任度
            label = '{}: {:.2f}%'.format(CLASSES[idx], confidence * 100)
            print(label)
            cv2.putText(image, label, (x1, y1) ,FONT, 2, COLORS[idx], 5)
    cv2.imshow('Image',image)
    # time.sleep(1)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# vc.release()

# 销毁所有窗口
# cv2.destroyAllWindows()