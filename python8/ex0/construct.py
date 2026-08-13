import sys
import os
import site


def main() -> None:
    try:
        is_venv: bool = sys.prefix != sys.base_prefix

        if not is_venv:
            print("MATRIX STATUS: You're still plugged in\n")

            print(f"Current Python: {sys.executable}")
            print("Virtual Environment: None detected\n")

            print("WARNING: You're in the global environment!")
            print("The machines can see everything you install.\n")

            print("To enter the construct, run:")
            print("python -m venv matrix_env")
            print("source matrix_env/bin/activate # On Unix")
            print("matrix_env\\Scripts\\activate  # On Windows\n")

            print("Then run this program again.")

        else:
            venv_path: str | None = os.environ.get('VIRTUAL_ENV')
            venv_name: str = (
                os.path.basename(venv_path) if venv_path else "Unknown"
            )

            print("MATRIX STATUS: Welcome to the construct\n")

            print(f"Current Python: {sys.executable}")
            print(f"Virtual Environment: {venv_name}")
            print(f"Environment Path: {sys.prefix}\n")

            print("SUCCESS: You're in an isolated environment!")
            print("Safe to install packages without affecting")
            print("the global system.\n")

            print("Package installation path:")

            site_packages = site.getsitepackages()
            if site_packages:
                print(site_packages[0])

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
