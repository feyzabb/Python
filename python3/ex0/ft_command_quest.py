import sys


def ft_command_quest():
    total_args = len(sys.argv)
    received_args = total_args - 1

    print("=== Command Quest ===")
    print(f"Program name: {sys.argv[0]}")

    if received_args == 0:
        print("No arguments provided!")
    else:
        print(f"Arguments received: {received_args}")

        i = 1
        while i < total_args:
            print(f"Argument {i}: {sys.argv[i]}")
            i = i + 1

    print(f"Total arguments: {total_args}")


if __name__ == "__main__":
    ft_command_quest()
