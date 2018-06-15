import os
import platform
import subprocess
import cat_factory


def print_header():
    print('-----------------------------')
    print('     LOLCAT FACTORY APP')
    print('-----------------------------')
    print('')


def create_directory():
    base_folder = os.path.abspath(os.path.dirname(__file__))
    folder = 'cat_pictures'
    full_path = os.path.join(base_folder, folder)

    if not os.path.exists(full_path) or not os.path.isdir(full_path):
        print('Creating new directory at {}'.format(full_path))
        os.mkdir(full_path)

    return full_path


def get_cats(full_path):
    print('Contacting server to download cats...')
    cat_count = 8
    for i in range(1, cat_count + 1):
        name = 'cat{}'.format(i)
        print('Downloading ' + name)
        cat_data = cat_factory.download_cats()
        cat_factory.save_cats(name, cat_data, full_path)
    print('Done!')
    return


def view_cats(folder):
    print('Displaying cats in OS window.')
    if platform.system() == 'Darwin':
        subprocess.call(['open', folder])
    elif platform.system() == 'Windows':
        subprocess.call(['explorer', folder])
    elif platform.system() == 'Linux':
        subprocess.call(['xdg-open', folder])
    else:
        print("We don't support your os: " + platform.system())


def main():
    print_header()
    full_path = create_directory()
    get_cats(full_path)
    view_cats(full_path)


if __name__ == '__main__':
    main()
