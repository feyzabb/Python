import math


def get_player_pos():
    while True:
        user_input = input("Enter new coordinates as floats"
                           "in format 'x,y,z': ")
        input_parts = user_input.split(",")

        if len(input_parts) != 3:
            print("Invalid syntax")
            continue

        try:
            current = input_parts[0]
            x = float(current)

            current = input_parts[1]
            y = float(current)

            current = input_parts[2]
            z = float(current)

            return (x, y, z)

        except ValueError as e:
            print(f"Error on parameter '{current}': {e}")


def main():
    print("=== Game Coordinate System ===")
    print()

    print("Get a first set of coordinates")
    pos1 = get_player_pos()

    print(f"Got a first tuple: {pos1}")
    print(f"It includes: X={pos1[0]}, Y={pos1[1]}, Z={pos1[2]}")

    dist_to_center = math.sqrt(pos1[0] ** 2 + pos1[1] ** 2 + pos1[2] ** 2)
    print(f"Distance to center: {round(dist_to_center, 4)}")

    print()
    print("Get a second set of coordinates")
    pos2 = get_player_pos()

    dist_between = math.sqrt(
        (pos2[0] - pos1[0]) ** 2
        + (pos2[1] - pos1[1]) ** 2
        + (pos2[2] - pos1[2]) ** 2
    )

    print(f"Distance between the 2 sets of coordinates: "
          f"{round(dist_between, 4)}")


if __name__ == "__main__":
    main()
