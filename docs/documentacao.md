
# CorretorENA

![logo](./images/CorretorENA_icon.png "CorretorENA")

Este documento descreve como baixar e usar o **CorretorENA**.
Um programa para corrigir automaticamente as provas do Exame Nacional de
Acesso ao Profmat (ENA), desenvolvido por Luis A. D'Afonseca, professor
do CEFET-MG e ex-coordenador local do Profmat. Para mais informações sobe o programa
acesse a [página](https://sites.google.com/view/prof-luis-dafonseca/profmat/Corretor_ENA)
ou o repositório [GitHub](https://github.com/luis-dafonseca/CorretorENA).

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

# Instalação

### Windows 10

Para baixar a última versão acesse a
[página de download](https://github.com/luis-dafonseca/CorretorENA/releases).

O programa é standalone, isso significa que ele não precisa ser
instalado, basta executá-lo diretamente após o download.
Até o momento ele foi testado apenas no Windows 10,
mas é provável que funcione normalmente no Windows 11.

### Outros Sistemas Operacionais

Ainda não foram criados pacotes para outros sistemas
operacionais. Nesses casos, a opção é baixar o código e executar o
programa pelo interpretador Python. Veja as instruções no final deste
arquivo.

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

## Baixar e executar o código fonte

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

3. Descompacte o arquivo `zip` e entrar na pasta do projeto

    Use seu descompactador preferido para descompactar o arquivo `zip` e salvar
    o código em uma pasta apropriada.

    Os próximos passos devem ser executados dentro da pasta do código, então
    agora você precisa entrar na pasta contém o arquivo `corretor.py`. Em um
    terminal (ou PowerShell se você estiver no Windows) você pode executar:

    Linux
    ```
    cd [pasta onde você salvou o código descompactado]/corretor
    ```

    Windows
    ```
    cd [pasta onde você salvou o código descompactado]\corretor
    ```

4. [_Opcional_] Criar um ambiente virtual

    Este passo é opcional mas fortemente recomendado.
    Para mais informações sobre como criar um ambiente virtual veja a
    [página](https://docs.python.org/pt-br/3/tutorial/venv.html).

    Para instalar o gerenciador de ambientes virtuais execute
    ```
    pip install virtualenv
    ```
    Para criar o ambiente virtual execute
    ```
    python -m venv venv
    ```
    O comando de ativamento do ambiente depende do terminal em uso,
    no Linux execute
    ```
    source venv/bin/activate
    ```
    No Windows com o Power Shell
    ```
    env/Scripts/Activate.ps1
    ```
    No Windows com o CMD
    ```
    env/Scripts/activate.bat
    ```
    Para desativá-lo, depois de executar o programa, feche o terminal ou execute
    ```
    deactivate
    ```

5. Instalar as dependências

    Para instalar as dependências do programa execute o comando
    ```
    pip install -r requirements.txt
    ```

6. Executar o interpretador

    Para rodar o programa de um terminal execute
    ```
    python corretor.py
    ```