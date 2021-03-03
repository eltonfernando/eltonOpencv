## Reconhecimento facial

Para cadastrar um face basta colocar uma image na pasta base.
* O nome da pessoa é o nome da imagem
* A imagem deve conter apenas o rosto que será cadastrado
* Não pode existir nem um arquivo nessa pasta que não seja uma imagem

OBS: A imagem da pasta base obrigatoriamente deve ter uma face, apenas uma por image.

## Prerequisito
* python3
* face_recognition
* dlib
* opencv

obs:Talvez você precisa do cmake para instalar o dlib

## instalação (Linux)

pip3 install opencv-python

pip3 install dlib

pip3 face_recognition

sudo apt install cmake

## instalar no windows

1 - instalar Cmake -> site cmake.org necessário colocar path para todos os usuarios
2 - pip install Cmake
3 - baixar o instalador vstudio 
 3.1 - instalar desenvolvimento C++
 3.2 - instalar todos os sdks
 3.3- instalar todos Ctools Cmake
4 - baixar o arquivo rar do DLIB
5 - extrair o arquivo copiar as pastas
6 - ir em C:\Users\admin\AppData\Local\Programs\Python\Python38\Lib\site-packages
7 - colar os arquivos do dlib nesta pasta
8- abrir CMD de comando e colocar cd C:\Users\admin\AppData\Local\Programs\Python\Python38\Lib\site-packages
9 - python setup.py install
