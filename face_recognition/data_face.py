"""
Gerencia o banco de dados de faces
* para cadastar uma face coloque uma imagem da passoa na pasta base
* edite o nome da imagem para o noma da pessoa
execute
    db=DataFace()
    db.update_data_face()

"""
import os
import face_recognition
import numpy as np

class DataFace():
    """
    constroi uma base com todas imagens da pasta ./base
    e salve em um objeto python faces.npz (depois de cadastrado esse é o arquivo que vc precisa)
    o faces.npz ja armazena a base encodada, isso melhor o tempo de incialização

    as imagem de ./base não precisa ser recortada (só com a area da face)
    Não pode ter uma imagem com duas ou mais faces, (isso dificultaria para atribuir os nomes)
    O nome cadastrado é o nome da imagem

    """
    def __init__(self):
        self.path_faces="base"
        self.data_face_names=[]
        self.data_face_encodings=[]


    def update_data_face(self):
        self._chek_dir_face()
        list_base = os.listdir(self.path_faces)
        for name in list_base:
            image = face_recognition.load_image_file("base/" + name)
            face_encoding = face_recognition.face_encodings(image)
            self._chek_image_dateset(face_encoding,name)
            self.data_face_names.append(name.split(".")[0])
            self.data_face_encodings.append(face_encoding[0])
            self._save_pnz_dataset()

    def _chek_dir_face(self):
        if not os.path.isdir(self.path_faces):
            raise("a pasta base deve ter pelo menos uma face")
        if len(os.listdir(self.path_faces))==0:
            raise ("A pasta base não pode estar vasiza")

    def _chek_image_dateset(self, face_encoding,name):
        if len(face_encoding)>1:
            raise NameError("a imagem  " + name + " tem mais de uma face, não consigo ligar os nomes. subistitua essa imagem")
        elif len(face_encoding)>1:
            raise NameError("não foi detectado face em " + name + "troque essa image")

    def _save_pnz_dataset(self):
        np.savez('./faces.npz', face=self.data_face_encodings, name=self.data_face_names)



if __name__=="__main__":
    db=DataFace()
    db.update_data_face()
