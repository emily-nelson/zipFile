import zipfile
with zipfile.ZipFile(path_to_zip_file, 'r') as zip_ref:
    zip_ref.extractall(directory_to_extract_to)



# 1. check if folder has already been extracted
# 2. extract zip file to outer directory
# 3. go into extracted file folder
# 4. loop through contents and unzip files into inner directory
# 5. go back to outer directory
# 6. repeat

# considerations:
# 1. everytime you extract a file, it adds to the directory, does this affect the loop?


# do all outer extract first?
# then go through all sub folders