import cv2


def load_image(path = "test_photo.png"):
    """
    :param path: string containing path to image
    :return: numpy array containg image
    """
    image = cv2.imread(path, 0)
    if image is None:
        print("Wrong image-path")
        raise TypeError
    return image


