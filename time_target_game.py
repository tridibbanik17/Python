# Create a function that runs a time target game.

# Example Output:
# 3s test. Hit ENTER to start
# Hit ENTER to stop
# 2.789s
# You were 0.211s off

from time import time
from random import randint

def play():
    target = randint(2,5)

    for i in range(3):
        input(f"{target}s test. Hit ENTER to start")
        start = time() 

        input("Hit ENTER to stop")
        end = time()

        elapsed = end - start
        print(f"{elapsed:.3f}s")
        print(f"You were {abs(elapsed - target):.3f}s off")

play()



