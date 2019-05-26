# Audio Resampler

This program changes the sample rate of all WAV files to 44.1kHz and names the files as "[original name] + [44.1kHz]". For example, an audio file named "test.wav" will be saved as "test [44.1kHz].wav" after the sample rate has been changed. The orignal audio files are not replaced/deleted.

Instructions:

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

Move all the WAV files that you want to change the sample rate of into the "Audio-Resampler-master" folder. You can now run the resampler by clicking on "resampler.py".
