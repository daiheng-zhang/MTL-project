import matplotlib.pyplot as plt
import numpy as np

# === Step 1: Define metrics and raw data ===
labels = [
    "mIoU (↑)", "Pix Acc (↑)", "Abs Err (↓)", "Rel Err (↓)",
    "Angle Mean (↓)", "Angle Median (↓)", "<11.25 (↑)", "<22.5 (↑)", "<30 (↑)"
]

data = {
    "STL":       [53.35, 75.26, 0.3909, 0.1615, 22.26, 15.61, 38.00, 64.12, 74.56],
    "EW":        [54.14, 75.65, 0.3864, 0.1628, 23.66, 16.99, 35.14, 60.99, 72.01],
    "GradNorm":  [53.98, 75.63, 0.3867, 0.1589, 23.43, 16.89, 35.35, 61.22, 72.28],
    "MGDA":      [48.58, 71.83, 0.4133, 0.1665, 22.81, 15.55, 38.25, 64.10, 74.50],
}

is_higher_better = [True, True, False, False, False, False, True, True, True]

# === Step 2: Normalize w.r.t. STL baseline ===
reference_method = "STL"
ref_values = data[reference_method]

normalized_data = {}
for method in data:
    normed = []
    for i, higher_better in enumerate(is_higher_better):
        ref_val = ref_values[i]
        val = data[method][i]
        if higher_better:
            norm = val / ref_val
        else:
            norm = ref_val / val
        norm = max(min(norm, 2.0), 0.0) / 2.0  # clip then scale to [0,1]
        normed.append(norm)
    normalized_data[method] = normed

# === Step 3: Rearrange by task group (segment / depth / normal) ===
segments = [0, 1]
depths = [2, 3]
normals = [4, 5, 6, 7, 8]
task_order = segments + depths + normals
labels_ordered = [labels[i] for i in task_order]

# angles for radar chart
num_vars = len(labels_ordered)
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
angles += angles[:1]  # loop

# prepare plotting values
plot_data = {
    method: [normalized_data[method][i] for i in task_order] + 
            [normalized_data[method][task_order[0]]]
    for method in normalized_data
}

# === Step 4: Plot ===
fig, ax = plt.subplots(figsize=(9, 9), subplot_kw=dict(polar=True))

for method, values in plot_data.items():
    ax.plot(angles, values, label=method, linewidth=2)
    ax.fill(angles, values, alpha=0.1)

# format
ax.set_theta_offset(np.pi / 2)
ax.set_theta_direction(-1)
ax.set_thetagrids(np.degrees(angles[:-1]), labels_ordered, fontsize=12)
ax.set_ylim(0, 1)
ax.set_rlabel_position(0)
ax.yaxis.grid(True, linestyle='--', color='gray')
ax.xaxis.grid(True, linestyle='--', color='gray')

# Add separation lines between task segments
for idx in [len(segments), len(segments) + len(depths)]:
    angle_sep = angles[idx]
    ax.plot([angle_sep, angle_sep], [0, 1], color='black', linestyle='--', linewidth=1)

# legend & title
ax.set_title("NYU-V2 with Task-Aligned Segments (Normalized to STL)", y=1.1, fontsize=14)
ax.legend(loc='upper right', bbox_to_anchor=(1.4, 1.1), fontsize=10)

plt.tight_layout()
plt.savefig("radar_nyu_tasks.png", dpi=300, bbox_inches='tight')  # Optional: save to file
plt.show()
