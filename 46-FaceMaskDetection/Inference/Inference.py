from PySide6.QtWidgets import *
from PySide6.QtUiTools import *
from PySide6.QtCore import *
from PySide6.QtGui import *
import cv2
from tensorflow.keras.models import load_model
import numpy as np


class FaceMask(QMainWindow):
    def __init__(self):
        super().__init__()
        loader = QUiLoader()
        self.ui = loader.load('maskForm.ui', None)
        self.ui.show()
        self.readData()
        
    
    def readData(self):
        video_cap = cv2.VideoCapture(0)
        width = height = 224
        model = load_model('Model/46_FaceMask.h5')
        while True:
            self.ui.lb_notMask.setVisible(False)
            self.ui.lb_mask.setVisible(False)
            
            ret, frame = video_cap.read()
            if ret == False:
                break
            
            image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) # cv2 image color format !# tensorflow image color format
             
            image = cv2.resize(image, (width, height))
            image = image / 255
            image = image.reshape(1, width, height, 3)
            result = model.predict(image)
            print(result)
            pred = np.argmax(result)
            print(pred)
            if pred == 0:
                self.ui.lb_mask.setVisible(True)
            elif pred ==1:
                self.ui.lb_notMask.setVisible(True)

            RGB_frame = cv2.resize(frame, (600, 500))
            image = QImage(RGB_frame, RGB_frame.shape[1], RGB_frame.shape[0], QImage.Format_RGB888)
            pixmap = QPixmap.fromImage(image)    
            self.ui.webcam.setPixmap(pixmap)
            cv2.waitKey(1)
        
        video_cap.release()
        cv2.destroyAllWindows()


app = QApplication([])
window = FaceMask()

app.exec()
