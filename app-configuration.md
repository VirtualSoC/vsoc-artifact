# App Configuration

We carefully control the runtime workloads of the apps. To replicate the evaluation, you need to configure the resources and settings for the following apps.

## UHD video and 360 video

We play local videos instead of network videos during evaluation, in order to prevent network variations from affecting the results. You can download the videos [here](https://drive.google.com/drive/folders/1fKdt2Vkl85X0q-GxcRm13p6N2T_ROb2d?usp=sharing). After downloading, push the videos into the emulator, using `adb push PATH_TO_VIDEO /sdcard/Download/`.

For UHD video apps, please play videos with `uhd_` prefix; for 360 videos, please use videos with `360_` prefix.

## Livestream

For similar reasons, livestream apps also need to stream to a local network. Therefore, we need to first set up a livestream server app, which is responsible for receiving and displaying the live video feed. We use `nginx`, a popular web server, as the livestream server app. We use `RTMP` as the livestream protocol, as it is universally supported by livestream platforms.

To prevent the server app from influencing evaluation results, it is hosted in a dedicated machine connected to the evaluation PC via ethernet (see [here](setup.md#livestream-server) for hardware configuration). Please configure the server app as follows.

* **Windows.** Download the prebuilt `nginx` binary with RTMP support [here](https://github.com/illuspas/nginx-rtmp-win32/archive/refs/heads/dev.zip). Unzip the file and click on `nginx.exe` to start the server. You can verify that the server is running by opening `http://localhost:8080` in your browser.

* **Linux.** Install nginx with `sudo apt install todo`. You can verify that the server is running by opening `http://localhost:8080` in your browser.

After setting up the server, please configure the streaming settings in the livestream app. If the app asks for an RTMP url and a stream key, enter the url as `rtmp://SERVER-IP-ADDRESS/live`, and the stream key to be `123`. You can set other stream keys as well; just make sure to enter the same stream key when measuring FPS in the next section.

![](assets/eval_streamkey_1.png)

If the app does not have a dedicated field for stream key, append the stream key to the RTMP url (e.g., `rtmp://SERVER-IP-ADDRESS/live/123`), as shown in the picture below.

![](assets/eval_streamkey_2.png)

Do not forget to configure the streaming resolution to be `3840×2160` / `Match display` and frame rate to be `60` as well. These options are usually found in the app settings.

![](assets/eval_livestream_1.png)
