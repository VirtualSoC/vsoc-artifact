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
LEGEND_FONTSIZE = 30
LABEL_FONTSIZE = 45
hatches = ['xx', '\\\\', '//', '--', '++', '||', 'o', 'O', '.', '*']
width = 0.4  # the width of the bars
line_width = 1.5
colors = ['#7F449B', '#009D72', '#E5A023', "#21130d"]
colors_dark = ['#ffffff', '#808080', '#000000']
font = {'family': 'Arial',
        'weight' : 'normal',
        'size'   : 40}
matplotlib.rcParams['pdf.fonttype']=42
matplotlib.rcParams['ps.fonttype']=42
bar_common_args = {"linewidth": line_width, "zorder": 3}
bar1_args = {"edgecolor": colors[3], "facecolor":colors_dark[0]}
bar2_args = {"edgecolor": colors[3], "facecolor":colors_dark[1]}
bar3_args = {"edgecolor": colors[3], "facecolor":colors_dark[2]}

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
    'elinewidth': 2,  # 误差线的粗细
    'ecolor': 'red',  # 误差线的颜色
    'capsize': 3,       # 误差线末端横杆的大小
    'linestyle': '-'   # 误差线的样式
}
app_id = ['vSoC', 'GAE','Q-K', "LD","BS"]
app_name=['Camera','AR','Livestream']

input_file = "data/latency_high_end.csv"
df = pd.read_csv(input_file)

simulators = ['vSoC', 'GAE', 'QEMU-KVM', 'LDplayer', 'Bluestacks']
latency = [[],[],[]]
errors = [[],[],[]]
software_types = df['Type'].unique()

for i in range(0,3):
    software_type = software_types[i]
    filtered_data = df[df['Type'] == software_type]

    for simulator in simulators:
        values = filtered_data[simulator].values
        values_filtered = [x for x in values if x != -1]
        if len(values_filtered) > 0:
            avg = np.mean(values_filtered)
            err = statistics.stdev(values_filtered) if len(values_filtered) > 1 else 0
        else:
            avg = 0
            err = 0
        latency[i].append(avg)
        errors[i].append(err)

print(latency)
f, ax = plt.subplots(figsize=FIGSIZE)

x = np.arange(len(app_id))  # the label locations
rects1 = ax.bar(x - width*2/3 , latency[0], label=app_id[0], width=width*2/3, **bar_common_args, **bar1_args, yerr= errors[0], error_kw=error_config)
rects2 = ax.bar(x, latency[1], label=app_id[1], width=width*2/3, **bar_common_args, **bar2_args, yerr= errors[1], error_kw=error_config)
rects3 = ax.bar(x + width*2/3, latency[2], label=app_id[2], width=width*2/3, **bar_common_args, **bar3_args, yerr= errors[2], error_kw=error_config)


# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('latency(ms)', size = LABEL_FONTSIZE)
ax.set_xticks(x, app_id)
ax.set_ylim((0.00, 900.0))
ax.set_yticks([0, 300, 600, 900], ['0','300','600','900'])

circ1 = mpatches.Patch(label=app_name[0], **bar_common_args, **bar1_args)
circ2 = mpatches.Patch(label=app_name[1], **bar_common_args, **bar2_args)
circ3 = mpatches.Patch(label=app_name[2], **bar_common_args, **bar3_args)
l2 = ax.legend(handles = [circ1, circ2, circ3],  loc = 'upper left', bbox_to_anchor=(0.002, 1.015), fontsize=LEGEND_FONTSIZE, edgecolor = 'black', fancybox = False, ncol=1)
plt.show()

f.savefig(PATH_TO_FIGURES + "high_end_latency.pdf", format = "pdf", bbox_inches = 'tight')