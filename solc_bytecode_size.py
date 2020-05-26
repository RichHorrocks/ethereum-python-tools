import sys
import json

# Input argument is a file containing the output of the BYTECODE field from
# Remix's "Compilation Details" modal.
#
#   > python solc_bytecode_size.py bytecode.txt


def main():
    with open(sys.argv[1], "r") as f:
        data = f.read()
        bytecode_string = json.loads(data)
        print("Bytecode size is: {:.0f} bytes".format(
            len(bytecode_string["object"]) / 2))


if __name__ == "__main__":
    main()

