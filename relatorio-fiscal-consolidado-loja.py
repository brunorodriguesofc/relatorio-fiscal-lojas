# Relatório Fiscal Consolidado por Lojas


#🔹 REGRAS DE IMPOSTO (OBRIGATÓRIO USAR FUNÇÃO)
#até 1000 → 10%
#acima de 1000 → 15%
#acima de 1500 → 20%



#🔹 DADOS INICIAIS 
lojas = {
    "Loja A": [1500, 1000, 800, 2000],
    "Loja B": [500, 4000, 3200, 2600, 1000],
    "Loja C": [700, 900, 1200, 1800]
}



#🔹 PARTE 1 — Função de imposto

def definir_taxa_imposto(preco):
    if preco > 1500:
        taxa = 0.20
    elif preco > 1000:
        taxa = 0.15
    else:
        taxa = 0.10        
    return taxa



#🔹 PARTE 2 — Função de cálculo

def calcular_totais(lista_precos):
    faturamento_total = 0
    imposto_total = 0
    for preco in lista_precos:
        taxa_imposto = definir_taxa_imposto(preco)
        imposto = preco * taxa_imposto
        imposto_total += imposto
        faturamento_total += preco
    return faturamento_total, imposto_total



#🔹 PARTE 3 — Loop principal

faturamento_geral = 0
imposto_geral = 0
maior_imposto = 0
loja_maior_imposto = ""
resumo_lojas = ""

for nome_loja, vendas in lojas.items():  # ← .items() pega nome e lista juntos

    # Faturamento e Imposto da loja
    faturamento_loja, imposto_loja = calcular_totais(vendas)
    
    # Acumula os totais
    faturamento_geral += faturamento_loja
    imposto_geral += imposto_loja
    
    # Identifica maior imposto
    if imposto_loja > maior_imposto:
        maior_imposto = imposto_loja
        loja_maior_imposto = nome_loja

    resumo_lojas += f"{nome_loja} → Faturamento: R${faturamento_loja:,.2f} | Imposto: R${imposto_loja:,.2f}\n"



#🔹 PARTE 4 — Classificação

#Baseado no imposto total geral:

#≥ 5000 → "Alta carga tributária"
#≥ 2000 → "Média carga tributária"
#< 2000 → "Baixa carga tributária"

if imposto_geral >= 5000:
    classificacao = "Alta carga tributária"
elif imposto_geral >= 2000:
    classificacao = "Média carga tributária"
else:
    classificacao = "Baixa carga tributária" 


#🔹 PARTE 5 — Saída final 

print()
print("RELATÓRIO FISCAL")
print()
print("Resumo por loja:")
print(resumo_lojas)
print()
print(f"Faturamento total: R${faturamento_geral:,.2f}")
print(f"Imposto total: R${imposto_geral:,.2f}")
print()
print(f"Loja com maior imposto: {loja_maior_imposto}")
print()
print(f"Classificação: {classificacao}")
print()
