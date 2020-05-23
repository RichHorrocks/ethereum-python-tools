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

        print("Bytecode size is:",
              len(bytecode_string["object"]) / 2, "bytes")


if __name__ == "__main__":
    main()
