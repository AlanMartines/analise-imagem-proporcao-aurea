import cv2
from PIL import Image, ImageDraw

def draw_guidelines(imagem_path, save_path):
    # Carregue a imagem usando OpenCV
    imagem_cv = cv2.imread(imagem_path, cv2.IMREAD_COLOR)
    if imagem_cv is None:
        print(f"Erro ao ler a imagem {imagem_path}")
        return

    altura, largura, _ = imagem_cv.shape

    # Calcule os pontos da proporção áurea e da regra dos terços
    pontos_aureos = {
        "horizontal": [largura * 0.61803398875, largura * (1 - 0.61803398875)],
        "vertical": [altura * 0.61803398875, altura * (1 - 0.61803398875)]
    }

    pontos_tercos = {
        "horizontal": [largura / 3, 2 * largura / 3],
        "vertical": [altura / 3, 2 * altura / 3]
    }

    # Converta a imagem OpenCV para PIL para desenho
    imagem_pil = Image.fromarray(cv2.cvtColor(imagem_cv, cv2.COLOR_BGR2RGB))
    draw = ImageDraw.Draw(imagem_pil)

    line_width = int(max(largura, altura) * 0.005)  # Ajuste a largura da linha com base na resolução da imagem

    # Desenhe as linhas da proporção áurea (em vermelho)
    for ponto in pontos_aureos["horizontal"]:
        draw.line((ponto, 0, ponto, altura), fill="red", width=line_width)
    for ponto in pontos_aureos["vertical"]:
        draw.line((0, ponto, largura, ponto), fill="red", width=line_width)

    # Desenhe as linhas da regra dos terços (em azul)
    for ponto in pontos_tercos["horizontal"]:
        draw.line((ponto, 0, ponto, altura), fill="blue", width=line_width)
    for ponto in pontos_tercos["vertical"]:
        draw.line((0, ponto, largura, ponto), fill="blue", width=line_width)

    # Salve a imagem com as linhas desenhadas
    imagem_pil.save(save_path)

# Uso
draw_guidelines("caminho_da_imagem_original.jpg", "imagem_analisada.jpg")
