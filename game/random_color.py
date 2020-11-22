# gera uma nova cor para cada ponto feito
def new_color(ponto):
    colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0),
                (0, 255, 255), (255, 0, 255), (255, 127, 255),
                (127, 0, 255), (127, 0, 127)]
    return colors[ponto%len(colors)]