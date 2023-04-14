import pandas as pd

fileName = "Sample.xlsx"
df = pd.read_excel(fileName)

def sort():
    print("Отсортировать по:\n1)Полу\n2)Уровню подготовки\n3)Структурному подразделению\n4)Форме обучения\n5)Курсу\n6)Гражданству")
    mv = int(input())
    student = pd.DataFrame
    if mv == 1:
        print("Выберите пол:\n1)Мужской\n2)Женский")
        sex = int(input())
        if (sex == 1):
            student = df[df["SEX"] == "Мужской"]
        elif sex == 2:
            student = df[df["SEX"] == "Женский"]
        if student.empty:
            print("Что=то пошло не так, введите данные заново")
        else:
            print(student)
    elif mv == 2:
        print("Выберите уровень подготовки:\n1)Бакалавр\n2)Специалист\n3)Магистр\n4)Дополнительная общеразвивающая программа\n5)Прикладной бакалавр")
        degree = int(input())
        if degree == 1:
            student = df[df["URPODG"] == "Бакалавр"]
        elif degree == 2:
            student = df[df["URPODG"] == "Специалист"]
        elif degree == 3:
            student = df[df["URPODG"] == "Магистр"]
        elif degree == 4:
            student = df[df["URPODG"] == "Дополнительная общеразвивающая программа"]
        elif degree == 5:
            student = df[df["URPODG"] == "Прикладной бакалавр"]
        if student.empty:
            print("Что=то пошло не так, введите данные заново")
        else:
            print(student)
    elif mv == 3:
        print("Выберите структурное подразделение:\n1)ИКТИБ\n2)ИРТСУ\n3)ИУЭС\n4)ИНЭП")
        faculty = int(input())
        if faculty == 1:
            student = df[df["FACULTY"] == "ИКТИБ"]
        elif faculty == 2:
            student = df[df["FACULTY"] == "ИРТСУ"]
        elif faculty == 3:
            student = df[df["FACULTY"] == "ИУЭС"]
        elif faculty == 4:
            student = df[df["FACULTY"] == "ИНЭП"]
        if student.empty:
            print("Что=то пошло не так, введите данные заново")
        else:
            print(student)
    elif mv == 4:
        print("Выберите форму обучения:\n1)Очная\n2)Заочная\n3)Очно-заочная")
        studyForm = int(input())
        if studyForm == 1:
            student = df[df["FOBUCH"] == "Очная"]
        if studyForm == 2:
            student = df[df["FOBUCH"] == "Заочная"]
        elif studyForm == 3:
            student = df[df["FOBUCH"] == "Очно-заочная"]
        if student.empty:
            print("Что=то пошло не так, введите данные заново")
        else:
            print(student)
    elif mv == 5:
        print("Выберите курс обучения:\n1)1\n2)2\n3)3\n4)4\n5)5\n6)6")
        course = int(input())
        student = df[df["KURS"] == course]
        if student.empty:
            print("Что=то пошло не так, введите данные заново")
        else:
            print(student)
    elif mv == 6:
        print("Выберите гражданство:\n1)Российская Федерация\n2)Туркменистан")
        citizenship = int(input())
        if citizenship == 1:
            student = df[df["CITIZEN"] == "Российская Федерация"]
        elif citizenship == 2:
            student = df[df["CITIZEN"] == "Туркменистан"]
        if student.empty:
            print("Что=то пошло не так, введите данные заново")
        else:
            print(student)
def switch(move):
    if move == 1:
        print(df)
    elif move == 2:
        sort()
    elif move == 3:
        print('Введите адрес электронной почты:')
        mailAddr = input()
        student = df[df["EMAIL"] == mailAddr]
        if (student.empty):
            print("Студент с таким адресом электронной почты не найден")
        else:
            print(student)
    elif move == 4:
        print("Введите номер телефона в формате \"+7 (xxx) xxx-xx-xx\":")
        phoneNum = input()
        student = df[df["NUMBER"] == phoneNum]
        if (student.empty):
            print("Студент с таким номером телефона не найден")
        else:
            print(student)
    elif move == 5:
        return

    print("Выберите действие:\n1)Вывести данные\n2)Отсортировать данные\n3)Найти по почте\n4)Найти по номеру телефона\n5)Выход")
    move = int(input())
    switch(move)

def main():
    print("Выберите действие:\n1)Вывести данные\n2)Отсортировать данные\n3)Найти по почте\n4)Найти по номеру телефона\n5)Выход")
    move = int(input())
    switch(move)

if __name__ == "__main__":
    main()