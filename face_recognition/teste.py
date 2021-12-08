import os
import face_recognition
import numpy as np
from os import listdir

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
image_dir= os.path.join(BASE_DIR,"image")
print(image_dir)

def chek_image_dateset(face_encoding,name):
        if len(face_encoding)>1:
            raise NameError("a imagem  " + name + " tem mais de uma face, não consigo ligar os nomes. subistitua essa imagem")
        elif len(face_encoding)>1:
            raise NameError("não foi detectado face em " + name + "troque essa image")



data_face_names=[]
data_face_encodings=[]
label_ids={}
current_id=0


for root, dirs,files in os.walk(image_dir):
        for file in files:
                if file.endswith("png") or file.endswith("jpeg")or file.endswith("jpg"):
                        path = os.path.join(root,file)
                        label= os.path.basename(root).replace(" ","-").lower()

                        image = face_recognition.load_image_file(path)
                       # print(image)
                        face_encoding=face_recognition.face_encodings(image)
                        if len(face_encoding)==0:
                                continue
                        data_face_encodings.append(face_encoding[0])
                        data_face_names.append(label)

np.savez('./faces.npz', face=data_face_encodings, name=data_face_names)