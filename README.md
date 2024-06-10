# Multi-threading and Multi-processing Challenge

Este repositório contém um template para aprender e implementar multi-threading e multi-processing em Python.

## Estrutura do Repositório

- `threading_example.py`: Exemplo básico de uso de multi-threading.
- `multiprocessing_example.py`: Exemplo básico de uso de multi-processing.
- `main.py`: Arquivo principal para executar os exemplos.

# Desafio

O desafio consiste em identificar alguma tarefa que você desenvolveu em um projeto atual/antigo e validar se a aplicação de multithreading/processing poderia tornar o processo mais rápido. 
Essa tarefa pode envolver:

- Processamento paralelo de grandes volumes de dados: automatizar aquela função que sempre é o gargalo no pipeline de manipulação da sua base de dados.
- Requests em APIs: requests podem tomar muito tempo se feitos em larga escala e/ou se eles retornam grandes volumes. Validar se utilizar multiprocessamento poderia tornar o processo mais eficiente sem perder a qualidade das informações retornadas.
- Treinamento paralelo de modelos: fazer o treinamento de modelos em paralelo.
- Processamento de imagens: muitos projetos de Visão computacional possuem etapas de pré-processamento de imagens. Validar se conseguimos processar grandes volumes de imagens, garantindo que todas passem pelas mesmas etapas.
- Embedding para RAG: dividir o dataset em batches e fazer o embedding de cada batch de forma paralela e simultânea.
