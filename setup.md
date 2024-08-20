# Experimental Setup

The evaluation in the vSoC paper tests the extreme performance of the various virtual devices in a mobile system. Therefore, the results are heavily related to your host machine's hardware configurations. In our paper, we use a high-end and a middle-end PC for evaluation. Their configurations are as follows.

#### High-end PC

* CPU: 24-core Intel i9-13900K CPU @ 3.0 GHz
* Memory: 64 GB RAM (DDR5 4800 MHz)
* GPU: NVIDIA RTX 3060 dedicated GPU
* Display: 3840×2160
* Camera: HIKVISION V148 USB camera (4K 60FPS)

#### Middle-end PC

* CPU: 6-core Intel i7-10750H CPU @ 2.6 GHz
* Memory: 16 GB RAM (DDR4 3200 MHz)
* GPU: NVIDIA GTX 1660 Ti dedicated GPU
* Display: 2560×1600
* Camera: integrated webcam (1080P 60FPS)

**Note 1**: If you want to faithfully reproduce the results, please use the Intel x64 CPU + NVIDIA GPU combination. Other hardware combinations (e.g. ARM CPUs or Intel GPUs) also work on vSoC, but they are less tested and are prone to bugs and inefficiencies.

**Note 2**: make sure you are using the dedicated GPU to run the emulators if your PC has both a dedicated and an integrated GPU. You can check the GPU that vSoC is using by turning on the `GPU Engine` tab in the Windows Task Manager. If the GPU is not correct, please change the default GPU for the executable `bin\qemu-system-x86_64.exe` with [this guide](https://www.asus.com/support/faq/1044213/).

**Note 3**: the benchmark results are subject to your machine's current state. If your PC is overheating, or is concurrently performing other computationally intensive tasks, the results may be lower than you expect.

The above setup allows you to reproduce 40 of the 50 apps we evaluate. Further, if you want to reproduce our results for the remaining 10 livestream apps in our evaluation, you are recommended to use an dedicated x64 computer running Linux or Windows as the livestream server. The configuration we use is listed below.

#### Livestream Server

* CPU: 6-core Intel i7-8700K CPU @ 3.7 GHz
* Memory: 32 GB RAM (DDR4 3200 MHz)
* Display: 1920×1080
* 1GbE wired connection to the high-end/middle-end PC
