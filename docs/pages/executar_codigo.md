
# Baixar e executar o código fonte

### __Instalar do UV__

[UV](https://docs.astral.sh/uv)
é o gerenciador de pacotes utilizado para garantir que
a instalação da versão correta do Python e das bibliotecas.
Para instalar o UV em seu computador siga as instruções
da [página](https://docs.astral.sh/uv/getting-started/installation).

### __Baixar o código fonte do GitHub__

Para baixar o código da página do GitHub siga os passos:

1. Acesse o [repositório do projeto no GitHub](https://github.com/luis-dafonseca/CorretorENA)
2. Clique no botão `Code`
3. Selecione `Download ZIP`
4. Salve o arquivo em seus computador

Caso você seja usuário do
[GitHub](https://github.com),
pode simplesmente baixar o repositório normalmente.

### __Descompactar o arquivo__

Use seu descompactador preferido para extrair o arquivo `zip`
e salvar o código em uma pasta apropriada.

### __Entrar na pasta do projeto__

Os próximos passos devem ser executados dentro da pasta do
código. Portanto, após a extração, entre na pasta que contém
o arquivo `pyproject.toml`. Em um terminal (ou PowerShell),
você pode executar:

``` title="Linux"
cd [pasta onde você salvou o código descompactado]
```

``` title="Windows"
cd [pasta onde você salvou o código descompactado]
```

### __Executar o corretor__

Utilize o uv para executar o corretor

```
uv run src/corretor.py
```

Na primeira execução do programa o UV vai instalar
todas as dependências em um ambiente virtual.