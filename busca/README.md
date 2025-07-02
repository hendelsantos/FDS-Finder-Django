# FDS Finder Django

Sistema web para busca, consulta e download automático de FDS (Ficha de Dados de Segurança) de produtos químicos, desenvolvido em Django.

---

## 📦 **Funcionalidades**

- Busca inteligente de FDS via Google, utilizando múltiplas variações e palavras-chave.
- Download automático do PDF do FDS, salvo localmente na pasta `FDS_Baixados/`.
- Interface web responsiva e moderna (Bootstrap 5).
- Pronto para rodar em Linux, Windows ou macOS (Python 3.12+).
- Rodapé personalizado: "Feito por Hendel".

---

## 🚀 **Como rodar o projeto localmente**

1. **Clone o repositório:**
    ```bash
    git clone https://github.com/seuusuario/fdsfinder.git
    cd fdsfinder
    ```

2. **Crie e ative o ambiente virtual (recomendado):**
    ```bash
    python -m venv venv
    source venv/bin/activate    # Linux/macOS
    venv\Scripts\activate       # Windows
    ```

3. **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Rode as migrações do Django:**
    ```bash
    python manage.py migrate
    ```

5. **Inicie o servidor:**
    ```bash
    python manage.py runserver
    ```

6. **Acesse no navegador:**
    ```
    http://127.0.0.1:8000/
    ```

---

## 🧰 **Principais arquivos e pastas**

- `busca/` — app principal (views, forms, templates, urls)
- `FDS_Baixados/` — local onde os PDFs das FDS são salvos
- `requirements.txt` — dependências do projeto
- `manage.py` — utilitário de administração Django

---

## 💡 **Como funciona a busca**

1. Digite o nome/marca do produto químico desejado.
2. O sistema realiza múltiplas buscas no Google (FDS, Ficha de Segurança, Ficha Técnica).
3. Exibe os links encontrados e baixa automaticamente o primeiro PDF na pasta `FDS_Baixados/`.

---

## 🔒 **Atenção**

- Não suba o arquivo `db.sqlite3`, nem a pasta `venv/` ou `FDS_Baixados/` para o GitHub.
- O projeto utiliza a busca pública do Google. Alguns fabricantes podem exigir login ou não permitir download automático.

---

## 🏗️ **To-do / Melhorias futuras**

- Integração direta com sites de fabricantes.
- Histórico de buscas realizadas.
- Upload em lote de listas de produtos.
- Exportação de relatórios.

---

## 👤 **Autor**

Desenvolvido por Hendel  
Contato: [Seu e-mail ou LinkedIn aqui, opcional]

---
