# import pandas as pd
# import numpy as np

# # 定义表格数据（第一行为 STL baseline）
# data = {
#     "Method": ["EW", "GradNorm", "MGDA"],
#     "mIoU": [54.14, 53.98, 48.58],
#     "Pix Acc": [75.65, 75.63, 71.83],
#     "Abs Err": [0.3864, 0.3867, 0.4133],
#     "Rel Err": [0.1628, 0.1589, 0.1665],
#     "Mean": [23.66, 23.43, 22.81],
#     "Median": [16.99, 16.89, 15.55],
#     "11.25": [35.14, 35.35, 38.25],
#     "22.5": [60.99, 61.22, 64.10],
#     "30": [72.01, 72.28, 74.50]
# }

# # 转为 DataFrame
# df = pd.DataFrame(data)
# df.set_index("Method", inplace=True)

# # 定义每个指标是否是越大越好（1）还是越小越好（-1）
# better_direction = {
#     "mIoU": 1,
#     "Pix Acc": 1,
#     "Abs Err": -1,
#     "Rel Err": -1,
#     "Mean": -1,
#     "Median": -1,
#     "11.25": 1,
#     "22.5": 1,
#     "30": 1
# }

# K = len(better_direction)  # 指标个数
# stl_values = df.loc["STL"]

# delta_m_results = []
# mean_rank_results = []

# # 针对每个方法计算 Δm% 和 Mean Rank
# for method in ["EW", "GradNorm", "MGDA"]:
#     deltas = []
#     ranks = []
#     for metric in better_direction:
#         m_val = df.loc[method, metric]
#         b_val = stl_values[metric]
#         # Δm% 公式： (-1)^δk * (Mm,k - Mb,k) / Mb,k × 100
#         delta = (-1) * better_direction[metric] * (m_val - b_val) / b_val * 100
#         deltas.append(delta)
#         # MR：排名（越小越好）
#         rank = df[metric].rank(ascending=(better_direction[metric] == -1)).loc[method]
#         ranks.append(rank)
#     delta_m = np.mean(deltas)
#     mean_rank = np.mean(ranks)
#     delta_m_results.append(delta_m)
#     mean_rank_results.append(mean_rank)

# # 输出结果
# result_df = pd.DataFrame({
#     "Method": ["EW", "GradNorm", "MGDA"],
#     "Δm% ↓": delta_m_results,
#     "MR ↓": mean_rank_results
# })

# print(result_df.round(3))

import matplotlib.pyplot as plt
import numpy as np

# === 原始数据 ===
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

# === 计算 mean of relative error ===
mean_relative_errors = {}

for method in data:
    if method == "STL":
        continue  # baseline 不需要比较
    total = 0
    for i in range(len(labels)):
        stl_val = data["STL"][i]
        val = data[method][i]
        if is_higher_better[i]:
            delta = (val - stl_val) / stl_val
        else:
            delta = (stl_val - val) / stl_val
        total += delta
    mean_relative_errors[method] = total / len(labels)

# === 打印结果 ===
print("Mean of Relative Errors (compared to STL):")
for k, v in mean_relative_errors.items():
    print(f"{k}: {v:.4f}")

# === 画图 ===
methods = list(mean_relative_errors.keys())
values = [mean_relative_errors[m] for m in methods]

plt.figure(figsize=(7, 5))
bars = plt.bar(methods, values, color=["#4c72b0", "#55a868", "#c44e52"])
plt.axhline(0, color='gray', linestyle='--')
plt.ylabel("Mean of Relative Error (vs STL)", fontsize=12)
plt.title("Average Performance Gain or Drop Compared to STL", fontsize=14)
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval, f'{yval:.3f}', ha='center', va='bottom', fontsize=10)
plt.tight_layout()
plt.savefig("mean_relative_error_bar.png", dpi=300, bbox_inches='tight')
plt.show()
