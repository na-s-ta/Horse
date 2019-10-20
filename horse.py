name = input("Как тебя зовут?\n")
print("Привет,", name)
age = input("Сколько тебе лет?\n")
if int(age) < 10:
    print("О, тебе нужно учить робототехнику ;)")
if (int(age) > 10) and (int(age) < 20):
    print("Отлично, тебе уже" , age, "лет")
    print("Уже даааавно пора учить Python :)")
