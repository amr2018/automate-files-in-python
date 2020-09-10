import os
import shutil
import time

#==============================================================================================================

user_name = os.environ['USERNAME']
my_dir = "G:/MyFiles/"
sorce = f"C:/Users/{user_name}/Downloads"
extensions = ['.exe .msi', '.pdf .txt .tar', '.rar .zip .jz', '.js .py', '.wave .mp3', '.mp4 .avi .mkv', '.png .jpg .gif .psd .bmp .PNG']
folder_names = ['exe', 'text', 'Compressed', 'scripts', 'audio', 'videos', 'imgs', 'other']
files = []

#make a new dirs
def make_diers(d):
    for folder in folder_names:
        if os.path.exists(d + folder):
            pass
        else:
            os.makedirs(d + folder)


#==============================================================================================================

#get all files from sorce
def get_files_from(sorce):
    for folder in os.listdir(sorce):
        if os.path.isdir(sorce + '/' + folder):
            for file in os.listdir(sorce + '/' + folder):
                if os.path.isfile(sorce + '/' + folder + '/' + file):
                    files.append(sorce + '/' + folder + '/' + file)

#==============================================================================================================

#move all fiels
def Move_files_to():

    for file in files: #get files paths
        for ex in extensions:
            for extension in ex.split(' '):
                if file.endswith(extension):
                    index = extensions.index(ex)
                    folder_name = folder_names[index] + '/'
                    dst = my_dir + folder_name + file.split('/')[-1]
                    time.sleep(1)
                    try:
                        if os.path.exists(dst):
                            files.remove(file)
                            os.remove(file)
                        else:
                            files.remove(file)
                            shutil.move(file, dst)
                    except:
                        Move_files_to() #restart the function if any problem


 #repeat working after 1s
    time.sleep(1)
    make_diers(my_dir) # make dires and chek if any folder not exists
    get_files_from(sorce) # get all files paths from the sorce of file and store them in list called files
    Move_files_to() # get all file paths and move all to distnaton file

#==============================================================================================================


def main():
    time.sleep(1)
    make_diers(my_dir)
    get_files_from(sorce)
    Move_files_to()

if __name__ == "__main__":
    main()
#==============================================================================================================
