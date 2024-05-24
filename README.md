
# Compressão de Texto com Codificação de Huffman

## Índice
- [Introdução](#introdução)
- [Codificação de Huffman](#codificação-de-huffman)
  - [Frequência dos Caracteres](#frequência-dos-caracteres)
  - [Construção da Árvore de Huffman](#construção-da-árvore-de-huffman)
  - [Geração do Livro de Códigos](#geração-do-livro-de-códigos)
  - [Codificação do Texto](#codificação-do-texto)
  - [Decodificação do Texto](#decodificação-do-texto)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Uso](#uso)
- [Exemplos](#exemplos)
- [Conclusão](#conclusão)

## Introdução
Este projeto implementa um programa para simular a compactação e descompactação de arquivos de texto usando a Codificação de Huffman. A Codificação de Huffman é um método eficiente de compressão de dados que usa códigos de comprimento variável para representar caracteres com base em suas frequências. Este projeto inclui as seguintes funcionalidades:
- Leitura de um arquivo de texto e cálculo das frequências dos caracteres
- Construção de uma Árvore de Huffman a partir das frequências dos caracteres
- Geração de um livro de códigos a partir da Árvore de Huffman
- Codificação de um arquivo de texto em um formato compactado
- Decodificação de um arquivo compactado de volta para o texto original

## Codificação de Huffman
A Codificação de Huffman é um algoritmo popular usado para compressão de dados sem perda. A ideia básica é atribuir códigos de comprimento variável aos caracteres de entrada, com códigos mais curtos atribuídos aos caracteres mais frequentes. Isso resulta em uma representação compactada dos dados de entrada.

### Frequência dos Caracteres
O primeiro passo na Codificação de Huffman é calcular a frequência de cada caractere no texto de entrada. Essas frequências são usadas para construir a Árvore de Huffman.

### Construção da Árvore de Huffman
A Árvore de Huffman é uma árvore binária construída de baixo para cima a partir das frequências dos caracteres. Os caracteres com menores frequências são colocados nas folhas mais profundas da árvore, enquanto os caracteres mais frequentes ficam mais próximos da raiz.

### Geração do Livro de Códigos
Após construir a Árvore de Huffman, geramos o livro de códigos, que mapeia cada caractere para seu código binário correspondente baseado no percurso da árvore.

### Codificação do Texto
Utilizando o livro de códigos, o texto de entrada é convertido em uma sequência de pseudo-bits (0s e 1s) que representam a versão compactada do texto.

### Decodificação do Texto
Para descompactar o texto, a sequência de pseudo-bits é convertida de volta para o texto original percorrendo a Árvore de Huffman.

## Estrutura do Projeto
- `huffman.py`: Contém a implementação dos métodos de compressão e descompressão usando Codificação de Huffman.
- `input.txt`: Arquivo de texto de entrada que será compactado.
- `encoded.txt`: Arquivo de texto gerado após a compactação (sequência de pseudo-bits).
- `decoded.txt`: Arquivo de texto gerado após a descompactação (texto original).

## Uso
1. Coloque o texto que deseja compactar no arquivo `input.txt`.
2. Execute o programa `huffman_compression.py`.
3. O programa irá gerar os arquivos `encoded.txt` (texto compactado) e `decoded.txt` (texto original descompactado).

### Comandos
```sh
python huffman.py
```

## Exemplos
### Frequência dos Caracteres
```
========================================
Character Frequencies
========================================
'e': 15
' ': 12
't': 9
'o': 8
...
========================================
```

### Árvore de Huffman
```
========================================
Huffman Tree:
[43]
    [18]
        [8]
            [4]
                ['e': 2]
                ['x': 2]
            ['a': 4]
        [10]
            [' ': 5]
            ['s': 5]
    [25]
        ...
========================================
```

### Livro de Códigos
```
========================================
Codebook:
'e': 1100
' ': 101
't': 100
'o': 1110
...
========================================
```

### Texto Codificado
```
========================================
Encoded Text:
101100111010001100101011...
========================================
```

### Texto Decodificado
```
========================================
Decoded Text:
Este é um exemplo de texto...
========================================
```

## Conclusão
Este projeto demonstra como a Codificação de Huffman pode ser usada para compactar e descompactar arquivos de texto de forma eficiente. A implementação inclui todas as etapas necessárias para calcular as frequências dos caracteres, construir a árvore de Huffman, gerar o livro de códigos, e realizar a codificação e decodificação do texto.

