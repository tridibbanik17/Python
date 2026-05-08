# Print the elapsed time of a code block using the time module
import time

input("Press Enter to start the timer...")  # Wait for the user to press Enter to start the timer
start_time = time.time()  # Record the current time in seconds since the epoch

input("Press Enter to stop the timer...")  # Wait for the user to press Enter to stop the timer
end_time = time.time()  # Record the current time in seconds since the epoch

elapsed_time = end_time - start_time  # Calculate the elapsed time in seconds

print(f"The elapsed time is {elapsed_time} seconds.")

print(time.time())  # This will print the current time in seconds since the epoch, which is a floating-point number representing the number of seconds that have elapsed since January 1, 1970 (UTC).