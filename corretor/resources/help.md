
# Corretor ENA

Esse é um programa para corrigir automaticamente as provas do Exame Nacional de Acesso ao Profmat - ENA. Ele foi desenvolvido por Luis A. D'Afonseca, professor do CEFET-MG e ex coordenador local do Profmat.

## Usando o programa

Explicamos aqui os arquivos e informações necessárias para executar o programa em seguida apresentamos um passo a passo para realizar a correção automaticamente. Depois apresentamos alguns cuidados que devem ser tomados para evitar possíveis erros na correção. Por fim apresentamos os métodos e algoritmos implementados.

Para usar o Corretor do ENA é necessário:

1. O modelo da folha de respostas;
2. O gabarito;
3. Um arquivo `pdf` com as folhas de respostas de cada candidato escaneada;
4. Opcionalmente um arquivo `xlsx` com a lista nomes de todos os candidatos

O programa vai produzir:

1. Um arquivo `pdf` para conferência das correções realizadas;
2. Um arquivo `xlsx` com as notas de cada candidato.

O **modelo** é o arquivo `pdf` com a folha de respostas sem identificação de candidato. Esse arquivo é sempre distribuído pela SBM junto com os demais arquivos usados em cada ENA. Ele vai ser usado como base para alinhar as folhas de respostas antes de correção.

As **respostas** dos candidatos precisam ser escaneadas em um único arquivo PDF. Não faz diferença se elas forem escaneadas em cores ou tons de cinza, durante o processamento cada página é convertida resolução de 300pdis em tons de cinza. Por isso, o ideal é que o escaneamento seja em 300dpis. Especial atenção deve ser data a ordem das folhas de respostas, ela deve ser a mesma da lista de nome da planilha fornecida pela SBM. Cuidado para não deixar nenhuma página invertida ou de ponta cabeça.

Para facilitar a verificação da ordem das folhas de respostas é possível fornecer uma planilha `xlsx` com os **nomes dos candidatos**. Esses nomes serão escritos nas folhas de respostas acima do local onde os nomes vêm previamente impressos. Assim se alguma página não estiver na ordem correta os nomes não vão coincidir. O programa não tenta extrair os nomes do `pdf` escaneado. Dessa forma ele não tem como identificar automaticamente se houver alguma discrepância. Esses nomes serão também escritos na planilha final com as notas dos candidatos.

O **gabarito** pode ser digitado no campo correspondente ou usando o quadro de dialogo dedicado. Se uma questão for anulada marque-a com `X`. Os gabaritos de ENAs anteriores podem ser acessados pelo menu. Tentaremos disponibilizar novas versões para cada ENA assim que o gabarito correspondente seja divulgado. Também é possível salvar o gabarito em um arquivo usando o menu.

## Passo a passo para executar o programa

1. Escanear todas as folhas de respostas em um arquivo `pdf`

2. No Corretor, clicar o botão `Abrir` do campo "Arquivo PDF com o modelo da folha de respostas" e selecionar o `pdf` fornecido pela SBM com a folha de respostas sem identificação de candidato.

3. Entrar com o gabarito. Isso pode ser feito selecionando uma opção do menu `Gabaritos`; digitando as respostas no campo correspondente ou clicando no botão `Editar` para abir um editor dedicado.

4. Esse passo é opcional mas altamente recomendado. No campo "Arquivo XLSX com a lista de nomes dos candidatos" clique no botão `Abrir` e selecione a planilha que contém os nomes dos candidatos. Essa planilha é fornecida pela SBM. Se a lista de nomes dos candidatos não começar na célula `A2` digite o endereço da célula no campo correspondente. Para conferir a leitura dos nomes clique no botão `Ver`, o programa vai exibir um quadro de dialogo com no três primeiros e três últimos nomes da lista.

5. No campo "Arquivo XLSX onde serão salvas as notas", clique no botão `Escolher` e escolha o arquivo onde as notas serão salvas. Se algum arquivo com o mesmo nome existir o programa vai substituí-lo pela nova verão.

6. No campo "Arquivo onde serão salvas as anotações da correção", clique no botão `Escolher` e escolha o arquivo onde serão salvas as folhas de respostas com as anotações das correções. Esse arquivo é fundamental para que seja possível conferir a correção realizada pelo programa.

7. Clique no botão `corrigir` e aguarde. Quando a correção terminar os arquivos serão salvos automaticamente e o programa pode ser fechado.

8. Verifique a correção de cada candidato conferindo o arquivo `pdf` gerado com as anotações.

## Cuidados

O resultado produzido pelo programa sempre deve ser verificado antes de divulgado. Existem situações onde os algoritmos usados podem não produzir o resultado esperado. A seguir listamos algumas situações onde podem ocorrer falhas. Note porém que essa lista não é exaustiva.

1. As folhas de respostas não estão na mesma ordem que os nomes dos candidatos na planinha original.
2. O candidato não marcou corretamente as respostas.
3. O programa não consegue alinhar alguma folha de respostas com o modelo. Isso pode acontecer por vários motivos:
    1. a página não foi adequadamente escaneada;
    2. a página está invertida ou muito fora do alinhamento;
    3. a página possui rasuras ou marcações não previstas;
    4. o escaneamento está muito escuro (causando sombras na página) ou
    5. muito claro (algumas partes não estão suficientemente visíveis).
