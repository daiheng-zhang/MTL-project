import matplotlib.pyplot as plt

# Average TRAIN times for GradNorm, MGDA, and EW
average_train_times = {
    'GradNorm': 114.7761,
    'MGDA': 116.9244,
    'EW': 38.8121
}

# Create a bar chart
plt.figure(figsize=(8, 6))
plt.bar(average_train_times.keys(), average_train_times.values(), color=['blue', 'green', 'red'])
plt.title('Average TRAIN Times for Different Methods')
plt.xlabel('Method')
plt.ylabel('Average TRAIN Time')
plt.ylim(0, max(average_train_times.values()) + 10)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Save the plot to a file
plt.savefig('average_train_times.png')

# Show the plot
plt.show() 