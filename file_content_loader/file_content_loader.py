import pkg_resources


def load_file_content(package, relative_path):
    absolute_path = pkg_resources.resource_filename(package, relative_path)
    with open(absolute_path, 'r') as file_to_read:
        return file_to_read.read().replace('\n', '')