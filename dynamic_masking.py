# dynamic_masking.py
import cv2
import numpy as np
import dlib

# Load the facial landmark predictor
predictor_path = "./gfpgan/weights/shape_predictor_68_face_landmarks.dat"
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(predictor_path)

def get_mouth_landmarks(image):
    faces = detector(image, 1)
    if len(faces) == 0:
        return None
    shape = predictor(image, faces[0])
    mouth_points = np.array([(shape.part(i).x, shape.part(i).y) for i in range(48, 68)])
    return mouth_points

def calculate_mouth_height(mouth_points):
    top_points = mouth_points[2:5]
    bottom_points = mouth_points[8:11]
    avg_top = np.mean(top_points[:, 1])
    avg_bottom = np.mean(bottom_points[:, 1])
    return avg_bottom - avg_top

def create_dynamic_mask(image, dilation_factor=1.5, min_dilation=10, max_dilation=30):
    mouth_points = get_mouth_landmarks(image)
    if mouth_points is None:
        return None
    mouth_height = calculate_mouth_height(mouth_points)
    dilation_size = int(mouth_height * dilation_factor)
    dilation_size = max(min_dilation, min(dilation_size, max_dilation))
    mask = np.zeros(image.shape[:2], dtype=np.uint8)
    cv2.fillConvexPoly(mask, mouth_points, 255)
    kernel = np.ones((dilation_size, dilation_size), np.uint8)
    dilated_mask = cv2.dilate(mask, kernel, iterations=1)
    feather_amount = dilation_size // 2
    dilated_mask = cv2.GaussianBlur(dilated_mask, (feather_amount*2+1, feather_amount*2+1), 0)
    return dilated_mask

def apply_mask(original_image, modified_image, mask):
    mask_normalized = mask.astype(float) / 255.0
    mask_normalized = np.expand_dims(mask_normalized, axis=2)
    result = (modified_image * mask_normalized) + (original_image * (1 - mask_normalized))
    return result.astype(np.uint8)