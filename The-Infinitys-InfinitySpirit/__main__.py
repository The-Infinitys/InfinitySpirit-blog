import os
import sys
import json
from script import github, convert, loadsetting, dirsearch


def main() -> int:
    def copy_right() -> None:
        print("∞" * 41)
        print("∞Infinity Spirit - Static Site Generator∞")
        print("∞" * 9 + " made by The Infinity's" + "∞" * 9)
        print("∞" * 41)

    if not os.path.isfile("InfinitySpirit.infinity"):
        print("InfinitySpirit Error: Invalid Current Directory")
        return 1

    copy_right()
    setting = loadsetting.load()

    return 0


if __name__ == "__main__":
    sys.exit(main())
