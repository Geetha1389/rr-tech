def factorial(n: int) -> int:
    if n < 0:
        raise ValueError("n must be >= 0")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def main():
    name = input("Your name: ").strip() or "Friend"
    try:
        n = int(input("Compute factorial of (non-negative integer): "))
        print(f"Hello, {name}! {n}! = {factorial(n)}")
    except ValueError as e:
        print("Input error:", e)


if __name__ == "__main__":
    main()
