def run():
    # for contador in range(1000):
    #     if contador % 2 != 0:
    #         continue
    #     print(contador)

    # for i in range(10000):
    #     if i == 3737:
    #         break
    #     print(i)

    palabra = input("Introduce una frase: ")
    for i in palabra:
        if i == "o" or i == "O":
            break
        print(i)

if __name__ == "__main__":
    run()