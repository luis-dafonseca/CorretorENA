
# Corretor ENA

### TODO

#### Novas funcionalidades

- Permitir salvar o pdf do modelo com as respostas do gabarito
- Exibição dos pdf
  - Permitir salvar
  - Permitir ampliar e reduzir
- Eliminar o arquivo temporário da conversão do pixmap
- Criar o help e o about

#### Testes de consistência

- Show Names: Tratar o caso em que existem menos do que 6 ou 7 candidatos
- Testar se a quantidade de nomes é igual a quantidade de páginas de respostas
- Perguntar que o usuário deseja abandonar o gabarito atual ao abrir um arquivo

#### Refinamentos

- Mudar o texto dos botões dos diálogos de escolha de "Salvar" para "Escolher"
- Não permitir abrir duas janelas de visualização
- Menu da janela principal
  - Incluir opções para abrir os arquivos no menu
- Criar um quadro de dialogo para o progress bar com a opção de cancelar a correção
- Escrever o número total de provas, de ausentes e eliminados no quadro de finalização da correção

#### Windows

- Descobrir porque a GUI é horrível
- Implementar o tema escuro
- Melhorar a aparência do fundos azul e vermelho para os botões

### In progress...

### DONE

- Open model: Testar se o arquivo pdf tem mais do que uma página
- Garantir que ao abrir um arquivo de gabarito ele contenha um gabarito
- Permitir salvar gabaritos
- Menu da janela principal
  - Colocar os gabaritos dos enas anteriores
- Dialogo que exibe os nomes
  - Alinhas números a direita
  - Aumentar o espaço dos números
  - Aumentar o espaço da célula
  - Usar os botões padrão
  - Tornar o dialogo modal
  - Usar a descrição como título
- First Name: Testar se o texto do lineedite é um endereço de uma célula
- Criar mascara para o first_name
- Colocar o _DPI e _COLORSPACE e um único arquivo
- Escrever o status de cada candidato na planinha com as notas
- Tratar corretamente os ausentes e desclassificados
- Implementar a entrada do gabarito
  - Criar o quadro de dialogo para preencher as respostas
  - Testar se a string digitada é um gabarito
  - Exibir o modelo com as respostas do gabarito

### GIVE UP

- Usar OCR para ler os nomes dos candidatos nas folhas de respostas e comparar com os nomes fornecidos
