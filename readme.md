# InfinitySpirit blog - Static Site Generator for writing blogs

<img src="./InfinitySpirit.jpeg" style="width:100%;">

## A Crazy Static Site Generator

Infinity Spirit is a static site generator.
Created by [The Infinity's](https://the-infinitys.f5.si/)

## links

- [change log](./change-log.md)

## How to use

first, please clone this repository's files.

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

## settings

You can change InfinitySpirit's function by [setting.json](InfinitySpirit/setting/setting.json)
default json

```json
{
  "custom-date": "all",
  "git-repository": {
    "name": "InfinitySpirit",
    "year": 2024
  },
  "converter": {
    "indent-level": 10
  }
}
```

### customdate

you can select which directory will be converted by InfinitySpirit
if you selected `all`, InfinitySpirit will convert all month articles.
if you selected `true`, InfinitySpirit will convert this month articles(for example if you do on July, `07` directory will be converted.)
if you want to set custom mode, you have to set a value like

```
[
  [2024, 5],
  [2024, 6],
  [2024, 7],
  [2024, 12],
]
```

### git repository
this setting was made for check root name and check repository year.
This repository is intended to be newly cloned every year and to separate articles by year.
It is set for this reason.
### converter
It is set for customize converter.

## style
you can change style by edit [InfinitySpirit/layout/](./InfinitySpirit/layout/)
default is recommended

# copyright
The Infinity's
