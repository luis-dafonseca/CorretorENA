
# Corretor ENA

### TODO

#### Novas funcionalidades

- Reverter o estado do pdf e xls no cancelamento da correção
- Testar o uso de arquivos de planinha diferentes do xlsx

- Configurações
  - Incluir parâmetros do ajuste da imagem e da verificação de marcações no ENAParam
  - Tornar a classe Rects ciente do DPI
  - Criar arquivo de configurações
  - Criar quadro de diálogo de configurações
  - Implementar parsing de parâmetros nos programas de linha de comando

#### Testes de consistência

- Perguntar que o usuário deseja abandonar o gabarito atual ao abrir um novo

#### Refinamentos

- Mudar o texto dos botões dos diálogos de escolha de "Salvar" para "Escolher"
- Incluir opções para abrir os arquivos no menu da janela principal

- Documentação e exemplos
  - Escanear algumas folhas de respostas com o celular para criar exemplos problemáticos
    - Sombras
    - Folha torta
    - Baixa resolução
  - Documentar que usar o celular para escanear não é uma boa ideia
  - Remover exemplos do git
  - Arte final no ícone

- Renomear o ena_param para algo como configuration

#### Windows

- Implementar o tema escuro
- Verficar Microsoft Version Information Structures https://pyinstaller.org/en/stable/usage.html

### In progress...


### DONE

2022-12-08
- Garantir que exite pelo menos uma página de respostas e um nome na planilha de candidatos
- Testar se a quantidade de nomes é igual a quantidade de páginas de respostas
- Show Names: Tratar o caso em que existem menos do que 6 ou 7 candidatos

2022-12-06
- Redesenhar o ícone
- Colocar as informações de autor, links, versão em um único arquivo
- Escrever script para "compilar" o programa
- Documentação e exemplos
  - Escrever a Documentação
  - Separar documentação do help
- Completar as informações do sobre
  - versão
  - nome do autor
  - endereço download e código - git
  - licença
  - ícones
- Escrever o help
- Criar recursos com:
  - ícones
- Substituir a barra de progresso na barra de status por um quadro de diálogo.
  - Criar botão cancel
  - Reverter o estado do pdf e xls no cancelamento
- Windows
  - Descobrir porque a GUI é horrível
  - Melhorar a aparência do fundos azul e vermelho para os botões
- Criar o help e o about
- Não permitir abrir duas janelas de visualização
- Exibição dos pdf - Permitir ampliar e reduzir
- Eliminar o arquivo temporário da conversão do pixmap
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

### GAVE UP

- Escrever o número total de provas, de ausentes e eliminados no quadro de finalização da correção
- ProgressDialog
  - Incluir tempo faltante estimado
- Usar OCR para ler os nomes dos candidatos nas folhas de respostas e comparar com os nomes fornecidos
- Exibição dos pdf - Permitir salvar
- Permitir salvar o pdf do modelo com as respostas do gabarito

