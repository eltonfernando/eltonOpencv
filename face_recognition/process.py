import face_recognition
import numpy as np
import cv2
import os
class CriaFaceRecongnition():
    def __init__(self):
        self.data_face_encodings = []
        self.data_face_names = []
        self.face_names=[]
        self.face_encodings=[]
        self._load_face_dataset()
    def detection(self,rgb_small_frame):
        """
        Procura faces na imagem, sem contrar aplica encoder

        deve ser chamada antes de compare()
        :param rgb_small_frame:
        :return:
        """
        self.face_names = []
        self.face_locations = face_recognition.face_locations(rgb_small_frame)
        if len(self.face_locations)>0:
            self.face_encodings = face_recognition.face_encodings(rgb_small_frame, self.face_locations)

    def compare(self):
        """
        Compara as faces encontrada por detecion() e
        se for um estranho o nome é ????
        :return:
        """
        if len(self.face_encodings)==0:
            return
        for face_encod in self.face_encodings:
            matches = face_recognition.compare_faces(self.data_face_encodings, face_encod)
            name = "????"
            best_match_index=self._confidencie(face_encod)

            if matches[best_match_index]:
                name = self.data_face_names[best_match_index]
            self.face_names.append(name)
    def _confidencie(self,face_encod):
        """
        A semelhança entre as face é dado pela distancia (quanto menor a distancia mais parecida e as faces)
        o corte é 0.6 vc pode diminuir para melhorar a confiança do reconhecimento (mais vai gerar mais falso positivo
        :param face_encod:
        :return: indixe da face com menor distância
        """
        face_distances = face_recognition.face_distance(self.data_face_encodings, face_encod)
        best_match_index = np.argmin(face_distances)
        return best_match_index

    def draw(self,frame,resized):
        for (top, right, bottom, left), name in zip(self.face_locations, self.face_names):
            top *= int(1/resized)
            right *= int(1/resized)
            bottom *= int(1/resized)
            left *= int(1/resized)
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
            cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

    def _load_face_dataset(self):
        if not os.path.isfile("faces.npz"):
            print("crian dataset de face cadastradas")
            from data_face import DataFace
            df=DataFace()
            df.update_data_face()
            #raise NameError("faces.npz não encontrado, veja data_face.py para cria-lo")
        binari_face = np.load('./faces.npz', allow_pickle=True)
        self.data_face_encodings=binari_face['face']
        self.data_face_names=binari_face['name']