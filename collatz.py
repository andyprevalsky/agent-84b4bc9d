"""Collatz sequence starting at 27, printed until it reaches 1."""

START = 27


def collatz(n: int) -> list[int]:
    sequence = [n]
    while n != 1:
        n = n // 2 if n % 2 == 0 else 3 * n + 1
        sequence.append(n)
    return sequence


def main() -> None:
    sequence = collatz(START)
    steps = len(sequence) - 1

    assert sequence[0] == 27
    assert sequence[-1] == 1
    assert len(sequence) == 112, len(sequence)
    assert steps == 111, steps

    for n in sequence:
        print(n)
    print(f"Total steps: {steps}")


if __name__ == "__main__":
    main()
