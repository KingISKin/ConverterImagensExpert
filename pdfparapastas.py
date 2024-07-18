import os
import shutil


def tratamento_de_pastas():
    pasta_principal = input('Caminho do lote a ser tratado: ')
    arquivos = os.listdir(pasta_principal)
    for arquivo in arquivos:
        caminho_arquivo = os.path.join(pasta_principal, arquivo)
        
        if os.path.isfile(caminho_arquivo):
            nome_pasta = os.path.splitext(arquivo)[0].strip()
            caminho_pasta_nova = os.path.join(pasta_principal, nome_pasta)
            os.makedirs(caminho_pasta_nova, exist_ok=True)
            caminho_destino = os.path.join(caminho_pasta_nova, arquivo.strip())
            shutil.move(caminho_arquivo, caminho_destino)

    print("Arquivos organizados em suas respectivas pastas.")
