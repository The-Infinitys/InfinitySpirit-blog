const generateTitle = () => {
  const InfinitySpiritTitle = document.querySelector(
    "InfinitySpiritArticleTitle"
  );
  const article_body = document.querySelector(".article-body");
  const titleBox = document.createElement("div");
  titleBox.innerHTML = InfinitySpiritArticleTitle.innerHTML;
  titleBox.className = "article-title";
};
generateTitle();
