print('''
GAME: É NOITE DE BRUXAS

Seja muito bem vindo ao jogo de RPG desenvolvido para atividade de Pensamento Computacional.

Quero que você se divirta muito, dê boas risadas e também sinta um pouco de medo e bastante suspense.

Espero que goste da nossa brincadeira.

Nos vemos ao final!

Bye bye

Viva o dia do Halloween!

Viva a sexta-feira 13!
''')

import random

nome_jogador = input('Digite o nome que deseja dar ao seu personagem: ').upper()
bairro = input('Digite o nome do seu bairro: ').upper()
sexo = input('Digite o sexo do seu personagem "homem" ou "mulher": ').upper()

if sexo == "HOMEM":
    print(f'''
{nome_jogador} é morador de uma pequena cidade no interior do Brasil, está vivendo
um paradoxo com a realidade da civilização, pois você ouviu algumas fofocas
de alunas de outros cursos da Univassouras que diziam que a cidade tinha sido
invadidada por algumas bruxas
\nVocê está correndo um grave perigo de vida, pois os cães do inferno estão
soltos rodeando alguns bairros da cidade.
\nPREPARA-SE QUE A BRINCADEIRA ESTÁ SÓ COMEÇANDO...\n
''')

    print(f'''
{nome_jogador} mora no bairro {bairro} da pequena cidade de Saquarema e 
ficou sabendo através do Instagram da prefeita Manuela que de 
forma misteriosa alguns animais estavam desaparecendo da sua cidade.\n
Além disso, haviam registros de pessoas que tinham sumido e estavam investigando
que no horário dos desaparecimentos dessas pessoas em alguns bairros a luz caia e 
voltava, e os computadores da prefeitura simplesmente ficavam loucos, 
reiniciavam, bugs, congelamentos, telas pretas, programas
abriam sem mais nem menos.
\n      Um verdadeiro caos!
''')

    print('''
Numa quinta-feira, precisamente dia 12 de outubro de 2023, poucos dias antes
do festival de Halloween, aconteceu o que você menos esperava, sua vizinha gostosa que
você tinha uma paixão desapareceu, por volta de 23:32 da noite, beirando a sexta-feira 13.
\nUns 05 minutos antes você reparou que as luzes da sua casa estavam apagando e acendendo,
tendo a certeza que não poderia ser falha da Enel, já que é uma empresa ímpar no fornecimento
de energia, você tem que decidir entre "ir" para fora verificar o que está acontecendo
ou "ficar" dentro de casa.
    ''')

    decisao1 = input('Digite "ir" ou "ficar": ').upper()

    if decisao1 == "IR":
        print('''
Ao caminhar até o portão você ouviu uma pequena sequência de gritos aterrorizantes
vindo do final da rua sem saída.\n
Assustado e ainda atrás do portão, você deve escolher, entre "abrir" o portão ou "correr" para dentro de casa?
        ''')

        decisao1_1 = input('Digite sua escolha "abrir" ou "correr": ').upper()
        if decisao1_1 == "ABRIR":
            print('''
Ao abrir o portão você se depara com duas figuras tenebrosas no final da rua,
agarrando e carregando sua vizinha gostosa.\n
Assustado com o que pode acontecer com ela, você decide segui-la para ver até
onde aquilo irá.
Você deve retornar para dentro de casa e pegar alguma arma para usar na sua aventura.
            ''')

            arma = input('''
Voltando para casa, você tem um "punhal", uma "espada" e um "revolver"
velho do seu avô.
\nEscolha uma dessas armas: Digite "punhal" ou "espada" ou "revolver": ''').upper()

            if arma == "PUNHAL":
                print("\nQue bosta hein, será que você vai conseguir matar aquele monstro somente com um punhal?!")
            elif arma == "ESPADA":
                print("\nUma ótima escolha, com uma espada você poderá lutar, mas correrá o risco de errar o golpe e morrer")
            elif arma == "REVOLVER":
                print("\nSerá que esse revólver vai mesmo disparar? kkk")
            else:
                print("\nEscolha a arma que tem disponível para sua aventura")

            print(f'''
Agora, equipado com {arma} você iniciará sua aventura
Ao seguir em direção ao terreno baldio e adentrar naquela mata baixa, você
escuta uns grunidos estranhos vindo da parte mais escura do terreno.
Quase se cagando de medo, você tem que decidir entre ir "investigar" ou "caminhar"
no sentido oposto.
            ''')

            decisao1_2 = input('Escreva sua decisão "investigar" ou "caminhar": ').upper()

            if decisao1_2 == "INVESTIGAR":

                print(f'''
Eu não teria escolhido isso, mas você decidiu!\n
Ao se aproximar entre os matos, você viu uma criatura tenebrosa, uma verdadeira
bruxa amarrando sua vizinha.
De repente, a bruxa se vira para você e corre para te atacar, você deverá
se defender!
                ''')

                tentativa = input('''
Caramba véi, agora você está ferrado a bruxa te viu e está correndo 
para te atacar, você vai ter que tomar uma decisão.
Você vai "sacar" seu punhal e atacar ou "correr"?
Digite sua escolha "sacar" ou "correr": ''').upper()
                if tentativa == "CORRER":
                    print('''Você é um frouxo! Correu e não adiantou a bruxa te pegou e te transformou numa tartaruga!
                          GAME OVER!!!
                          ''')
                elif tentativa == "SACAR":
                    print('\nVocê é muito corajoso! Vamos ver se você terá sorte nessa luta')


                    if arma == "PUNHAL":
                        print('''Você saca seu punhal e agora deverá tentar matar a bruxa na faquinha!
\nVocê terá que conseguir golpear ela por 3 vezes, só assim você conseguirá matá-la e você terá 5 tentativas\n Vamos ver se você terá sucesso!
                        ''')
                        dificuldade = 5
                        sucessos = []
                        for _ in range(5):
                            dado = random.randint(1, 10)
                            if dado >= dificuldade:
                                sucessos.append(dado)
                        print(sucessos)
                        num_sucessos = len(sucessos)
                        print(f'Número de sucessos: {num_sucessos}')
                                
                        if num_sucessos >= 3:
                            print('''
Você conseguiu vencer a bruxa! Caramba que sorte tremenda!\n
Eu não acreditava rsrs
                                    ''')
                        else:
                            print('''
Infelizmente você não conseguiu ganhar da bruxa e ela te
transformou num franguinho.\n
Agora você servirá de jantar para os cães de guarda delas.\n
                GAME OVER!
''')

                    elif arma == "ESPADA":
                        print('Você saca sua espada e prepara-se para atacar! Você precisará conseguir golpear ela 3 vezes!')
                        dificuldade = 5
                        sucessos = []
                        for _ in range(5):
                            dado = random.randint(1, 10)
                            if dado >= dificuldade:
                                sucessos.append(dado)
                        print(sucessos)
                        num_sucessos = len(sucessos)
                        print(f'Número de sucessos: {num_sucessos}')
                                
                        if num_sucessos >= 3:
                            print('''
Você conseguiu vencer a bruxa! Caramba que sorte tremenda!\n
Eu não acreditava rsrs
                                    ''')
                        else:
                            print('''Infelizmente você não conseguiu ganhar da bruxa e ela te
transformou num franguinho.\n
Agora você servirá de jantar para os cães de guarda delas.\n
                GAME OVER!
                                    ''')

                    elif arma == "REVOLVER":
                        print('''Você saca o revólver velho do seu avô,
mas será que esse revólver velho vai mesmo disparar? kkk\n
Você tem que ser rápido porque a bruxa vem correndo na sua direção
Então você terá apenas chance de dar 2 tiros, vamos para roletar russa!!!
                        ''')
                        dificuldade = 6
                        sucessos = []
                        for _ in range(6):
                            dado = random.randint(1, 10)
                            if dado >= dificuldade:
                                sucessos.append(dado)
                        print(sucessos)
                        num_sucessos = len(sucessos)
                        print(f'Número de sucessos: {num_sucessos}')

                        if num_sucessos >= 3:
                            print('''
Caraca! O revólver disparou e você conseguiu vencer a bruxa! 
Tu é sortudo véi!\n
Eu não acreditava rsrs
''')
                        else:
                            print('''Putz!! O revólver falhou e você não conseguiu matar a bruxa
e agora ela te transformou num franguinho.\n
Agora você servirá de jantar para os cães de guarda dela.\n
                GAME OVER!
                                ''')
                    
                    if num_sucessos >= 3:
                        print('''
\nParabéns!!! Você conseguiu resgatar sua vizinha e será que vai ser recompensado?
                        ''')
                        recompensa = input('''Você começa a desamarrar sua vizinha e nota que ela estava só de sutiã e calcinha.
Você deve ajudar a ela a levantar.
Você tira sua camisa e entrega a ela ou tenta beija-la?
O que você vai fazer agora?\n
Digite sua escolha "entregar" camisa ou tentar "beijar" a vizinha: ''').upper()
                        if recompensa == "BEIJAR":
                            x = random.randrange(1,6)
                            if x >= 3:
                                print(f'''Caramba que sorte a sua, sua vizinha estava muito feliz que você conseguiu resgata-la e quer te dar um beijo!
Parabéns! Você conseguiu vencer a bruxa e vai descobrir que existe um mundo além do xvideos!!!\n 
                                {nome_jogador} WINS!!!
                                ''')
                            else:
                                print(f'''Putz!!! Sua vizinha te acha um zé ruela e o máximo que você
vai ganhar é uma tapa nessa sua cara gorda e bolachuda!
GAME OVER para {nome_jogador}!!!
                                ''')
                        elif recompensa == "ENTREGAR":
                            x = random.randrange(1,6)
                            if x >= 3:
                                print(f'''Putz cara, você é um zé ruela, mal sabia que sua vizinha iria te dar um bom prêmio.
Agora o que te resta é voltar para casa para continuar assistindo xvideos! 
GAME OVER para {nome_jogador} !!!
                                ''')
                            else:
                                print(f'''Que cena linda você tirando sua camisa para ela se proteger, muito fofo!
Ela se encantou com isso e te deu um selinho
Pena que você continuará chupando o dedo e jogando LOL
Vamos ver se na próxima aventura sua você consegue sair da fossa do xvideos!!!       
                        THE END!''')

        elif decisao1_1 == "CORRER":
            print('''
Você escolheu correr de volta para dentro de casa e sua mãe ordenou que você vá lavar a louça suja, o banheiro e arrumar seu quarto.
Putz véi! Que vacilo, que péssima escolha! Você saiu do quarto, deixou a partida de LOL rolando e ainda vai ter que arrumar a casa
Agora sua vizinha gostosa está correndo risco de vida e você vai ficar em casa tendo que arrumar as coisas!
Depois que sua mãe te da a ordem, você decide "arrumar" ou "discutir" com ela
            ''')

            decisao1_3 = input('Digite sua escolha "arrumar" ou "discutir: ').upper()
            if decisao1_3 == "ARRUMAR":
                print(f'''
Parabéns, você é um ótimo filho!
        LOUÇAS WINSSS!!!
{nome_jogador} LOSE!!! GAME OVER!!!
                ''')

            elif decisao1_3 == "DISCUTIR":
                print(f'''
Putz véi! Você parece que come coco!
Vai discutir com tua mãe?!
Agora você acabou de tomar uma tapa na tua cara gorda e bolachuda e vai ficar sem jogar computador por uma semana!
         MAMÃE WINSSS!
{nome_jogador} LOSE!!! GAME OVER!!!
                ''')

            else:
                print('''
Qual a parte você não entendeu que é para escolher entre "arrumar" ou "discutir"
Por isso que tirou nota baixa em Resolução de Problemas da Engenharia!!!
    Meu Deus do céu!
      GAME OVER!!!
                ''')
        
        else:
            print('''
Meu Deus do céu!
Mano, qual a parte você não entendeu que é para escolher entre "abrir" ou "correr"
Por isso que tirou nota baixa em Resolução de Problemas da Engenharia!!!
        GAME OVER para você!!!
            ''')

    elif decisao1 == "FICAR":
        print('''
Você escolheu ficar dentro de casa e sua mãe ordenou que você vá lavar a louça suja, o banheiro e arrumar seu quarto.
Putz véi! Que vacilo, que péssima escolha! Você saiu do quarto, deixou a partida de LOL rolando e ainda vai ter que arrumar a casa
Agora sua vizinha gostosa está correndo risco de vida e você vai ficar em casa tendo que arrumar as coisas!
Depois que sua mãe te da a ordem, você decide "arrumar" ou "discutir" com ela
''')
        decisao2_1 = input('Digite sua escolha "arrumar" ou "discutir: ').upper()
        if decisao2_1 == "ARRUMAR":
            print(f'''
Parabéns, você é um ótimo filho!\n
        LOUÇAS WINSSS!!!
      {nome_jogador} LOSE!!! 
          GAME OVER!!!
            ''')
        elif decisao2_1 == "DISCUTIR":
            print(f'''
Putz véi! Você parece que come coco!
Vai discutir com tua mãe?!
Agora você acabou de tomar uma tapa na tua cara gorda 
e bolachuda e vai ficar sem jogar computador por uma semana!\n
            MAMÃE WINSSS!
            {nome_jogador} LOSE!!! GAME OVER!!!
            ''')
        else:
            print('''
Qual a parte você não entendeu que é para escolher entre "arrumar" ou "discutir"
Por isso que tirou nota baixa em Resolução de Problemas da Engenharia!!!
Meu Deus do céu!\n
        GAME OVER!!!
            ''')

    else:
        print(f'''
Meu Deus do céu!
Mano, qual a parte você não entendeu que é para escolher entre "ir" ou "ficar"
Por isso que tirou nota baixa em Resolução de Problemas da Engenharia!!!
        GAME OVER para {nome_jogador}!!!
        ''')

#PARTE DA MULHER

if sexo == "MULHER":
    print(f'''
{nome_jogador} é moradora de uma pequena cidade no interior do Brasil, está vivendo
um paradoxo com a realidade da civilização, pois você ouviu algumas fofocas
de alunas de outros cursos da Univassouras que diziam que a cidade tinha sido
invadidada por algumas bruxas
\nVocê está correndo um grave perigo de vida, pois os cães do inferno estão
soltos rodeando alguns bairros da cidade.
\nPREPARA-SE QUE A BRINCADEIRA ESTÁ SÓ COMEÇANDO...\n
''')

    print(f'''
{nome_jogador} mora no bairro {bairro} da pequena cidade de Saquarema e 
ficou sabendo através do Instagram da prefeita Manuela que de 
forma misteriosa alguns animais estavam desaparecendo da sua cidade.\n
Além disso, haviam registros de pessoas que tinham sumido e estavam investigando
que no horário dos desaparecimentos dessas pessoas em alguns bairros a luz caia e 
voltava, e os computadores da prefeitura simplesmente ficavam loucos, 
reiniciavam, bugs, congelamentos, telas pretas, programas
abriam sem mais nem menos.
\n      Um verdadeiro caos!
''')

    print('''
Numa quinta-feira, precisamente dia 12 de outubro de 2023, poucos dias antes
do festival de Halloween, aconteceu o que você menos esperava, seu vizinho sarado que
você tinha uma paixão desapareceu, por volta de 23:32 da noite, beirando a sexta-feira 13.
\nUns 05 minutos antes você reparou que as luzes da sua casa estavam apagando e acendendo,
tendo a certeza que não poderia ser falha da Enel, já que é uma empresa ímpar no fornecimento
de energia, você tem que decidir entre "ir" para fora verificar o que está acontecendo
ou "ficar" dentro de casa.
    ''')

    decisao1 = input('Digite "ir" ou "ficar": ').upper()

    if decisao1 == "IR":
        print('''
Ao caminhar até o portão você ouviu uma pequena sequência de gritos de socorro
vindo do final da rua sem saída.\n
Assustada e ainda atrás do portão, você deve escolher, entre "abrir" o portão ou "correr" para dentro de casa?
        ''')

        decisao1_1 = input('Digite sua escolha "abrir" ou "correr": ').upper()
        if decisao1_1 == "ABRIR":
            print('''
Ao abrir o portão você se depara com duas figuras tenebrosas no final da rua,
agarrando e carregando seu vizinho gostoso.\n
Assustada com o que pode acontecer com ele, você decide segui-los para ver até
onde aquilo irá.
Você retorna para dentro de casa e pegar alguma arma para usar na sua aventura.
            ''')

            arma = input('''
Voltando para casa, você tem um "punhal", uma "espada" e um "revolver"
velho do seu avô.
\nEscolha uma dessas armas: Digite "punhal" ou "espada" ou "revolver": ''').upper()

            if arma == "PUNHAL":
                print("\nQue bosta hein, será que você vai conseguir matar aquele monstro somente com um punhal?!")
            elif arma == "ESPADA":
                print("\nUma ótima escolha, com uma espada você poderá lutar, mas correrá o risco de errar o golpe e morrer")
            elif arma == "REVOLVER":
                print("\nSerá que esse revólver vai mesmo disparar? kkk")
            else:
                print("\nEscolha a arma que tem disponível para sua aventura")

            print(f'''
Agora, equipada com {arma} você iniciará sua aventura
Ao seguir em direção ao terreno baldio e adentrar naquela mata baixa, você
escuta uns grunidos estranhos vindo da parte mais escura do terreno.
Quase se cagando de medo, você tem que decidir entre ir "investigar" ou "caminhar"
no sentido oposto.
            ''')

            decisao1_2 = input('Escreva sua decisão "investigar" ou "caminhar": ').upper()

            if decisao1_2 == "INVESTIGAR":

                print(f'''
Eu não teria escolhido isso, mas você decidiu!\n
Ao se aproximar entre os matos, você viu uma criatura tenebrosa, uma verdadeira
bruxa amarrando seu vizinho.
De repente, a bruxa se vira para você e corre para te atacar, você deverá
se defender!
                ''')

                tentativa = input('''
Caramba véi, agora você está ferrada a bruxa te viu e está correndo 
para te atacar, você vai ter que tomar uma decisão.
Você vai "sacar" seu punhal e atacar ou "correr"?
Digite sua escolha "sacar" ou "correr": ''').upper()
                if tentativa == "CORRER":
                    print('''Você é uma franguinha! Correu e não adiantou nada, a bruxa te pegou e te transformou numa joaninha!
                          GAME OVER!!!
                          ''')
                elif tentativa == "SACAR":
                    print('\nVocê é muito corajosa! Vamos ver se você terá sorte nessa luta')


                    if arma == "PUNHAL":
                        print('''Você saca seu punhal e agora deverá tentar matar a bruxa na faquinha!
\nVocê terá que conseguir golpear ela por 3 vezes, só assim você conseguirá matá-la e você terá 5 tentativas\n Vamos ver se você terá sucesso!
                        ''')
                        dificuldade = 5
                        sucessos = []
                        for _ in range(5):
                            dado = random.randint(1, 10)
                            if dado >= dificuldade:
                                sucessos.append(dado)
                        print(sucessos)
                        num_sucessos = len(sucessos)
                        print(f'Número de sucessos: {num_sucessos}')
                                
                        if num_sucessos >= 3:
                            print('''
Você conseguiu vencer a bruxa! Caramba que sorte tremenda!\n
Eu não acreditava rsrs
                                    ''')
                        else:
                            print('''
Infelizmente você não conseguiu ganhar da bruxa e ela te
transformou num franguinho.\n
Agora você servirá de jantar para os cães de guarda delas.\n
                GAME OVER!
''')

                    elif arma == "ESPADA":
                        print('Você saca sua espada e prepara-se para atacar! Você precisará conseguir golpear ela 3 vezes!')
                        dificuldade = 5
                        sucessos = []
                        for _ in range(5):
                            dado = random.randint(1, 10)
                            if dado >= dificuldade:
                                sucessos.append(dado)
                        print(sucessos)
                        num_sucessos = len(sucessos)
                        print(f'Número de sucessos: {num_sucessos}')
                                
                        if num_sucessos >= 3:
                            print('''
Você conseguiu vencer a bruxa! Caramba que sorte tremenda!\n
Eu não acreditava rsrs
                                    ''')
                        else:
                            print('''Infelizmente você não conseguiu ganhar da bruxa e ela te
transformou num franguinho.\n
Agora você servirá de jantar para os cães de guarda delas.\n
                GAME OVER!
                                    ''')

                    elif arma == "REVOLVER":
                        print('''Você saca o revólver velho do seu avô,
mas será que esse revólver velho vai mesmo disparar? kkk\n
Você tem que ser rápido porque a bruxa vem correndo na sua direção
Então você terá apenas chance de dar 2 tiros, vamos para roletar russa!!!
                        ''')
                        dificuldade = 6
                        sucessos = []
                        for _ in range(6):
                            dado = random.randint(1, 10)
                            if dado >= dificuldade:
                                sucessos.append(dado)
                        print(sucessos)
                        num_sucessos = len(sucessos)
                        print(f'Número de sucessos: {num_sucessos}')

                        if num_sucessos >= 3:
                            print('''
Caraca! O revólver disparou e você conseguiu vencer a bruxa! 
Tu é sortuda véi!\n
Eu não acreditava rsrs
''')
                        else:
                            print('''Putz!! O revólver falhou e você não conseguiu matar a bruxa
e agora ela te transformou num franguinho.\n
Agora você servirá de jantar para os cães de guarda dela.\n
                GAME OVER!
                                ''')
                    
                    if num_sucessos >= 3:
                        print('''
\nParabéns!!! Você conseguiu resgatar seu vizinho e será que vai ser recompensada?
                        ''')
                        recompensa = input('''Você começa a desamarrar seu vizinho e nota que ele está só de sunga.
Você deve ajudar a ele a se levantar, pois estava dominado sob o feitiço da bruxa má.
Agora você decide se fará alguma maldade com ele.
Você quer tentar beija-lo ou quer somente ajudar ele a levantar?
O que você vai fazer agora?\n
Digite sua escolha para tentar "beijar" ou somente tenar ajudar a "levantar": ''').upper()
                        if recompensa == "BEIJAR":
                            x = random.randrange(1,6)
                            if x >= 3:
                                print(f'''Caramba que sorte a sua, seu sonho de consumo se realizou!
Parabéns! Você conseguiu vencer a bruxa e vai descobrir que existe um mundo além da revista G Magazine!!!\n 
        {nome_jogador} WINS!!!
                                ''')
                            else:
                                print(f'''Putz!!! Seu vizinho não tem atração por você e o máximo que você
vai ganhar é uma chega pra lá garotaaa
Pense pelo lado positivo, pelo menos você salvou ele, ou era melhor deixar ser devorado hein?!
    GAME OVER para {nome_jogador}!!!
                                ''')
                        elif recompensa == "ENTREGAR":
                            x = random.randrange(1,6)
                            if x >= 3:
                                print(f'''Putz cara, você é uma franguinha, 
mal sabia que seu vizinho iria te dar um bom prêmio. 
                                      
        8====================D
                                      
Agora o que te resta é voltar para casa para continuar vendo sua revistinha G Magazine! 
    GAME OVER para {nome_jogador} !!!
                                ''')
                            else:
                                print(f'''Que cena linda você tirando ajudando seu vizinho meio tonto a se levantar, muito fofo!
Ele se encantou com isso e te deu um selinho
Pena que você continuará chupando o dedo e jogando Barbie Girl!
Pelo menos lhe sobraram os dedos né...
Vamos ver se na próxima aventura sua você consegue sair da fossa da G Magazine!!!       
                THE END!''')

        elif decisao1_1 == "CORRER":
            print('''
Você escolheu correr de volta para dentro de casa e sua mãe ordenou que você vá lavar a louça suja, o banheiro e arrumar seu quarto.
Putz véi! Que vacilo, que péssima escolha! Você saiu do quarto, deixou o video game na melhor fase de Barbie Girl rolando
e ainda vai ter que arrumar a casa!\n
Agora seu vizinho gostoso está correndo risco de vida e você vai ficar em casa tendo que arrumar as coisas!
Depois que sua mãe te da a ordem, você decide "arrumar" ou "discutir" com ela
            ''')

            decisao1_3 = input('Digite sua escolha "arrumar" ou "discutir: ').upper()
            if decisao1_3 == "ARRUMAR":
                print(f'''
                Parabéns, você é uma ótima filha!
                LOUÇAS WINSSS!!!
                {nome_jogador} LOSE!!! GAME OVER!!!
                ''')

            elif decisao1_3 == "DISCUTIR":
                print(f'''
                Putz véi! Você parece que come coco!
                Vai discutir com tua mãe?!
                Agora você acabou de tomar uma tapa nessa tua cara gorda e bolachuda e vai ficar sem jogar computador por uma semana!
                MAMÃE WINSSS!
                {nome_jogador} LOSE!!! GAME OVER!!!
                ''')

            else:
                print('''
Qual a parte você não entendeu que é para escolher entre "arrumar" ou "discutir"
Por isso que tirou nota baixa em Resolução de Problemas da Engenharia!!!
    Meu Deus do céu!
      GAME OVER!!!
                ''')
        
        else:
            print('''
Meu Deus do céu!
Mano, qual a parte você não entendeu que é para escolher entre "abrir" ou "correr"
Por isso que tirou nota baixa em Resolução de Problemas da Engenharia!!!
        GAME OVER para você!!!
            ''')

    elif decisao1 == "FICAR":
        print('''
Você escolheu ficar dentro de casa e sua mãe ordenou que você vá lavar a louça suja, o banheiro e arrumar seu quarto.
Putz véi! Que vacilo, que péssima escolha! Você saiu do quarto, deixou a partida de Barbie Girl rolando e ainda vai ter que arrumar a casa
Agora seu vizinho gostoso está correndo risco de vida e você vai ficar em casa tendo que arrumar as coisas!
Depois que sua mãe te da a ordem, você decide "arrumar" ou "discutir" com ela
''')
        decisao2_1 = input('Digite sua escolha "arrumar" ou "discutir: ').upper()
        if decisao2_1 == "ARRUMAR":
            print(f'''
Parabéns, você é uma ótima filha!\n
        LOUÇAS WINSSS!!!
     {nome_jogador} LOSE!!! 
          GAME OVER!!!
            ''')
        elif decisao2_1 == "DISCUTIR":
            print(f'''
Putz véi! Você parece que come coco!
Vai discutir com tua mãe?!
Agora você acabou de tomar uma tapa na tua cara gorda 
e bolachuda e vai ficar sem jogar video game por uma semana!\n
              MAMÃE WINSSS!
    {nome_jogador} LOSE!!! GAME OVER!!!
            ''')
        else:
            print('''
Qual a parte você não entendeu que é para escolher entre "arrumar" ou "discutir"
Por isso que tirou nota baixa em Resolução de Problemas da Engenharia!!!
Meu Deus do céu!\n
        GAME OVER!!!
            ''')

    else:
        print(f'''
Meu Deus do céu!
Mano, qual a parte você não entendeu que é para escolher entre "ir" ou "ficar"
Por isso que tirou nota baixa em Resolução de Problemas da Engenharia!!!
        GAME OVER para {nome_jogador}!!!
        ''')        