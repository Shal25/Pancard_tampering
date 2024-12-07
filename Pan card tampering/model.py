from skimage.metrics import structural_similarity
import imutils
import cv2
from PIL import Image
import requests

reference_image_path = "D:\Pan card tampering\image\original.jpg"
reference_image = cv2.imread(reference_image_path, cv2.IMREAD_GRAYSCALE)

def calculate_ssim(uploaded_image_path):
    uploaded_image = cv2.imread(uploaded_image_path, cv2.IMREAD_GRAYSCALE)
    uploaded_image = cv2.resize(uploaded_image, (250, 160))

    score = structural_similarity(reference_image, uploaded_image, full=True)
    return round(score[0]*100,2)