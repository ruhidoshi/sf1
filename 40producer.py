mutex = 1    # Decrement when producing, increment when consuming
full = 0
empty = 10   # Number of empty slots in the buffer
data = 0     # Data is produced

def producer():
    global mutex, full, empty, data
    mutex -= 1
    full += 1
    empty -= 1
    data += 1
    print("\nProducer produces item number:", data)
    mutex += 1

def consumer():
    global mutex, full, empty, data
    mutex -= 1
    full -= 1
    empty += 1
    print("\nConsumer consumes item number:", data)
    data -= 1
    mutex += 1

if __name__ == "__main__":
    while True:
        print("Enter 1 for Producer\nEnter 2 for Consumer\nEnter 3 for Exit")
        ch = int(input("Enter your choice: "))

        if ch == 1:
            if mutex == 1 and empty != 0:
                producer()
            else:
                print("Buffer is full. New data can't be produced.")
        elif ch == 2:
            if mutex == 1 and full != 0:
                consumer()
            else:
                print("Buffer is empty. Data can't be consumed.")
        elif ch == 3:
            exit(0)
        else:
            print("Wrong choice")
