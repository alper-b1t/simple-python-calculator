def main():
    is_continue = input("işlem yapacak mısınız(y/n)").lower()
    while is_continue == "y":
        while True:
            try:
                first_number = float(input("işlem yapılacak ilk ifadeyi giriniz= "))
                second_number = float(input("işlem yapılacak ikinci ifadeyi giriniz= "))
                op = input("işlem türü giriniz= ").strip()
            except ValueError:
                print("geçersiz değer girdiniz")
            else:
                break
        hesap_makinesi(first_number, second_number, op)
        is_continue = input("işlem yapacak mısınız(y/n)").lower()


def hesap_makinesi(first_number, second_number, op):
    if op == "+":
        print(first_number + second_number)
    elif op == "-":
        print(first_number - second_number)
    elif op == "*":
        print(first_number * second_number)
    elif op == "/":
        try:
            print(first_number / second_number)
        except ZeroDivisionError:
            print("sayı sıfıra bölünemez")
    else:
        print("geçersiz işlem")


main()
