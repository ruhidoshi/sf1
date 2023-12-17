def first_fit(memory_blocks, process_sizes):
    n = len(memory_blocks)
    m = len(process_sizes)
    allocation = [-1] * m  # Initialize allocation array with -1 (unallocated)

    for i in range(m):
        for j in range(n):
            # Check if the memory block is large enough and unallocated
            if memory_blocks[j] >= process_sizes[i]:
                allocation[i] = j
                memory_blocks[j] -= process_sizes[i]
                break  # Break the inner loop once a suitable block is found

    return allocation

# Example usage:
memory_blocks = [100, 200, 300, 400, 500]
process_sizes = [212, 417, 112, 426]

# Convert process numbers to actual process names (P0, P1, ...)
processes_names = [f"Process {size}" for size in process_sizes]
# Convert memory block numbers to actual memory block names (M0, M1, ...)
memory_blocks_names = [f"Memory Block {size}" for size in memory_blocks]

allocation = first_fit(memory_blocks, process_sizes)

# Print the results with comments
print("First Fit Memory Allocation:")
for i in range(len(process_sizes)):
    if allocation[i] != -1:
        print(f"{processes_names[i]} - Allocated in {memory_blocks_names[allocation[i]]}")
    else:
        print(f"{processes_names[i]} - Not Allocated")
