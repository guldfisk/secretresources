import os
import sys

from secretresources import paths


def create_project(name: str):
    path = paths.project_name_to_secret_dir(name)

    if os.path.exists(path):
        print(f'Project called "{name}" already exists')
        return

    os.makedirs(path)

    print(f'created project "{name}"')


def _create_project(*args):
    if len(args) != 1:
        print('Invalid arguments, expected: <str>')
        return

    create_project(*args)


def run():
    if len(sys.argv) < 2:
        print('Invalid invocation, use: <Command> arguments')
        return

    command = sys.argv[1]
    arguments = sys.argv[2:]

    if command == 'create_project':
        _create_project(*arguments)

    else:
        print(f'Unknown command "{command}"')


if __name__ == '__main__':
    run()
