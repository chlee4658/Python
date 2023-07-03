import os
import time
from zAI import zImage

file_name = "IMG_0067.jpg"

def file_rename(path_dir, file_name):
    get_time = os.path.getmtime(path_dir + "\\" + file_name)
    file_date = time.strftime("%Y%m%d_%H%M", time.localtime(get_time))

    myPhoto = zImage(path_dir + "\\" + file_name)
    text = myPhoto.label(backend='Microsoft')

    to_filename = file_date

    for i in text:
        to_filename = to_filename + "_" + i

    to_filename = to_filename[0:250] + ".jpg"

    command = "rename " + path_dir + "\\" + file_name + " \"" + to_filename + "\""
    os.system(command)

    return 0


if __name__ == "__main__":
    path_dir = "G:\그림\사진들"
    file_list = os.listdir(path_dir)
    image_list = list()

    # 이미지 파일 리스트 가져오기
    for i in file_list:
        try:
            if i.split(".")[1]=="jpg":
                image_list.append(i)
        except Exception as e:
            print(e)

    # 파일 이름 변경
    for i in image_list:
        file_rename(path_dir, i)
        time.sleep(3)
