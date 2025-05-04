# import matplotlib.pyplot as plt

# # Average TRAIN times for GradNorm, MGDA, and EW
# average_train_times = {
#     'GradNorm': 179.0981,
#     'MGDA': 296.5867,
#     'EW': 28.2188
# }

# # Create a bar chart
# plt.figure(figsize=(10, 6))
# bars = plt.bar(average_train_times.keys(), average_train_times.values(), color=['#1f77b4', '#ff7f0e', '#2ca02c'], width=0.5)

# # Add title and labels with larger font sizes
# plt.title('QM9 TRAIN Times for Different Methods', fontsize=16, fontweight='bold')
# plt.xlabel('Method', fontsize=14)
# plt.ylabel('Average TRAIN Time', fontsize=14)

# # Add data labels on top of each bar
# for bar in bars:
#     yval = bar.get_height()
#     plt.text(bar.get_x() + bar.get_width()/2, yval + 1, round(yval, 2), ha='center', va='bottom', fontsize=12)

# # Set y-axis limit
# plt.ylim(0, max(average_train_times.values()) + 20)

# # Add grid and background color
# plt.grid(axis='y', linestyle='--', alpha=0.7)
# plt.gca().set_facecolor('#f7f7f7')

# # Save the plot to a file
# plt.savefig('QM9_average_train_times.png')

# # Show the plot
# plt.show()
import matplotlib.pyplot as plt
import numpy as np

# Task labels (in order from table)
tasks = ['μ', 'α', 'ε_HOMO', 'ε_LUMO', '⟨R²⟩', 'ZPVE', 'U₀', 'U', 'H', 'G', 'cᵥ']

# STL as baseline (lower is better)
stl = np.array([0.12, 0.45, 100.3, 102.49, 1.79, 8.87, 187.8, 201.8, 205.1, 201.3, 0.17])
ew = np.array([0.38, 0.87, 197.1, 250.8, 11.2, 32.0, 437.2, 439.7, 440.6, 431.0, 0.31])
gradnorm = np.array([0.21, 0.67, 127.1, 176.8, 13.6, 26.7, 373.9, 376.0, 377.2, 369.5, 0.27])
mgda = np.array([0.55, 0.86, 234.5, 259.0, 6.0, 22.7, 327.9, 369.6, 360.9, 342.7, 0.29])

# Normalize by STL
ew_norm = ew / stl
gradnorm_norm = gradnorm / stl
mgda_norm = mgda / stl
baseline = np.ones_like(stl)

# Radar chart setup
labels = tasks
num_vars = len(labels)
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
angles += angles[:1]

def extend(values):
    return np.concatenate((values, [values[0]]))

fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

ax.plot(angles, extend(baseline), label='STL', linewidth=2, linestyle='--')
ax.plot(angles, extend(ew_norm), label='EW')
ax.plot(angles, extend(gradnorm_norm), label='GradNorm')
ax.plot(angles, extend(mgda_norm), label='MGDA')

ax.fill(angles, extend(ew_norm), alpha=0.1)
ax.fill(angles, extend(gradnorm_norm), alpha=0.1)
ax.fill(angles, extend(mgda_norm), alpha=0.1)

ax.set_theta_offset(np.pi / 2)
ax.set_theta_direction(-1)
ax.set_thetagrids(np.degrees(angles[:-1]), labels)
# ax.set_title("Radar Chart of Normalized MAE (STL Baseline = 1.0)", size=14)
ax.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1))

# Save figure
plt.tight_layout()
plt.savefig("normalized_mae_radar.png", dpi=300)
plt.close()

