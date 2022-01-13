# osu-resampler
A video resampler for osr2mp4/danser high fps videos.

The resampler can also use ffmpeg-bar for better experience. https://github.com/sidneys/ffmpeg-progressbar-cli

Compiled using pyinstaller.	

Commands:
-h/--help -> Show help. <br>
-i -> Full path to video file you want to resample. <br>
-fps -> FPS of the video you're trying to resample. <br>
-crf -> Quality of the video, the lower the better (0 is lossless, default=7). <br>
--gui -> Choice of type of gui - ffmpeg/ffbar(ffmpeg-bar). <br>
output -> After all extra arguments, write <Output folder path> <Output video name> (The space in between is needed).
