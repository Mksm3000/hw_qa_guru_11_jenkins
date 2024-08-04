import os


def path(value):
    starting_path = os.path.abspath(__file__)
    project_root_directory = os.path.join(starting_path, os.pardir, os.pardir)
    image_directory = os.path.join(project_root_directory, 'resources')
    return os.path.abspath(os.path.join(image_directory, value))
