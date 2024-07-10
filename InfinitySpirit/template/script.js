const create_gotop_button = () => {
  const go_top = document.createElement("button");
  go_top.id = "go-top";
  go_top.innerHTML = `
  <svg
    viewBox="0 0 100 100"
    version="1.1"
    xmlns="http://www.w3.org/2000/svg"
    xmlns:xlink="http://www.w3.org/1999/xlink"
    fill="none"
    stroke="#888"
    stroke-width="2">
    <g>
      <circle cx="50" cy="50" r="40" />
      <path d="M 80 55 L50 45 L 20 55" />
      <path d="M 80 65 L50 55 L 20 65" />
    </g>
  </svg>
  `;
  go_top.onclick = () => {
    document.querySelector("body").scrollIntoView({
      behavior: "smooth",
      block: "start",
      inline: "center",
    });
  };
  document.body.append(go_top);
};
create_gotop_button();
const makeIndex = () => {
  const article_index = document.querySelector(".article-index");
  const article_content = document.querySelector("InfinitySpiritContent");
  const addIndex = (element) => {
    const tag = document.createElement(element.tagName);
    tag.innerHTML = element.innerHTML;
    tag.onclick = () => {
      element.scrollIntoView({
        behavior: "smooth",
        block: "center",
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
  const scroll_index = () => {
    const body_scroll = window.scrollY / document.body.scrollHeight;
    const index_scrollTop_target =
      body_scroll * document.querySelector(".article-index").scrollHeight -
      document.querySelector(".article-index").scrollTop;
    const index_scrollTop_now =
      document.querySelector(".article-index").scrollTop;
    document.querySelector(".article-index").scrollTop +=
      (index_scrollTop_target - index_scrollTop_now) / 30;
    requestAnimationFrame(scroll_index);
  };
  scroll_index();
};
makeIndex();

let renew_clock_watch_count = 0;
try {
  document.querySelector("InfinitySpiritDate").innerHTML =
    document.querySelector("date").innerHTML;
} catch (SyntaxError) {
  console.log("not found date object");
}
if (document.querySelector(".article-title").innerHTML == "") {
  document.querySelector("InfinitySpiritArticleTitle").innerHTML =
    document.querySelector("InfinitySpiritContent h1").innerHTML;
}
const renew_Infinity_clock = () => {
  renew_clock_watch_count = (renew_clock_watch_count + 1) % 5;
  if (renew_clock_watch_count == 0) {
    const now = new Date();
    const clock_hand_svg = document.querySelector(".Infinity-clock_hands");
    const now_hours = now.getHours();
    const now_minutes = now.getMinutes();
    const now_seconds = now.getSeconds() + now.getMilliseconds() / 1000;
    const short_way =
      ((((now_hours + now_minutes / 60) / 12) * 360 - 90) * Math.PI) / 180;
    const long_way = (((now_minutes / 60) * 360 - 90) * Math.PI) / 180;
    const thin_way = (((now_seconds / 60) * 360 - 90) * Math.PI) / 180;
    clock_hand_svg.innerHTML =
      `
    <path d="M50 50,l` +
      (30 * Math.cos(thin_way)).toString() +
      " " +
      (30 * Math.sin(thin_way)).toString() +
      `Z" stroke-width="1" />
    <path d="M50 50,l` +
      (30 * Math.cos(long_way)).toString() +
      " " +
      (30 * Math.sin(long_way)).toString() +
      `Z" />
    <path d="M50 50,l` +
      (20 * Math.cos(short_way)).toString() +
      " " +
      (20 * Math.sin(short_way)).toString() +
      `Z" />
  `;
  }
  requestAnimationFrame(renew_Infinity_clock);
};
renew_Infinity_clock();