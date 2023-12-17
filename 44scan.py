def scan_disk_scheduling(requests, head_start, direction="left"):

    requests_copy = list(requests)

    # Sort the requests in ascending order
    requests_copy.sort()

    # Initialize variables to store the total head movement and the current head position
    total_head_movement = 0
    current_head_position = head_start
    sequence_of_movements = []

    # Set the initial direction of head movement
    if direction == "left":
        head_movement_direction = -1  # Move left
    elif direction == "right":
        head_movement_direction = 1  # Move right
    else:
        raise ValueError("Invalid direction. Use 'left' or 'right'.")

    # Main loop - iterate through requests
    while requests_copy:
        # Iterate through requests in the current direction
        for request in range(current_head_position, -1, -1):
            if request in requests_copy:
                # Calculate head movement for the current request
                head_movement = abs(current_head_position - request)
                # Add the calculated head movement to the total
                total_head_movement += head_movement
                # Update the current head position to the current request
                current_head_position = request
                # Remove the serviced request from the copy of requests
                requests_copy.remove(request)
                # Append the current head position to the sequence
                sequence_of_movements.append(current_head_position)

        # Change direction and reset current head position if needed
        if requests_copy and direction == "left":
            direction = "right"
            current_head_position = 0
            continue
        elif requests_copy and direction == "right":
            direction = "left"
            current_head_position = max(requests_copy)
            continue

    # Return the total head movement and the sequence of head movements
    return total_head_movement, sequence_of_movements

if __name__ == "__main__":
    # Example usage
    # Define a list of disk access requests
    requests = [98, 183, 37, 122, 14, 124, 65, 67]
    # Specify the initial position of the disk head
    initial_head_position = 53

    # Call the scan_disk_scheduling function with the specified requests, head position, and direction
    total_movement, sequence = scan_disk_scheduling(requests, initial_head_position, direction="left")

    # Print the total head movement after servicing all requests
    print(f"Total head movement: {total_movement}")

    # Print the sequence of head movements
    print("Sequence of head movements:", sequence)
