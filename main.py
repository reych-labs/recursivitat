def hanoi_tower(n, from_disc, to_disc, aux):
    if n == 1:
        print("Mou el disc 1 des de",from_disc, "fins a", to_disc)
    else:
        hanoi_tower(n - 1, from_disc, aux, to_disc)
        print("Mou el disc", n, "des de", from_disc, "fins a", to_disc)
        hanoi_tower(n - 1, aux, to_disc, from_disc)

def main():
    n = int(input("Introdueix el nombre de discos: "))
    hanoi_tower(n, 'A', 'C', 'B')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
