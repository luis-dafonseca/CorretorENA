
# CorretorENA

# Usando o programa

Para usar o CorretorENA é necessário ter em mãos:

1. o arquivo PDF com o modelo da folha de respostas;
2. o arquivo PDF com as folhas de respostas de cada candidato escaneada;
3. \[Opcional\] o arquivo XLSX com a lista nomes de todos os candidatos e
4. o gabarito.

O programa vai produzir:

1. um arquivo PDF para conferência das correções realizadas;
2. um arquivo XLSX com as notas de cada candidato.

O **modelo** é o arquivo PDF com a folha de respostas sem identificação de
candidato. Esse arquivo é sempre distribuído pela SBM junto com os demais
arquivos usados em cada ENA. Ele vai ser usado como base para alinhar as folhas
de respostas antes de correção.

As **respostas** dos candidatos precisam ser escaneadas em um único arquivo PDF.
Não faz diferença se elas forem escaneadas em cores ou tons de cinza, durante o
processamento cada página é convertida para a resolução de 300 dpi em tons de
cinza. Por isso, o ideal é que o escaneamento seja em 300 dpi.  Especial atenção
deve ser data a ordem das folhas de respostas, ela deve ser a mesma da lista de
nome da planilha fornecida pela SBM.  Cuidado para não deixar nenhuma página
invertida.

Especial atenção dever ser dedicada ao processo de escanear as folhas
de respostas. Se as imagens produzidas não forem de boa qualidade
e com o devido contraste entre o fundo e as marcações
o programa não será capaz de identificar as marcações corretamente.
A recomendação usar sempre a opção _documento_ comumente disponível
nos scanners.

Para facilitar a verificação da ordem das folhas de respostas é possível
fornecer uma planilha XLSX com os **nomes dos candidatos**.  Esses nomes serão
escritos nas folhas de respostas acima do local onde os nomes vêm previamente
impressos. Assim se alguma página não estiver na ordem correta os nomes não vão
coincidir. O programa não tenta extrair os nomes do PDF escaneado. Dessa forma
ele não tem como identificar automaticamente se houver alguma discrepância.
Esses nomes serão também escritos na planilha final com as notas dos candidatos.

O **gabarito** pode ser digitado no campo correspondente ou usando o quadro de
dialogo dedicado. Se uma questão for anulada marque-a com X.  Os gabaritos de
ENAs anteriores podem ser acessados pelo menu. Também é possível ler
o gabarito de um arquivo tipo texto.


### Passo a passo para executar o programa

1. Escanear todas as folhas de respostas em um arquivo PDF.

2. No CorretorENA, clicar o botão `Abrir` do campo "Arquivo PDF com o modelo da
folha de respostas" e selecionar o PDF fornecido pela SBM com a folha de
respostas sem identificação de candidato.

3. Entrar com o gabarito. Isso pode ser feito selecionando uma opção do menu
`Gabaritos`; digitando as respostas no campo correspondente ou clicando no botão
`Editar` para abir um editor dedicado.  O programa oferece a opção de mudar o
número mínimo de acertos para a aprovação do candidato, mas essa opção não
precisa ser usada na correção das provas do ENA.

4. Esse passo é opcional mas altamente recomendado. No campo "Arquivo XLSX com a
lista de nomes dos candidatos" clique no botão `Abrir` e selecione a planilha
que contém os nomes dos candidatos. Essa planilha é fornecida pela SBM.  Se a
lista de nomes dos candidatos não começar na célula `A2` digite o endereço da
célula no campo correspondente. Para conferir a leitura dos nomes clique no
botão `Ver`, o programa vai exibir um quadro de dialogo com no três primeiros e
três últimos nomes da lista.

5. No campo "Arquivo XLSX onde serão salvas as notas", clique no botão
`Escolher` e escolha o arquivo onde as notas serão salvas. Se algum arquivo com
o mesmo nome existir o programa vai substituí-lo pela nova verão.

6. No campo "Arquivo onde serão salvas as anotações da correção", clique no
botão `Escolher` e escolha o arquivo onde serão salvas as folhas de respostas
com as anotações das correções. Esse arquivo é fundamental para que seja
possível conferir a correção realizada pelo programa.

7. Clique no botão `Corrigir` e aguarde. Quando a correção terminar os arquivos
serão salvos automaticamente e o programa pode ser fechado.

8. Verifique a correção de cada candidato conferindo o arquivo PDF gerado com
as anotações.

### Cuidados

O resultado produzido pelo programa sempre deve ser verificado antes de
divulgado.  Existem situações onde os algoritmos usados podem não produzir o
resultado esperado.  A seguir listamos algumas situações que podem gerar
falhas.  Note que esta lista não é exaustiva.

1. As folhas de respostas não estão na mesma ordem que os nomes dos candidatos
na planinha original.
2. O candidato não marcou corretamente as respostas.
3. O programa não consegue alinhar alguma folha de respostas com o modelo.
Isso pode acontecer por vários motivos:
    1. a página não foi adequadamente escaneada;
    2. a página está invertida ou muito fora do alinhamento;
    3. a página possui rasuras ou marcações não previstas;
    4. o escaneamento está muito escuro (causando sombras na página) ou
    5. muito claro (algumas partes não estão suficientemente visíveis).

### Usando o programa para corrigir outras provas

Desde que a folha de respostas seja equivalente o programa pode ser
usado para corrigir as respostas de qualquer prova.

Para garantir a equivalência é necessário que a parte da página que
contém as respostas seja idêntica a do ENA. Não basta que os retângulos
com as marcações estejam no mesmo lugar, é necessário que os números
e outros elementos sejam idênticos. Porém, na parte superior da folha
basta que os retângulos que indicam ausência ou eliminação estejam no mesmo
lugar.

## Como o programa corrige as provas

Para corrigir as provas o programa precisa identificar quais foram as respostas
marcadas por cada candidato. Para isso foram implementados os seguintes passos.

O programa usa a biblioteca [PyMuPDF](https://pymupdf.readthedocs.io/) para ler
os arquivos PDF com o modelo e com as respostas dos candidatos. Depois converte
cada página para uma imagem com 300 dpi. Essa biblioteca também é usada para
criar as marcações no PDF de anotações que é usado para conferir a correção
gerada pelo programa.

Como, no escaneamento, as páginas nunca são perfeitamente alinhadas, os campos das
respostas não coincidem exatamente. Para resolver esse problema o programa
alinha cada página com o modelo antes de iniciar a busca pelas marcações. Isso é
realizado por um algoritmo de _registration_ implementado na biblioteca de visão
computacional [OpenCV](https://opencv.org/). Uma descrição do algoritmo pode ser
encontrado nesta
[página](https://pyimagesearch.com/2020/08/31/image-alignment-and-registration-with-opencv/).

Assim que a imagem da página com as respostas foi alinhada com o modelo, ela é
convertida para um `array` numérico da biblioteca [NumPy](https://numpy.org/).
Nessa etapa o programa conta o número de _pixels_ de cor diferente de branco nos
retângulos correspondentes a cada marcação. O algoritmo não tem como distinguir
marcações intencionais de rabiscos, sombras ou a própria moldura que indica onde
o candidato deve marcar sua resposta. Todo _pixel_ não branco é contado. Se o
número de _pixels_ não brancos dento do retângulo ultrapassar o limiar a entrada
é considerada marcada. O programa não analisa marcações fora dos retângulos
predeterminados, isso é, o programa não vai identificar se algo foi escrito
indevidamente fora dos retângulos. Para ver os retângulos que o programa usa
como referência basta clicar no botão `Ver` após carregar o modelo.

Tendo identificado quais entradas foram marcadas pelo candidato a etapa final é
simplesmente verificar se existem mais do que uma marcação por questão e se a
resposta coincide com o gabarito.

A nota de cada candidato é salva em um arquivo XLSX. Esse arquivo também
registra se ele foi eliminado ou foi ausente. Um PDF com marcações indicando
a correção gerada pelo
programa também é gerado. Esse arquivo é fundamental para que seja possível
conferir com facilidade a correção realizada e identificar possíveis erros.

O arquivo XLSX fornecido com os nomes dos candidatos é usado apenas para
escrever o nome de cada candidato junto com o nome originalmente impresso na
folha de questões. Isso é importante para que seja possível conferir que nas
páginas estão na mesma ordem que os nomes da planilha.