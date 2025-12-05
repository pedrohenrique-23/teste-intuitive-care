-- Criação do Banco de Dados
CREATE DATABASE IF NOT EXISTS intuitive_db;
USE intuitive_db;

-- Tabela de Operadoras
CREATE TABLE IF NOT EXISTS operadoras (
    Registro_ANS INT PRIMARY KEY,
    CNPJ VARCHAR(20),
    Razao_Social VARCHAR(255),
    Nome_Fantasia VARCHAR(255),
    Modalidade VARCHAR(100),
    Logradouro VARCHAR(255),
    Numero VARCHAR(100),
    Complemento VARCHAR(255),
    Bairro VARCHAR(100),
    Cidade VARCHAR(100),
    UF CHAR(2),
    CEP VARCHAR(20),
    DDD VARCHAR(5),
    Telefone VARCHAR(20),
    Fax VARCHAR(20),
    Endereco_Eletronico VARCHAR(255),
    Representante VARCHAR(255),
    Cargo_Representante VARCHAR(100),
    Data_Registro_ANS VARCHAR(20)
);

-- Tabela Contábil
CREATE TABLE IF NOT EXISTS demonstracoes_contabeis (
    id INT AUTO_INCREMENT PRIMARY KEY,
    DATA DATE,
    REG_ANS INT,
    CD_CONTA_CONTABIL VARCHAR(50),
    DESCRICAO VARCHAR(500),
    VL_SALDO_FINAL DECIMAL(20,2),
    INDEX idx_reg_ans (REG_ANS),
    INDEX idx_descricao (DESCRICAO)
);