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
LEGEND_FONTSIZE = 27
LABEL_FONTSIZE = 45
hatches = ['xx', '\\\\', '//', '--', '++', '||', 'o', 'O', '.', '*']
width = 0.4  # the width of the bars
line_width = 1.5
colors = ['#7F449B', '#009D72', '#E5A023', "#21130d"]
# colors_dark = ['#f0f0f0', '#d0d0d0', '#b0b0b0', '#909090', '#21130d']
colors_dark = ['#ffffff', '#c0c0c0', '#808080', '#404040', '#000000']

font = {'family': 'Arial',
        'weight' : 'normal',
        'size'   : 40}
bar_common_args = {"edgecolor": 'black', "linewidth": line_width, "zorder": 0}
bar1_args = {"facecolor":colors_dark[0]}
bar2_args = {"facecolor":colors_dark[1]}
bar3_args = {"facecolor":colors_dark[2]}
bar4_args = {"facecolor":colors_dark[3]}
bar5_args = {"facecolor":colors_dark[4]}

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
    'elinewidth': 2,
    'ecolor': 'red',
    'capsize': 3,
    'linestyle': '-'
}
app_id = ['vSoC', 'GAE','Q-K', "LD","Trinity","BS"]
app_name=['UHD Video','360° Video','Camera','AR','Livestream']

input_file = "data/fps_middle_end.csv"
df = pd.read_csv(input_file)

simulators = ['vSoC', 'GAE', 'QEMU-KVM', 'LDplayer', 'Trinity', 'Bluestacks']
fps = [[],[],[],[],[]]
errors = [[2.292512974813285, 2.6374420864452066, 2.9704994168934142, 1.9391484449954688, 3.0510440533032313, 0.5550194863388731], [3.9950933424928063, 6.240477801669336, 2.656531983271874, 1.4179904900599412, 2.3650182479686306, 0.9302243571093499], [1.3587791435625785, 1.1722784847372838, 7.299400072908349, 0.9290769907057008, 0.0, 0.6672182070543937], [1.893197313404547, 1.2537476556140126, 1.4581839572616786, 0.9265476824789346, 0.0, 0.5673972977209737], [3.560608127911289, 4.1754897847731165, 2.322357444044352, 1.4288252115574642, 0.0, 4.804391002999176]]
software_types = df['Type'].unique()

for i in range(0,5):
    software_type = software_types[i]
    filtered_data = df[df['Type'] == software_type]

    for simulator in simulators:

        values = filtered_data[simulator].values

        values_filtered = [x for x in values if x != -1]

        if len(values_filtered) > 0:
            avg = np.mean(values_filtered)
        else:
            avg = 0
        fps[i].append(avg)

print(fps)
f, ax = plt.subplots(figsize=FIGSIZE)

x = np.arange(len(app_id))  # the label locations
rects1 = ax.bar(x - width*4/5 , fps[0], label=app_id[0], width=width*2/5, **bar_common_args, **bar1_args, yerr= errors[0], error_kw=error_config)
rects2 = ax.bar(x - width*2/5 , fps[1], label=app_id[1], width=width*2/5, **bar_common_args, **bar2_args, yerr= errors[1], error_kw=error_config)
rects3 = ax.bar(x - 0.0, fps[2], label=app_id[2], width=width*2/5, **bar_common_args, **bar3_args, yerr= errors[2], error_kw=error_config)
rects4 = ax.bar(x + width*2/5 , fps[3], label=app_id[3], width=width*2/5, **bar_common_args, **bar4_args, yerr= errors[3], error_kw=error_config)
rects5 = ax.bar(x + 4*width/5 , fps[4], label=app_id[4], width=width*2/5, **bar_common_args, **bar5_args, yerr= errors[4], error_kw=error_config)


# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('FPS', size = LABEL_FONTSIZE)
ax.set_xticks(x, app_id)
ax.set_ylim((0.00, 66.0))

circ1 = mpatches.Patch(label=app_name[0], **bar_common_args, **bar1_args)
circ2 = mpatches.Patch(label=app_name[1], **bar_common_args, **bar2_args)
circ3 = mpatches.Patch(label=app_name[2], **bar_common_args, **bar3_args)
circ4 = mpatches.Patch(label=app_name[3], **bar_common_args, **bar4_args)
circ5 = mpatches.Patch(label=app_name[4], **bar_common_args, **bar5_args)
l2 = ax.legend(handles = [circ1, circ2, circ3, circ4, circ5], loc = 'upper right', bbox_to_anchor=(1.005, 1.005), fontsize=LEGEND_FONTSIZE, edgecolor = 'black', fancybox = False, ncol=2)

l3 = ax.legend(handles = [circ1, circ2, circ3, circ4, circ5], loc = 'upper right', bbox_to_anchor=(1.005, 1.005), fontsize=LEGEND_FONTSIZE, edgecolor = 'black', fancybox = False, ncol=2)

plt.show()

f.savefig(PATH_TO_FIGURES + "application_fps_middle.pdf", format = "pdf", bbox_inches = 'tight')