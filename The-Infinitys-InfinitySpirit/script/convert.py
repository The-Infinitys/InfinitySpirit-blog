import os, sys, markdown

template_html = ""
replace_pos = {"meta-title": "", "title": "", "content": ""}
with open("./The-Infinitys-InfinitySpirit/template/index.html") as f:
    template_html = f.read()
    if (
        "<InfinitySpiritMetaTitle>" in template_html
        and "</InfinitySpiritMetaTitle>" in template_html
    ):
        print(
            "InfinitySpirit.markdownconverter log: succeeded to load location of meta title"
        )
        
    else:
        print(
            "InfinitySpirit.markdownconverter error: failed to load location of meta data"
        )
        sys.exit(1)
