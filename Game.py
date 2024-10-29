time = 0
day = 1

people = False
water = False
flare_gun = False
shelter = False
resources = {
    'food': 1,
    'fuel': 1,
}

def start_game():
    print("\nДобро пожаловать на _Остров заброшенных мечт_!")
    print("\n|ВВЕДЕНИЕ|")
    print("Вы — единственный выживший после кораблекрушения.")
    print("Остров покрыт густыми джунглями, а вокруг него бушует океан.")
    print("Ваша цель — выжить, исследовать остров и найти способ покинуть его.")
    print("\n|НАЧАЛО ПРИКЛЮЧЕНИЙ|")
    print("Вы просыпаетесь на пляже, окруженном обломками вашего корабля.")
    print("У вас есть несколько предметов: рюкзак, кусок дерева, фляга с водой и зажигалка.")
    print("Вы сразу понимаете, что вам КРУПНО повезло и не стоит медлить, так как еды хватит на 2 дня.")
    first_choice()

def first_choice():
    global time, day, shelter, resources, people
    if day < 3 and time == 3 and shelter:
        print("\nУже темнеет. Стоит вернуться в убежище.")
        response = input("Вернуться? (да/нет): ")
        if response == 'да':
            if resources['fuel'] > 0:    
                if resources['food'] > 0:
                    if flare_gun:
                        flare_gun_win()
                        return
                    else:
                        time -= 3
                        resources['food'] -= 1
                        resources['fuel'] -= 1
                        day += 1
                        print("Вы благополучно пережили эту ночь, но нельзя останавливать. Воды:", resources['food'], " топлива для кострища: ", resources['fuel'])    
                else:
                    food_lose()
                    return       
            else:
                fuel_lose()
                return
        else:
            print("")
            play_again()
            return
    elif time == 3 and not shelter:
        night_lose()
        return
    elif day == 3:
        day_lose()
        return
    
    print("\nЧто вы хотите сделать?")
    print("1. Исследовать пляж")
    print("2. Зайти в джунгли")
    print("3. Проверить обломки корабля")
    
    if time == 0 and day == 1:
        print("4. Хто я такой?")
        
    choice = input("Введите номер вашего выбора: ")
    if choice == '1':
        explore_beach()
    elif choice == '2':
        enter_jungle()
    elif choice == '3':
        check_wreckage()
    elif choice == '4' and time == 0 and day == 1:
        memory_loss()
    else:
        print("Неверный ввод. Попробуйте снова.")
        first_choice()

def explore_beach():
    global time, resources, people
    if time == 3:
        first_choice()
        return
    elif time == 2:
        print("Уже темнеет. У вас есть последний шанс найти убежище для ночлега.")    
    print("\n|ПЛЯЖ|")
    print("Что вы хотите сделать?")
    print("1. Собрать ракушки и камни")
    print("2. Пособирать веток и листьев на кострище")
    print("3. Проверить, нет ли других людей на острове")
    print("4. Подумать что ещё можно предпринять")

    choice = input("Введите номер вашего выбора: ")
    
    if choice == '1':
        print("\nВы пособирали красивые ракушки, но вы зря потратили время.")
        time += 1
        explore_beach()
        
    elif choice == '2':
        print("\nВы пособирали палок и сухих листьев для кострища и сложили все в свой рюкзак.")
        time += 1
        resources['fuel'] += 1
        explore_beach()
        
    elif choice == '3':
        if not people:
            print("\nВы не нашли других людей на острове, но есть предчувствие, что стоит поискать ещё.")
            time += 1
            people = True
            explore_beach()
        else:
            people_lose() 
            
    elif choice == '4':
        first_choice()
    else:
        print("Неверный ввод. Попробуйте снова.")    
        explore_beach()

def enter_jungle():
    global time, resources, water, shelter  
    if time == 3:
        first_choice()
        return
    elif time == 2:
        print("Уже темнеет. У вас есть последний шанс найти убежище для ночлега.")        
    print("\n|ДЖУНГЛИ|")
    print("\nВы углубляетесь в джунгли, полные звуков природы и необычных растений.")
    
    print("Что вы хотите сделать?")
    print("1. Следовать за звуками ручья")
    print("2. Искать съедобные растения")
    
    if not shelter:
        print("3. Пойти в глубь джунглей")
        print("4. Подумать что ещё можно предпринять")
    else:
        print("3. Подумать что ещё можно предпринять")    
    
    choice = input("Введите номер вашего выбора: ")
    
    if choice == '1':
        if not water:
            print("\nВы нашли пресный источник воды и безопасное место для лагеря!")
            resources['food'] += 1
            time += 1
            water = True
            enter_jungle()
        else:
            print("\nВам не повезло: у ручья были дикие животные. Они на вас напали и убили...")
            play_again()
            
    elif choice == '2':
        print("\nЭто была ошибка. На этом острове много ядовитых растений, и вы отравились.")
        play_again()
        
    elif choice == '3' and not shelter:
        print("\nВам невероятно повезло: вы нашли хижину в скале!")
        time += 1
        shelter = True
        enter_jungle()
        
    elif choice == '3' and shelter:
        first_choice()
        
    elif choice == '4' and not shelter:
        first_choice()
        
    else:
        print("Неверный ввод. Попробуйте снова.")
        enter_jungle()

def check_wreckage():
    global time, flare_gun, shelter
    if time == 3:
        first_choice()
        return
    elif time == 2:
        print("Уже темнеет. У вас есть последний шанс найти убежище для ночлега.")    
    print("\n|КОРАБЛЬ|")
    
    print("\nВы решаете осмотреть обломки вашего корабля после крушения.")
    
    print("Что вы хотите сделать?")
    print("1. Поискать членов экипажа")
    print("2. Проверить запасы еды, воды и других ресурсов")
    
    if not shelter:
        print("3. Побродить по кораблю")
        print("4. Подумать что ещё можно предпринять")
    else:
        print("3. Подумать что ещё можно предпринять")

   
    choice = input("Введите номер вашего выбора: ")

    if choice == '1':
        print("\nК сожалению, все ваши товарищи погибли и вы долго не могли отойти от увиденного. Вы потратили время впустую.")
        time += 1
        check_wreckage()
        
    elif choice == '2':
        print("\nВы нашли флягу воды и дополнительно сигнальную ракету. После проверки на работоспособность вы поняли, что она вся промокла и её надо высушить (возможно это получится возле кострища).")
        time += 1
        resources['food'] += 1
        flare_gun = True
        check_wreckage()
        
    elif choice == '3' and not shelter:
        print("\nВы бродите по кораблю. Тут почти всё сломано, но пару кают осталось целыми и вы решили остаться ночью именно здесь.")
        time += 1
        shelter = True
        check_wreckage()
        
    elif choice == '3' and shelter:
        first_choice()
        
    elif choice == '4' and not shelter:
        first_choice()

    else:
        print("Неверный ввод. Попробуйте снова.")
        check_wreckage()

def memory_loss():
   print("\nКто-то потерял память. Пока вы разбирались, что произошло, уже стемнело и дикие животные вас съели.")
   play_again()

def night_lose():
   print("К сожалению, вы не нашли убежище для ночлега и вас съели дикие животные...")
   play_again()

def fuel_lose():
   print("К сожалению, хоть вы и в убежище, но эта ночь оказалась достаточно холодной и вы замерзли...")
   play_again()

def flare_gun_win():
   print("Вы сумели просушить сигнальную ракету и запустили её. Вы выжили!")
   play_again()

def food_lose():
   print("К сожалению, хоть вы и в убежище и в тепле, но воды не осталось и вы засохли...")
   play_again()

def day_lose():
   print("Вы наткнулись на людей. Вы поначалу обрадовались, но это оказалось старинное племя недолюбливающее чужеземцев. Сегодняшним главным блюдом являетесь вы...")
   play_again()

def people_lose():
   print("На другой стороне пляжа вы нашли племя живущее на этом острове. Они недолюбливают чужеземцев. Сегодняшним главным блюдом являетесь вы...")
   play_again()  
   
def play_again():
   response = input("\nХотите сыграть еще раз? (да/нет): ")
   if response == 'да':
       global time, day, shelter, resources, people, water  
       time = 0
       day = 1
       shelter = False
       resources['food'] = 1
       resources['fuel'] = 1
       people = False
       water = False
       start_game()
   else:
        print("Спасибо за игру!")
        return
if __name__ == "__main__":
   start_game()