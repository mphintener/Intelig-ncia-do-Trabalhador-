# Inteligência do Trabalhador 🛠️

**Plataforma de Monitoramento do Rendimento Real e Expropriação do Tempo na RMSP.**

Este projeto é parte de uma pesquisa de doutorado focada na exploração do trabalho sob a égide do Toyotismo. A ferramenta calcula o impacto real do deslocamento metropolitano sobre o salário nominal, revelando o **Salário Real Confiscado**.

---

## 📊 Lógica Técnica
O cálculo da "Sobra Final" não altera o valor da hora contratada, mas aplica a lógica de expropriação:
- **Custo Direto:** Tarifas de transporte (Municipal SP e Intermunicipal EMTU).
- **Custo de Tempo:** Valorização das horas gastas no "trecho" (não remuneradas) com base no valor/hora do trabalhador.

---

## 🎨 Identidade Visual
O projeto segue uma estética de **Alto Contraste**:
- **Fundo:** Preto (#000000)
- **Detalhes:** Amarelo (#FFD700) e Vermelho (#FF0000)

---

## 🏗️ Arquitetura do Projeto
- **Linguagem:** Python 3.10
- **Automação:** GitHub Actions (Rodando diariamente às 03:00 BRT)
- **Interface:** PWA (Progressive Web App) para acesso mobile offline.
- **Dados:** JSON gerado dinamicamente cruzando vagas de mercado com a matriz tarifária da Grande SP.

---

## 📁 Estrutura de Arquivos
- `.github/workflows/`: Scripts de automação (Bot).
- `scripts/`: Motores de captura e cálculo (Scraper).
- `data/`: Base de dados em tempo real (JSON).
- `index.html`: Interface do PWA.

---
**Desenvolvido por um pesquisador focado em Mobilidade Urbana e Mercado de Trabalho.**

