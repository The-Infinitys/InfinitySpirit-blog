import os, sys, markdown
from script import dirsearch, loadsetting

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


def mdc(markdown_text):
    extensions = [
        "extra",
        "admonition",
        "codehilite",
        "legacy_attrs",
        "legacy_em",
        "nl2br",
        "sane_lists",
        "toc",
        "wikilinks",
        "meta",
        "smarty",
    ]
    configs = {
        "codehilite": {
            "noclasses": True,
            "pygments_style": "monokai",
        }
    }
    global markdown_title
    markdown_result = ""
    convert_mode = {"~~": False}
    for markdown_line in markdown_text.split("\n"):
        # ~~を変換する機能がないので自分で実装する
        while "~~" in markdown_line:
            if convert_mode["~~"]:
                markdown_line = markdown_line.replace("~~", "</s>", 1)
            else:
                markdown_line = markdown_line.replace("~~", "<s>", 1)
            convert_mode["~~"] = not convert_mode["~~"]
        if markdown_line.startswith("# title: "):
            markdown_title = markdown_line[:]
        elif markdown_line.startswith("date: "):
            markdown_result += "<date>" + markdown_line[6:] + "</date>\n"
        else:
            markdown_result += markdown_line + "\n"
    return markdown.markdown(
        markdown_result, extensions=extensions, extension_configs=configs
    )


def convert(date, now_year) -> None:
    target = {"year": date[0], "month": date[1]}
    if target["year"] == now_year:
        month_dir = str(target["month"]).zfill(2)
        article_dirs = dirsearch.folders(month_dir)
        for article_dir in article_dirs:
            print(article_dir)
            markdown_path = "./" + month_dir + "/" + article_dir + "/article.md"
            if os.path.isfile(markdown_path):
                base_html = mdc(markdown_path)
                print(base_html)
