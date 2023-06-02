import os
import sys
import traceback
import uuid
from PIL import Image

try:
    flag_argv_input = False
    if len(sys.argv) > 2:
        flag_argv_input = True
        source_file = sys.argv[2]
    else:
        source_file = input("输入原始图标路径:\n")
    source_path = os.path.dirname(source_file)
    source_file_name = os.path.splitext(os.path.split(source_file)[1])[0]
    new_file = os.path.join(source_path, f"{source_file_name}_new.ico")
    sizes = [16, 32, 64, 128, 256, 512]
    while os.path.exists(new_file):
        new_file = os.path.join(source_path, f"{source_file_name}_new_{uuid.uuid1().hex[0:8]}.ico")
    img = Image.open(source_file)
    icon_sizes = [(size, size) for size in sizes]
    img.save(new_file, sizes=icon_sizes)

    print("文件保存至:", new_file)
    if not flag_argv_input:
        input("按回车退出")
except Exception as e:
    print(f"发生错误({e.__class__.__name__}): {e}")
    print(traceback.format_exc())
    input("按回车退出")
