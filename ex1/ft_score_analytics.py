import sys


def ft_score_analytics() -> None:
    if len(sys.argv) == 1:
        print("No scores provided. Usage: \
python3 ft_score_analytics.py <score1> <score2> ...")
        return
    scores = []
    try:
        for s in sys.argv[1:]:
            scores.append(int(s))
    except Exception as e:
        print(e)
        return
    print(f"Scores processed: {scores}")
    print(f"Total players: {len(sys.argv[1:])}")
    print(f"Total score: {sum(scores)}")
    print(f"Average score: {(sum(scores) / len(sys.argv[1:])):.1f}")
    print(f"High score: {max(scores)}")
    print(f"Low score: {min(scores)}")
    print(f"Score range: {max(scores) - min(scores)}")


if __name__ == "__main__":
    print("=== Player Score Analytics ===")
    ft_score_analytics()
    print()
