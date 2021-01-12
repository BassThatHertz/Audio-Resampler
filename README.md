A command line program that changes the sample rate of WAV files.

#Usage:

```
usage: resampler.py [-h] [-p WAV_FILES_PATH] -r {44100,48000,96000,192000} -os {windows,macos}

Available arguments:
  -h, --help            show this help message and exit
  -p WAV_FILES_PATH, --wav-files-path WAV_FILES_PATH
                        Enter the path of the directory that the WAV files are in. If the path contains a space, it must be surrounded in double quotes.
                        If this argument is not specified, the current directory will be used.
                        Example: -p "C:/Users/H/Desktop/WAV files"
  -r {44100,48000,96000,192000}, --sample-rate {44100,48000,96000,192000}
                        Choose a sample rate (Hz).
  -os {windows,macos}, --operating-system {windows,macos}
                        Specify your operating system. Only the Windows and macOS operating systems are supported.
```

# Examples:
`python resampler.py -p C:\Users\H\Desktop -r 48000 -os windows`
`python resampler.py -r 96000 -os macos`