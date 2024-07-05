import markdown

template_html = ""
with open("./The-Infinitys-InfinitySpirit/template/index.html") as f:
    template_html = f.read()
    if (
        "<InfinitySpiritMetaTitle>" in template_html
        and "</InfinitySpiritMetaTitle>" in template_html
    ):
        print("InfinitySpirit.markdownconverter log: succeeded to load location of meta title")
