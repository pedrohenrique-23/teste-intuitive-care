from src.scraper import AnsScraper
from src.transformer import PdfTransformer

def main():
    # --- PARTE 1: SCRAPING ---
    print("=== INICIANDO PARTE 1: SCRAPING ===")
    scraper = AnsScraper(output_dir="./data")
    scraper.run()
    print("=== PARTE 1 FINALIZADA ===\n")
    
    # --- PARTE 2: ETL ---
    print("=== INICIANDO PARTE 2: TRANSFORMACAO DE DADOS ===")
    transformer = PdfTransformer(data_dir="./data")
    
    try:
        # 1. Acha o arquivo PDF baixado na etapa anterior
        pdf_path = transformer.find_anexo_i()
        
        # 2. Extrai a tabela (Isso é o mais demorado)
        raw_data = transformer.extract_table(pdf_path)
        
        # 3. Transforma (Limpa e substitui siglas)
        df = transformer.transform_data(raw_data)
        
        # 4. Salva (Gera o ZIP final)
        transformer.save_csv_zip(df, filename="Teste_Pedro_Silva.zip")
        
        print("=== PROCESSO COMPLETO FINALIZADO COM SUCESSO! ===")
        
    except Exception as e:
        print(f"Ocorreu um erro na Parte 2: {e}")

if __name__ == "__main__":
    main()