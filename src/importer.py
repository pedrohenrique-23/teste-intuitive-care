import pandas as pd
from sqlalchemy import create_engine
import os
import glob

# Configuração do Banco
db_connection_str = 'mysql+mysqlconnector://root:root@localhost/intuitive_db'
db_connection = create_engine(db_connection_str)

def import_operadoras():
    print("\n=== IMPORTANDO OPERADORAS ===")
    csv_path = "./raw_data/Relatorio_cadop.csv"
    
    if not os.path.exists(csv_path):
        print("Arquivo de operadoras não encontrado.")
        return

    try:
        # Lê com UTF-8 (Assumindo que você converteu no VS Code)
        df = pd.read_csv(csv_path, sep=';', encoding='utf-8', skiprows=0)
        
        df = df.rename(columns={"REGISTRO_OPERADORA": "Registro_ANS", "Data_Registro_ANS": "Data_Registro_ANS"})
        
        colunas_banco = ["Registro_ANS", "CNPJ", "Razao_Social", "Nome_Fantasia", "Modalidade",
            "Logradouro", "Numero", "Complemento", "Bairro", "Cidade", "UF", 
            "CEP", "DDD", "Telefone", "Fax", "Endereco_Eletronico", 
            "Representante", "Cargo_Representante", "Data_Registro_ANS"]
        
        df_final = df[[c for c in colunas_banco if c in df.columns]]
        
        df_final.to_sql('operadoras', con=db_connection, if_exists='replace', index=False)
        print(f"✅ Sucesso! {len(df_final)} operadoras importadas.")
    except Exception as e:
        print(f"❌ Erro operadoras: {e}")

def import_contabil():
    print("\n=== IMPORTANDO DADOS CONTÁBEIS (Financeiro) ===")
    
    # Procura todos os arquivos que tenham "202" no nome (ex: 1T2024.csv, 4T2023.csv)
    arquivos = glob.glob("./raw_data/*202*.csv")
    
    if not arquivos:
        print("⚠️ Nenhum arquivo contábil (ex: 1T2024.csv) encontrado na pasta raw_data.")
        return

    for arquivo in arquivos:
        print(f"Processando arquivo: {arquivo}...")
        try:
            # Lê com UTF-8, convertendo decimal brasileiro
            df = pd.read_csv(arquivo, sep=';', encoding='utf-8', decimal=',', thousands='.')
            
            df = df.rename(columns={
                "DATA": "DATA",
                "REG_ANS": "REG_ANS",
                "CD_CONTA_CONTABIL": "CD_CONTA_CONTABIL",
                "DESCRICAO": "DESCRICAO",
                "VL_SALDO_FINAL": "VL_SALDO_FINAL"
            })
            
            # Formatar a DATA
            df['DATA'] = pd.to_datetime(df['DATA'], format='%d/%m/%Y', errors='coerce')

            cols = ["DATA", "REG_ANS", "CD_CONTA_CONTABIL", "DESCRICAO", "VL_SALDO_FINAL"]
            df_final = df[cols]
            
            df_final.to_sql('demonstracoes_contabeis', con=db_connection, if_exists='append', index=False)
            print(f"   -> ✅ Importado com sucesso: {len(df_final)} linhas.")
            
        except Exception as e:
            print(f"   -> ❌ Erro ao importar {arquivo}: {e}")

if __name__ == "__main__":
    import_operadoras()
    import_contabil()