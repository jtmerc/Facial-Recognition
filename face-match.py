# Import Modules
import face_recognition

# Images
image_of_bill = face_recognition.load_image_file('./img/known/Bill Gates.jpg')
bill_face_encoding = face_recognition.face_encodings(image_of_bill)[0]

unknown = face_recognition.load_image_file('./img/unknown/d-trump.jpg')
unknown_face_encoding = face_recognition.face_encodings(unknown)[0]

# Compares faces
results = face_recognition.compare_faces([bill_face_encoding], unknown_face_encoding)

if results[0]:
    print('This is Bill Gates')
else:
    print('This is not Bill Gates'
          )