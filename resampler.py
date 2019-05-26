import os 

current_dir_files = os.listdir()

filepath_of_sox = os.path.join("sox", "sox")

compatible_filetypes = ["wav"]
compatible_file_list = [filename for filename in current_dir_files if filename.split(".")[-1] in compatible_filetypes]


for file in compatible_file_list:
    print("Resampling {}...".format(file))
    os.system('{} -G "{}" -r 44100 "{}".wav'.format(filepath_of_sox, file, file + " [44.1kHz]"))

