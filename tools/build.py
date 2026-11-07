"""Render the deliberately small Markdown subset used by the handbook. No raw HTML."""
import argparse
from pathlib import Path
import html
import json
import re
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]


def inline(value):
    value = html.escape(value)
    def link(match):
        label, url = match.groups()
        if urlsplit(html.unescape(url)).scheme != 'https':
            raise ValueError('Only HTTPS links are supported')
        return '<a href="' + url + '">' + label + '</a>'
    value = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', link, value)
    return re.sub(r'`([^`]+)`', r'<code>\1</code>', value)


def markdown(value):
    blocks = []
    for line in value.splitlines():
        if not line.strip():
            continue
        if line.startswith('# '):
            continue
        if line.startswith('## '):
            blocks.append('<h3>' + inline(line[3:]) + '</h3>')
        else:
            # Numbered steps remain numbered readable paragraphs; native page TOC is separate.
            blocks.append('<p>' + inline(line) + '</p>')
    return '\n'.join(blocks)


def render(lang):
    catalog = json.loads((ROOT / 'catalog.json').read_text(encoding='utf-8'))
    prefix = '/en' if lang == 'en' else ''
    title = 'Player Wiki' if lang == 'en' else '玩家 Wiki'
    toc = ''.join('<a href="#' + row['id'] + '">' + html.escape(row[lang]) + '</a>' for row in catalog)
    articles = []
    for row in catalog:
        text = (ROOT / 'pages' / lang / (row['id'] + '.md')).read_text(encoding='utf-8')
        articles.append('<section id="' + row['id'] + '"><h2>' + html.escape(row[lang]) + '</h2>\n' + markdown(text) + '</section>')
    alt = '/wiki' if lang == 'en' else '/en/wiki'
    alternate_lang = 'zh-CN' if lang == 'en' else 'en'
    language = '中文' if lang == 'en' else 'EN'
    nav = [('','Home' if lang=='en' else '主页'),('/download','Download' if lang=='en' else '下载'),('/rules','Rules' if lang=='en' else '规则'),('/tasks','All Tasks' if lang=='en' else '全部任务')]
    nav_html = ''.join('<a href="' + (prefix+path+'/' if not path else prefix+path) + '">'+label+'</a>' for path,label in nav)
    return f'''<!DOCTYPE html>
<html lang="{'en' if lang=='en' else 'zh-CN'}"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} · BoardRaid</title>
<meta name="description" content="{title}: BoardRaid installation, gameplay and replay handbook.">
<link rel="icon" href="/favicon.ico" sizes="any">
<link rel="canonical" href="https://boardraid.cn{prefix}/wiki">
<link rel="alternate" hreflang="{alternate_lang}" href="https://boardraid.cn{alt}">
<link rel="stylesheet" href="/assets/css/style.css?v=20261026a">
<link rel="stylesheet" href="/assets/css/art.css?v=20261026a">
<link rel="stylesheet" href="/assets/css/wiki.css?v=20261026a">
<script src="/assets/js/i18n.js?v=20261026a"></script>
<script src="/assets/js/motion.js?v=20261026a"></script>
</head><body data-page="wiki">
<header class="topbar"><div class="wrap topbar__inner"><a class="brand" href="{prefix+'/' if prefix else '/'}"><img class="brand__mark" src="/assets/brand/logo-mark.webp" width="22" height="22" alt=""><span class="brand__name">BOARDRAID</span></a><nav class="nav">{nav_html}<a href="{prefix}/wiki">Wiki</a></nav><a class="langtoggle" href="{alt}" lang="{alternate_lang}" hreflang="{alternate_lang}">{language}</a></div></header>
<main class="wrap br-wiki"><aside class="br-wiki-nav"><h1>{title}</h1><p>0.5.5 · Minecraft 1.16.1</p><nav aria-label="{'Chapters' if lang=='en' else '章节'}">{toc}</nav><a href="https://github.com/BoardraidDev/wiki">{'Edit this handbook' if lang=='en' else '编辑与贡献'}</a><a href="https://github.com/BoardraidDev/api-docs">API Docs</a></aside><article class="br-wiki-content"><p class="br-wiki-note">{'Review draft · Updated 2026-11-07. Official rules take precedence.' if lang=='en' else '审阅初稿 · 更新于 2026-11-07。实际对局以房规和正式规则为准。'}</p>{''.join(articles)}</article></main>
<footer class="wrap"><p>BoardRaid · <a href="https://github.com/BoardraidDev/wiki">Wiki</a> · <a href="https://github.com/BoardraidDev/releases">Releases</a></p></footer>
</body></html>
'''


def self_test():
    assert '<script>' not in inline('<script>alert(1)</script>')
    try:
        inline('[unsafe](javascript:alert)')
    except ValueError:
        pass
    else:
        raise AssertionError('unsafe URL accepted')
    assert '<a href="https://example.org">safe</a>' == inline('[safe](https://example.org)')
    assert '<h3>' in markdown('## Heading\nText')
    print('PASS: HTML escaping, unsafe URL rejection, link and heading rendering')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--self-test', action='store_true')
    parser.add_argument('--output', type=Path, default=ROOT / 'site')
    args = parser.parse_args()
    if args.self_test:
        self_test()
    else:
        for lang, rel in [('zh', 'wiki.html'), ('en', 'en/wiki.html')]:
            path = args.output / rel
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(render(lang), encoding='utf-8', newline='\n')
        print('Built wiki.html and en/wiki.html')
