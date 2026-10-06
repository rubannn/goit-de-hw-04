import part1
import part2
import part3

PARTS = {
    "1": part1.run,
    "2": part2.run,
    "3": part3.run,
}


def main() -> None:
    choice = input("Яку частину запустити? (1-3): ").strip()

    run = PARTS.get(choice)
    if run is None:
        print("Невірний вибір. Введіть 1, 2 або 3.")
        return

    run()


if __name__ == "__main__":
    main()
