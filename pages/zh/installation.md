# Prism 安装

## 导入官方整合包
1. 从[Prism 官网](https://prismlauncher.org/download/)下载适合系统的启动器，并完成正版账号登录。
2. 下载 BoardRaid.zip，保持压缩包原样，不先解压，也不要把 zip 改名为 jar。
3. Prism 中点「添加实例 / Add Instance」→「导入 / Import」→ 浏览本地文件，选择 BoardRaid.zip，确认导入。
4. 等待组件安装完成，编辑实例检查版本为 Minecraft 1.16.1、加载器为 Fabric，然后启动。
## 单独安装模组
在 1.16.1 Fabric 实例的 mods 文件夹放入官网正式版 jar。BoardRaid 本体最低 Fabric Loader 0.15.0；官方整合包中 Glacier 要求 0.18.4 或更新，应采用整合包的更严格下限。还需匹配 1.16.1 的 Speedrun API 或 Fabric API。
不要在同一实例保留多个 BoardRaid 版本，也不要混入其他 Minecraft 版本的模组。Prism 支持从 zip 导入实例，但 jar 必须放到 mods，不能当成整合包导入。
## Java 和内存
优先保留整合包配套环境。启动失败时在「编辑实例 → 设置 → Java」核对实际使用的 Java 与报错。原版 1.16.1 以 Java 8 为基线，不能从其他模组教程直接照搬 Java 25 和 JVM 参数。
最大内存可先设为 2048 MiB，按设备余量调整；这是起点，不是每台设备的性能保证。不要把全部物理内存分给游戏。
## 升级保留设置
退出游戏并备份旧实例。优先使用官方更新提示；重新导入时可谨慎迁移 options.txt 与所需 config 配置，保留旧实例以便恢复。不要复制账号令牌、缓存或整套旧 mods 覆盖新包。
