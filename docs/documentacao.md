
# Corretor ENA

Esse é um programa para corrigir automaticamente as provas do Exame Nacional de Acesso ao Profmat - ENA. Ele foi desenvolvido por Luis A. D'Afonseca, professor do CEFET-MG e ex coordenador local do Profmat.

Este documento descreve como usar o programa.

## Licença e Ausência Garantia

Esse programa é distribuído sob a Licença Pública Geral GNU seu código pode ser obtido no [repositório GitHub do projeto](https://github.com/luis-dafonseca/Corretor_ENA). Você tem direito a usar o programa sem nenhum custo assim como distribui-lo e alterá-lo. A Licença Pública Geral GNU podem ser encontrada nesse [link](https://www.gnu.org/licenses/gpl-3.0.html), uma tradução para o português pode ser lida nesse [link](http://licencas.softwarelivre.org/gpl-3.0.pt-br.html). Ambos os textos podem ser encontrados também junto ao código do programa.

_Não há nenhuma garantia para o programa, na extensão permitida pela lei aplicável. Exceto quando indicado por escrito, os detentores de direitos autorais e/ou outras partes fornecem o programa "como está" sem garantia de qualquer tipo, expressa ou implícita, incluindo, mas não se limitando a, garantias implícitas de comercialização e adequação para um fim específico. Todo o risco sobre a qualidade e o desempenho do programa está com você. Se o programa apresentar defeito, você assume o custo de toda a manutenção, reparação ou correção necessária._

_Em nenhum caso, a menos que exigido pela lei aplicável ou acordado por escrito, qualquer detentor de direitos autorais, ou qualquer outra parte que modifica e/ou transmite o programa, se responsabilizará por danos, incluindo qualquer dano geral, especial, incidental ou consequencial que surgir do uso ou incapacidade de usar o programa (incluindo, mas não se limitando à perda de dados ou dados que são prestados imprecisamente ou perdas sustentadas por você ou terceiros ou uma falha do programa a operar com outros programas), mesmo se tal detentor ou outra parte tenha sido avisado da possibilidade de tais danos._

## Usando o programa

Para usar o Corretor do ENA é necessário:

1. O modelo da folha de respostas;
2. O gabarito;
3. Um arquivo PDF com as folhas de respostas de cada candidato escaneada;
4. Opcionalmente um arquivo XLSX com a lista nomes de todos os candidatos

O programa vai produzir:

1. Um arquivo PDF para conferência das correções realizadas;
2. Um arquivo XLSX com as notas de cada candidato.

O modelo é o arquivo PDF com a folha de respostas sem identificação de candidato. Esse arquivo é sempre distribuído pela SBM junto com os demais arquivos usados em cada ENA. Ele vai ser usado como base para alinhar as folhas de respostas antes de correção.

As respostas dos candidatos precisam ser escaneadas em um único arquivo PDF. Não faz diferença se elas forem escaneadas em cores ou tons de cinza, durante o processamento cada página é convertida resolução de 300pdis em tons de cinza. Por isso, o ideal é que o escaneamento seja em 300dpis. Especial atenção deve ser data a ordem das folhas de respostas, ela deve ser a mesma da lista de nome da planilha fornecida pela SBM. Cuidado para não deixar nenhuma página invertida ou de ponta cabeça.

Como no processo de escaneamento as páginas não são rigidamente alinhadas, os campos das respostas não coincidem perfeitamente. Para resolver esse problema o programa alinha cada página com o modelo antes de iniciar a busca pelas marcações. Essa é a razão pelo qual o modelo é necessário.

Para facilitar a verificação da ordem das folhas de respostas é possível fornecer uma planilha XLSX com os nomes dos candidatos. Esses nomes serão escritos nas folhas de respostas acima do local onde os nomes vêm previamente impressos. Assim se alguma página não estiver na ordem correta os nomes não vão coincidir. O programa não tenta extrair os nomes do PDF escaneado. Dessa forma ele não tem como identificar automaticamente se houver alguma discrepância. Esses nomes serão também escritos na planilha final com as notas dos candidatos.

O Gabarito pode ser digitado no campo correspondente ou usando o quadro de dialogo dedicado. Os gabaritos de ENAs anteriores podem ser acessados pelo menu. Tentaremos distribuir novas versões para cada ENA assim que o gabarito correspondente seja divulgado.

## Como o programa corrige as provas

Para corrigir as provas o programa precisa identificar quais foram as respostas marcadas por cada candidato. Para isso foram implementados os seguintes passos.

O programa usa a biblioteca [PyMuPDF](https://pymupdf.readthedocs.io/) para ler os arquivos PDF com o modelo e com as respostas dos candidatos e converter cada página dos PDF para o formato de imagem com 300pdi. Essa biblioteca também é usada para criar as marcações no PDF de anotações que é usado para conferir a correção gerada pelo programa.

Porém, quando as folhas de respostas são escaneadas, em geral as folhas ficam desalinhadas, isso poder ser facilmente visto passando as páginas do PDF e observando como as posições dos itens se movimentam de uma página para a outra.

Assim, o primeiro passo necessário é usar um algoritmo de _registration_ para alinhar os elementos de cada página com a página modelo. Nessa etapa usamos a biblioteca de visão computacional [OpenCV](https://opencv.org/). O algoritmo implemento é descrito nessa [página](https://pyimagesearch.com/2020/08/31/image-alignment-and-registration-with-opencv/).

Assim que a imagem da página com as respostas foi alinhada com o modelo, ela é convertida para um _array_ numérico da biblioteca [NumPy](https://numpy.org/). Nessa etapa o programa conta o número de _pixels_ de cor diferente de brando nos retângulos correspondentes a cada marcação. O algoritmo não tem como distinguir marcações intencionais de rabiscos, sombras ou a própria moldura que indica onde o candidato deve marcar sua resposta. Todo _pixel_ não branco é contado. Se o número de _pixels_ não brancos dento do retângulo ultrapassar 50% a entrada é considerada marcada. O programa não analisa marcações fora dos retângulos predeterminados, isso é, o programa não vai identificar se algo foi escrito indevidamente fora dos retângulos. Para ver os retângulos que o programa usa como referência basta clicar no botão `Ver` após carregar o modelo.

Tendo identificado quais entradas foram marcadas pelo candidato a etapa final é simplesmente verificar se existem mais do que uma marcação por questão e se a resposta coincide com o gabarito.

A nota de cada candidato é salva em um arquivo XLSX, assim como se ele foi eliminado ou ausente. Um PDF com marcações indicando a correção gerada pelo programa também é gerado. Esse arquivo é fundamental para que seja possível conferir com facilidade a correção realizada e identificar possíveis erros.

O arquivo XLSX com os nomes dos candidatos é usado apenas para escrever o nome de cada candidato junto com o nome originalmente impresso na folha de questões. Isso é importante para que seja possível conferir que nas páginas estão na mesma ordem que os nomes da planilha.

## Cuidados

O resultado produzido pelo programa sempre deve ser verificado antes de divulgado. Existem situações onde os algoritmos usados podem não produzir o resultado esperado. A seguir listamos algumas situações onde podem ocorrer falhas. Note porém que essa lista não é exaustiva.

1. As folhas de respostas não estão na mesma ordem que os nomes dos candidatos na planinha da SBM.
2. O candidato não marcou corretamente as respostas.
3. O programa não consegue alinhar alguma folha de respostar com o modelo. Isso pode acontecer por vários motivos:
    1. a página não foi adequadamente escaneada;
    2. a página está invertida ou muito fora do alinhamento;
    3. a página possui rasuras ou marcações não previstas;
    4. o escaneamento está muito escuro (causando sombras na página) ou muito claro (algumas partes não estão suficientemente visíveis).
