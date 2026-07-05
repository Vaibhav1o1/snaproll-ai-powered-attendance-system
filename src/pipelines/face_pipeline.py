import streamlit as st

import dlib
import cv2
import numpy as np
import face_recognition_models

from src.database.db import get_all_students


@st.cache_resource
def load_dlib_models():
    detector = dlib.get_frontal_face_detector()

    sp = dlib.shape_predictor(
        face_recognition_models.pose_predictor_model_location()
    )   

    facerec = dlib.face_recognition_model_v1(
        face_recognition_models.face_recognition_model_location()
    )

    return detector, sp, facerec



def get_face_embeddings(image_np):
    detector, sp, facerec = load_dlib_models()

    faces = detector(image_np, 1)

    encodings = []

    for face in faces:
        shape = sp(image_np, face)
        face_descriptor = facerec.compute_face_descriptor(image_np, shape, 5) # 128 Embeddings

        encodings.append(np.array(face_descriptor))

    return encodings


@st.cache_resource
def get_face_gallery():
    student_db = get_all_students()

    if not student_db:
        return None
    
    gallery = []

    for student in student_db:
        embs = student.get('face_embedding')

        if not embs:
            continue

        if isinstance(embs[0], (int, float)):
            embs = [embs]

        for e in embs:
            gallery.append((student['student_id'], np.array(e)))

    return gallery or None


def train_classifier():
    st.cache_resource.clear()

    gallery = get_face_gallery()
    return bool(gallery)



def predict_attendance(class_image_np):
    encodings = get_face_embeddings(class_image_np)

    detected_students = {}

    gallery = get_face_gallery()

    if not gallery: # Present_Students, All_Students, No_of_Present_Students
        return detected_students, [], len(encodings) 
    
    all_students = sorted(set(sid for sid, _ in gallery))
    resemblance_threshold = 0.45

    for encoding in encodings:
        best_sid, best_dist = None, float('inf')

        for sid, emb in gallery:
            dist = np.linalg.norm(emb - encoding)

            if dist < best_dist:
                best_dist, best_sid = dist, sid

        if best_sid is not None and best_dist <= resemblance_threshold:
            detected_students[best_sid] = True

    return detected_students, all_students, len(encodings)



def is_face_quality_ok(image_np, face_rect):
    gray = cv2.cvtColor(image_np, cv2.COLOR_RGB2GRAY)
    blur_score = cv2.Laplacian(gray, cv2.CV_64F).var()
    if blur_score < 50:
        return False, "Image too blurry, hold steady."

    face_area = face_rect.width() * face_rect.height()
    image_area = image_np.shape[0] * image_np.shape[1]
    if face_area / image_area < 0.03:
        return False, "Move closer to the camera."

    return True, None
    



