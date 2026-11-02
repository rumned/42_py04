#!/usr/bin/env python3
import sys
import typing


def get_file_to_open() -> str:
    f: typing.IO[str] = open(sys.argv[1])
    content = f.read()
    f.close()
    return content


def write_char_to_line(content: str) -> str:
    lines = [line + '#' for line in content.split('\n')]
    lines = '\n'.join(lines)
    print(f'Transform data:\n---{lines}\n---')
    new_file = input('Enter new file name or:'
                     'leave empty to discard read text:', end='')
    if new_file:
        new_file = open(new_file, 'w')
        new_file = lines
        print(f"Data saved in '{new_file}'")
        return new_file
    else:
        print('Not saving data.')


if __name__ == '__main__':

    if len(sys.argv) < 2:
        print('Usage: ft_ancient_text.py <file>')
    else:
        try:
            content = get_file_to_open()
            content = write_char_to_line(content)
        except Exception as e:
            print(f"Error opening file '{sys.argv[1]}' : {e}")
        else:
            print("=== Cyber Archives Recovery ===")
            print(f"Accessing file '{sys.argv[1]}'")
            print("---\n")
            print(content)
            print("\n---")
            print(f"File '{sys.argv[1]}' closed.")
