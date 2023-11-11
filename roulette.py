a = int (input())
if a == 0:
    print ("зеленый")
if ((1 <= a <= 10) or (19 <= a <= 28)) and a % 2 == 0:
    print ("черный")
if ((1 <= a <= 10) or (19 <= a <= 28)) and a % 2 != 0:
        print ("красный")
if ((11 <= a <= 18) or (29 <= a <= 36)) and  a % 2 == 0:
            print ("красный")
if ((11 <= a <= 18) or (29 <= a <= 36)) and  a % 2 != 0:
    print ("черный")
if  a > 36:
    print ("ошибка ввода")