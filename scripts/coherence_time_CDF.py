import os
import matplotlib
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import warnings
import logging

# GLOBAL CONSTANTS

PATH_TO_FIGURES = "../figs/"
FIGSIZE=(11, 7)
LEGEND_FONTSIZE = 28
LABEL_FONTSIZE = 40
hatches = ['xx', '\\\\', '//', '--', '++', '||', 'o', 'O', '.', '*']
width = 0.35  # the width of the bars
line_width = 3.5
colors = ['#7F449B', '#009D72', '#E5A023']
font = {'family': 'Arial',
        'weight' : 'normal',
        'size'   : 40}
bar_common_args = {"linewidth": line_width, "zorder": 3, "facecolor": "white"}
bar1_args = {"edgecolor": colors[0], "hatch": hatches[0]}
bar2_args = {"edgecolor": colors[1], "hatch": hatches[1]}

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

folder_path = './data/coherence_time/'
sub_folders = ['GAE/', 'QK/']


data = []

for folder in sub_folders:
    path = folder_path + folder
    file_names = os.listdir(path)
    print(len(file_names))
    tmp = []
    for file_name in file_names:
        file_path = os.path.join(path, file_name)
        with open(file_path, 'r') as file:
            content = file.read()
            if len(content) == 0:
                numbers = []
            else:
                numbers = [float(num) for num in content.split(',')]
            tmp += numbers
    print(len(tmp))
    data.append(tmp)
f, ax = plt.subplots(figsize=(9.6, 7))
plt.ylim((0, 1.2))
plt.yticks(ticks=[0, 0.2, 0.4, 0.6 ,0.8, 1], labels = ['0', '0.2', '0.4', '0.6' ,'0.8', '1'])
plt.xlim((0, 12000))


count2, bins_count2 = np.histogram(data[0], bins=5000)
pdf2 = count2 / sum(count2)
cdf2 = np.cumsum(pdf2)
cdf2 = np.insert(cdf2, 0, 0)  # 确保从0开始
plt.plot(bins_count2, cdf2, color=colors[1], zorder=1, clip_on=True, linewidth=4)
# post_per[0] = 201.1
count, bins_count = np.histogram(data[1], bins=5000)

# finding the PDF of the histogram using count values
pdf = count / sum(count)

# using numpy np.cumsum to calculate the CDF
cdf = np.cumsum(pdf)
cdf = np.insert(cdf, 0, 0);

plt.xlabel('Coherence Maintenance (ms)', fontsize = LABEL_FONTSIZE)
plt.ylabel('CDF', fontsize = LABEL_FONTSIZE)
ax.set_xticks([0, 2000, 4000, 6000, 8000, 10000, 12000], ['0','2','4','6','8','10','12'])

# plot the actual lines
plt.plot(bins_count, cdf, color=colors[0], zorder=1, clip_on=True, linewidth=4, linestyle='dashed')



bbox = dict(boxstyle="square,pad=0.3", facecolor='none', edgecolor='black')
def get_bbox_text(freq_diff):
    bbox_text = f"Max = {round(np.max(data[0]),2)}%\nMean = {round(np.mean(data[0]),2)}%\nMedian = {round(np.median(data[0]),2)}%\nMin = {round(np.min(data[0]),2)}%"
    return bbox_text

plt.annotate(
    text="Max = {:.2f}\nMean = {:.2f}\nMedian = {:.2f}\nMin = {:.2f}".format(round(np.max(data[1]),2)/1e3, round(np.mean(data[1]),2)/1e3, round(np.median(data[1]),2)/1e3, round(np.min(data[1]),2)/1e3),
    xy=(bins_count[496], cdf[496]),
    xytext=(7500, 0.22),
    textcoords="data",
    fontsize=26,
    arrowprops=dict(arrowstyle="<-", connectionstyle="arc3", color=colors[0],linewidth=4,),
    bbox=bbox
)

# 对第二条线添加bbox
plt.annotate(
    text="Max = {:.2f}\nMean = {:.2f}\nMedian = {:.2f}\nMin = {:.2f}".format(round(np.max(data[0]),2)/1e3, round(np.mean(data[0]),2)/1e3, round(np.median(data[0]),2)/1e3, round(np.min(data[0]),2)/1e3),
    xy=(bins_count2[50], cdf2[50]),
    xytext=(600, 0.6),
    textcoords="data",
    fontsize=26,
    arrowprops=dict(arrowstyle="<-", connectionstyle="arc3", color=colors[1],linewidth=4),
    bbox=bbox
)
for label in ax.get_yticklabels():
    if label.get_text() == '0':
        label.set_visible(False)
        break

line_up, = ax.plot([0], label='GAE', linewidth=4, linestyle='dashed', color=colors[0])
line_down, = ax.plot([0], label='QEMU-KVM', linewidth=4, color=colors[1])
l2 = ax.legend(handles = [line_up, line_down], loc = 'upper left', bbox_to_anchor=(-0.005, 1.005), fontsize=LEGEND_FONTSIZE, edgecolor = 'black', fancybox = False, ncol=2)

plt.show()

f.savefig(PATH_TO_FIGURES + "coherence_cdf.pdf", format = "pdf", bbox_inches = 'tight')