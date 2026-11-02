#!/usr/bin/env python3

def secure_archive(
        file: str,
        action: str = "read",
        content: str = "") -> tuple[bool, str]:
    try:
        if action == "read":
            with open(file, "r") as f:
                content = f.read()
            return (True, content)
        elif action == "write":
            with open(file, "w") as f:
                f.write(content)
            return (True, "Content successfully written to file")
        elif action == "append":
            with open(file, "a") as f:
                f.write(content)
            return (True, "Content successfully appended to file")
        else:
            return (False, f"Invalid action '{action}'")
    except Exception as e:
        return (False, f"{e}")


if __name__ == "__main__":
    print("=== Cyber Archives Security ===\n")
    print("Using 'secure_archive' to read from a nonexistent file:")
    print(f"{secure_archive('/not/existing/file')}")

    print("\nUsing 'secure_archive' to write to an inaccessible file:")
    print(f"{secure_archive('forb.txt', 'write', 'helloworld42')}")

    print("\nUsing 'secure_archive' to read from a regular file:")
    print(f"{secure_archive('test.txt')}")

    print("\nUsing 'secure_archive' to write previous content to a new file:")
    result = secure_archive('new.txt', 'write',
                            secure_archive('test.txt')[1])
    print(f"{result}")

    print("\nUsing 'secure_archive' to append previous content "
          "to a new file:")
    result = secure_archive('new.txt',
                            'append',
                            secure_archive('test2.txt')[1])
    print(f"{result}")

    print("\nUsing 'secure_archive' with an action "
          "other than 'write','read','append'")
    print(f"{secure_archive('new.txt', 'delete', 'byebyeworld24')}")
