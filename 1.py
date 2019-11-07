# Написать функцию, которая будет принимать два параметра A и N.
# Функция должна возвести число A в целую степень N, и вернуть ответ


def turn_to_1(n):
    while n == int:
        if n % 2 == 0:
            n /= 2
            if n == 1:
                break
        if n % 2 == 1:
            n = (n * 3 + 1) / 2
            if n == 1:
                break
    return n


if __name__ == "__main__":
    n = int(input("insert the number: \n"))
    result = turn_to_1(n)
    print("Yes")