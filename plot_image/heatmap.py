import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 模拟数据：4种模式，每种是10行×11列的数值矩阵，数值范围为0到0.5
np.random.seed(42)
data = np.random.rand(4, 10, 11) * 0.5  # shape: (4, 10, 11)

# 子图标题（代表不同视觉模式）
titles = ['Monocular', 'Mono-inertial', 'Stereo', 'Stereo-inertial']

# 列标签（代表不同序列）
seq_labels = ['MH01', 'MH02', 'MH03', 'MH04', 'MH05',
              'V101', 'V102', 'V103', 'V201', 'V202', 'V203']

# 行标签（10次执行）
run_labels = [str(i) for i in range(1, 11)]

# 创建图像和子图网格
fig, axs = plt.subplots(2, 2, figsize=(14, 8))
cbar_ax = fig.add_axes([0.92, 0.15, 0.02, 0.7])  # 统一 colorbar 放在右边

# 遍历 4 个子图，绘制 heatmap
for idx, ax in enumerate(axs.flat):
    sns.heatmap(data[idx],
                ax=ax,
                vmin=0, vmax=1,
                cmap='jet',
                xticklabels=seq_labels,
                yticklabels=run_labels,
                cbar=(idx == 0),  # 只给第一个图加 colorbar
                cbar_ax=None if idx != 0 else cbar_ax)

    ax.set_title(titles[idx], fontsize=12)
    ax.tick_params(axis='x', rotation=45)
    ax.set_xlabel('')
    ax.set_ylabel('Run ID')

# 调整整体布局
fig.tight_layout(rect=[0, 0, 0.9, 1])  # 给 colorbar 留空间
plt.show()
