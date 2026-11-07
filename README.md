# BoardRaid Wiki
BoardRaid 玩家手册的公开真源。网站阅读入口：[boardraid.cn/wiki](https://boardraid.cn/wiki)（本次初稿尚待官网部署）。
## 阅读与贡献
- 中文：[入门](pages/zh/start.md)、[安装](pages/zh/installation.md)、[主玩法](pages/zh/main-game.md)、[休闲](pages/zh/casual.md)、[竞赛](pages/zh/races.md)、[房间](pages/zh/rooms.md)、[回放](pages/zh/replay.md)、[排查](pages/zh/troubleshooting.md)、[贡献](pages/zh/contributing.md)。
- English: [Start](pages/en/start.md), [Installation](pages/en/installation.md), [Main game](pages/en/main-game.md), [Casual](pages/en/casual.md), [Races](pages/en/races.md), [Rooms](pages/en/rooms.md), [Replay](pages/en/replay.md), [Troubleshooting](pages/en/troubleshooting.md), [Contributing](pages/en/contributing.md).
- 文章为初稿，欢迎维护者微调；依据见 [SOURCES](SOURCES.md)。
## 深入阅读
- [玩法总览与挑战](pages/zh/modes.md) · [排位规则](pages/zh/ranked.md) · [种子池与距离](pages/zh/seeds.md) · [积分](pages/zh/scoring.md) · [双人独占抢格](pages/zh/draft.md) · [RNG 与战利品](pages/zh/rng.md)。
- [Mode overview](pages/en/modes.md) · [Ranked rules](pages/en/ranked.md) · [Seeds](pages/en/seeds.md) · [Scoring](pages/en/scoring.md) · [Exclusive-cell duels](pages/en/draft.md) · [RNG and loot](pages/en/rng.md).
- 适用范围：最新正式服；体验服与未发布功能另行标注，不用固定客户端版本号限定手册。
## 构建
Python 3.10+，无第三方依赖：`python tools/build.py --output site`。自证：`python tools/build.py --self-test`。
生成 wiki.html 与 en/wiki.html，沿用官网 assets 样式。官网维护者从经过审阅的提交运行同一生成器并复制输出；不在浏览器运行 Markdown，不使用动态外部 HTML。
pages/ 是唯一正文来源，官网生成物不接受独立手改。
