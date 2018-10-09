import cv2

class Image:
    def __init__(self, path = "test_photo.png"):
        self.load_image(path)

    def load_image(self, path):
        """
        :param path: string containing path to image
        :return: numpy array containg image
        """
        self.image_array = cv2.imread(path, 0)
        if self.image_array is None:
            print("Wrong image-path")
            raise TypeError


