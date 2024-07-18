import os
import shutil
import re
from utils import create_directory, load_cache
from pdf_processor import pdf_to_tiff
from pdfparapastas import tratamento_de_pastas

def listar_pastas(diretorio):
    return [f for f in os.listdir(diretorio) if os.path.isdir(os.path.join(diretorio, f))]

def atualizar_progresso(total_concluidos, total_pdfs):
    porcentagem_conclusao = (total_concluidos / total_pdfs) * 100
    barra_largura = 40
    progresso = int(barra_largura * total_concluidos / total_pdfs)
    barra = '━' * progresso + '-' * (barra_largura - progresso)
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Processando...")
    print(f'[{barra}] {porcentagem_conclusao:.2f}% concluído')

def processar_lote():
    entrada_dir = r"./entrada"
    saida_dir = r"./saida"
    cache_dir = r"./cache"
    cache_path = os.path.join(cache_dir, "cache.json")

    pastas = listar_pastas(entrada_dir)
    
    if not pastas:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Não existem lotes disponíveis.")
        return
    
    print("Escolha seu lote:")
    for i, pasta in enumerate(pastas, start=1):
        print(f"{i}. {pasta}")
    
    while True:
        escolha = input("Digite o número do lote escolhido: ")
        if escolha.isdigit() and 1 <= int(escolha) <= len(pastas):
            entrada_lote = pastas[int(escolha) - 1]
            break
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Escolha inválida. Tente novamente.")
    
    entrada_lote_dir = os.path.join(entrada_dir, entrada_lote)
    saida_lote_dir = os.path.join(saida_dir, entrada_lote)

    create_directory(saida_lote_dir)
    create_directory(cache_dir)

    pastas_lote = listar_pastas(entrada_lote_dir)
    pdf_files = []

    for subpasta in pastas_lote:
        subpasta_dir = os.path.join(entrada_lote_dir, subpasta)
        pdf_files.extend([os.path.join(subpasta_dir, f) for f in os.listdir(subpasta_dir) if f.lower().endswith(".pdf")])

    cache = load_cache(cache_path)
    print(f'Quantidade total: {len(pdf_files)}')
    total_pdfs = len(pdf_files)

    total_concluidos = 0
    numero_batchtrack = int(input('Digite o valor do primeiro Batchtrack: '))

    for pdf_path in pdf_files:
        try:
            novo_nome = f"{str(numero_batchtrack).zfill(8)}"
            pasta_saida_pdf = os.path.join(saida_lote_dir, novo_nome)
            create_directory(pasta_saida_pdf)
            
            pdf_to_tiff(pdf_path, pasta_saida_pdf)
            total_concluidos += 1
            numero_batchtrack += 1
        except Exception as e:
            print(f"Erro ao processar {pdf_path}: {str(e)}")
            continue
        atualizar_progresso(total_concluidos, total_pdfs)

    os.system('cls' if os.name == 'nt' else 'clear')
    print(f'Total de PDFs processados com sucesso: {total_concluidos}')

def main():
    while True:
        print("Menu Principal:")
        print("1. Iniciar Processamento")
        print("2. Organizar Pastas")
        print("3. Encerrar Programa")
        escolha = input("Escolha uma opção: ")
        
        if escolha == '1':
            os.system('cls' if os.name == 'nt' else 'clear')
            processar_lote()
        elif escolha == '2':
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Vamos organizar esse lote...")
            tratamento_de_pastas()
        elif escolha == '3':
            print("Encerrando o programa...")
            break
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
