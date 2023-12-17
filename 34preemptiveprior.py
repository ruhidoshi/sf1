class Process:
    def __init__(self, name, arrival_time, burst_time, priority):
        self.name = name
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.priority = priority
        self.remaining_time = burst_time

def preemptive_priority_scheduling(processes):
    current_time = 0
    waiting_time = 0
    turnaround_time = 0
    completed_processes = []

    print("Preemptive Priority Scheduling:")
    print("Process\tBurst Time\tPriority\tWaiting Time\tTurnaround Time")

    while processes:
        # Filter processes that have arrived by the current time
        available_processes = [p for p in processes if p.arrival_time <= current_time]

        if available_processes:
            # Find the process with the highest priority among the available processes
            highest_priority_process = min(available_processes, key=lambda x: x.priority)

            # Update waiting time and current time
            waiting_time += current_time - highest_priority_process.arrival_time
            current_time += 1

            # Update turnaround time
            turnaround_time += current_time - highest_priority_process.arrival_time

            # Reduce the remaining time of the selected process by 1
            highest_priority_process.remaining_time -= 1

            # Print the current status of the process
            print(f"{highest_priority_process.name}\t{highest_priority_process.burst_time}\t\t{highest_priority_process.priority}\t\t{waiting_time}\t\t{turnaround_time}")

            # If the process is completed, add it to the completed processes list
            if highest_priority_process.remaining_time == 0:
                processes.remove(highest_priority_process)
                completed_processes.append(highest_priority_process)
        else:
            # If no processes are available, increment the current time
            current_time += 1

    # Calculate the number of completed processes
    num_processes = len(completed_processes)

    # Calculate average waiting time and average turnaround time
    average_waiting_time = waiting_time / num_processes
    average_turnaround_time = turnaround_time / num_processes

    # Print the summary
  
    print("Average Waiting Time:", round(average_waiting_time, 2))
    print("Total Waiting Time:", waiting_time)
    print("Average Turnaround Time:", round(average_turnaround_time, 2))
    print("Total Turnaround Time:", turnaround_time)


# Example usage:
processes = [
    Process("P1", 0, 7, 2),
    Process("P2", 2, 5, 1),
    Process("P3", 4, 3, 3),
    Process("P4", 6, 1, 4),
]

preemptive_priority_scheduling(processes)
