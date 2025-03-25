# fireBnB
## Tarefa 2: Mostrar os imóveis disponíveis

### Bibliotecas utilizadas:
- pandas: para transformar os arquivos csv em dicionario

- datetime: para poder trabalhar com as datas na hora da filtragem 

- pytest: para realizar os testes

- OS: Limpar a tela do programa

### Explicação modulo "app.py"
Onde o programa está localizado, ele inicia a partir da função "main()"
####funções:
- main: função inicial do programa, irá chamar a tela para o usúario.
        Começo usando "os.system('cls')" para limpar a tela anterior,
        depois chamo a função "exibir_nome_programa()". Depois solicito ao usuario entrada de dados, uso o "try" para validar as informações e tambem uso as variaveis "quantidade_pessoas", "data_entrada" e "data_saida" para receber os dados informados pelo usúario.
        Recebido as informações do usuário chamo a função "verifica_imovel_disponivel()" com os parâmetros recebidos pelo usuário, as informações que retornarem dessa função vão ser recebidas pela variável "imoveis_disponiveis".
        Depois uso um if para mostrar ao usúario os imóveis disponiveis, caso não houver nenhum, irá mostrar uma mensagem que nenhum imóvel está disponível.

- exibir_nome_programa: função para mostrar para o usuario o nome do programa.

- verifica_imovel_disponivel: Essa função irá verificar pelos parâmetros recebido do usuário         
                              nos dicionários "dicionario_imoveis" e "dicionario_reservas" e irão retorna-los para a variável "imoveis_disponiveis" na função "main()".
                              Na linha 21 e 22, converti as datas para objetos datetime, depois criei uma lista chamada "imoveis_disponiveis" que irá receber os imóveis disponiveis.
                              Então uso o "for" para verificar cada imóvel no dicionario "dicionario_imoveis", dentro do "for" utilizo o "if" para verificar a quantidade de pessoas de cada imóvel do dicionario.
                              Então crei uma variavel booleana chamada "conflito" com o valor False e depois um outro "for" para verificar se as datas recebidas do usuario estão conflitando com as datas dos imoveis reservados.
                              obs: essa foi a parte mais dificil do codigo kkk
                              usei o "if" para verificar se o codigo do imovel era o mesmo nos dicionarios,
                              depois criei duas variaveis chamadas "reserva_entrada" "reserva_saida" para a data reservada do imovel que esta no looping e depois uso outro "if para verificar se as datas estão em conflito". se estiver em conflito a variavel "conflito" irá receber o valor True, se não o imóvel vai para a lista "imoveis_disponiveis" e por fim ela é retornada com todos os imoveis disponiveis.


### Explicação modulo "teste.py"
Para os teste usei novamente o pytest, dessa vez criando um módulo novo somente para o teste
Comecei importando o pytest e o modulo "app.py".
criei 10 funções, separado por 5 grupos para realizar os testes. Todas as funções tem a mesma lógica cria uma variaavel chamada "imoveis_disponiveis" que ira receber o resultado da função "verifica_imovel_disponivel()", cada teste muda os parametros passados. dai utilizo o "assert" para comparar o resultado do teste, que é o numero de imóveis disponiveis com o resultado correto.

### Testando
Para testar deve ter o pytest instalado, para instalalo é necessário rodar o comandos "pip install pytest".
Depois de instalar o pytest, voce deve rodar o comando "pytest teste.py" no terminal.

![image](https://github.com/user-attachments/assets/911ea19a-24c6-4082-9268-ebaf0dbf9a0b)


para saber que o teste deu certo, no terminal deve estar como na imagem.

#### funções teste:

- test_capacidade_poucas_pessoas(): Essa função irá passar como parametro o número de capacidade de pessoas    
                                    como 1 e deve retornar o numero de imóveis disponiveis como 5

- test_capacidade_media_pessoas(): Essa função irá passar como parametro o número de capacidade de pessoas    
                                    como 4 e deve retornar o numero de imóveis disponiveis como 5

- test_capacidade_quase_todas_pessoas(): Essa função irá passar como parametro o número de capacidade de 
                                         pessoas como 6 e deve retornar o numero de imóveis disponiveis como 1

- test_capacidade_maxima_pessoas(): Essa função irá passar como parametro o número de capacidade de 
                                         pessoas como 8 e deve retornar o numero de imóveis disponiveis como 0

- test_data(): Essa função irá passar como parametro as datas '2025-04-05', '2025-06-22', 
               e deve retornar o numero de imóveis disponiveis como 2

- test_data_inicio(): Essa função irá passar como parametro as datas '2025-04-08', '2025-04-10', 
               e deve retornar o numero de imóveis disponiveis como 5

- test_data_inicio_reservada_comeco(): Essa função irá passar como parametro as datas '2025-05-10', 
                                       '2025-05-12', e deve retornar o numero de imóveis disponiveis como 4

- test_data_inicio_reservada_fim(): Essa função irá passar como parametro as datas '2025-06-24', 
                                       '2025-06-29', e deve retornar o numero de imóveis disponiveis como 4

- test_data_saida_reservada_comeco(): Essa função irá passar como parametro as datas '2025-08-12', 
                                       '2025-08-16', e deve retornar o numero de imóveis disponiveis como 4

- test_capacidade_data(): Essa função irá passar como parametro o número de capacidade de pessoas    
                          como 4, as datas '2025-08-15', '2025-08-20', e deve retornar o numero de imóveis disponiveis como 2


