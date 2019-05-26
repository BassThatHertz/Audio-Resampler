import os 

current_dir_files = os.listdir()

compatible_filetypes = ["wav"]
compatible_file_list = [filename for filename in current_dir_files if filename.split(".")[-1] in compatible_filetypes]

filepath_of_sox = os.path.join("sox", "sox")

desired_sample_rate = int(input("What would you like to change the sample rate to? \nUnit: Hz \nExample: For 44.1kHz, enter '44100'\nPlease enter an integer: "))

sample_rate_in_kHz = desired_sample_rate / 1000
end_of_filename = " [{}kHz]".format(sample_rate_in_kHz)
print(end_of_filename)

for file in compatible_file_list:
    print("Resampling {}...".format(file))
    os.system('{} -G "{}" -r {} "{}".wav'.format(filepath_of_sox, file, desired_sample_rate, file + end_of_filename))
