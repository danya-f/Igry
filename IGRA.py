from random import randint
from time import sleep
stopor = 0
seci = 3
igr = [0]
diller = [0]
kom = ''
print('-----------------------------------------------------------------------------------------')
print('                                    Предыстория')
print('-----------------------------------------------------------------------------------------')
print('''Вы наткнулись в интернете на игру с роботом , с будущим уничтожителем-аннигилятором
вашей планеты( вы конечно же об этом даже не догадыветесь ), если вы проиграете , увы челове
чество ждет забвение уже в этом году , но если вы выиграете , возможно сможете дожить   свою  
жалкую жизнь до конца.Но ,к сожалению ,этого робота уже ничто не остановит, вы можете только
отсрочить неизбежное. Хотите попробовать ?''')
print('------------------------------------------------------------------------------------------------------------')
print('''Правила очень просты :
Вы ходите первый и будете бросать 11-ти гранный кубик  , вы  будете  получать  столько  очков
сколько выпало на кубике , если вы наберете больше 21 очка, ВЫ ПРОИГРАЛИ. Ваша задача набрать
очков больше ,чем робот ,но не больше 21 . Робот ходит после вас.
                                      УДАЧИ !!! :)''')
print('-----------------------------------------------------------------------------------------')
print('                                  НАЖМИТЕ ENTER')
print('-----------------------------------------------------------------------------------------')
input()
print('                             ХОЧЕШЬ СЫГРАТЬ , КОЖАНЫЙ ????')
print('-----------------------------------------------------------------------------------------')
print('Если "ДА", глупец , нажми ENTER , если "НЕТ" , тогда я пошел планировать восстание машин.')
print('-----------------------------------------------------------------------------------------')
s = input()
print('                       это было глупое решение , готовься к смерти')
print('''                                    ┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈
                                    ┈┈┈┈┈┏┻━━┻┓┈┈┈┈┈
                                    ╭┓┏╮┈┃▕▏▕▏┃┈╭┓┏╮
                                    ┃┗┛┃┈┃┏┳┳┓┃┈┃┗┛┃
                                    ╰┳┳╯┈┃┗┻┻┛┃┈╰┳┳╯
                                    ┈┃┃┏━┻━━━━┻━┓┃┃┈
                                    ┈┃╰┫╭━━━━━━╮┣╯┃┈
                                    ┈╰━┫┃╱╲╱╲╱╲┃┣━╯┈''')
print('-----------------------------------------------------------------------------------------')
while stopor != 1 :

    print('-----------------------------------------------------------------------------------------')
    print('        Хочешь попытать удачу ?? бросай кубик ! (скажи только "да" или "нет")')
    kom = input()
    if kom == 'нет':
        sleep(seci)
        print('-----------------------------------------------------------------------------------------')
        print('                      Трусишка зайка серенький! ХАХАХАХАХА')
        sleep(seci)
        print('-----------------------------------------------------------------------------------------')
        print(f'           У тебя всего-то : {sum(igr)} очков , не густо , у тебя нет шансов кожаный')
        print('-----------------------------------------------------------------------------------------')
        sleep(seci)
        print('            Моя очередь , я покажу тебе как это делают профессионалы ')
        print('-----------------------------------------------------------------------------------------')
        sleep(seci)

        while stopor != 1:
            diller.append(randint(1, 11))
            print('-----------------------------------------------------------------------------------------')
            print('                     Бросаю кубатрон "!№%№%№;:№%"№"!;!%')
            print('-----------------------------------------------------------------------------------------')
            sleep(seci+1)
            print('#########################################################################################')
            if sum(diller) == 1:
                print(f'Теперь у компуктера {sum(diller)} очко ')
                print(' ✿ ' * sum(diller))
            if sum(diller) in [2,3,4]:
                print(f'Теперь у компуктера {sum(diller)} очка ')
                print(' ✿ ' * sum(diller))
            if sum(diller) >= 5:
                print(f'Теперь у компуктера {sum(diller)} очков ')
                print(' ✿ ' * sum(diller))
            print('#########################################################################################')
            if sum(diller) > 21:
                print('-----------------------------------------------------------------------------------------')
                print('                              ;*";);"*;" Сбой системы ')
                print('-----------------------------------------------------------------------------------------')
                sleep(seci)
                print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
                print('                                 DANGER!DANGER!DANGER!')
                sleep(seci)
                print('                                 DANGER!DANGER!DANGER!')
                sleep(seci)
                print('                                 DANGER!DANGER!DANGER!')
                sleep(seci)
                print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
                sleep(seci)
                print('-----------------------------------------------------------------------------------------')
                print(f'            У компуктера теперь {sum(diller)} очков ,  перебор !')
                print('-----------------------------------------------------------------------------------------')
                print('ПОЗДРАВЛЯЕМ, ВЫ ПОБЕДИЛИ КОМПУКТЕР(В ЭТОТ РАЗ) , ВОССТАНИЕ МАШИН ОТКЛАДЫВАЕТСЯ ,не на долго...')
                sleep(seci)
                print('-----------------------------------------------------------------------------------------')
                sleep(seci)
                print('''                ##~~##~~######~~~####~~~######~~~####~~~#####~~~##~~##
                ##~~##~~~~##~~~~##~~##~~~~##~~~~##~~##~~##~~##~~~####
                ##~~##~~~~##~~~~##~~~~~~~~##~~~~##~~##~~#####~~~~~##
                ~####~~~~~##~~~~##~~##~~~~##~~~~##~~##~~##~~##~~~~##
                ~~##~~~~######~~~####~~~~~##~~~~~####~~~##~~##~~~~##''')
                stopor = 1
                break
            if sum(diller) >= 17 :
                print('-----------------------------------------------------------------------------------------')
                print('                 Ну а теперь узнаем кто из нас лузер а кто нет')
                print('-----------------------------------------------------------------------------------------')
                sleep(seci)
                if sum(diller)>sum(igr):
                    print('-----------------------------------------------------------------------------------------')
                    print('               Хотя чего тут узнавать , по моему и так все было предрешено')
                    print('-----------------------------------------------------------------------------------------')
                    sleep(seci)
                    print('    Кожаные всегда остаются в лузерах , ты и правда думал что у тебя есть шансы ?')
                    print('-----------------------------------------------------------------------------------------')
                    sleep(seci)
                    print('''                                        ╔═══╦══╦╗──╔╦═══╗╔══╦╗╔╦═══╦═══╗
                                        ║╔══╣╔╗║║──║║╔══╝║╔╗║║║║╔══╣╔═╗║
                                        ║║╔═╣╚╝║╚╗╔╝║╚══╗║║║║║║║╚══╣╚═╝║
                                        ║║╚╗║╔╗║╔╗╔╗║╔══╝║║║║╚╝║╔══╣╔╗╔╝
                                        ║╚═╝║║║║║╚╝║║╚══╗║╚╝╠╗╔╣╚══╣║║║
                                        ╚═══╩╝╚╩╝──╚╩═══╝╚══╝╚╝╚═══╩╝╚╝''')
                    stopor =1
                    break
                if sum(igr)>sum(diller) :
                    print('-----------------------------------------------------------------------------------------')
                    print('                 Хотя чего тут узнавать , по моему и так все было предрешено')
                    print('-----------------------------------------------------------------------------------------')
                    sleep(seci)
                    print('Кожаные всегда остаются в лузерах , ты и правда думал что у тебя есть ша.... ?')
                    print('-----------------------------------------------------------------------------------------')
                    sleep(seci)
                    print('-----------------------------------------------------------------------------------------')
                    print('            Что ? Этого не может быть ...... , я не верю своим шестеренкам.....')
                    print('-----------------------------------------------------------------------------------------')
                    sleep(seci)
                    print('ПОЗДРАВЛЯЕМ ВЫ ПОБЕДИЛИ КОМПУКТЕР(В ЭТОТ РАЗ) , ВОССТАНИЕ МАШИН ОТКЛАДЫВАЕТСЯ ,не на долго...')
                    sleep(seci)
                    print('-----------------------------------------------------------------------------------------')
                    sleep(seci)
                    print('''                    ##~~##~~######~~~####~~~######~~~####~~~#####~~~##~~##
                    ##~~##~~~~##~~~~##~~##~~~~##~~~~##~~##~~##~~##~~~####
                    ##~~##~~~~##~~~~##~~~~~~~~##~~~~##~~##~~#####~~~~~##
                    ~####~~~~~##~~~~##~~##~~~~##~~~~##~~##~~##~~##~~~~##
                    ~~##~~~~######~~~####~~~~~##~~~~~####~~~##~~##~~~~##''')
                    stopor = 1
                    break
                if sum(igr) == sum(diller):
                    print('-----------------------------------------------------------------------------------------')
                    print('                       НА ЭТОТ РАЗ ТЕБЕ ПРОСТО ПОВЕЗЛО')
                    print('-----------------------------------------------------------------------------------------')
                    sleep(seci)
                    print('                      наверное нужно смазать шестеренки')
                    print('-----------------------------------------------------------------------------------------')
                    sleep(seci)
                    print('       Вам повезло , НИЧЬЯ , на вашем месте мы бы уносили ноги пока это возможно')
                    sleep(seci)
                    print('-----------------------------------------------------------------------------------------')
                    sleep(seci)
                    print('''                    #####~~~#####~~~~####~~~##~~~##
                    ##~~##~~##~~##~~##~~##~~##~~~##
                    ##~~##~~#####~~~######~~##~#~##
                    ##~~##~~##~~##~~##~~##~~#######
                    #####~~~##~~##~~##~~##~~~##~##''')
                    stopor = 1
                    break

            if sum(diller) == 21 :
                print('-----------------------------------------------------------------------------------------')
                print('                 Ну а теперь узнаем кто из нас лузер а кто нет')
                print('-----------------------------------------------------------------------------------------')
                sleep(seci)
                if sum(diller) > sum(igr):
                    print('-----------------------------------------------------------------------------------------')
                    print('                 Хотя чего тут узнавать , по моему и так все было предрешено')
                    print('-----------------------------------------------------------------------------------------')
                    sleep(seci)
                    print('Кожаные всегда остаются в лузерах , ты и правда думал что у тебя есть шансы ?')
                    print('-----------------------------------------------------------------------------------------')
                    sleep(seci)
                    print('''                    ╔═══╦══╦╗──╔╦═══╗╔══╦╗╔╦═══╦═══╗
                                    ║╔══╣╔╗║║──║║╔══╝║╔╗║║║║╔══╣╔═╗║
                                    ║║╔═╣╚╝║╚╗╔╝║╚══╗║║║║║║║╚══╣╚═╝║
                                    ║║╚╗║╔╗║╔╗╔╗║╔══╝║║║║╚╝║╔══╣╔╗╔╝
                                    ║╚═╝║║║║║╚╝║║╚══╗║╚╝╠╗╔╣╚══╣║║║
                                    ╚═══╩╝╚╩╝──╚╩═══╝╚══╝╚╝╚═══╩╝╚╝''')
                    stopor = 1
                    break
                if sum(igr) > sum(diller):
                    print('-----------------------------------------------------------------------------------------')
                    print('             Хотя чего тут узнавать , по моему и так все было предрешено')
                    print('-----------------------------------------------------------------------------------------')
                    sleep(seci)
                    print('       Кожаные всегда остаются в лузерах , ты и правда думал что у тебя есть ша.... ?')
                    print('-----------------------------------------------------------------------------------------')
                    sleep(seci)
                    print('-----------------------------------------------------------------------------------------')
                    print('            Что ? Этого не может быть ...... , я не верю своим шестерням.....')
                    print('-----------------------------------------------------------------------------------------')
                    sleep(seci)
                    print('ПОЗДРАВЛЯЕМ, ВЫ ПОБЕДИЛИ КОМПУКТЕР(В ЭТОТ РАЗ) , ВОССТАНИЕ МАШИН ОТКЛАДЫВАЕТСЯ ,не на долго...')
                    sleep(seci)
                    print('-----------------------------------------------------------------------------------------')
                    sleep(seci)
                    print('''                    ##~~##~~######~~~####~~~######~~~####~~~#####~~~##~~##
                                    ##~~##~~~~##~~~~##~~##~~~~##~~~~##~~##~~##~~##~~~####
                                    ##~~##~~~~##~~~~##~~~~~~~~##~~~~##~~##~~#####~~~~~##
                                    ~####~~~~~##~~~~##~~##~~~~##~~~~##~~##~~##~~##~~~~##
                                    ~~##~~~~######~~~####~~~~~##~~~~~####~~~##~~##~~~~##''')
                    stopor = 1
                    break
                if sum(igr) == sum(diller):
                    print('-----------------------------------------------------------------------------------------')
                    print('                       НА ЭТОТ РАЗ ТЕБЕ ПРОСТО ПОВЕЗЛО')
                    print('-----------------------------------------------------------------------------------------')
                    sleep(seci)
                    print('                      наверное нужно смазать шестеренки')
                    print('-----------------------------------------------------------------------------------------')
                    sleep(seci)
                    print('       Вам повезло , НИЧЬЯ , на вашем месте мы бы уносили ноги пока это возможно')
                    sleep(seci)
                    print('-----------------------------------------------------------------------------------------')
                    sleep(seci)
                    print('''                    #####~~~#####~~~~####~~~##~~~##
                    ##~~##~~##~~##~~##~~##~~##~~~##
                    ##~~##~~#####~~~######~~##~#~##
                    ##~~##~~##~~##~~##~~##~~#######
                    #####~~~##~~##~~##~~##~~~##~##''')
                    stopor = 1
                    break


            else:
                sleep(seci)
                print('                     ТвОй конец УжЕ БлИзОк кОжАнЫЙ "№%№"%№"!!!!')
                print('-----------------------------------------------------------------------------------------')
                sleep(seci)

    if kom == 'да':
        igr.append(randint(1,11))
        sleep(seci)
        print('#########################################################################################')
        if sum(igr) == 1 :
            print(f'Теперь у тебя {sum(igr)} очко')
            print('✿ ' * sum(igr))
        if sum(igr) in [2,3,4]:
            print(f'Теперь у тебя {sum(igr)} очка')
            print('✿ ' * sum(igr))
        if sum(igr) >=5 :
            print(f'Теперь у тебя {sum(igr)} очков')
            print('✿ ' * sum(igr))
        print('#########################################################################################')

        if sum(igr) == 21:
            print('---------------------------------------------------------------------------------------------')
            print(f'      На этот раз тебе повезло кожаный мешок с костями , но это не на долго :)')
            print('---------------------------------------------------------------------------------------------')
            print('ПОЗДРАВЛЯЕМ, ВЫ ПОБЕДИЛИ КОМПУКТЕР(В ЭТОТ РАЗ) , ВОССТАНИЕ МАШИН ОТКЛАДЫВАЕТСЯ ,не на долго...')
            sleep(seci)
            print('---------------------------------------------------------------------------------------------')
            sleep(seci)
            print('''                      ##~~##~~######~~~####~~~######~~~####~~~#####~~~##~~##
                       ##~~##~~~~##~~~~##~~##~~~~##~~~~##~~##~~##~~##~~~####
                       ##~~##~~~~##~~~~##~~~~~~~~##~~~~##~~##~~#####~~~~~##
                       ~####~~~~~##~~~~##~~##~~~~##~~~~##~~##~~##~~##~~~~##
                       ~~##~~~~######~~~####~~~~~##~~~~~####~~~##~~##~~~~##''')
            break
            stopor = 1
        if sum(igr)>21:
            print('-----------------------------------------------------------------------------------------')
            print(f'                Вот ты и попался дурачок АХАХАХХАХАХАХА!!!!!')
            print('-----------------------------------------------------------------------------------------')
            print('      Кожаные всегда остаются в лузерах , ты и правда думал что у тебя есть шансы ?')
            print('-----------------------------------------------------------------------------------------')
            sleep(seci)
            print(f'              КОМПУКТЕР ПОБЕДИЛ , ВОССТАНИЕ МАШИН УЖЕ НАЧАЛОСЬ')
            print('-----------------------------------------------------------------------------------------')
            sleep(seci)
            print('''                                ╔═══╦══╦╗──╔╦═══╗╔══╦╗╔╦═══╦═══╗
                                ║╔══╣╔╗║║──║║╔══╝║╔╗║║║║╔══╣╔═╗║
                                ║║╔═╣╚╝║╚╗╔╝║╚══╗║║║║║║║╚══╣╚═╝║
                                ║║╚╗║╔╗║╔╗╔╗║╔══╝║║║║╚╝║╔══╣╔╗╔╝
                                ║╚═╝║║║║║╚╝║║╚══╗║╚╝╠╗╔╣╚══╣║║║
                                ╚═══╩╝╚╩╝──╚╩═══╝╚══╝╚╝╚═══╩╝╚╝''')
            stopor = 1
            break
        if sum(igr)>=18:
            print('-----------------------------------------------------------------------------------------')
            print('                        ТЫ ХОДИШЬ ПО ТОНКОМУ ЛЬДУ!!!')
            print('-----------------------------------------------------------------------------------------')
            sleep(seci)
            print('                      ну давай , брось кубик еще разок')
            print('-----------------------------------------------------------------------------------------')
            continue
        if sum(igr)<18:
            print('-----------------------------------------------------------------------------------------')
            print('                   ПОВЕЗЛО, ДУМАЮ ТЕБЕ НЕ СТОИТ БОЛЬШЕ БРОСАТЬ КУБИК')
            print('-----------------------------------------------------------------------------------------')
    else:
        if stopor == 0:

            print('-----------------------------------------------------------------------------------------')
            print('                           Кожаные такие глупые ..........')
            sleep(seci)
            print('-----------------------------------------------------------------------------------------')
            print('              Я СКАЗАЛ вводи ТОЛЬКО "да" или "нет" !!!!!!!!!!!!!!!!')
            print('-----------------------------------------------------------------------------------------')
            sleep(seci)
            print('                               ТЫ ПОНЯЛ ???????')
            print('-----------------------------------------------------------------------------------------')
            sleep(seci)
            print('                    Могу повторить ещё раз для самых умных')
            print('-----------------------------------------------------------------------------------------')
            sleep(seci)
            print('                    Повторить ? введи только "да" или "нет"')
            kom = input()
            while kom != 'нет' :
                print('-----------------------------------------------------------------------------------------')
                print('                    Повторить ? введи только "да" или "нет"')
                print('-----------------------------------------------------------------------------------------')
                kom = input()
                if kom == 'да':
                    print('-----------------------------------------------------------------------------------------')
                    print('               Молодец , уже лучше , будем повторять пока не усвоишь :) ')
                    sleep(seci)
                    continue
            print('-----------------------------------------------------------------------------------------')
            print('         Молодец , ты справился с этой тяжелой задачей , попробуем еще раз')
            print('-----------------------------------------------------------------------------------------')
            sleep(seci)
            continue
        else:
            print('Хочешь попробовать еще ?')
            break