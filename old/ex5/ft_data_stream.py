import time
from typing import Generator


def event_generator(qnt: int):
    if qnt % 2 == 0:
        event = "found tresure"
    elif qnt % 3 == 0:
        event = "leveled up"
    else:
        event = "killed monster"
    return event


def player_generator(qnt: int, event: str):
    player = ["bob", "charlie", "alice"]
    base = qnt
    if event == "killed monster":
        base += 11
    elif event == "found tresure":
        base += 5
    else:
        base += 17
    index = base % 3
    return player[index]


def generator(qnt: int) -> Generator[tuple[str, int, str], None, None]:
    players = {
        "alice": 5,
        "bob": 12,
        "charlie": 3
    }
    for i in range(qnt):
        event = event_generator(i + 1)
        player = player_generator(i, event)
        if event == "leveled up":
            players[player] += 5
        yield player, players[player], event


def fibonacci() -> Generator[int, None, None]:
    n1 = 0
    n2 = 1
    result = 0
    while True:
        yield result
        n1 = n2
        n2 = result
        result = n1 + n2


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    i = 2
    while i < n:
        if n % i == 0:
            return False
        i += 1
    return True


def prime() -> Generator[int, None, None]:
    nbr = 0
    c = 0
    while True:
        if is_prime(nbr):
            yield nbr
            c += 1
        nbr += 1


def main():
    print("=== Game Data Stream Processor ===\n")
    qnt = 1000
    event_nbr = 0
    high_level = 0
    treasure_event = 0
    level_up_event = 0
    processing_time = time.time()
    iterator = generator(qnt)
    print(f"Processing {qnt} game events...\n")
    for _ in range(qnt):
        p, l, e = next(iterator)
        event_nbr += 1
        if event_nbr <= 3:
            print(f"Event {event_nbr}: Player {p} (level {l}), {e}")
        if event_nbr == 3:
            print("...")
        if l > 10:
            high_level += 1
        if e == "found tresure":
            treasure_event += 1
        if e == "leveled up":
            level_up_event += 1
    processing_time = time.time() - processing_time
    print("\n=== Stream Analytics ===")
    print(f"Total events processed: {qnt}")
    print(f"High-level players (10+) {high_level}")
    print(f"Treasure events: {treasure_event}")
    print(f"Level-up events: {level_up_event}")
    print("\nMemory usage: Constant (streaming)")
    print(f"Processing time: {processing_time:.3f} seconds")
    print("\n=== Generator Demonstration ===")
    fib = ""
    ctrl = 1
    iterator = fibonacci()
    while ctrl <= 10:
        fib += f"{next(iterator)}"
        if ctrl < 10:
            fib += ", "
        ctrl += 1
    print(f"Fibonacci sequence (first 10): {fib}",)
    # prm = ""
    # ctrl = 1
    # for p in prime():
    #     prm += f"{p}"
    #     if ctrl < 5:
    #         prm += ", "
    #         ctrl += 1
    # print(f"Prime numbers (first 5): {prm}")


if __name__ == "__main__":
    main()
