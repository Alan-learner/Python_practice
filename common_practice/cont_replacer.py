import os
import re

"""
this stript is to change certain str in specific directory
authur:Alan_learner
date:2021/10/22
"""


pwd = r'D:\files'
old_str = "learning"
new_str = "coding"

def files_update(dir,old,new):
    """

    :param dir: directory the operating files in
    :param old: contens that you want to replace
    :param new: new contens that replace the old
    :return: replacing operation
    """
    content = os.walk(dir)
    for path,dir_list,file_list in content:
        for file in file_list:
            file_path = os.path.join(path,file) #find all files in this dir
            r = open(file_path,'r',encoding='utf-8')
            txt = r.read()
            r.close()
            res = re.sub(old,new,txt,count=0,flags=0)
            w = open(file_path,'w',encoding='utf-8')
            w.write(res)
            w.close
            
            
def main():
    files_update(pwd,old_str,new_str)   # please input your params
    
    
if __name__ == '__main__':
    print('yes')
    main()
            