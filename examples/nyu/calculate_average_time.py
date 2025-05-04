import re

# Update the log file paths
log_files = {
    'GradNorm': 'examples/qm9/output_GradNorm.log',
    'MGDA': 'examples/qm9/output_MGDA.log',
    'EW': 'examples/qm9/output_EW.log'
}

# Function to calculate average time for each method

def calculate_average_times(log_files):
    average_times = {}
    for method, log_file_path in log_files.items():
        with open(log_file_path, 'r') as file:
            lines = file.readlines()

        train_times = []

        for line in lines:
            # Match lines with time information
            match = re.search(r'Time: ([\d.]+)', line)
            if match:
                time_value = float(match.group(1))
                if 'TRAIN' in line:
                    train_times.append(time_value)

        # Calculate average time
        avg_train_time = sum(train_times) / len(train_times) if train_times else 0
        average_times[method] = avg_train_time

    return average_times

# Calculate average times for each method
average_times = calculate_average_times(log_files)

# Print the average times
for method, avg_time in average_times.items():
    print(f"{method}: {avg_time:.4f}")

# Example usage
if __name__ == "__main__":
    average_times = calculate_average_times(log_files)
    for method, avg_time in average_times.items():
        print(f"{method}: {avg_time:.4f}") 