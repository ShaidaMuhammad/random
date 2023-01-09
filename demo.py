import subprocess
import os
import argparse

def make_file_accessible(self, file_path: str, file_name: str, user: str) -> str:
    full_path = os.path.join(file_path, file_name)
    command = ['sudo', 'chown', f'{user}:', full_path]
    subprocess.run(command)
    return full_path

if __name__ == "__main__":
    # create an argument parser object
    parser = argparse.ArgumentParser()

    # add the arguments to the parser
    parser.add_argument("arg1", type=str, help="first argument")
    parser.add_argument("arg2", type=str, help="second argument")
    parser.add_argument("arg3", type=str, help="third argument")

    # parse the arguments
    args = parser.parse_args()

    # call the function and pass the arguments
    make_file_accessible(args.arg1, args.arg2, args.arg3)
