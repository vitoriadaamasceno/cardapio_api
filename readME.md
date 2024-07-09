História
"Estou tendo uma demanda muito grande e está difícil gerenciar pelo whatsapp. Fica difícil gerenciar a fila de pedidos e não atrasar os pedidos mais antigos (pedidos por ordem de chegada). Outro dia por conta das várias mensagens acabamos esquecendo um pedido feito às 19h e só colocando ele de fato na cozinha quando o cliente cobrou o prazo de entrega, que era de 50 min. Ou seja, a pizza só chegou na casa do cliente quase 21h. Foi uma dor de cabeça horrível. Eu gostaria de um sistema que me permitisse receber os pedidos, identificando quando é 1 ou 2 sabores, que permitisse também exibir para o cliente o status desse pedido. O pagamento vai ser feito na entrega mas gostaríamos de saber quando levar troco ou a maquininha de cartão. Outra coisa que gostaríamos é ter o telefone das pessoas para mandar as ofertas promocionais numa lista de transmissão do whatsapp. Ah simmento. Vocês fazem esse serviço? Conseguem me entregar na semana que vem?"

Restaurante:
- POST /cardapio
- PUT /cardapio
- DELETE /itemcardapio
- GET /pedidos: Retorna os pedidos solicitados
- PUT /pedido/status: seta o status do pedido
- GET /clientes: pega informações dos clientes
- GET /relatorio: pega informações de vendas
Clientes:
- GET /pedido
- POST /pedido
- POST /cliente
- PUT /cliente
Em comum:
- GET /cardapio
- POST /login
- POST-GET /chat


Referencias :
pydantic : https://docs.pydantic.dev/latest/concepts/fields/#default-values
sqlachemy: https://docs.sqlalchemy.org/en/20/