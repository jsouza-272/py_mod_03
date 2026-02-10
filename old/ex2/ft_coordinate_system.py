import math


def ft_coordinate_system(first: tuple, second: tuple) -> None:
    distance = math.sqrt((first[0] - second[0])**2
                         + (first[1] - second[1])**2
                         + (first[2] - second[2])**2)
    print(f"Distance between {first} and {second}: {distance:.2f}")


def parsing(coord: str) -> tuple:
    try:
        coords = coord.split(",")
        coordinate = []
        for c in coords:
            coordinate.append(int(c))
        coordinate = tuple(coordinate)
        print(f"Parsed position: {coordinate}")
        return coordinate
    except ValueError as e:
        print(f"Error parsing coordinates: {e}")
        print(f"Error details - Type: {type(e).__name__}, Args: {e.args}")


def main() -> None:
    print("=== Game Coordinate System ===\n")
    coordinate = (10, 20, 5)
    print(f"Position created: {coordinate}")
    ft_coordinate_system((0, 0, 0), coordinate)
    print('\nParsing coodinates: "3,4,0"')
    coordinate = parsing("3,4,0")
    ft_coordinate_system((0, 0, 0), coordinate)
    print('\nParsing invalid coordinates: "abc,def,ghi"')
    parsing("abc,def,ghi")
    print("\nUnpacking demonstration:")
    (x, y, z) = coordinate
    print(f"Player at x={x}, y={y}, z={z}")
    print(f"Coordinates: x={x}, y={y}, z={z}")


if __name__ == "__main__":
    main()
