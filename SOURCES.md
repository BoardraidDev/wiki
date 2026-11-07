# 资料与适用边界
查阅日期：2026-11-07。正文为原创，不复制第三方指南或截图。
- [Prism 导入说明](https://prismlauncher.org/wiki/help-pages/Zip-import/)：zip/mrpack 从导入入口安装。
- [Minecraft Wiki](https://minecraft.wiki/)：主题索引与章节阅读参考；自动读取受 robots 限制，未据此核对正文。
用户提供的安装 PDF 仅作阅读参考，不在公开仓库重新分发，也不复制其中联系方式。
BoardRaid 的版本、环境和行为由本项目资料核对，不能套用其他游戏版本的参数。真实截图与安装体验仍需人工验收。

- [MultiMC 官方导入实例说明](https://github.com/MultiMC/Launcher/wiki/Import-Instance)：查阅 2026-11-07，确认本地 Zip 路径、浏览和拖放导入方式。
房间与休闲章节对照本项目当前设置编辑器、房规校验、预设模板及模式规则文案；开发分支功能不据此视为全部正式发布。

## 规则核对
核对日期：2026-11-07。排位、种子、积分与随机机制对照正式版本线提交 `886b0506306674a3e4c660aa3b7baa055b273010` 的实现；提交是编辑取证锚点，手册适用范围仍是最新正式服。
- 开局权重：SeedCategories 与 SeedLibrary；不以库存频率冒充抽取概率。
- 结构入库规格：SeedFinder、SeedBatchFinder 与维度融合筛选器；主世界类型分开列出，区别现行规格与历史库存复验。
- 卡板配比：BoardDifficulty；独占归属与元任务限制：CellTrustLadder、MetaPlacementRules 和房规校验。
- 积分：RankedService 的有效执行路径；不采用旧注释中的零分下限或未启用反刷分开关。
- 重置与共同换种：MatchManager、Room 与 VoteGate；个人重建和共同投票不混淆。
- RNG：SharedRngScope、SharedRngGroups、SharedLootRng、RngParams、PityPolicy；箱子调整：MixinLootableContainerBlockEntity。
结构距离是水平筛选距离，不是路线长度；并未在本次文档工作中重新生成并验收全部线上库存。性能、概率标定与实际两端游玩验收是不同证据，不相互替代。
