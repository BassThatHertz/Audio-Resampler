import os 

wav_files = [filename for filename in os.listdir() if os.path.splitext(filename)[-1] == '.wav']

filepath_of_sox = os.path.join("sox", "sox")

print('You can choose one of the following sample rates:')

sample_rate_options = ['44.1 kHz', '48 kHz', '96 kHz', '192 kHz']

for position, sample_rate in enumerate(sample_rate_options):
	print(position, sample_rate) 

sample_rate_index = int(input('Choose your desired sample rate by entering the number that it is associated with.\n'
	'For example, to choose 44.1 kHz, enter 0: '))

sample_rate = int(sample_rate_options[sample_rate_index][:-4]) * 1000

end_of_filename = ' [' + sample_rate_options[sample_rate_index] + ']'

for file in wav_files:
    new_filename = os.path.splitext(file)[0] + end_of_filename + ".wav"
    print("Resampling {}...".format(file))
    os.system('{} -G "{}" -r {} "{}"'.format(filepath_of_sox, file, desired_sample_rate, new_filename))
    print("{} resampled. Resampled file saved as {}".format(file, new_filename))

input("You may now close this window.")
