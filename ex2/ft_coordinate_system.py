import math


def parser(str_coords: str) -> tuple[int]:
    str_array = str_coords.split(',')
    int_coords = []
    try:
        for nbr in str_array:
            int_coords.append(int(nbr))
        coords = tuple(int_coords)
        return coords
    except ValueError as error:
        print("Error parsing coordinates:", error)
        print("Error details - "
              + f'Type: {type(error).__name__}, Args: {error.args}')


def distance(first: tuple[int], second: tuple[int]) -> int:
    return math.sqrt((first[0] - second[0])**2 +
                     (first[1] - second[1])**2 +
                     (first[2] - second[2])**2)


def main() -> None:
    print("=== Game Coordinate System ===\n")
    coords1 = (10, 20, 5)
    coords2 = "3,4,0"
    invalid = "abc,def,ghi"
    spawn = (0, 0, 0)
    print("Position created:", coords1)
    print(f"Distance between {spawn} and {coords1}: "
          + f"{distance(spawn, coords1):.2f}")
    print()
    print(f'Parsing coordinates: "{coords2}"')
    coords2 = parser(coords2)
    print("Parsed position", coords2)
    print(f"Distance between {spawn} and {coords2}: "
          + f"{distance(spawn, coords2):.2f}")
    print()
    print(f'Parsing invalid coordinates: "{invalid}"')
    parser(invalid)
    print()
    print("Unpaking demonstration:")
    x, y, z = coords2
    print(f"Player at x={x}, y={y}, z={z}")
    print(f"Coordinates: X={x}, Y={y}, Z={z}")


if __name__ == "__main__":
    main()
