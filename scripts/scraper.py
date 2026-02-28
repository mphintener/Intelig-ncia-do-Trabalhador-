import json
import os

# --- MATRIZ GEOGRÁFICA DE EXPROPRIAÇÃO (Custos Fixos 2026) ---
# Tarifas integradas e tempos médios de deslocamento para SP Capital
MATRIZ_MUNICIPIOS = {
    "FRANCO_DA_ROCHA": {"tarifa": 24.80, "tempo": 2.5},
    "CAIEIRAS": {"tarifa": 23.60, "tempo": 2.0},
    "OSASCO": {"tarifa": 20.40, "tempo": 1.2},
    "CARAPICUIBA": {"tarifa": 21.60, "tempo": 1.5},
    "ITAPEVI": {"tarifa": 25.00, "tempo": 2.2},
    "ALPHAVILLE": {"tarifa": 29.60, "tempo": 2.5},
    "ABCD": {"tarifa": 23.00, "tempo": 1.8},
    "SAO_PAULO_CAPITAL": {"tarifa": 10.70, "tempo": 1.0}
}

def calcular_sobra_real(salario_bruto, tarifa_diaria, horas_trecho):
    """Lógica da tese: Sobra final confiscada pelo transporte e tempo."""
    DIAS_UTEIS = 22
    valor_hora = salario_bruto / 220 # Base 44h semanais
    
    custo_passagem = tarifa_diaria * DIAS_UTEIS
    custo_tempo = (horas_trecho * DIAS_UTEIS) * valor_hora
    
    sobra = salario_bruto - custo_passagem - custo_tempo
    return round(sobra, 2)

def gerar_inteligencia():
    # Simulando a captura de vagas dos 3 setores do Toyotismo em SP
    vagas_mercado = [
        {"setor": "Logística", "salario": 2100.00},
        {"setor": "Telemarketing", "salario": 1650.00},
        {"setor": "Varejo", "salario": 1900.00}
    ]
    
    relatorio_final = []

    for municipio, dados in MATRIZ_MUNICIPIOS.items():
        analise_vagas = []
        for vaga in vagas_mercado:
            sobra = calcular_sobra_real(vaga['salario'], dados['tarifa'], dados['tempo'])
            percentual_confisco = round(((vaga['salario'] - sobra) / vaga['salario']) * 100, 1)
            
            analise_vagas.append({
                "setor": vaga['setor'],
                "salario_nominal": vaga['salario'],
                "sobra_real": sobra,
                "confisco": f"{percentual_confisco}%"
            })
            
        relatorio_final.append({
            "origem": municipio.replace("_", " "),
            "vagas": analise_vagas
        })

    # Garante a pasta data
    os.makedirs('data', exist_ok=True)
    
    # Salva o JSON final que o PWA vai consumir
    with open('data/inteligencia.json', 'w', encoding='utf-8') as f:
        json.dump(relatorio_final, f, ensure_ascii=False, indent=4)
    
    print("Inteligência do Trabalhador atualizada com sucesso.")

if __name__ == "__main__":
    gerar_inteligencia()

