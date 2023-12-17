import os

def sort_descending(arr):
    # Sort the array in descending order
    arr.sort(reverse=True)
    print(f"Parent Process ({os.getpid()}) - Sorted Descending: {arr}")

def sort_ascending(arr):
    # Sort the array in ascending order
    arr.sort()
    print(f"Child Process ({os.getpid()}) - Sorted Ascending: {arr}")

def main():
    # Shared array between parent and child processes
    arr = [7, 2, 5, 1, 8, 6]

    # Use fork to create a child process
    pid = os.fork()

    if pid == 0:
        # This code runs in the child process
        sort_ascending(arr)
    else:
        # This code runs in the parent process
        sort_descending(arr)

if __name__ == "__main__":
    main()
