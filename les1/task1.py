""" Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

Пример:

- 6 -> да
- 7 -> да
- 1 -> нет """

numDay = int(input())
if numDay < 1 or numDay > 7:
    print("Что за дичь")
elif numDay > 0 and numDay < 6:
    print(numDay, "=> No")
else:
    print(numDay,"=> Yes")