import os, sys
import shutil
from functools import partial

def makefolders(root_dir, folders):
    for folder in folders:print('CREATE '+folder)
    concat_path = partial(os.path.join, root_dir)
    makedirs = partial(os.makedirs, exist_ok=True)  # Python 3.2+
    for path in map(concat_path, folders):
        makedirs(path)

def movefolders(folders_to_move):
    print('MOVE ' + folders_to_move[0], folders_to_move[1])
    shutil.move(folders_to_move[0], folders_to_move[1])

def deletefolder(folder_to_delete):
    print('DELETE '+folder_to_delete)
    try:
        shutil.rmtree(folder_to_delete)
    except OSError as err:
        # print("OS error: {0}".format(err))
        print('Cannot delete', folder_to_delete, ' - ', folder_to_delete.split("/")[0], 'does not exist')

def list_files(startpath):
    print('LIST')
    for root, dirs, files in sorted(os.walk(startpath)):
        level = root.replace(startpath, '').count(os.sep)
        indent = ' ' * (level)
        if level>0:
            print('{}{}'.format(indent, os.path.basename(root)))
        
        # WON'T WORK IN ORDER
        # subindent = ' ' * 2 * (level + 0)
        # for d in sorted(dirs):
            # print('')
            # print('{}{}'.format(subindent, d))

if __name__=='__main__':
    root_dir = sys.argv[1]
    # root_dir = os.getcwd()
    folder_list = [['fruits','vegetables','grains','fruits/apples','fruits/apples/fuji'],
        ['grains/squash'],['foods']]
    moves = [['grains/squash', 'vegetables'],['grains', 'foods'],
        ['fruits', 'foods'],['vegetables', 'foods']]
    deletes = ['fruits/apples','foods/fruits/apples']
    makefolders(root_dir, folder_list[0])
    list_files(root_dir)
    makefolders(root_dir, folder_list[1])
    movefolders(moves[0])
    makefolders(root_dir, folder_list[2])
    movefolders(moves[1])
    movefolders(moves[2])
    movefolders(moves[3])
    list_files(root_dir)
    # deletefolder(deletes)
    for i in range(len(deletes)):
        deletefolder(deletes[i])
    list_files(root_dir)
