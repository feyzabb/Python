import importlib
import importlib.metadata
import importlib.util


def check_dependencies() -> bool:
    print("LOADING STATUS: Loading programs...\n")
    print("Checking dependencies:")

    packages: dict[str, str] = {
        'pandas': 'Data manipulation ready',
        'numpy': 'Numerical computation ready',
        'matplotlib': 'Visualization ready'
    }

    all_ready: bool = True

    for pkg, desc in packages.items():
        spec = importlib.util.find_spec(pkg)
        if spec is not None:
            try:
                version = importlib.metadata.version(pkg)
                print(f"[OK] {pkg} ({version}) - {desc}")
            except importlib.metadata.PackageNotFoundError:
                print(f"[OK] {pkg} (unknown) - {desc}")
        else:
            print(f"[MISSING] {pkg} - {desc}")
            all_ready = False

    print()

    if not all_ready:
        print("ERROR: Missing dependencies detected!")
        print("Please install the required packages using one of the following methods:\n")
        print("Using pip:")
        print("  pip install -r requirements.txt\n")
        print("Using Poetry:")
        print("  poetry install")
        print("  poetry run python loading.py")
        return False

    return True


def run_analysis() -> None:
    import numpy as np  # type: ignore
    import pandas as pd  # type: ignore
    import matplotlib.pyplot as plt  # type: ignore

    print("Analyzing Matrix data...")
    print("Processing 1000 data points...")

    matrix_data = np.random.rand(1000, 2)

    df = pd.DataFrame(matrix_data, columns=['X', 'Y'])

    print("Generating visualization...\n")

    plt.figure(figsize=(8, 6))
    plt.scatter(df['X'], df['Y'], alpha=0.5, c='green')
    plt.title('Matrix Data Analysis')
    plt.xlabel('X Coordinate')
    plt.ylabel('Y Coordinate')

    plt.savefig('matrix_analysis.png')

    print("Analysis complete!")
    print("Results saved to: matrix_analysis.png")


def main() -> None:
    if check_dependencies():
        run_analysis()


if __name__ == "__main__":
    main()
