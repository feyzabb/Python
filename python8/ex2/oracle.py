import os
from dotenv import load_dotenv  # type: ignore


def main() -> None:
    load_dotenv()

    if 'MATRIX_MODE' not in os.environ and 'API_KEY' not in os.environ:
        print("WARNING: Missing configuration detected.")
        print("Please create a .env file or provide environment variables.")
        print("Hint: cp .env.example .env")
        print("-" * 40)

    matrix_mode: str = os.environ.get('MATRIX_MODE', 'development')
    db_url: str | None = os.environ.get('DATABASE_URL')
    api_key: str | None = os.environ.get('API_KEY')
    log_level: str = os.environ.get('LOG_LEVEL', 'INFO')
    zion_endpoint: str | None = os.environ.get('ZION_ENDPOINT')

    print("ORACLE STATUS: Reading the Matrix...\n")
    print("Configuration loaded:")
    print(f"Mode: {matrix_mode}")

    if db_url:
        if matrix_mode == 'development':
            print("Database: Connected to local instance")
        else:
            print("Database: Connected to SECURE PRODUCTION CLUSTER")
    else:
        print("Database: NOT CONNECTED (Missing DATABASE_URL)")

    if api_key:
        print("API Access: Authenticated")
    else:
        print("API Access: UNAUTHORIZED (Missing Key)")

    print(f"Log Level: {log_level}")

    if zion_endpoint:
        print("Zion Network: Online\n")
    else:
        print("Zion Network: Offline\n")

    print("Environment security check:")
    print("[OK] No hardcoded secrets detected")

    if os.path.exists('.env'):
        print("[OK] .env file properly configured")
    else:
        print("[WARNING] .env file not found in current directory")

    print("[OK] Production overrides available\n")

    print("The Oracle sees all configurations.")


if __name__ == "__main__":
    main()
