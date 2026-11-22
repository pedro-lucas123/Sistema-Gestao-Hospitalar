
# Sistema de Gestão Hospitalar

## 1. Descrição do Projeto

Este projeto consiste no desenvolvimento de um Sistema de Gestão Hospitalar utilizando a linguagem Python e as quatro estruturas fundamentais de dados estudadas na disciplina: Lista, Pilha, Fila e Árvore.

O sistema funciona por meio de um menu interativo no terminal e permite gerenciar pacientes internados, organizar a fila de triagem, controlar o histórico de prontuários e estruturar especialidades médicas e diagnósticos.

Os dados podem ser salvos e recuperados por meio de um arquivo de texto chamado `dados_sistema.txt`.

## 2. Tecnologias Utilizadas

- Python 3
- Biblioteca nativa collections
- Estruturas list e deque
- Dicionários aninhados
- Manipulação de arquivos TXT

Não são utilizados bancos de dados, JSON, CSV ou pickle.

## 3. Estruturas de Dados Utilizadas

### Lista

A lista é utilizada para armazenar os pacientes atualmente internados.

Cada paciente possui:
- ID
- Nome
- Leito
- Estado clínico

A escolha da lista ocorre porque ela permite armazenar vários registros de forma dinâmica, acessar elementos por índice e realizar operações de inserção, consulta, atualização e remoção.

### Fila

A fila é utilizada para organizar os pacientes que aguardam atendimento na triagem.

Foi implementada utilizando `collections.deque`.

A fila segue a regra FIFO (First In, First Out), ou seja, o primeiro paciente que entra é o primeiro a ser atendido.

A inserção ocorre no final da fila, enquanto a remoção acontece no início.

### Pilha

A pilha é utilizada para armazenar o histórico de prontuários médicos acessados recentemente.

Foi implementada utilizando uma lista nativa do Python.

A pilha segue a regra LIFO (Last In, First Out), na qual o último elemento inserido é o primeiro a ser removido.

A inserção e a remoção acontecem pelo topo da pilha.

### Árvore

A árvore é utilizada para organizar hierarquicamente as especialidades médicas e seus diagnósticos.

Foi implementada por meio de dicionários aninhados do Python.

Cada chave representa uma especialidade ou diagnóstico, enquanto seu valor contém os elementos subordinados.

Essa estrutura permite inserir, consultar, listar, renomear e excluir caminhos hierárquicos.

## 4. Funcionalidades

O sistema oferece:

- Cadastro, consulta, atualização e exclusão de pacientes internados.
- Inserção, consulta, atualização e atendimento de pacientes na fila.
- Inserção, consulta, atualização e remoção de prontuários na pilha.
- Inserção, consulta, renomeação e exclusão de elementos na árvore.
- Salvamento dos dados em arquivo TXT.
- Carregamento dos dados do arquivo TXT.

## 5. Persistência dos Dados

A persistência é realizada no arquivo `dados_sistema.txt`.

Cada linha começa com um identificador da estrutura correspondente:

- LISTA
- FILA
- PILHA
- ARVORE

Os campos são separados pelo caractere `|`.

Exemplos:

```text
LISTA|101|Carlos Silva|Leito 04|Estavel
FILA|205|Roberto Alves|Prioridade Alta
PILHA|PRONT-889|Paciente 101|Consulta Cardiologia
ARVORE|Clinica Geral|Cardiologia|Arritmia
```

O sistema preserva a ordem dos registros da fila e da pilha durante o salvamento e o carregamento.

## 6. Como Executar

1. Instale o Python 3 no computador.
2. Salve o código-fonte no arquivo `main.py`.
3. Abra o terminal na pasta onde o arquivo foi salvo.
4. Execute o comando:

```bash
python main.py
```

No Windows, também pode ser utilizado:

```bash
py main.py
```

5. Utilize as opções numéricas do menu para acessar as funcionalidades.

## 7. Salvamento e Carregamento

Para salvar os dados, selecione a opção 5 no menu principal.

Para recuperar os dados salvos anteriormente, selecione a opção 6.

O arquivo `dados_sistema.txt` será criado automaticamente na pasta de execução do programa quando os dados forem salvos pela primeira vez.

## 8. Considerações Finais

O projeto demonstra a aplicação prática das estruturas fundamentais de dados em um cenário de gestão hospitalar.

A utilização de Lista, Pilha, Fila e Árvore permite organizar diferentes tipos de informações de acordo com suas necessidades operacionais.

A persistência em arquivo TXT garante que os dados possam ser recuperados após o encerramento do programa.
