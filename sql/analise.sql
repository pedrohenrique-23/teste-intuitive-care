USE intuitive_db;

-- 1. Correção prévia das datas (necessária pois a importação trouxe NULL)
SET SQL_SAFE_UPDATES = 0;
UPDATE demonstracoes_contabeis SET DATA = '2024-01-01' WHERE DATA IS NULL;
SET SQL_SAFE_UPDATES = 1;

-- 2. Query: Top 10 Operadoras (Último Trimestre)
SELECT 
    o.Registro_ANS, 
    o.Razao_Social, 
    FORMAT(SUM(d.VL_SALDO_FINAL), 2, 'de_DE') AS Total_Despesas
FROM demonstracoes_contabeis d
JOIN operadoras o ON d.REG_ANS = o.Registro_ANS
WHERE 
    d.DESCRICAO LIKE '%EVENTOS%SINISTROS%CONHECIDOS%'
    AND d.DATA >= '2024-01-01'
GROUP BY o.Registro_ANS, o.Razao_Social
ORDER BY SUM(d.VL_SALDO_FINAL) DESC
LIMIT 10;

-- 3. Query: Top 10 Operadoras (Último Ano)
SELECT 
    o.Registro_ANS, 
    o.Razao_Social, 
    FORMAT(SUM(d.VL_SALDO_FINAL), 2, 'de_DE') AS Total_Despesas
FROM demonstracoes_contabeis d
JOIN operadoras o ON d.REG_ANS = o.Registro_ANS
WHERE 
    d.DESCRICAO LIKE '%EVENTOS%SINISTROS%CONHECIDOS%'
    AND d.DATA >= '2023-01-01'
GROUP BY o.Registro_ANS, o.Razao_Social
ORDER BY SUM(d.VL_SALDO_FINAL) DESC
LIMIT 10;