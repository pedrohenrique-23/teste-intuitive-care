import os
import requests
from bs4 import BeautifulSoup
import zipfile

class AnsScraper:
    def __init__(self, output_dir):
        # URL oficial do teste
        self.url = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"
        self.output_dir = output_dir
        
        # Garante que a pasta de destino exista
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

    def fetch_links(self):
        """Acessa o site e busca os links dos Anexos I e II."""
        print(f"Acessando {self.url}...")
        try:
            # User-Agent para evitar ser bloqueado (boa prática de scraping)
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
            }
            response = requests.get(self.url, headers=headers)
            response.raise_for_status() 
        except requests.RequestException as e:
            print(f"Erro ao acessar o site: {e}")
            return []

        soup = BeautifulSoup(response.content, 'html.parser')
        links_found = []

        # Busca links que contenham "Anexo" no texto e terminem com .pdf
        for tag in soup.find_all('a', href=True):
            href = tag['href']
            text = tag.get_text().upper()
            
            # Filtra Anexo I e Anexo II (ignora outros)
            if "ANEXO" in text and href.lower().endswith('.pdf'):
                if "ANEXO I" in text or "ANEXO II" in text:
                    links_found.append(href)
                    print(f"Link encontrado: {text.strip()} -> {href}")

        # Remove duplicatas
        return list(dict.fromkeys(links_found))

    def download_pdfs(self, links):
        """Baixa os arquivos encontrados."""
        downloaded_files = []
        for link in links:
            filename = link.split('/')[-1]
            filepath = os.path.join(self.output_dir, filename)
            
            print(f"Baixando {filename}...")
            try:
                response = requests.get(link)
                with open(filepath, 'wb') as f:
                    f.write(response.content)
                downloaded_files.append(filepath)
            except Exception as e:
                print(f"Erro ao baixar {filename}: {e}")
        
        return downloaded_files

    def zip_files(self, file_paths, zip_name="Anexos_ANS.zip"):
        """Compacta os arquivos baixados."""
        if not file_paths:
            print("Nenhum arquivo para zipar.")
            return

        zip_path = os.path.join(self.output_dir, zip_name)
        print(f"Criando arquivo ZIP: {zip_path}")
        
        with zipfile.ZipFile(zip_path, 'w') as zipf:
            for file in file_paths:
                zipf.write(file, arcname=os.path.basename(file))
        
        print("Compactação concluída!")

    def run(self):
        """Método principal que orquestra tudo."""
        links = self.fetch_links()
        if not links:
            print("Nenhum link encontrado. Verifique a lógica de busca.")
            return
        
        files = self.download_pdfs(links)
        self.zip_files(files)