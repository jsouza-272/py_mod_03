import sys


def you_have_no_desires() -> None:
    print("Tell me your wish!")
    print(f"Name of desire: {sys.argv[0]}")
    print(f"Total desires: {len(sys.argv)}")


def i_heard_your_wish() -> None:
    print(f"Name of desire: {sys.argv[0]}")
    print(f"Wishes received: {len(sys.argv[1:])}")
    nbr = 1
    for wish in sys.argv[1:]:
        print(f"Wish {nbr}: {wish}")
        nbr += 1
    print(f"Total desires: {len(sys.argv)}")


def main() -> None:
    print("=== Command Quest ===")
    if len(sys.argv) <= 1:
        you_have_no_desires()
    else:
        i_heard_your_wish()


if __name__ == "__main__":
    main()
