import os
import matplotlib
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import warnings
import logging
import statistics

# GLOBAL CONSTANTS

PATH_TO_FIGURES = "../figs/"
FIGSIZE=(11, 7)
LEGEND_FONTSIZE = 27
LABEL_FONTSIZE = 45
hatches = ['xx', '\\\\', '//', '--', '++', '||', 'o', 'O', '.', '*']
width = 0.4  # the width of the bars
line_width = 3
colors = ['#7F449B', '#009D72', '#E5A023', "#21130d"]
# colors_dark = ['#f0f0f0', '#d0d0d0', '#b0b0b0', '#909090', '#21130d']
colors_dark = ['#ffffff', '#c0c0c0', '#808080', '#404040', '#000000']

font = {'family': 'Arial',
        'weight' : 'normal',
        'size'   : 35}
matplotlib.rcParams['pdf.fonttype']=42
matplotlib.rcParams['ps.fonttype']=42
bar_common_args = {"edgecolor": 'black', "linewidth": line_width, "zorder": 0}
# bar1_args = {"facecolor":colors_dark[2]}

# envsetup

plt.rc('font', **font)
plt.rcParams.update({'legend.handlelength': 1.3, 'legend.borderpad': 0.25, "legend.labelspacing": 0.25, "legend.handletextpad": 0.5})
plt.rcParams['hatch.linewidth'] = line_width
pd.set_option("display.max_colwidth", 5000)
pd.set_option("display.max_columns", 10000)
pd.set_option("display.max_rows", 100)
os.makedirs(PATH_TO_FIGURES, exist_ok=True)
warnings.filterwarnings('ignore')

# refresh the fonts just installed
matplotlib.font_manager._load_fontmanager(try_read_cache=False)

error_config = {
    'elinewidth': 3,
    'ecolor': 'red',
    'capsize': 5,
    'linestyle': '-'
}
app_id = ['vSoC', 'GAE', 'Q-K',"LD","Trinity","BS"]
app_name=['UHD Video','360° Video','Camera','AR','Livestream']

input_file = "./data/normal_apps_fps.csv"
df = pd.read_csv(input_file)

simulators = ['vSoC', 'GAE', 'QEMU-KVM', 'LDplayer', 'Bluestacks', 'Trinity']
fps = []
errors = []


for emulator in simulators:
    values = df[emulator][:25]  # 前25个应用的数据
    values = values[values != 0]
    print(values)
    mean_value = values.mean()
    std_value = values.std()
    fps.append(mean_value)
    errors.append(std_value)

print(fps)
for i in range(1, 6):
    print((fps[0]-fps[i])/fps[i])
f, ax = plt.subplots(figsize=FIGSIZE)

x = np.arange(len(app_id))  # the label locations
cmap = plt.get_cmap('Greys')  # 'Greys' 颜色映射用于生成灰度
colors = cmap(np.linspace(0.0, 0.8, len(x)))  # 生成 len(x) 个不同灰度的颜色，范围在 0.3 到 0.7 之间

rects1 = ax.bar(
    x, fps, label=app_id[0], width=width*1.1,
    color=colors,
    **bar_common_args,
    yerr=errors, error_kw={'elinewidth': 2, 'capsize': 5, **error_config}  # 设置 error bar 的线条宽度
)
ax.set_xlim([-0.8, len(app_id) - 0.2])

ax.set_ylabel('FPS', size = LABEL_FONTSIZE)
ax.set_xticks(x, app_id)
ax.set_ylim((0.00, 80.0))

plt.show()

f.savefig(PATH_TO_FIGURES + "other_fps.pdf", format = "pdf", bbox_inches = 'tight')