import os
import sys
import datetime
from script import github, convert, loadsetting


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
    target_dates = None
    if setting["custom-date"] == True:
        target_dates = datetime.datetime.now()
        target_dates = [[target_dates.year, target_dates.month]]
    else:
        target_dates = setting["custom-date"]
    for target_date in target_dates:
        convert.convert(target_date, setting["git-repository"]["year"])
    github.renew()
    return 0


if __name__ == "__main__":
    sys.exit(main())
