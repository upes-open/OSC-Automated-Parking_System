ALPR is one of the widely used computer vision applications. It makes use of various methods like object detection, OCR, segmentation, etc. For hardware, the ALPR system only requires a camera and a good GPU. In our Case we already have the Dtasets of Images generated. So Work on those.

Detection: Firstly, an image or a frame of the video sequence is passed to the detection algorithm from a camera or an already stored file, which detects the license plate and returns the bounding box(contour) location of that plate.

Recognition: The OCR is applied to the detected license plate for recognizing the characters of the plate and returns the characters in the same order in text format. The output can be stored in a database or can be plotted on the image for visualization.

The detection process can be done using any detector whether it’s a region-based detector or a single shot detector. For example you could use a single shot detector known as YOLOv4, mainly because of its good speed and accuracy tradeoff and ability to detect small objects better. YOLOv4 will be implemented using the darknet framework. <- If you decide to implement this.