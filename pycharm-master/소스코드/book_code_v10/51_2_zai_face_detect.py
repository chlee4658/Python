from zAI import zImage

myPhoto = zImage('./img/test1.jpg')
text = myPhoto.label(backend='Microsoft')

myPhoto.find_faces(backend='local')
len(myPhoto.faces)

myCloseup = myPhoto.extract_face(n=0, margin=50)  # margin is the number of pixels we will expand
# the tight face rentangle around the face
myCloseup.display()
myCloseup.save("./face.jpg")