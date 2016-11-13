import dlib
from skimage import io
detector = dlib.get_frontal_face_detector()
img = io.imread('obama.jpg')
faces = detector(img)
for d in faces:
    print "left,top,right,bottom:", d.left(), d.top(), d.right(), d.bottom()
win = dlib.image_window()
win.set_image(img)
win.add_overlay(faces)
options = dlib.simple_object_detector_training_options()
options.C = 5  # Set the SVM C parameter to 5.  
dlib.train_simple_object_detector("training.xml","detector.svm", options)
detector = dlib.simple_object_detector("detector.svm")
