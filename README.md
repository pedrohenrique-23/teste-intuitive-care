# Teste Técnico - Intuitive Care

Solução desenvolvida por Pedro Henrique do Nascimento Silva.

## 📋 Descrição
Este projeto resolve as etapas de **Web Scraping** e **Transformação de Dados** solicitadas no teste de nivelamento.

### Funcionalidades
- **Web Scraping:** Acessa o site da ANS, localiza e baixa os Anexos I e II (PDF) mais recentes.
- **ETL (Extração e Transformação):** Processa o PDF do Anexo I, remove cabeçalhos repetidos, substitui siglas (OD/AMB) e exporta os dados estruturados para CSV compactado.

## 🛠️ Como Rodar

1. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt

2. **Execute o script principal:**
   ```bash
    python main.py

3. **Resultado:**
Verifique a pasta ./data. O arquivo final será Teste_Pedro_Silva.zip.

🧰 Tecnologias
- Python 3.x
- Pandas (Manipulação de dados)
- Pdfplumber (Extração de tabelas em PDF)
- BeautifulSoup4 (Web Scraping)