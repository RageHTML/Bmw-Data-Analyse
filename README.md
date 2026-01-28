# README.md

# Projeto BMW - Análise de Dados

## Contato

- **LinkedIn:** [Deyvid Martins](https://www.linkedin.com/in/deyvid-martins/)  
- **E-mail:** deyvidmail24@gmail.com

## Descrição
Neste projeto foi realizada uma análise estatística exploratória para compreender a relação entre as variáveis do dataset de carros e o preço dos veículos. Como a estatística trabalha com tendências e não com certezas absolutas, os resultados apresentados indicam padrões observados nos dados.
## Problema 
Entender como as variáveis mileage, engineSize e tax estão relacionadas com o price dos veículos.

## Decisao Apoiada 
Com base na análise estatística exploratória, o projeto apoia decisões relacionadas à precificação de veículos a partir de suas características. Os resultados indicam que a quilometragem tende a ter um impacto negativo relevante no preço, enquanto o tamanho do motor apresenta uma relação positiva moderada com o valor dos veículos. Já a variável tax demonstra uma influência mais fraca sobre o preço. Dessa forma, a análise auxilia na compreensão de quais fatores tendem a pesar mais na definição do valor de mercado de um carro, servindo como suporte para decisões de compra, venda ou segmentação de veículos.

## Beneficiario 
Este projeto beneficia pessoas interessadas na análise de dados e no mercado automotivo, como estudantes, analistas iniciantes, compradores e vendedores de veículos, ao oferecer suporte analítico para entender como características dos carros tendem a influenciar o preço, auxiliando a tomada de decisão baseada em dados.

# Hipoteses ou causas provaveis 
Veículos com maior quilometragem (mileage) tendem a apresentar preços mais baixos, devido ao maior nível de uso e desgaste ao longo do tempo.

Carros com motores maiores (engineSize) tendem a ter preços mais elevados, pois geralmente estão associados a maior desempenho e valor de mercado.

O imposto (tax) tende a apresentar uma relação positiva fraca com o preço, podendo estar indiretamente associado a características como motorização ou ano do veículo.

O preço dos veículos tende a ser influenciado por um conjunto de fatores, e não por uma única variável isolada.

## Métricas:
Neste projeto foi utilizada a correlação de Pearson como métrica estatística para avaliar a relação entre as variáveis mileage, engineSize e tax com o price, permitindo identificar a direção e a intensidade das associações entre essas variáveis.

## O dataset contém as seguintes colunas:

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

### 1. Carregamento e inspeção inicial do dataset para compreensão das variáveis disponíveis.

### 2. Seleção das variáveis mileage, engineSize, tax e price para análise.

### 3. Aplicação da correlação de Pearson como método estatístico para avaliar a relação entre as variáveis selecionadas.

### 4. Interpretação dos coeficientes de correlação para identificar tendências e padrões nos dados.

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
