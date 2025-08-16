import os

# create a folder
folder_name = "My_folder"
if not os.path.exists(folder_name):
    os.mkdir(folder_name)


files_names = ["as.txt", "dcf.txt", "fdnc.txt", "wer.png"]
# add files to the folder
for names in files_names:
    file_path = os.path.join(folder_name, names)
    with open(file_path, "w") as f:
        f.write(f"this is {names}\n")


# rename files having a particular extension
def rename_files(folder, extension):
    for i, f in enumerate(os.listdir(folder), start=1):
        if os.path.isfile(os.path.join(folder, f)) and f.endswith(extension):
            os.rename(
                os.path.join(folder, f), os.path.join(folder, (f"data_ {i}{extension}"))
            )


rename_files(folder_name, ".txt")
