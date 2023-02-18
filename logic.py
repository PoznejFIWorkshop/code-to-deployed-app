# This code is intentionaly badly written - you should fix it. :)
# You can get help at https://edulint.com/


def factorial(n: int) -> int:
    assert n >= 0, "This factorial function only works for n >= 0"

    if n in [0, 1]:
        return 1
    else:
        answer = 1
        for i in range(2, n+1):
            answer = answer * i
        return answer


if __name__ == "__main__":
    n = input("Input n for calculation of factorial: ")
    answer = factorial(int(n))
    print(f"{n}! = {answer}")
