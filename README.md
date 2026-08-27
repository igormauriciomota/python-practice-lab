# Python Practice Lab

> Laboratório de estudos e prática deliberada em Python, organizado do fundamento à construção de soluções mais seguras, testáveis e bem estruturadas.

![Python](https://img.shields.io/badge/Python-3.13%2B-3776AB?style=flat-square&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/status-em%20desenvolvimento-F59E0B?style=flat-square)
![Learning](https://img.shields.io/badge/foco-prática%20deliberada-0F766E?style=flat-square)

## Sobre o projeto

O **Python Practice Lab** é meu repositório principal para estudar a linguagem Python, desenvolver lógica de programação e praticar a resolução de problemas.

O objetivo não é apenas acumular códigos prontos. Cada etapa deve ajudar a compreender:

- como interpretar um problema;
- como decompor uma tarefa em partes menores;
- como escolher estruturas de dados adequadas;
- como escrever funções claras e reutilizáveis;
- como validar entradas e tratar erros;
- como organizar, testar e melhorar o código;
- como transformar fundamentos em pequenos sistemas funcionais.

Este repositório será dedicado ao **núcleo da linguagem e às bases da engenharia de software com Python**. Flask, Django, APIs, Análise de Dados e Automação serão estudados em projetos separados.

## Objetivos de aprendizagem

- Consolidar os fundamentos da linguagem Python.
- Desenvolver lógica e autonomia para resolver problemas.
- Praticar coleções, funções, arquivos, módulos e orientação a objetos.
- Entender algoritmos, complexidade e estruturas de dados.
- Aprender SQL, SQLite, CRUD e organização em camadas.
- Escrever testes automatizados e depurar erros.
- Aplicar princípios básicos de autenticação e segurança.
- Criar uma base sólida para avançar posteriormente para frameworks e áreas especializadas.

## Estrutura do repositório

```text
python-practice-lab/
├── 00-study-guide/
├── 01-python-fundamentals/
├── 02-python-strings-practice/
├── 03-python-collections-practice/
│   ├── lists/
│   ├── tuples/
│   ├── sets/
│   ├── dictionaries/
│   └── comprehensions/
├── 04-python-conditionals-practice/
├── 05-python-loops-practice/
├── 06-python-functions-practice/
├── 07-python-exceptions-debugging/
├── 08-python-files-formats-practice/
│   ├── pathlib/
│   ├── txt/
│   ├── csv/
│   ├── json/
│   └── xml/
├── 09-python-modules-practice/
├── 10-python-packages-environments/
├── 11-python-oop-practice/
├── 12-python-advanced-practice/
├── 13-python-standard-library-practice/
├── 14-algorithms-complexity-practice/
├── 15-data-structures-practice/
│   ├── stacks/
│   ├── queues/
│   ├── linked-lists/
│   ├── trees/
│   └── graphs/
├── 16-python-testing-practice/
├── 17-sql-database-design-practice/
├── 18-sqlite-practice/
├── 19-crud-architecture-practice/
├── 20-python-auth-security-practice/
├── .gitignore
└── README.md
```

## O que estudar em cada etapa

| Pasta | Conteúdo principal | Resultado esperado |
|---|---|---|
| `00-study-guide` | Cronograma, anotações, checklists e referências | Acompanhar a evolução dos estudos |
| `01-python-fundamentals` | Variáveis, tipos, operadores, entrada, saída e conversões | Criar programas simples e compreender a execução sequencial |
| `02-python-strings-practice` | Indexação, fatiamento, métodos, formatação e validação | Manipular e normalizar textos com segurança |
| `03-python-collections-practice` | Listas, tuplas, conjuntos, dicionários e comprehensions | Organizar, buscar e transformar conjuntos de dados |
| `04-python-conditionals-practice` | `if`, `elif`, `else`, operadores lógicos e decisões aninhadas | Traduzir regras de negócio em decisões claras |
| `05-python-loops-practice` | `for`, `while`, `range`, `break`, `continue` e iteração | Automatizar tarefas repetitivas sem duplicar código |
| `06-python-functions-practice` | Parâmetros, retorno, escopo, documentação e decomposição | Dividir problemas em funções pequenas e reutilizáveis |
| `07-python-exceptions-debugging` | Exceções, `try`, `except`, `else`, `finally`, `raise` e depuração | Antecipar falhas e diagnosticar erros com método |
| `08-python-files-formats-practice` | `pathlib`, TXT, CSV, JSON e XML | Ler, validar, transformar e gravar arquivos |
| `09-python-modules-practice` | Imports, módulos próprios, `__name__` e separação de responsabilidades | Organizar programas em vários arquivos |
| `10-python-packages-environments` | Pacotes, `venv`, `pip`, dependências e estrutura de projeto | Criar ambientes isolados e projetos reproduzíveis |
| `11-python-oop-practice` | Classes, objetos, encapsulamento, herança, composição e polimorfismo | Modelar entidades e comportamentos do mundo real |
| `12-python-advanced-practice` | Iteradores, geradores, decorators, context managers e tipagem | Utilizar recursos avançados com propósito e clareza |
| `13-python-standard-library-practice` | `datetime`, `decimal`, `collections`, `itertools`, `functools`, `re` e outras bibliotecas | Resolver problemas utilizando recursos nativos do Python |
| `14-algorithms-complexity-practice` | Busca, ordenação, recursão e notação Big O | Comparar soluções e avaliar custo de tempo e memória |
| `15-data-structures-practice` | Pilhas, filas, listas ligadas, árvores e grafos | Implementar e aplicar estruturas de dados clássicas |
| `16-python-testing-practice` | Testes unitários, `pytest`, fixtures, parametrização e mocks | Proteger regras de negócio contra regressões |
| `17-sql-database-design-practice` | Modelagem, normalização, DDL, DML, consultas, joins e índices | Projetar bancos relacionais consistentes |
| `18-sqlite-practice` | Conexão com Python, transações, parâmetros e persistência | Integrar programas Python a um banco SQLite |
| `19-crud-architecture-practice` | Create, Read, Update, Delete, camadas e separação de responsabilidades | Construir CRUDs organizados e testáveis |
| `20-python-auth-security-practice` | Hash de senhas, validação, permissões e práticas seguras | Compreender a base da autenticação sem criar segurança improvisada |

## Progressão recomendada

O estudo será dividido em cinco fases. A numeração das pastas representa uma sequência recomendada, mas cada etapa pode ser revisitada quando necessário.

### Fase 1 — Fundamentos e lógica

Pastas `01` a `06`.

Ao concluir esta fase, devo ser capaz de receber dados, validar informações, tomar decisões, repetir processos e decompor problemas em funções.

### Fase 2 — Organização e domínio da linguagem

Pastas `07` a `13`.

Nesta fase, o foco passa a ser tratamento de erros, arquivos, modularização, ambientes, orientação a objetos e recursos importantes da linguagem.

### Fase 3 — Pensamento computacional

Pastas `14` e `15`.

O objetivo é compreender por que uma solução funciona, quanto ela custa e quais estruturas são mais adequadas para cada problema.

### Fase 4 — Qualidade e persistência

Pastas `16` a `18`.

Esta fase reúne testes, modelagem de bancos de dados, SQL e integração do Python com SQLite.

### Fase 5 — Arquitetura e segurança

Pastas `19` e `20`.

Aqui os conhecimentos anteriores serão integrados em aplicações CRUD organizadas, com validação, autenticação e controle básico de permissões.

## Como praticar

Cada assunto deve seguir um ciclo simples de aprendizagem:

1. **Compreender:** estudar a teoria e escrever pequenas anotações com minhas próprias palavras.
2. **Observar:** analisar exemplos e explicar o papel de cada parte do código.
3. **Reproduzir:** digitar o exemplo sem copiar e colar.
4. **Modificar:** alterar regras, entradas, saídas e casos de teste.
5. **Resolver:** implementar um exercício sem consultar a solução.
6. **Testar:** experimentar dados válidos, inválidos e casos extremos.
7. **Refatorar:** melhorar nomes, funções, validações e organização.
8. **Registrar:** documentar o que aprendi, as dificuldades e a solução encontrada.

> Um exercício só está realmente concluído quando consigo explicar sua lógica, testar casos diferentes e reconstruí-lo sem depender da resposta pronta.

## Padrão recomendado para os exercícios

Os arquivos devem utilizar nomes descritivos em inglês e o conteúdo pode ser escrito em português do Brasil.

```text
06-python-functions-practice/
├── README.md
├── 01-basic/
│   ├── 01-age-validator.py
│   └── 02-salary-calculator.py
├── 02-intermediate/
│   ├── 01-student-grade-summary.py
│   └── 02-customer-search.py
├── 03-advanced/
│   └── 01-order-processor.py
└── tests/
    └── test_order_processor.py
```

Sugestão de níveis:

- `01-basic`: fixação da sintaxe e de um conceito por vez;
- `02-intermediate`: combinação de conceitos e validações;
- `03-advanced`: decomposição, arquivos, testes e regras mais complexas;
- `04-challenges`: problemas sem solução inicial;
- `05-mini-projects`: integração dos conhecimentos da matéria.

## Padrões de código

- Utilizar nomes claros para variáveis, funções, classes e arquivos.
- Manter cada função responsável por uma tarefa principal.
- Evitar repetição de código.
- Separar entrada, processamento e saída sempre que possível.
- Validar os dados nas fronteiras do programa.
- Não esconder erros com blocos `except` genéricos.
- Utilizar docstrings quando a intenção da função não for evidente.
- Aplicar formatação compatível com a PEP 8.
- Criar testes para regras importantes e casos extremos.
- Nunca armazenar senhas em texto puro nem publicar dados secretos.

## Convenção para commits

Exemplos de mensagens simples e objetivas:

```text
study: add notes about dictionaries
exercise: solve customer search challenge
test: add tests for age validator
refactor: simplify order total calculation
fix: handle invalid CSV rows
docs: update study progress
```

## Projetos mantidos separadamente

Os assuntos abaixo não farão parte deste repositório principal. Cada área terá espaço próprio para que seus projetos, dependências e arquiteturas não se misturem.

| Projeto separado | Finalidade |
|---|---|
| `flask-practice-lab` | Flask, Jinja, formulários, autenticação, CRUD e projetos web |
| `django-practice-lab` | Django, apps, ORM, templates, admin, autenticação e projetos web |
| `api-practice-lab` | APIs REST, HTTP, JSON, Flask API, FastAPI, testes e documentação |
| `data-analysis-practice-lab` | NumPy, Pandas, visualização, estatística e projetos de análise |
| `automation-practice-lab` | Automação de arquivos, planilhas, navegadores, e-mails e rotinas |

A organização geral dos estudos poderá ficar assim:

```text
python-studies/
├── python-practice-lab/
├── flask-practice-lab/
├── django-practice-lab/
├── api-practice-lab/
├── data-analysis-practice-lab/
└── automation-practice-lab/
```

Essa separação permite que cada projeto tenha seu próprio `README.md`, ambiente virtual, dependências, exercícios, testes e projetos finais.

## O que não deve ser versionado

O arquivo `.gitignore` deve impedir o envio de ambientes virtuais, caches, arquivos locais de configuração, bancos temporários e segredos.

```gitignore
.venv/
venv/
__pycache__/
*.py[cod]
.pytest_cache/
.coverage
htmlcov/
.env
.env.*
!.env.example
*.db
*.sqlite3
.vscode/
.idea/
```

> Bancos usados como exemplos didáticos podem ser versionados somente quando não contiverem informações reais ou sensíveis.

## Checklist de evolução

### Fundamentos

- [ ] Compreendo variáveis, tipos e operadores.
- [ ] Consigo manipular strings sem depender de exemplos prontos.
- [ ] Sei escolher entre lista, tupla, conjunto e dicionário.
- [ ] Consigo construir decisões com condições claras.
- [ ] Sei utilizar `for` e `while` de forma consciente.
- [ ] Consigo decompor um problema em funções pequenas.

### Python aplicado

- [ ] Sei tratar exceções específicas e investigar erros.
- [ ] Consigo ler e gravar TXT, CSV, JSON e XML.
- [ ] Sei manipular caminhos com `pathlib`.
- [ ] Consigo dividir um programa em módulos e pacotes.
- [ ] Sei criar e reproduzir um ambiente virtual.
- [ ] Compreendo classes, objetos, composição e herança.

### Engenharia e dados

- [ ] Consigo analisar a complexidade básica de uma solução.
- [ ] Sei quando utilizar pilha, fila, árvore ou grafo.
- [ ] Escrevo testes automatizados para regras importantes.
- [ ] Consigo modelar tabelas e relacionamentos.
- [ ] Sei utilizar SQL e SQLite com consultas parametrizadas.
- [ ] Consigo criar um CRUD organizado em camadas.
- [ ] Compreendo hash de senha, autenticação e autorização.

## Critério para avançar

Antes de seguir para a próxima matéria, devo conseguir:

- explicar o conteúdo sem apenas repetir definições;
- resolver exercícios básicos e intermediários sem consultar a solução;
- identificar e corrigir erros comuns;
- testar entradas normais, inválidas e extremas;
- concluir pelo menos um desafio ou mini projeto da etapa;
- registrar no `00-study-guide` o que aprendi e o que precisa de revisão.

## Projetos de consolidação sugeridos

Ao longo do repositório, os fundamentos poderão ser consolidados em projetos progressivos:

1. Calculadora e validador de dados no terminal.
2. Cadastro de clientes utilizando listas e dicionários.
3. Gerenciador de tarefas com persistência em JSON.
4. Importador e validador de arquivos CSV e XML.
5. Sistema orientado a objetos para pedidos e produtos.
6. CRUD de clientes, fornecedores e pedidos com SQLite.
7. CRUD em camadas, com testes, autenticação e permissões.

## Meta principal

Evoluir de alguém que conhece a sintaxe para alguém que consegue analisar um problema, planejar uma solução, implementá-la, testá-la e explicar as decisões tomadas.

```text
SINTAXE → LÓGICA → ESTRUTURA → ARQUITETURA → ENGENHARIA
```

---

Desenvolvido como parte da trilha de estudos de **Igor Mota** em Python, desenvolvimento de sistemas e análise de dados.
