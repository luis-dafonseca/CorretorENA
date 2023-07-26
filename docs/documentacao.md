
# CorretorENA

![logo](./images/CorretorENA_icon.png "CorretorENA")

Esse é um programa para corrigir automaticamente as provas do Exame Nacional de
Acesso ao Profmat - ENA.  Ele foi desenvolvido por Luis A. D'Afonseca, professor
do CEFET-MG e ex-coordenador local do Profmat.

Este documento descreve como instalar e usar o programa.  No final existe uma
explicação sucinta sobre como o programa realiza a correção das provas.

--------------------------------------------------------------------------------
## Licença e Ausência Garantia

Esse programa é distribuído sob a Licença Pública Geral GNU seu código pode ser
obtido no [repositório GitHub do
projeto](https://github.com/luis-dafonseca/CorretorENA).  Você tem direito a
usar o programa sem nenhum custo assim como distribui-lo e alterá-lo.  A Licença
Pública Geral GNU pode ser encontrada
[aqui](https://www.gnu.org/licenses/gpl-3.0.html), uma tradução para o português
pode ser lida [aqui](http://licencas.softwarelivre.org/gpl-3.0.pt-br.html).
Ambos os textos podem ser encontrados também junto ao código do programa.  Note
que o programa é oferecido "como está" de acordo com o seguinte trecho extraído
da Licença.

> _Não há nenhuma garantia para o programa, na extensão permitida pela lei
aplicável.  Exceto quando indicado por escrito, os detentores de direitos
autorais e/ou outras partes fornecem o programa "como está" sem garantia de
qualquer tipo, expressa ou implícita, incluindo, mas não se limitando a,
garantias implícitas de comercialização e adequação para um fim específico. Todo
o risco sobre a qualidade e o desempenho do programa está com você. Se o
programa apresentar defeito, você assume o custo de toda a manutenção, reparação
ou correção necessária._

> _Em nenhum caso, a menos que exigido pela lei aplicável ou acordado por
escrito, qualquer detentor de direitos autorais, ou qualquer outra parte que
modifica e/ou transmite o programa, se responsabilizará por danos, incluindo
qualquer dano geral, especial, incidental ou consequencial que surgir do uso ou
incapacidade de usar o programa (incluindo, mas não se limitando à perda de
dados ou dados que são prestados imprecisamente ou perdas sustentadas por você
ou terceiros ou uma falha do programa a operar com outros programas), mesmo se
tal detentor ou outra parte tenha sido avisado da possibilidade de tais danos._

--------------------------------------------------------------------------------
## Instalação

### Versão Standalone

Com a versão standalone não é necessário realizar nenhuma instalação. Você pode
baixar diretamente o arquivo executável.

1. Download do executável para Windows

    _Ainda não disponível_

2. Para executar o programa clique duas vezes do executável

### Instalação no Windows

1. Download do instalador para Windows

    _Ainda não disponível_

2. Executar o instalador

### Instalação no Linux e MacOS

Ainda não foram criados pacotes para a instalação do programa para esses
sistemas. A opção no momento é baixar o código fonte e executar o programa pelo
interpretador Python.

### Download do código fonte e execução via interpretador Python

Essa opção está disponível para qualquer sistema compatível com Python e Qt.

1. Instalação do Python

    Para instalar o Python em seu computador siga as instruções
    específicas para seu sistema descritas nestas páginas:
    - [Windows](https://python.org.br/instalacao-windows/)
    - [MacOS](https://python.org.br/instalacao-mac/)
    - [Linux](https://python.org.br/instalacao-linux/)

2. Baixar o código fonte do GitHub

    Para baixar o código da página do GitHub siga os passos:
    1. Acesse o repositório do projeto no
    [GitHub](https://github.com/luis-dafonseca/CorretorENA)
    2. Clique no botão `Code`
    3. Selecione `Download ZIP`

    No Linux você pode preferir executar o comando

    ```
    wget https://github.com/luis-dafonseca/CorretorENA/archive/refs/heads/master.zip
    ```

3. Descompacte o arquivo `zip` e entre na pasta do projeto

    Use seu descompactador preferido para descompactar o arquivo `zip` e salvar
    o código em uma pasta apropriada.

    Os próximos passos devem ser executados dentro da pasta do código, então
    agora você precisa entrar na pasta contém o arquivo `corretor.py`. Em um
    terminal você pode executar:

    ```
    cd [pasta onde você salvou o código descompactado]/corretor
    ```

4. [_Opcional_] Criar um ambiente virtual

    Para mais informações sobre como criar um ambiente virtual veja a
    [página](https://docs.python.org/pt-br/3/tutorial/venv.html).

5. Instalar as dependências

    Para instalar as dependências do programa em um terminal execute o comando

    ```
    pip install -r requirements.txt
    ```

6. Executar o interpretador

    Para rodar o programa de um terminal execute

    ```
    python corretor.py
    ```

-------------------------------------------------------------------------------
## Usando o programa

Explicamos aqui os arquivos e informações necessárias para executar o programa
em seguida apresentamos um passo a passo para realizar a correção
automaticamente. Depois apresentamos alguns cuidados que devem ser tomados para
evitar possíveis erros na correção. Por fim apresentamos os métodos e algoritmos
implementados.

Para usar o CorretorENA é necessário:

1. O modelo da folha de respostas;
2. O gabarito;
3. Um arquivo `pdf` com as folhas de respostas de cada candidato escaneada;
4. Opcionalmente um arquivo `xlsx` com a lista nomes de todos os candidatos

O programa vai produzir:

1. Um arquivo `pdf` para conferência das correções realizadas;
2. Um arquivo `xlsx` com as notas de cada candidato.

O **modelo** é o arquivo `pdf` com a folha de respostas sem identificação de
candidato. Esse arquivo é sempre distribuído pela SBM junto com os demais
arquivos usados em cada ENA. Ele vai ser usado como base para alinhar as folhas
de respostas antes de correção.

As **respostas** dos candidatos precisam ser escaneadas em um único arquivo PDF.
Não faz diferença se elas forem escaneadas em cores ou tons de cinza, durante o
processamento cada página é convertida para a resolução de 300 dpi em tons de
cinza. Por isso, o ideal é que o escaneamento seja em 300 dpi.  Especial atenção
deve ser data a ordem das folhas de respostas, ela deve ser a mesma da lista de
nome da planilha fornecida pela SBM.  Cuidado para não deixar nenhuma página
invertida ou de ponta cabeça.

Para facilitar a verificação da ordem das folhas de respostas é possível
fornecer uma planilha `xlsx` com os **nomes dos candidatos**.  Esses nomes serão
escritos nas folhas de respostas acima do local onde os nomes vêm previamente
impressos. Assim se alguma página não estiver na ordem correta os nomes não vão
coincidir. O programa não tenta extrair os nomes do `pdf` escaneado. Dessa forma
ele não tem como identificar automaticamente se houver alguma discrepância.
Esses nomes serão também escritos na planilha final com as notas dos candidatos.

O **gabarito** pode ser digitado no campo correspondente ou usando o quadro de
dialogo dedicado. Se uma questão for anulada marque-a com `X`.  Os gabaritos de
ENAs anteriores podem ser acessados pelo menu.  Tentaremos disponibilizar novas
versões para cada ENA assim que o gabarito correspondente seja divulgado.
Também é possível salvar o gabarito em um arquivo usando o menu.

### Passo a passo para executar o programa

1. Escanear todas as folhas de respostas em um arquivo `pdf`

2. No CorretorENA, clicar o botão `Abrir` do campo "Arquivo PDF com o modelo da
folha de respostas" e selecionar o `pdf` fornecido pela SBM com a folha de
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

7. Clique no botão `corrigir` e aguarde. Quando a correção terminar os arquivos
serão salvos automaticamente e o programa pode ser fechado.

8. Verifique a correção de cada candidato conferindo o arquivo `pdf` gerado com
as anotações.

### Cuidados

O resultado produzido pelo programa sempre deve ser verificado antes de
divulgado.  Existem situações onde os algoritmos usados podem não produzir o
resultado esperado.  A seguir listamos algumas situações onde podem ocorrer
falhas.  Note porém que essa lista não é exaustiva.

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

-------------------------------------------------------------------------------
## Como o programa corrige as provas

Para corrigir as provas o programa precisa identificar quais foram as respostas
marcadas por cada candidato. Para isso foram implementados os seguintes passos.

O programa usa a biblioteca [PyMuPDF](https://pymupdf.readthedocs.io/) para ler
os arquivos `pdf` com o modelo e com as respostas dos candidatos e converter
cada página para uma imagem com 300 dpi. Essa biblioteca também é usada para
criar as marcações no `pdf` de anotações que é usado para conferir a correção
gerada pelo programa.

Como no escaneamento as páginas não são perfeitamente alinhadas, os campos das
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

A nota de cada candidato é salva em um arquivo `xlsx`, assim como se ele foi
eliminado ou ausente. Um `pdf` com marcações indicando a correção gerada pelo
programa também é gerado. Esse arquivo é fundamental para que seja possível
conferir com facilidade a correção realizada e identificar possíveis erros.

O arquivo `xlsx` fornecido com os nomes dos candidatos é usado apenas para
escrever o nome de cada candidato junto com o nome originalmente impresso na
folha de questões. Isso é importante para que seja possível conferir que nas
páginas estão na mesma ordem que os nomes da planilha.

-------------------------------------------------------------------------------
