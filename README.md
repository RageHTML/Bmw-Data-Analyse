# README.md

# Projeto BMW - Análise de Dados

## Contato

- **LinkedIn:** [Deyvid Martins](https://www.linkedin.com/in/deyvid-martins/)  
- **E-mail:** deyvidmail24@gmail.com

## Descrição
Este projeto analisa dados de vendas de veículos BMW com o objetivo de identificar quais faixas de preço, modelos e anos apresentam maior velocidade de venda, fornecendo suporte à gestão de estoque e à tomada de decisões comerciais.

O dataset contém as seguintes colunas:

- `model` : Modelo do carro
- `year` : Ano do modelo
- `price` : Preço do carro
- `transmission` : Tipo de transmissão
- `mileage` : Quilometragem
- `fuelType` : Tipo de combustível
- `tax` : Imposto
- `mpg` : Consumo médio (miles per gallon)
- `engineSize` : Tamanho do motor

---


## Passos Realizados

### 1. Limpeza dos Dados
- Remoção de **linhas duplicadas**
- Verificação de valores ausentes
- Conversão de tipos de dados (ex.: `price` para inteiro)

### 2. Organização e Análise
- **Preço médio por modelo** calculado usando pandas (`groupby('model')['price'].mean()`)
- **Carro mais barato individual** identificado
- **Carros com maior quilometragem** destacados para análise

### 3. Visualização
- Gráficos gerados com matplotlib:
  - **Preço médio por modelo**
  - **Carro mais barato destacado**
  - **Carros com maior quilometragem** sobrepostos no gráfico
- Anotações e cores usadas para **destacar insights importantes**.

### 4. Uso de Git e GitHub
- Repositório inicializado com `git init`
- `.gitignore` criado para **ignorar venv e arquivos temporários**
- Adicionados apenas os arquivos essenciais (`bmw.csv`, `s.py`, `.gitignore`)
- Push para o GitHub realizado

---

## Como Rodar o Projeto

1. Clonar o repositório:
```bash
git clone https://github.com/SEU_USUARIO/projeto-bmw.git

## Criar um ambiente virtual 
python -m venv venv
# Windows
venv\Scripts\activate
# Mac/Linux
source venv/bin/activate
## instlar dependecia 
pip install -r requirements.txt
## rodar script 
python s.py
