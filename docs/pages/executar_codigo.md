
# Baixar e executar o código fonte

1. __Instalar do UV, o gerenciado de pacotes Python__

    Para instalar o Python em seu computador siga as instruções
    da [página](https://docs.astral.sh/uv/getting-started/installation).

2. __Baixar o código fonte do GitHub__

    Para baixar o código da página do GitHub siga os passos:
    1. Acesse o repositório do projeto no
    [GitHub](https://github.com/luis-dafonseca/CorretorENA)
    2. Clique no botão `Code`
    3. Selecione `Download ZIP`

    Caso você seja usuário do GitHub você pode simplesmente baixar o repositório normalmente.

3. __Descompactar o arquivo `zip` e entrar na pasta do projeto__

    Use seu descompactador preferido para descompactar o arquivo `zip` e salvar
    o código em uma pasta apropriada.

    Os próximos passos devem ser executados dentro da pasta do código, então
    agora você precisa entrar na pasta contém o arquivo `pyproject.toml`. Em um
    terminal (ou PowerShell se você estiver no Windows) você pode executar:

    Linux

    ```
    cd [pasta onde você salvou o código descompactado]
    ```

    Windows

    ```
    cd [pasta onde você salvou o código descompactado]
    ```

4. __Executar o corretor__

    Utilize o uv para executar o corretor

    ```
    uv run src/corretor.py
    ```

    Na primeira execução do programa o UV vai instalar todas as dependências em um ambiente virtual.