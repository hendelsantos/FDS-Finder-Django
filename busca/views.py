import os
import requests
import pandas as pd
from django.conf import settings
from django.shortcuts import render
from .forms import BuscaForm
from googlesearch import search

def processa_produto(nome_produto, pasta_destino):
    queries = [
        f"FDS {nome_produto} site:.br filetype:pdf",
        f"Ficha de Segurança {nome_produto} site:.br filetype:pdf",
        f"Ficha Técnica {nome_produto} site:.br filetype:pdf"
    ]
    for query in queries:
        try:
            for url in search(query):
                if url.lower().endswith(".pdf"):
                    response = requests.get(url)
                    if response.status_code == 200:
                        nome_arquivo = nome_produto.replace(" ", "_").replace("/", "_") + ".pdf"
                        caminho_arquivo = os.path.join(pasta_destino, nome_arquivo)
                        with open(caminho_arquivo, "wb") as f:
                            f.write(response.content)
                        return f"FDS de '{nome_produto}' salva em: {caminho_arquivo}"
        except Exception as e:
            continue
    return f"Nenhuma FDS encontrada para '{nome_produto}'"

def index(request):
    links = []
    mensagens = []

    if request.method == 'POST':
        form = BuscaForm(request.POST, request.FILES)
        nomes_produto = []

        if form.is_valid():
            # Busca por campo individual
            nome_produto = form.cleaned_data['nome_produto']
            if nome_produto:
                nomes_produto.append(nome_produto)

            # Busca por lista enviada
            arquivo_lista = request.FILES.get('arquivo_lista')
            if arquivo_lista:
                extensao = os.path.splitext(arquivo_lista.name)[1].lower()
                if extensao == ".txt":
                    for linha in arquivo_lista:
                        nome = linha.decode('utf-8').strip()
                        if nome:
                            nomes_produto.append(nome)
                elif extensao in [".xlsx", ".xls"]:
                    df = pd.read_excel(arquivo_lista)
                    for col in df.columns:
                        nomes_produto += df[col].dropna().astype(str).tolist()
                else:
                    mensagens.append("Formato de arquivo não suportado. Use .txt ou .xlsx")

            # Processar todos os produtos
            if nomes_produto:
                pasta_destino = os.path.join(settings.BASE_DIR, 'FDS_Baixados')
                os.makedirs(pasta_destino, exist_ok=True)

                for nome in nomes_produto:
                    status = processa_produto(nome, pasta_destino)
                    mensagens.append(status)
            else:
                mensagens.append("Nenhum produto informado ou detectado no arquivo.")

    else:
        form = BuscaForm()

    return render(request, 'busca/index.html', {'form': form, 'mensagens': mensagens})
