import os, shutil, subprocess
from argparse import ArgumentParser, RawTextHelpFormatter
from pathlib import Path


def line():
    print('-----------------------------------------------------------------------------------------------------------')

parser = ArgumentParser(formatter_class=RawTextHelpFormatter)

parser.add_argument('-p', '--wav-files-path', type=str, 
                    help='Enter the path of the directory that the WAV files are in. '
                    'If the path contains a space, it must be surrounded in double quotes.\n'
                    'If this argument is not specified, the current directory will be used. \n'
                    'Example: -p "C:/Users/H/Desktop/WAV files"')

parser.add_argument('-r', '--sample-rate', type=str, required=True, choices=['44100', '48000', '96000', '192000'],
                    help='Choose a sample rate (Hz).')

parser.add_argument('-os', '--operating-system', type=str.lower, required=True, choices=['windows', 'macos'],
                    help='Specify your operating system. Only the Windows and macOS operating systems are supported.')

args = parser.parse_args()

wav_files_path = os.listdir(args.wav_files_path) if args.wav_files_path else os.listdir()

wav_files = [filename for filename in wav_files_path if Path(filename).suffix == '.wav']

line()
print('The following WAV files have been found:')

for file in wav_files:
    print(file)

line()

if args.operating_system == 'windows':
    for file in os.listdir('Windows'):
        shutil.move(f'Windows/{file}', 'sox')
else:
    for file in os.listdir('macOS'):
        shutil.move(f'macOS/{file}', 'sox')

sox_path = os.path.join('sox', 'sox')

output_folder = f'{args.sample_rate} Hz'
os.makedirs(output_folder, exist_ok=True)

wav_files_path = args.wav_files_path if args.wav_files_path else ''

for file in wav_files:
    output_path = os.path.join(output_folder, file)
    args = [sox_path, '-G', os.path.join(wav_files_path, file), '-r', args.sample_rate, output_path]
    print(f'Resampling {file}...')
    subprocess.run(args)
    print(f'{file} resampled.')

line()
input("All done! You may now close this window.")
