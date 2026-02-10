import sys


def utf8toi() -> list[int] | None:
    scores = []
    try:
        for av in sys.argv[1:]:
            scores.append(int(av))
    except ValueError as error:
        print(error)
        return None
    return scores


def basic_stats(scores: list[int]) -> None:
    ln = len(scores)
    sm = sum(scores)
    mx = max(scores)
    mn = min(scores)
    print(f"Scores processed: {scores}")
    print(f"Total players: {ln}")
    print(f"Average score: {(sm / ln):.1f}")
    print(f"High score: {mx}")
    print(f"Low score: {mn}")
    print(f"Score range: {mx - mn}")


def main() -> None:
    print("=== Player Score Analytics ===")
    if len(sys.argv) == 1:
        print("No scores provided. "
              + f"Usage: python3 {sys.argv[0]} <score1> <score2> ...")
        return
    scores = utf8toi()
    if scores is None:
        return
    else:
        basic_stats(scores)


if __name__ == "__main__":
    main()
