import os
import sys
import markdown
import json
from script import search, loadsetting

template_html = ""
replace_pos = {}
legacy_repository_name = "article-2024"


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
    else:
        print(
            "InfinitySpirit.markdownconverter error: failed to load location of",
            key,
        )
        sys.exit(1)


with open("./InfinitySpirit/layout/index.html") as f:
    template_html = f.read()
    find_elem("InfinitySpiritTitle", "title")
    find_elem("InfinitySpiritContent", "content")
    find_elem("InfinitySpiritDate", "date")


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
    markdown_title = ""
    markdown_date = ""
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
            markdown_title = markdown_line[9:]
        elif markdown_line.startswith("# ") and markdown_title == "":
            markdown_title = markdown_line[2:]
        elif markdown_line.startswith("<h1>") and markdown_title == "":
            markdown_title = markdown_line.replace("<h1>", "").replace("</h1>", "")
        elif markdown_line.startswith("# date: "):
            markdown_date = markdown_line[8:]
        elif markdown_line.startswith("<date>"):
            markdown_date = (
                markdown_line.replace("<date>", "")
                .replace("</date>", "")
                .replace(" ", "")
            )
        else:
            markdown_result += markdown_line + "\n"
    return {
        "html": markdown.markdown(
            markdown_result, extensions=extensions, extension_configs=configs
        ),
        "title": markdown_title,
        "date": markdown_date,
    }


def indent_html(html, indent_level) -> str:
    result = ""
    for line in html.split("\n"):
        result += " " * indent_level + line + "\n"
    return result


def convert(date, now_year, indent) -> None:
    target = {"year": date[0], "month": date[1]}
    if target["year"] == now_year:
        month_dir = str(target["month"]).zfill(2)
        article_dirs = search.folders(month_dir)
        article_index_list = []
        for article_dir in article_dirs:
            print(article_dir)
            markdown_path = "./" + month_dir + "/" + article_dir + "/article.md"
            if os.path.isfile(markdown_path):
                with open(markdown_path) as f:
                    converted = mdc(f.read())
                    base_html = converted["html"]
                    article_title = converted["title"]
                    article_date = converted["date"]
                    print("article id:", article_dir)
                    print("article title:", article_title)
                    print("article date:", article_date)
                    export_html = template_html
                    export_html = export_html.replace(
                        replace_pos["title"], article_title
                    )
                    base_html = (
                        indent_html(base_html, indent)
                        + "\n"
                        + indent * " "
                        + "</InfinitySpiritContent>"
                    )
                    export_html = export_html.replace(
                        replace_pos["content"], "<InfinitySpiritContent>\n" + base_html
                    )
                    export_html = export_html.replace(
                        replace_pos["date"],
                        "<InfinitySpiritDate>" + article_date + "</InfinitySpiritDate>",
                    )
                    with open(
                        "./" + month_dir + "/" + article_dir + "/index.html", mode="w"
                    ) as index_html:
                        index_html.write(export_html)
                    article_thumbnail = ""
                    for file_name in search.files("./" + month_dir + "/" + article_dir):
                        if file_name.startswith("thumbnail"):
                            article_thumbnail = file_name
                    article_index_list.append(
                        {
                            "id": article_dir,
                            "title": article_title,
                            "date": article_date,
                            "thumbnail": article_thumbnail,
                        }
                    )

        def get_date(obj) -> str:
            return obj["date"]

        with open("./" + month_dir + "/articles.json", mode="w") as f:
            article_index_list.sort(key=get_date, reverse=True)
            f.write(
                json.dumps(
                    {"articles": article_index_list},
                    indent=2,
                )
            )
        # legacy mode
        legacy_index = []
        for article_index in article_index_list:
            pass
            legacy_index.append(
                {
                    "index": "/"
                    + legacy_repository_name
                    + "/"
                    + month_dir
                    + "/"
                    + article_index["id"]
                    + "/",
                    "name": article_index["id"],
                    "thumbnail": "/"
                    + legacy_repository_name
                    + "/"
                    + month_dir
                    + "/"
                    + article_index["id"]
                    + "/"
                    + article_index["thumbnail"],
                    "title": article_index["title"],
                    "date": article_index["date"],
                }
            )
        legacy_index.sort(key=get_date, reverse=True)
        legacy_index = {"info": legacy_index}
        with open(
            "./" + "/index/" + str(target["year"]) + "-" + month_dir + ".json",
            mode="w",
        ) as f:
            f.write(
                json.dumps(
                    legacy_index,
                    indent=2,
                )
            )
