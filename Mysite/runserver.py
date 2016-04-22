import os

root = r'E:\MyCode\DjangoProjects'

allfiles = os.listdir(root)
allfolders = []
for name in allfiles:
    if name not in ['.gitattributes','.gitignore','.git'] and \
    os.path.isdir(os.path.join(root,name)):
        allfolders.append(name)
    
for i in range(0,len(allfolders)):
    print str(i+1)+'.'+allfolders[i]
no = raw_input("input the server no:")


cmd = [
    'E:',
    'cd '+os.path.join( root, allfolders[int(no)-1]),
    #'manage.py runserver 127.0.0.1:8000',
    'manage.py runserver 0.0.0.0:8000',
    ]

for c in cmd:
    os.system(c)
    print c
##os.system('E:')
