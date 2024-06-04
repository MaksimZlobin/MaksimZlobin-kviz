#print ("добро пожаловать в квиз по стартапам!")
#answer="Стартап"
#print ("добро пожаловать в квиз по стартапам!")
#print("Ответьте на следующие вопросы:")
#question= "Как называется компания, которая создается для развития новой идеи или инновационного продукта?"
#answer="Стартап"
#product = imput("Введи продукт: ")
#money = int(imput("Введи цену продукта: "))

#print("Сегодня скидки!")
#print("Вы", product, "за",money - 10, "рублей")
#product =input("Введите название товара: ")
#price = int(input("Введите цену товара: "))
#a = int(5.99999)
#print(a)
#from typing import Text


#x =  int(float(input( 6.4444444)))
#x = str(5)
#print(x)
#x = str(type(5))
#print(x)
#name = "vlad"
#messenge ="hello"
#print(messenge + name )
#name = "vlad"
#messenge ="hello"
#print(messenge + " " + name )
#a = "11"
#b = "22"
#с = (a + b)
#print(c)
#numbers = int( 123456789 )
#letters = "Я программист!"
#print(numbers, letters)
print("Добро пожаловать в квиз по стартапам!")
print("Ответь на следующие вопросы:")
answer="Стартап"

questions = ["1. Как называется компания, которая создается для развития новой идеи или инновационного продукта?", "2. Как назвается человек или компания, который вкладывает деньги в бизнес с целью получения прибыли?", "3. Как называется капитал, который дают инвесторы на развитие стартапа?", "4. Как пишется минимально жизнеспособный продукт, который создается для тестирования идей и концепций?", "5. Какой план создают перед тем, как открывать стартап и занимать деньги?", "6. Как называются другие компании на рынке, которые предлагают аналогичные товары или услуги?", "7. Как называется разница между выручкой и затратами компании?"]

answers = [
    "Стартап",
    "Инвестор",
    "Инвестиция",
    "MVP",
    "Бизнес-план",
    "Конкуренты",
    "Прибыль"
] 
score = 0

print(questions[0])
user_answer = input("Введи свой ответ: ")
if user_answer.lower() == answers[0].lower():
    print("Правильно!")
    score = score + 1
else:
    print("Неправильно.")
print(questions[1])
user_answer = input("Введи свой ответ: ")
if user_answer.lower() == answers[1].lower():
      print("Правильно!")
      score = score +1
else:
      print("Неправильно.")
print(questions[2])
user_answer = input("Введи свой ответ: ")
if user_answer.lower() == answers[2].lower():
      print("Правильно!")
      score = score +1
else:
      print("Неправильно.")
print(questions[3])
user_answer = input("Введи свой ответ: ")
if user_answer.lower() == answers[3].lower():
        print("Правильно!")
        score = score +1
else:
        print("Неправильно.")
print(questions[4])
user_answer = input("Введи свой ответ: ")
if user_answer.lower() == answers[4].lower():
          print("Правильно!")
          score = score +1
else:
          print("Неправильно.")
print(questions[5])
user_answer = input("Введи свой ответ: ")
if user_answer.lower() == answers[5].lower():
          print("Правильно!")
          score = score +1
else:
          print("Неправильно.")
print(questions[6])
user_answer = input("Введи свой ответ: ")
if user_answer.lower() == answers[6].lower():
            print("Правильно!")
            score = score +1
else:
            print("Неправильно.")

print("Вы набрали", score, "баллов")

if score > 5 :
    print("Это отличный результат! Ты много знаешь о стартапах.")
elif score > 3 :
    print("Неплохой результат! Как здорово, что тебе предстоит узнать ещё так много о стартапах.")
else:
    print("Видимо, ты только начинаешь свой путь к стартапам! Ты ещё много чего узнаешь о мире, где мы живём.")