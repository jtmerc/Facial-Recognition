# Import modules
import face_recognition

image = face_recognition.load_image_file('./group/ryangroup1.jpg')
face_locations = face_recognition.face_locations(image)

# Arrays of coords of faces
print(face_locations)

print(f'There are {len(face_locations)} people in this image'
      )