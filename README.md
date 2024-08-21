# vSoC Evaluation Data and Scripts

This repository will guide interested readers to generate the figures in the paper with the data we collected.

## 1. Running Scripts

### Prerequisites

To run the scripts, you'll need to clone this repository and install the `Python 3` environment. Also, we have some additional dependencies. To install them, type `pip3 install -r requirements.txt` at the root directory of the repo.

### Script Usage

The scripts are in the `scripts` folder. To run a script named `xxx.py`, simpy `cd scripts` and type `python3 xxx.py` in your terminal. The generated figures will be in the `figs` folder at the root directory of the repo.

The scripts' functions are detailed as follows.

- `memory_size_CDF.py`

  This script draws `Figure 4`. Drawn figures are placed in `scripts/figs/datasize_cdf.pdf`.

- `coherence_time_CDF.py`

  This script draws `Figure 5` . Drawn figures are placed in ``scripts/figs/coherence_cdf.pdf``.

- `slack_interval_CDF.py`

  This script draws `Figure 6` . Drawn figures are placed in `scripts/figs/interval_cdf.pdf`.

- `high_end_fps.py`

  This script draws `Figure 10` . Drawn figures are placed in `scripts/figs/application_fps_high.pdf`.

- `middle_end_fps.py`

  This script draws `Figure 11`. Drawn figures are placed in `scripts/figs/application_fps_middle.pdf`.

- `breakdown_fps.py`

  This script draws `Figure 12` . Drawn figures are placed in `scripts/figs/breakdown_fps.pdf`.

- `high_end_latency.py`

  This script draws `Figure 13` . Drawn figures are placed in `scripts/figs/high_end_latency.pdf`.

- `middle_end_latency.py`

  This script draws `Figure 14` . Drawn figures are placed in `scripts/figs/middle_end_latency.pdf`.

- `access_latency_CDF.py`

  This script draws `Figure 15`. Drawn figures are placed in `scripts/figs/micro_latency_cdf.pdf`.

## 2. Data Format

### FPS and Latency Data

FPS and latency measurement data are recorded in `.csv` tables in `scripts/data`, It contains the FPS performance data of each different emulator across 50 applications and the latency performance data (in milliseconds) across 30 applications.

We distinguish between functional problems and performance problems in the tables. If the app crashes, generates an ANR (App-Not-Responding) error, does not respond to user input during the evaluation, or does not produce any meaningful content, we consider it a functional problem and the relevant performance field will be marked `-1`. In contrast, if the app frequently stutters, but does not crash, does not generate ANR, and reacts to user input normally, we consider it a performance problem and continue the evaluation. The bar plots include apps with performance problems, but exclude those with functional ones.

### Microbenchmark Data

Microbenchmark data is stored in `.txt` files, whose data units are consistent with the annotations in the figures. The data are organized into different subfolders under the `data` folder according to different scenarios.

| Folder         | Discription                                                  |
| -------------- | ------------------------------------------------------------ |
| access_latency | Benchmark data for `scripts/figs/micro_latency_cdf.pdf` |
| coherence_time | Benchmark data for `scripts/figs/coherence_cdf.pdf` |
| memory_size    | Benchmark data for `scripts/figs/datasize_cdf.pdf` |
| slack_interval | Benchmark data for `scripts/figs/interval_cdf.pdf`  |

## 3. Licensing

Our code and scripts are under the GPLv3 license.