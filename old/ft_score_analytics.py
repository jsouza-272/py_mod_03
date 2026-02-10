import sys


def ft_score_analytics():
    if len(sys.argv) <= 1:
        print("No argument is passed")
        return
    scores = []
    try:
        for score in sys.argv[1:]:
            scores.append(int(score))
    except ValueError as e:
        print(e)
        return
    print(f"scores: {scores}")
    print(f"len: {len(scores)}")
    print(f"sum: {sum(scores)}")
    print(f"max: {max(scores)}")
    print(f"min: {min(scores)}")
    print(f"sorted: {sorted(scores)}")
    high_score = [score for score in scores if score > 2000]
    print(f"High scores (>2000): {high_score}")
    low_score = [score for score in scores if score <= 2000]
    print(f"Low scores (<=2000): {low_score}")
    print(scores)
    print(f"second: {scores[::2]}")


if __name__ == "__main__":
    ft_score_analytics()
