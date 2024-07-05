const makeIndex = () => {
  const article_index = document.createElement("div");
  article_index.className = "article-index";
  const article_body = document.querySelector(".article-body");
  const article_content = document.querySelector("InfinitySpiritContent");
  const addIndex = (element) => {
    const tag = document.createElement(element.tagName);
    tag.innerHTML = element.innerHTML;
    tag.onclick = () => {
      element.scrollIntoView({
        behavior: "smooth",
        block: "end",
        inline: "center",
      });
    };
    article_index.append(tag);
  };
  for (let index = 0; index < article_content.children.length; index++) {
    const element = article_content.children[index];
    const tagname = element.tagName.toLowerCase();
    if (
      tagname in
      {
        h1: "",
        h2: "",
        h3: "",
        h4: "",
      }
    ) {
      addIndex(element);
    }
  }
  article_body.append(article_index);
};
makeIndex();
const recommendArticles = () => {
  const article_list = document.createElement("div");
  article_list.className = "articles-recommended";
  document.querySelector(".article-body").append(article_list);
};
recommendArticles();
