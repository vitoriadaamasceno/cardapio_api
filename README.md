## cardapio API - em construção

### História

"Estou tendo uma demanda muito grande e está difícil gerenciar pelo whatsapp. Fica difícil gerenciar a fila de pedidos e não atrasar os pedidos mais antigos (pedidos por ordem de chegada). Outro dia por conta das várias mensagens acabamos esquecendo um pedido feito às 19h e só colocando ele de fato na cozinha quando o cliente cobrou o prazo de entrega, que era de 50 min. Ou seja, a pizza só chegou na casa do cliente quase 21h. Foi uma dor de cabeça horrível. Eu gostaria de um sistema que me permitisse receber os pedidos, identificando quando é 1 ou 2 sabores, que permitisse também exibir para o cliente o status desse pedido. O pagamento vai ser feito na entrega mas gostaríamos de saber quando levar troco ou a maquininha de cartão. Outra coisa que gostaríamos é ter o telefone das pessoas para mandar as ofertas promocionais numa lista de transmissão do whatsapp. Ah simmento. Vocês fazem esse serviço? Conseguem me entregar na semana que vem?"

### Rotas( todas que tem ok já estão feitas)


Restaurante:
- POST /cardapio OK
- PUT /cardapio
- DELETE /itemcardapio
- GET /pedidos: Retorna os pedidos solicitados
- Patch /pedido/status: seta o status do pedido
- GET /clientes: pega informações dos clientes
- GET /relatorio: pega informações de vendas
Clientes:
- GET /pedido
- POST /pedido
- POST /cliente OK
- PUT /cliente
Em comum:
- GET /cardapio OK
- POST /login OK
- POST-GET /chat


### Explicando sobre o projeto(pastas e docs):

- alembic: o alembic é uma ferramenta para criar migrações so banco de dados , ele é muito bom para organizar as mudanças no banco de dados principalmente quando ela é feita um tempo depois do projeto já esta feito. Foi feita uma configuração no alembic para que as mudanças no banco sejam feitas de forma assincrona.

- restaurante:

    - config: todas as configurações do projeto isso pode incluir configurações de banco de dados, configurações de servidor, etc, no arquivo settings estão todas as variaveis de configuração.

    - contrib: como o nome já diz contrib são todos os arquivos de contribuição, ou seja arquivos que podem ser compartilhados entre maais de uma classe.Exemplo : o arquivo dependencia está na pasta contrib pois o DatabaseDependency é usado para todos os controllers que acessam o banco de dados, assim como o schema configurado no contrib vai ser refletido em todos os schemas do projeto.

    - controllers : a pasta de controladores ou seja responsaveis por fazer as requisições e enviar para as rotas. ela foi dividida entre rotas para admin, rotas para cliente e todas que estão foram são contrib( podem ser usadas por todos os usuarios cadastrados)

    - models : armazena os modelos de dados da aplicação , onde está o modelo inicial do banco de dados e suas entidades

    - repository : onde fica as funções que chamam o banco de dados 

    - schemas : os schemas são o tratamento e serialização dos dados usando pydantic , ou seja , onde eu defino os tipo de dados que deverar ser recebido para evitar erros e conflitos com o banco.

    - utils:  todos os códigos auxiliares.

    - main: arquivo que inicia o código

    - routers: controle de rotas.



- docker-compose.yml: o docker compose é um orquestrador de containers do docker , usei o docker compose para iniciar e criar o meu banco de dados. A intenção é que futuramente tudo seja feito por containers do docker

- Makefile : define os comandos para iniciar nossa aplicação e facilitar na hora de rodar

- requirements.txt: são as instalações necessarias 



### Como rodar o projeto ?

1. Clone o projeto 

2. Tenha o docker instalado na sua maquina

3. rode o comando make install - para instalar as dependencias

4. em seguida rode make db - iniciar o banco de dados

5. make run - para iniciar a api

6. na rota /docs - você pode olhar a documentação



Referencias :

pydantic : https://docs.pydantic.dev/latest/concepts/fields/#default-values

sqlachemy: https://docs.sqlalchemy.org/en/20/

docker:https://livro.descomplicandodocker.com.br/

curso da dio: backend em python