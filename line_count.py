#!/bin/bash

def count_lines_in_file(file_path: str) -> int:
    ''''''
    the_file = None
    try:
        the_file = open(file_path, 'r')
        line_count = 0
        for line in the_file:
            line_count += 1
        print(line_count)
    finally:
        if the_file != None:
            the_file.close()


def user_interface() -> None:
    ''''''
    while True:
        file_path = input('What file? ').strip()
        if file_path == '':
            break
        try:
            lines_in_file = count_lines_in_file(file_path)
            print('{} line(s) in {}'.format(lines_in_file, file_path))
        except OSError:
            print('Failed to open the file successfully')
        except ValueError:
            print('Failed to read from the file successfully; it is not a text file')



if __name__ == '__main__':
    #user_interface()
    count_lines_in_file(input())
