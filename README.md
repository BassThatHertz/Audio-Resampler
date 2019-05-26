# Audio Resampler

- This program allows you to change the sample rate of all WAV files in the current directory (the folder "Audio-Resampler-master" after you extract the ZIP file of this repository).

- The resampled files are saved as "*original name* [new sample rate]". For example, if you specify a desired sample rate of 44.1kHz, an audio file named "test.wav" will be saved as "test [44.1kHz].wav" after the resampling is complete.

- The orignal audio files are not replaced/deleted.

A batch resample of all WAV files in the the "Audio-Resampler-master" folder takes place; you do not have to manually select each file when running the program.

# Instructions:

Step 1:

Click on "Clone or download" and select "Download ZIP".

Step 2:

Extract the zip file. A new folder named "Audio-Resampler-master" should appear which contains resampler.py and two subfolders; "Windows" and "macOS".

Step 3: 

Create a folder in the "Audio-Resampler-master" folder. Name the folder "sox".

Step 4:
- If you're on Windows, move the files in the "Windows" folder into the "sox" folder.
- If you're on macOS, move the files in the "macOS" folder into the "sox" folder.

Step 5:

Put the WAV files that you want to change the sample rate of into the "Audio-Resampler-master" folder. You can now run the resampler by clicking on "resampler.py".
