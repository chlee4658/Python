from zAI import zImage

picasso = zImage('./img/picasso.png')

myPhoto = zImage('./img/face.jpg')
changePhoto = myPhoto.style(picasso)
changePhoto.display()
changePhoto.save("./img/change_face.jpg")
