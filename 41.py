P = 5
R = 3

def calculateNeed(need, maxm, allot):
    # Calculate the need matrix: maxm - allot
    for i in range(P):
        for j in range(R):
            need[i][j] = maxm[i][j] - allot[i][j] 

def isSafe(processes, avail, maxm, allot):
    # Initialize the need matrix
    need = []
    for i in range(P):
        l = [0] * R
        need.append(l)
        
    # Calculate the need matrix using the calculateNeed function
    calculateNeed(need, maxm, allot)
    
    # Initialize finish, safeSeq, and work
    finish = [0] * P
    safeSeq = [0] * P 
    work = avail.copy()

    count = 0
    # Continue until all processes are in the safe sequence
    while count < P:
        found = False
        # Iterate over each process
        for p in range(P):
            # Check if the process is not finished
            if finish[p] == 0:
                # Check if the need can be satisfied with the available resources
                for j in range(R):
                    if need[p][j] > work[j]:
                        break
                
                # If the need can be satisfied, mark the process as finished
                if j == R - 1:
                    # Update the available resources and add the process to the safe sequence
                    for k in range(R):
                        work[k] += allot[p][k]
                    
                    safeSeq[count] = p
                    count += 1
                    finish[p] = 1
                    found = True

        # If no process can be added to the safe sequence, the system is not in a safe state
        if not found:
            print("System is not in a safe state")
            return False
    
    # Print the safe state and the safe sequence
    print("System is in a safe state.", "\nSafe sequence is: ", end=" ")
    print(*safeSeq)

    return True

if __name__ == "__main__":
    # Example input
    processes = [0,1,2,3,4]  
    avail = [3, 3, 2] 
    maxm = [[7, 5, 3], [3, 2, 2], [9, 0, 2], [2, 2, 2], [4, 3, 3]]
    allot = [[0, 1, 0], [2, 0, 0], [3, 0, 2], [2, 1, 1], [0, 0, 2]] 

    # Call the isSafe function with the example input
    isSafe(processes, avail, maxm, allot) 
