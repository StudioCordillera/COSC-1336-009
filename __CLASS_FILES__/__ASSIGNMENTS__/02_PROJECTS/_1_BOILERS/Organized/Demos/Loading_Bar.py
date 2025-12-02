import time

def animation(length, delay):
    display = 'Loading'
    animation = ['|', '/', '-', '\\']
    for _ in range(length):  # Repeat animation 5 times
        for frame in animation:
            print(f"\r{display} {frame}", end='', flush=True)
            time.sleep(delay)

animation(10, 0.125)