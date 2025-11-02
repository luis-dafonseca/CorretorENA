
# Download e Instalação

## Baixar o programa


## Arquivos Exemplo para Testes

## Instalação

### Windows 10

Para baixar a última versão acesse a [página de download](download.md).

O programa é standalone, isso significa que ele não precisa ser
instalado, basta executá-lo diretamente após o download.
Até o momento ele foi testado apenas no Windows 10,
mas é provável que funcione normalmente no Windows 11.

### Outros Sistemas Operacionais

Ainda não foram criados pacotes para outros sistemas
operacionais. Nesses casos, a opção é baixar o código e executar o
programa pelo interpretador Python. Veja as instruções no final deste
arquivo.


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