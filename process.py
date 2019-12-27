import cv2

import matplotlib.pyplot as plt


from skimage import measure
import skimage.filters as filters
import io
import cv2

def convert_color(image):
    img_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    h,s,v = cv2.split(img_hsv)
    return v

def filter_image(image):
    #edges = cv2.Canny(image, 50, 200)
    image_threshold = filters.threshold_li(image)
    filtered = image < image_threshold
    return filtered

def detect_contour(image):
    contours       = measure.find_contours(image, 0.8)

    max = 0
    result_contour = 0
    for n, contour in enumerate(contours):
        if (len(contour) > max):
            max = len(contour)
            result_contour = contour
    return result_contour

def save_image_as_bytes(image, contour):
    fig, ax = plt.subplots()
    ax.imshow(image, cmap=plt.cm.gray)

    ax.plot(contour[:, 1], contour[:, 0], linewidth=2)

    ax.axis('image')
    ax.set_xticks([])
    ax.set_yticks([])

    buf = io.BytesIO()
    plt.savefig(buf, format = 'png', bbox_inches='tight')
    buf.seek(0)
    imageBytes = buf.read()
    buf.close()
    return imageBytes

def process_image(filename):
    img            = cv2.imread(filename,1)
    img_color      = convert_color(img)
    filtered_image = filter_image(img_color)
    result_contour = detect_contour(filtered_image)
    image_bytes    = save_image_as_bytes(img, result_contour)
    return image_bytes, result_contour





