# Prism 与 MultiMC 安装

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

## MultiMC：导入官方整合包
1. 从 [MultiMC 官网](https://multimc.org/#Download)下载启动器。Windows 压缩版先解压启动器本身，再运行 MultiMC.exe；这与下面不解压整合包是两件事。
2. 在账号管理中添加拥有 Minecraft Java 版的微软账号，完成浏览器登录。不要把账号令牌粘贴给其他人。
3. 从官网下载 BoardRaid.zip，保留整合包原样，不要先解压或改成 jar。
4. 点击左上角「添加实例 / Add Instance」，选择「导入 Zip 压缩包 / Import from zip」，点「浏览 / Browse」选中 BoardRaid.zip，再确认导入。也可把兼容的实例压缩包拖到 MultiMC 主窗口。
5. 等待实例与组件安装完成。在「编辑实例 → 版本」核对 Minecraft 1.16.1 和 Fabric，选择正确账号启动。
## MultiMC：Java、内存和手动安装
在「编辑实例 → 设置 → Java」检查实例专用 Java 路径与内存；使用自动检测后仍要核对实际选中的版本。不要照搬其他 Minecraft 版本的 Java 或启动参数。最大内存可先用 2048 MiB，并为系统保留余量。
只下载 jar 时，先创建 1.16.1 实例，在版本页安装符合要求的 Fabric，再把唯一一份 BoardRaid jar 与匹配的 API 放入该实例的 mods。jar 不是整合包，不能通过导入 Zip 直接安装。
## MultiMC：常见导入问题
「无法识别整合包」通常意味着选成了启动器压缩包、只含 mods 的普通 zip，或拿 jar 当实例包。重新选择官网 BoardRaid.zip；不要随意改后缀或解压后重新打包。启动器下载组件失败时保留具体错误，先检查网络与版本依赖，不反复创建混杂的实例。
更新前退出游戏并备份实例。迁移设置时谨慎复制 options.txt 与所需配置，不把旧 mods 整体覆盖新包；保留旧实例供恢复。官方操作参考：[导入实例](https://github.com/MultiMC/Launcher/wiki/Import-Instance)。
