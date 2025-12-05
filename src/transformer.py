import os
import pdfplumber
import pandas as pd
import zipfile

class PdfTransformer:
    def __init__(self, data_dir):
        self.data_dir = data_dir
    
    def find_anexo_i(self):
        """Busca automaticamente o arquivo CORRETO do Anexo I."""
        print(f"Buscando Anexo I na pasta: {self.data_dir}")
        for file in os.listdir(self.data_dir):
            # Garante que tem 'Anexo_I_' no nome e ignora 'Anexo_II' explicitamente
            if "Anexo_I_" in file and "Anexo_II" not in file and file.endswith(".pdf"):
                print(f"Arquivo encontrado: {file}")
                return os.path.join(self.data_dir, file)
        raise FileNotFoundError("Anexo I não encontrado! Verifique se o download funcionou.")

    def extract_table(self, pdf_path):
        """Extrai tabelas com proteção contra páginas vazias."""
        print(f"Iniciando extração do arquivo: {os.path.basename(pdf_path)}")
        
        all_data = []
        
        with pdfplumber.open(pdf_path) as pdf:
            total_pages = len(pdf.pages)
            print(f"Total de páginas encontradas: {total_pages}")
            
            for i, page in enumerate(pdf.pages):
                if (i + 1) % 50 == 0:
                    print(f"Processando página {i + 1}/{total_pages}...")

                table = page.extract_table()
                
                if table:
                    # Se for a primeira tabela encontrada (cabeçalho + dados)
                    if not all_data:
                        all_data.extend(table)
                    else:
                        # Verifica se a nova tabela tem o mesmo cabeçalho da primeira
                        if table[0] == all_data[0]:
                            all_data.extend(table[1:])
                        else:
                            all_data.extend(table)
        
        return all_data

    def transform_data(self, raw_data):
        """Limpa os dados e substitui as siglas."""
        if not raw_data:
            raise ValueError("Nenhum dado foi extraído do PDF. Verifique o arquivo.")

        print("Transformando dados...")
        
        columns = raw_data[0]
        data = raw_data[1:]
        
        df = pd.DataFrame(data, columns=columns)
        
        # Substituição das Siglas (OD e AMB)
        if 'OD' in df.columns:
            df['OD'] = df['OD'].replace({'OD': 'Seg. Odontológica'})
        
        if 'AMB' in df.columns:
            df['AMB'] = df['AMB'].replace({'AMB': 'Seg. Ambulatorial'})

        return df

    def save_csv_zip(self, df, filename="Teste_Pedro_Silva.zip"):
        """Salva o DataFrame em CSV dentro de um ZIP."""
        zip_path = os.path.join(self.data_dir, filename)
        csv_name = "Rol_Procedimentos.csv"
        
        print(f"Salvando arquivo final: {zip_path}")
        
        with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zf:
            csv_data = df.to_csv(index=False, sep=';', encoding='utf-8-sig')
            zf.writestr(csv_name, csv_data)
        
        print("Arquivo Salvo com Sucesso!")