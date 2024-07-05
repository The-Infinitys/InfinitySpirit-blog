import os, sys, markdown
from script import dirsearch

template_html = ""
replace_pos = {"meta-title": "", "title": "", "content": ""}


def find_elem(tag, key) -> None:
    if "<" + tag + ">" in template_html and "</" + tag + ">" in template_html:
        print(
            "InfinitySpirit.markdownconverter log: succeeded to load location of",
            key,
        )
        replace_pos[key] = template_html[
            template_html.find("<" + tag + ">") : template_html.find("</" + tag + ">")
            + len("</" + tag + ">")
        ]
        print(replace_pos[key])
    else:
        print(
            "InfinitySpirit.markdownconverter error: failed to load location of",
            key,
        )
        sys.exit(1)


with open("./The-Infinitys-InfinitySpirit/template/index.html") as f:
    template_html = f.read()
    find_elem("InfinitySpiritMetaTitle", "meta-title")
    find_elem("InfinitySpiritArticleTitle", "title")
    find_elem("InfinitySpiritContent", "content")


def convert(date) -> None:
    target = {"year": date[0], "month": date[1]}
    pass
