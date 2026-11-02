#!/usr/bin/env python3
import sys
import typing


def get_file_to_open() -> str:
    f: typing.IO[str] = open(sys.argv[1])
    content = f.read()
    f.close()
    return content


def write_char_to_line(content: str) -> str | None:
    print("Enter new file name or "
          "leave empty to discard read text:")
    new_file = sys.stdin.readline().rstrip('\n')
    if new_file:
        lines = [line + '#' for line in content.split('\n')]
        lines_joined = '\n'.join(lines)
        f = open(new_file, 'w')
        f.write(lines_joined)
        f.close()
        print(f'\nTransform data:\n---\n{lines_joined}\n---')
        print(f"Saving data to '{new_file}'")
        print(f"Data saved in file '{new_file}'.")
        return lines_joined
    else:
        print('Not saving data.')
    return None


if __name__ == '__main__':

    if len(sys.argv) < 2:
        print(f'Usage: {sys.argv[0]} <file>')
    else:
        try:
            content = get_file_to_open()
            print("=== Cyber Archives Recovery & Preservation ===")
            print(f"Accessing file '{sys.argv[1]}'")
            print("---\n")
            print(content)
            print("\n---")
            print(f"File '{sys.argv[1]}' closed.\n")
            lines = write_char_to_line(content)
        except Exception as e:
            print(f"[STDERR] Error opening file '{sys.argv[1]}' : {e}",
                  file=sys.stderr)
