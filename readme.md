# InfinitySpirit - Static Site Generator
<img src="./InfinitySpirit.jpeg" style="width:100%;">

## A Crazy Static Site Generator
Infinity Spirit is a static site generator.
Created by [The Infinity's](https://the-infinitys.f5.si/)

## links
* [change log](./change-log.md)

## How to use
first, please clone this repository.
```
git clone https://github.com/The-Infinitys/InfinitySpirit
```

then, go to the directory that cloned repository.
```
cd InfinitySpirit
```

next, please make articles.
for example, if you want to write an article that named "technology of AI", on July 13...
```
mkdir 07/technology-of-AI
cd 07/technology-of-AI/
touch article.md
```
then, please write article to article.md with markdown.
and if you need, add thumbnail image(example: thumbnail.png, thubmnail.webp, thumbnail.svg)

Finally, move repository root dir and run InfinitySpirit
```
cd ../../
```
```
python InfinitySpirit
```
