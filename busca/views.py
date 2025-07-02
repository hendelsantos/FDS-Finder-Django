import os
import requests
from django.conf import settings
from django.shortcuts import render
from .forms import BuscaForm
from googlesearch import search

def index(request):
    links = []
    mensagens = []

    if request.method == 'POST':
        form = BuscaForm(request.POST)
        if form.is_valid():
            nome_produto = form.cleaned_data['nome_produto']

            # Variações de busca para melhorar resultados
            queries = [
                f"FDS {nome_produto} site:.br filetype:pdf",
                f"Ficha de Segurança {nome_produto} site:.br filetype:pdf",
                f"Ficha Técnica {nome_produto} site:.br filetype:pdf"
            ]

            resultados = set()

            try:
                for query in queries:
                    for url in search(query):
                        if url.lower().endswith(".pdf"):
                            resultados.add(url)
                        if len(resultados) >= 10:
                            break
                    if len(resultados) >= 10:
                        break

                links = list(resultados)

                if links:
                    pasta_destino = os.path.join(settings.BASE_DIR, 'FDS_Baixados')
                    os.makedirs(pasta_destino, exist_ok=True)

                    url_pdf = links[0]
                    try:
                        response = requests.get(url_pdf)
                        if response.status_code == 200:
                            nome_arquivo = nome_produto.replace(" ", "_").replace("/", "_") + ".pdf"
                            caminho_arquivo = os.path.join(pasta_destino, nome_arquivo)
                            with open(caminho_arquivo, "wb") as f:
                                f.write(response.content)
                            mensagens.append(f"FDS salva em: {caminho_arquivo}")
                        else:
                            mensagens.append(f"Erro ao baixar PDF: Status {response.status_code}")
                    except Exception as e:
                        mensagens.append(f"Erro ao baixar PDF: {e}")
                else:
                    mensagens.append("Nenhum link encontrado para o produto.")

            except Exception as e:
                mensagens.append(f"Erro na busca: {e}")

    else:
        form = BuscaForm()

    return render(request, 'busca/index.html', {'form': form, 'links': links, 'mensagens': mensagens})
