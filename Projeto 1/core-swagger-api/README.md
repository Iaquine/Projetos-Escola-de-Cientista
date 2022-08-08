# api-Should-I-go

Projeto que sobe um Container e, neste, uma API RESTful com o Swagger

## Uso do Docker no Mac em ambientes corporativos

### 1. Instalar o homebrew

O homebrew é um gestor de pacotes para o MAC

```console
$ sudo /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

### 2. Instalar o Lima

O Lima é uma ferramenta de virtualização que permite subir máquinas virtuais Linux no MAC

```console
brew install lima
```

### 3. Subir a primeira máquina Linux

Para subir a primeira máquina, agora, basta executar `limactl start default`, para inicializar a engine na máquina.

Uma vez inicializado, confirme a opção de continuar com as configurações padrão e aguarde a instalação da máquina.

### 4. Instalação e configuração do Docker e do docker-compose

Instalando a engine do Docker, conseguiremos utilizar a mesma para a virtualização

```console
$ sudo curl -fsSL https://get.docker.com | sh
```

Além disso, também é necessário instalar o docker-compose, uma ferramenta de orquestração do Docker. Para isso:

```console
$ sudo curl -L "https://github.com/docker/compose/releases/download/1.26.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
```

Configuração do Docker para usuários não root

```console
$ sudo groupadd docker
$ sudo usermod -aG docker $USER
$ newgrp docker 
```

Configuração do docker compose para usuários não root

```console
$ sudo chmod +x /usr/local/bin/docker-compose
```

### 5. Configuração final do container

Por fim, faremos uma configuração final do container que o Lima provisiona. Para isso, vamos pausar o lima com o comando `limactl stop default` e editar o arquivo de configurações do mesmo.

Para editar o arquivo de configurações, use o seu editor de preferência para editar o arquivo em `~/.lima/default/lima.yaml
`.

```console
$ nano ~/.lima/default/lima.yaml
```

Por padrão, o Lima monta os arquivos do Mac na VM *read only*, e precisamos mudar esta configuração. Dentro da seção `mount` do arquivo, mude a configuração `write: null` para `write: true`.

Outra configuração válida em máquinas com 16GB de RAM ou mais é aumentar a quantidade de memória disponibilizado à VM. Para isso, dentro da seção `memory` mude a configuração de `null` para `"8GiB"` (sem esquecer das aspas duplas e da configuração de caixa alta e baixa).

Por fim, salve o arquivo e suba a VM novamente com o comando `limactl start default`.

Lembrando que, para executar um comando dentro da VM Linux do lima, há duas formas.

A primeira é abrindo o shell Linux, com o comando `lima` e executando as instruções ali. Após terminar, basta tipar `exit` (pode ser que seja necessário executar o comando 2x) e o seu terminal voltará para o zsh do mac.

A segunda é adicionando o comando `lima` antes de qualquer instrução e o comando automaticamente será enviado para a VM. Exemplo:

```console
$ free -h
zsh: command not found: free

$ lima free -h
               total        used        free      shared  buff/cache   available
Mem:           7.8Gi       360Mi       3.9Gi       5.0Mi       3.5Gi       7.1Gi
Swap:             0B          0B          0B
```

## Getting Started

Para executar a aplicação, basta compilar o Docker e executar o mesmo com os seguintes comandos

```
docker-compose build
docker-compose up
```

Instruções adicionais podem ser encontrados na [Apresentação Swagger](https://github.ibm.com/patrick-ibm/swagger_api/blob/master/Apresenta%C3%A7%C3%A3o%20Swagger.pdf) no repositório

## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Autores

* **Patrick Luiz** - *Trabalho inicial*
* **Iaquine** - *Finalização*

## Exemplo de template copiado de: https://gist.github.com/PurpleBooth/109311bb0361f32d87a2
