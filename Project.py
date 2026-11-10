def countdown(n):
    print(" " * (5 - n) + f"--> Enter ({n})")
    if n <= 0:
        print("\n💣 BLAST OFF!\n")
        return
    countdown(n - 1)
    print(" " * (5 - n) + f"<-- Exit ({n})")


def countup(current, target):
    print(f"📝 Count up: {current}")
    if current >= target:
        return
    countup(current + 1, target)


countdown(3)
countup(1, 3)