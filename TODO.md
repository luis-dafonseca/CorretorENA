
# Corretor ENA

### TODO

#### Novas funcionalidades

- Tratar corretamente os ausentes e desclassificados
- Escrever o status de cada candidato na planinha com as notas
- Permitir salvar o pdf do modelo com as respostas do gabarito
- Exibição dos pdf
  - Permitir salvar
  - Permitir ampliar e reduzir
- Eliminar o arquivo temporário da conversão do pixmap
- Criar o help e o about
- Colocar o _DPI e _COLORSPACE e um único arquivo

#### Testes de consistência

- Show Names: Tratar o caso em que existem menos do que 6 ou 7 candidatos
- Open model: Testar se o arquivo pdf tem mais do que uma página
- First Name: Testar se o texto do lineedite é um endereço de uma célula
- Testar se a quantidade de nomes é igual a quantidade de páginas de respostas

#### Refinamentos

- Mudar o texto dos botões dos diálogos de escolha de "Salvar" para "Escolher"
- Criar mascara para o first_name
- Não permitir abrir duas janelas de visualização
- Dialogo que exibe os nomes
  - Alinhas números a direira
  - Aumentar o espaço dos números
  - Aumentar o espaço da célula
  - Usar os botões padrão
  - Tornar o dialogo modal
  - Usar a descrição como título
- Menu da janela principal
  - Incluir opções para abrir os arquivos no menu
  - Colocar os gabaritos dos enas anteriores

### In progress...

### DONE

### GIVE UP

- Usar OCR para ler os nomes dos candidatos nas folhas de respostas e comparar com os nomes fornecidos
- Implementar a entrada do gabarito
  - Criar o quadro de dialogo para preencher as respostas
  - Testar se a string digitada é um gabarito
  - Exibir o modelo com as respostas do gabarito
