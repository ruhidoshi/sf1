def sstf_disk_scheduling(requests, head_start):
   
    requests_copy = list(requests)
    
    # Initialize variables to store the total head movement and the current head position
    total_head_movement = 0
    current_head_position = head_start
    sequence_of_movements = []

    # Continue until all requests are serviced
    while requests_copy:
        # Find the nearest request to the current head position
        nearest_request = min(requests_copy, key=lambda x: abs(current_head_position - x))
        
        # Calculate the head movement for the nearest request
        head_movement = abs(current_head_position - nearest_request)
        
        # Add the calculated head movement to the total
        total_head_movement += head_movement
        
        # Update the current head position to the nearest request
        current_head_position = nearest_request
        
        # Append the movement to the sequence
        sequence_of_movements.append(current_head_position)
        
        # Remove the serviced request from the copy of requests
        requests_copy.remove(nearest_request)

    # Return the total head movement and the sequence of movements
    return total_head_movement, sequence_of_movements

if __name__ == "__main__":
    # Example usage
    # Define a list of disk access requests
    requests = [98, 183, 37, 122, 14, 124, 65, 67]
    # Specify the initial position of the disk head
    initial_head_position = 53

    # Call the sstf_disk_scheduling function with the specified requests and head position
    total_movement, sequence = sstf_disk_scheduling(requests, initial_head_position)

    # Print the total head movement after servicing all requests
    print(f"Total head movement: {total_movement}")

    # Print the sequence of head movements
    print("Sequence of head movements:", sequence)
