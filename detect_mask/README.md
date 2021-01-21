# Detector de máscara
Técnicas de Deep learning tem sido amplamente usada para resolver problemas de visão computacional. Entretanto, para obter um modelo ideal de Deeep learning para uma aplicação, precisamo conciliar acurácia e performance, principalmente para análise de video em tempo real. A yolo é uma arquitetura de redes neurais convolucionais desenvolvida com propósito de entregar boa performance. Por esse motivo escolhemos treinar uma rede yolov3-tiny parar detecção de máscara. 

# Motivação
No cenário atual, com Covid-19, é obrigatório o uso de mascaras. Essa medida é fundamental para evitar a transmissão em massa do vírus. Nesse sentido, ferramenta de visão computacional pode ser usada para monitoramento principalmente em locais públicos com muita circulação de pessoas.

# Demo

![start](./doc/demo.gif)

# Como usar
## Dependência
Para executar o dector, você vai precisar dos seguinte pacotes e arquivos

* Python3
* opencv-python ou opencv-contrib-python
* Pesos em ``weights/mask_yolov3-tiny.weights``
* Arquivo com nome da classes ``data/calsses.names``
* Arquivo com arquitetura da rede ``cfg/mask_yolov3-tiny``

## Passo a passo
Para baixar esse repositório você pode clonar  com ``git clone https://github.com/eltonfernando/eltonOpencv`` ou baixar com .zip

por padrão o video de entrada é a webecam. isso pode ser alterado em.

``cap = cv2.VideoCapture(0)``

mudando 0 pelo caminho do video.

### Linux
Você já tem o python e o pip3 instalado, então basta executar 
* ``pip3 install opencv-python``
para executar basta abrir o terminal no local (pasta detect_mask).

``python3 yolov3_video_mask.py``

### Windows
* baixar e instalar python3, lembre-se de setar a variável de ambiente na instalação e incluir o pip

depois abra o cmd 
* ``pyhton -m pip install opencv-python``

navege até o diretorio detect_mask (dentro o arquivo clonado ou baixado)
 
 No campo superir (onde mostra o caminho que você está) apage tudo e digite cmd precione enter. Uma janela preta deve abrir no local.
 digite. ``python -m yolov3_video_mask.py``
 
 # Mais
 para saber mais detalhes sobre com esse algoritmo funciona visite meu post completo em [visioncompy](http://visioncompy.com/)

---

Baixe meu ebook grátis Guia de visão computacional. [Baixar](https://eltonfernando904.wixsite.com/meusite)
