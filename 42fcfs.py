# Define a function for the FCFS disk scheduling algorithm
def fcfs_disk_scheduling(requests, head_start):
    # Initialize variables to store the total head movement, the current head position, and the sequence of requests
    total_head_movement = 0
    current_head_position = head_start
    sequence_of_requests = []

    # Iterate through the list of disk access requests
    for request in requests:
        
        head_movement = abs(current_head_position - request)
        total_head_movement += head_movement
        current_head_position = request
        sequence_of_requests.append(request)

    # Return the total head movement and the sequence of requests
    return total_head_movement, sequence_of_requests


if __name__ == "__main__":
   
    requests = [98, 183, 37, 122, 14, 124, 65, 67]
    
    initial_head_position = 53

   
    total_movement, sequence = fcfs_disk_scheduling(requests, initial_head_position)

    # Print the total head movement after servicing all requests
    print(f"Total head movement: {total_movement}")

    # Print the sequence of requests serviced
    print("Sequence of requests serviced:", sequence)
