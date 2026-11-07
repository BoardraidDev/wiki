"""Render the deliberately small Markdown subset used by the handbook. No raw HTML."""
import argparse
from pathlib import Path
import html
import json
import re
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]


def validate_catalog(catalog):
    ids = set()
    for row in catalog:
        slug = row['id']
        if not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', slug) or slug in ids:
            raise ValueError('Invalid or duplicate chapter identifier')
        if not all(isinstance(row[lang], str) and row[lang] for lang in ['zh', 'en']):
            raise ValueError('Missing chapter title')
        ids.add(slug)


def inline(value):
    value = html.escape(value)
    def link(match):
        label, url = match.groups()
        parsed = urlsplit(html.unescape(url))
        if not (re.fullmatch(r'#[a-z0-9-]+', url) or
                (parsed.scheme == 'https' and parsed.hostname and not parsed.username
                 and not re.search(r'[\s<>\x00-\x1f]', html.unescape(url)))):
            raise ValueError('Only HTTPS URLs and chapter anchors are supported')
        return '<a href="' + url + '">' + label + '</a>'
    value = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', link, value)
    value = re.sub(r'`([^`]+)`', r'<code>\1</code>', value)
    return re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', value)


def markdown(value, chapter='chapter'):
    blocks = []
    lines = value.splitlines()
    index = heading = 0
    while index < len(lines):
        line = lines[index]
        index += 1
        if not line.strip():
            continue
        if line.startswith('# '):
            continue
        if line.startswith('## '):
            heading += 1
            blocks.append('<h3 id="' + chapter + '-' + str(heading) + '">' + inline(line[3:]) + '</h3>')
        elif line.startswith('|'):
            rows = [line]
            while index < len(lines) and lines[index].startswith('|'):
                rows.append(lines[index]); index += 1
            cells = lambda row: [cell.strip() for cell in row.strip().strip('|').split('|')]
            if len(rows) < 2 or not all(re.fullmatch(r':?-{3,}:?', cell) for cell in cells(rows[1])):
                raise ValueError('Table requires a separator row')
            width = len(cells(rows[0]))
            if any(len(cells(row)) != width for row in rows):
                raise ValueError('Inconsistent table columns')
            table = '<div class="wiki-table" tabindex="0"><table><thead><tr>'
            table += ''.join('<th scope="col">' + inline(cell) + '</th>' for cell in cells(rows[0]))
            table += '</tr></thead><tbody>'
            for row in rows[2:]:
                table += '<tr>' + ''.join('<td>' + inline(cell) + '</td>' for cell in cells(row)) + '</tr>'
            blocks.append(table + '</tbody></table></div>')
        elif re.match(r'(?:- |\d+\. )', line):
            ordered = not line.startswith('- ')
            pattern = r'\d+\. (.*)' if ordered else r'- (.*)'
            items = [re.fullmatch(pattern, line).group(1)]
            while index < len(lines) and re.fullmatch(pattern, lines[index]):
                items.append(re.fullmatch(pattern, lines[index]).group(1)); index += 1
            tag = 'ol' if ordered else 'ul'
            blocks.append('<' + tag + '>' + ''.join('<li>' + inline(item) + '</li>' for item in items) + '</' + tag + '>')
        elif line.startswith('> '):
            blocks.append('<blockquote>' + inline(line[2:]) + '</blockquote>')
        else:
            blocks.append('<p>' + inline(line) + '</p>')
    return '\n'.join(blocks)


def render(lang):
    catalog = json.loads((ROOT / 'catalog.json').read_text(encoding='utf-8'))
    validate_catalog(catalog)
    prefix = '/en' if lang == 'en' else ''
    title = 'Player Wiki' if lang == 'en' else '玩家 Wiki'
    toc = ''.join('<a href="#' + row['id'] + '" data-chapter-link="' + row['id'] + '"><span class="wiki-index">' + str(i+1).zfill(2) + '</span>' + html.escape(row[lang]) + '</a>' for i, row in enumerate(catalog))
    articles = []
    for i, row in enumerate(catalog):
        text = (ROOT / 'pages' / lang / (row['id'] + '.md')).read_text(encoding='utf-8')
        title_html = html.escape(row[lang])
        body = markdown(text, row['id'])
        if row['id'] == 'start':
            shortcuts = [('installation', '01', 'Install and launch' if lang=='en' else '安装与启动', 'Prism / MultiMC'),
                         ('modes', '02', 'Find your mode' if lang=='en' else '选择你的玩法', 'Solo · Duel · Multiplayer' if lang=='en' else '单人 · 双人 · 多人'),
                         ('ranked', '03', 'Play a ranked match' if lang=='en' else '开始一场排位', 'Board · Seeds · Points' if lang=='en' else '卡板 · 种子 · 积分'),
                         ('rng', '04', 'Understand fair randomness' if lang=='en' else '了解统一随机', 'RNG · Loot' if lang=='en' else 'RNG · 战利品')]
            body = '<div class="wiki-cards">' + ''.join('<a href="#' + slug + '"><small>' + number + '</small><strong>' + label + '</strong><span>' + detail + '</span></a>' for slug, number, label, detail in shortcuts) + '</div>' + body
        items = re.findall(r'<h3 id="([^"]+)">(.*?)</h3>', body)
        local_toc = ''.join('<a href="#' + key + '">' + label + '</a>' for key, label in items)
        adjacent = []
        for neighbor, label in [(i-1, 'Previous' if lang=='en' else '上一章'), (i+1, 'Next' if lang=='en' else '下一章')]:
            if 0 <= neighbor < len(catalog):
                other = catalog[neighbor]
                adjacent.append('<a href="#' + other['id'] + '"><small>' + label + '</small><span>' + html.escape(other[lang]) + '</span></a>')
        articles.append('<section class="wiki-chapter" id="' + row['id'] + '" aria-labelledby="' + row['id'] + '-title"><div class="wiki-reading"><div class="wiki-prose"><p class="wiki-eyebrow">BOARDRAID / ' + str(i+1).zfill(2) + '</p><h2 id="' + row['id'] + '-title">' + title_html + '</h2>\n' + body + '<nav class="wiki-adjacent" aria-label="' + ('Reading order' if lang=='en' else '阅读顺序') + '">' + ''.join(adjacent) + '</nav><a class="wiki-edit" href="https://github.com/BoardraidDev/wiki/blob/master/CONTRIBUTING.md">' + ('Improve this page ↗' if lang=='en' else '本页纠错与贡献 ↗') + '</a></div><aside class="wiki-outline"><p>' + ('On this page' if lang=='en' else '本页目录') + '</p><nav>' + local_toc + '</nav></aside></div></section>')
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
<script src="/assets/js/wiki.js?v=20261026a" defer></script>
</head><body data-page="wiki">
<header class="topbar"><div class="wrap topbar__inner"><a class="brand" href="{prefix+'/' if prefix else '/'}"><img class="brand__mark" src="/assets/brand/logo-mark.webp" width="22" height="22" alt=""><span class="brand__name">BOARDRAID</span></a><nav class="nav">{nav_html}<a href="{prefix}/wiki">Wiki</a></nav><a class="langtoggle" href="{alt}" lang="{alternate_lang}" hreflang="{alternate_lang}">{language}</a></div></header>
<a class="wiki-skip" href="#wiki-content">{'Skip to content' if lang=='en' else '跳至正文'}</a>
<main class="wrap br-wiki"><aside class="br-wiki-nav"><p class="wiki-eyebrow">THE PLAYER HANDBOOK</p><h1>{title}</h1><p class="wiki-scope">{'Latest production release' if lang=='en' else '适用于最新正式服'}</p><label class="wiki-search"><span>{'Search handbook' if lang=='en' else '搜索手册'}</span><input id="wiki-search" type="search" placeholder="{'Mode, seed, loot…' if lang=='en' else '玩法、种子、战利品…'}" autocomplete="off"></label><p class="wiki-results" role="status" aria-live="polite"></p><nav class="wiki-chapters" aria-label="{'Chapters' if lang=='en' else '章节'}">{toc}</nav><div class="wiki-community"><a href="https://github.com/BoardraidDev/wiki">{'Contribute ↗' if lang=='en' else '编辑与贡献 ↗'}</a><a href="https://github.com/BoardraidDev/api-docs">API Docs ↗</a></div></aside><article id="wiki-content" class="br-wiki-content" tabindex="-1"><p class="br-wiki-note">{'Rules follow the latest production server. Room settings and official announcements take precedence; test features may differ.' if lang=='en' else '规则以最新正式服为准。请同时查看局内房规与官方公告；体验服功能可能有所不同。'}</p>{''.join(articles)}</article></main>
<footer class="wrap"><p>BoardRaid · <a href="https://github.com/BoardraidDev/wiki">Wiki</a> · <a href="https://github.com/BoardraidDev/releases">Releases</a></p></footer>
</body></html>
'''


def self_test():
    validate_catalog([{'id': 'getting-started', 'zh': 'Start', 'en': 'Start'}])
    for slug in ['../private', '\"><script>', 'UPPER CASE']:
        try:
            validate_catalog([{'id': slug, 'zh': 'Title', 'en': 'Title'}])
        except ValueError:
            pass
        else:
            raise AssertionError('unsafe chapter identifier accepted')
    assert '<script>' not in inline('<script>alert(1)</script>')
    try:
        inline('[unsafe](javascript:alert)')
    except ValueError:
        pass
    else:
        raise AssertionError('unsafe URL accepted')
    assert '<a href="https://example.org">safe</a>' == inline('[safe](https://example.org)')
    assert '<h3 id="chapter-1">Heading</h3>' in markdown('## Heading\nText')
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
