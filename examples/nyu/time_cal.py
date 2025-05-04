import matplotlib.pyplot as plt

# Average TRAIN times for GradNorm, MGDA, and EW
average_train_times = {
    'GradNorm': 114.7761,
    'MGDA': 116.9244,
    'EW': 38.8121
}

# Create a bar chart
plt.figure(figsize=(10, 6))
bars = plt.bar(average_train_times.keys(), average_train_times.values(), color=['#1f77b4', '#ff7f0e', '#2ca02c'], width=0.5)

# Add title and labels with larger font sizes
plt.title('NYU-V2 TRAIN Times for Different Methods', fontsize=16, fontweight='bold')
plt.xlabel('Method', fontsize=14)
plt.ylabel('Average TRAIN Time', fontsize=14)

# Add data labels on top of each bar
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 1, round(yval, 2), ha='center', va='bottom', fontsize=12)

# Set y-axis limit
plt.ylim(0, max(average_train_times.values()) + 20)

# Add grid and background color
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.gca().set_facecolor('#f7f7f7')

# Save the plot to a file
plt.savefig('NYUv2_average_train_times.png')

# Show the plot
plt.show()