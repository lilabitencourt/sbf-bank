Contratação de Depósito a Prazo

## Contexto do Problema

Instituições financeiras realizam campanhas de marketing para oferta de depósitos a prazo.  
Entretanto, a taxa de conversão costuma ser baixa, o que gera alto custo operacional.

O objetivo deste projeto é:

- Identificar os principais fatores que influenciam a contratação de depoósito a prazo
- Desenvolver um modelo preditivo de propensão
- Comparar estratégias de decisão
- Propor uma implementação viável operacionalmente


# 1. Análise Exploratória dos Dados (EDA)

A análise exploratória foi conduzida para compreender:

- Distribuição das variáveis numéricas
- Frequência das variáveis categóricas
- Relação entre variáveis explicativas e a variável alvo (`y`)
- Possível presença de desbalanceamento

## Estatísticas Descritivas

- A base apresenta forte desbalanceamento (~11% de conversão). A maioria dos clientes não contratou o depósito a prazo.
- Variáveis como  `poutcome`, `month` e `contact` mostraram forte associação com a resposta.

## Principais Visualizações Utilizadas

- Boxplots com intervalo de confiança para variáveis numéricas
- Barplots com taxa de conversão por categoria
- Heatmap de correlação
- Distribuição da variável alvo

A EDA evidenciou padrões claros relacionados ao histórico de contato e sazonalidade.

# 2. Quais os 3 principais fatores que levam à contratação?

Com base na regressão logística (Odds Ratio) e análise de impacto:
##  Top 3 Variáveis Mais Relevantes

1. **Resultado da campanha anterior (`poutcome_success`)**
2. **Mês da campanha**
3. **Tipo de contato (contact_unknown`)**
   
1.1 poutcome_sucess -> clientes em que resultado anterior foi sucess tem 888% - (988-1)*100 - maior chance de contratar do que quem não teve sucesso em campanhas anteriores. Entendemos que o histórico de resultados anteriores é o principal fator.

2.1  Contatos do tipo unknown tem -80,3%  (0,19-1)*100. Ou seja, quando o contato é desconhecido a cahnce de contratação é 80,3% menor do que quando é conhecido.
Necessário investir em enriquecer o canal, buscando contatos reais dos clientes, evitando unknown.

3.1 Campanhas em março possuem quase 390,3% mais chance de contratação do que as que não são realizadas em março.  Sugere sazonalidade forte


#  3. Qual a chance de uma pessoa aposentada com 59 anos ou mais contratar?
Nossa Regressão Logística (Modelo1) trouxe o OR para pessoas aposentadas de 1,28. Então,
(1,28-1) * 100 = 28%, sendo assim:
Para quem é aposentado a chance de contratar é 28% maior de contratar do quem não é aposentado.

# 4. Relação entre resultado da campanha anterior e contratação

A variável `poutcome` apresentou forte impacto:

- `success` → aumento expressivo na probabilidade
Conclusão:

O histórico de interação anterior é um dos principais preditores da decisão futura.

#  5. Modelo Preditivo

## Metodologia
- Remoção da variável `duration` 
- One-hot encoding
- Separação treino/teste estratificada (80/20)
- Validação cruzada 5-fold
- Seleção de hiperparâmetros via GridSearch
- Métrica principal: ROC-AUC

## Modelo Base (Modelo 1)
- Regressão Logística
  
Inclui todas as variáveis relevantes.
Performance média:
- AUC ≈ 0.76–0.77
Importância das variáveis relacionadas a campanha e relacionamento

# 6. Modelo Alternativo (Modelo 3)
- Regressão Logística
  
Foi desenvolvido um segundo modelo desconsiderando as 3 variáveis mais influentes:
- `poutcome`
- `month`
- `contact`

Objetivo:
Avaliar dependência de variáveis operacionais e testar robustez estrutural.

Resultado:
- AUC reduzida (~0.70)
Importância das variáveis relacionadas a perfil dos clientes

---

# 7. Comparação via Simulação A/B

Foi realizada simulação histórica:

- Seleção do Top 20% com maior score
- Comparação da taxa de conversão
- Teste estatístico de diferença de proporções (Z-test)

A simulação indicou que se a estratégia for baseada no modelo1 (considera campanha e relacionamento) a taxa de conversão será maior.
Temos 32% de taxa de conversão para o modelo1 e 27% para o modelo3. Entendendo melhor:

- supondo que entramos em contato e 10.000 clientes fecharam
- supondo ticket médio de R$ 5.000
- Para o modelo1 temos: 10.000 x 32% = 3200 contratos fechados
- Para o modelo3 temos: 10.000 x 27% = 2700 contratos fechados
- diferença de 500 contratos adicionais

#  8. Proposta de Implementação Híbrida

Foi proposta uma estratégia híbrida:
- A estratégia baseada no modelo1 apresenta ganho estatisticamente significativo e economicamente relevante.
Lembrando que a estratégia baseada no modelo1 (campanha e relacionamento) busca maximizar a taxa de conversão a curto prazo. A abordagem do modelo3 (perfil de clientes) visa mudança estrutural, pensando em sustentabilidade e expansão a longo prazo

A recomendação seria uma avordagem híbrida,não é apenas otimizar a próxima campanha, mas estruturar uma estratégia sustentável ao longo do tempo. Sugestão de implementação:

- 1 Usar modelo1 (campanha) para clientes já trabalhados, ativos e remarketing
- 2 Usar modelo3 (perfil) para clientes sem histórico e aquisição de novos clientes

- A abordagem nos permite concentrar esforço nos clientes com maior probabilidade, aumentando eficiência da campanha sem necessariamente aumentar custo.
---

#  9. Dificuldades para Generalização

O modelo pode enfrentar desafios em novos datasets:

1. **Mudança de distribuição (Data Drift)**
2. **Alterações na estratégia comercial**
3. **Dependência de variáveis históricas**
4. **Sazonalidade não capturada adequadamente**
5. **Mudanças macroeconômicas**

Recomenda-se:

- Monitoramento contínuo
- Validação temporal
- Recalibração periódica



# Como Executar
1. Configure o arquivo config.py
2. Coloque o dataset em:
   `data/bank-full-case.csv`
2. Instale dependências:
   `pip install -r requirements.txt`
3. Execute:
   `python main.py`

#Autora

Aline Sousa  
Cientista de Dados
