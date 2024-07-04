import os
import sys
import json


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
    setting = None
    with open("./The-Infinitys-InfinitySpirit/setting/setting.json") as f:
        setting = json.loads(f.read())
    print("Loaded settings")
    print("-" * 40)
    print("repository name:", setting["git-repository"]["name"])
    print("repository year:", setting["git-repository"]["year"])
    if setting["custom-date"] == True:
        print("auto date detecter is enabled")
    else:
        print("manual date detect")
        try:
            for date in setting["custom-date"]:
                print(date[0], "-", date[1])
        except IndexError:
            print(
                "InfinitySpirit Error: Invalid Custom Date Index",
                setting["custom-date"],
            )
            return 1
        except TypeError:
            print(
                "InfinitySpirit Error: Invalid Custom Date Type", setting["custom-date"]
            )
            return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
