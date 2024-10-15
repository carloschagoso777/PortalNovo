import os
from docx import Document

def obter_nomes_documentos_pasta_atual():
    pasta_atual = os.getcwd()  # Obtém o diretório de trabalho atual
    nomes_documentos = []

    # Lista todos os arquivos na pasta atual
    for arquivo in os.listdir(pasta_atual):
        caminho_arquivo = os.path.join(pasta_atual, arquivo)

        # Verifica se o arquivo é um documento Word (.docx)
        if os.path.isfile(caminho_arquivo) and arquivo.lower().endswith('.png'):
            # Remove a extensão .docx e substitui "_" por " "
            nome_documento = os.path.splitext(arquivo)[0].replace("_", " ")

            # Remove a string "_perfil" do nome do documento
            nome_documento = nome_documento.replace("perfil", "")

            nomes_documentos.append(nome_documento)

    return nomes_documentos

nomes_documentos = obter_nomes_documentos_pasta_atual()

# Exibe os nomes dos documentos
for nome_documento in nomes_documentos:
    print(nome_documento)
