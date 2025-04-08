import sys

def run_ezlang(code):
    try:
        exec(code)  # Executes Ezlang (which is currently Python-compatible)
    except Exception as e:
        print(f"Ezlang Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python ezlang.py <file.ez>")
    else:
        with open(sys.argv[1], "r") as file:
            ezlang_code = file.read()
        run_ezlang(ezlang_code)
