
#Створюємо перемінні для кількості котів та кількості кіл
#Створюємо пустий список для котів у капелюхах #
#Хочемо щоб кола були від 1 до 100 
#Для "кіл" у діапазоні почанаючи з одного до 100:
    #Для "котів" у діапазоні від 1 до 100:
    
        #Якщо залишок від ділення "котів" на "кола" дорювнює 0:
            #В такому разі якщо коти є в списку cats_with_hats[]:
                #Видаляємо їх з даного списку
            #Якщо немає - додаємо у список.

#Виводимо список.







number_of_cats = 100
number_of_laps = 100
cats_with_hats = []

for lap in range(1, number_of_laps + 1):
    for cat in range(1, number_of_cats + 1):

        if cat % lap == 0:
            if cat in cats_with_hats:
                cats_with_hats.remove(cat)
            else:
                cats_with_hats.append(cat)

print(cats_with_hats)