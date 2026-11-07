# Prism and MultiMC installation

## Import the official pack
1. Install [Prism Launcher](https://prismlauncher.org/download/) for your system and sign into a licensed account.
2. Download BoardRaid.zip. Do not unpack it or rename it to jar.
3. Select Add Instance → Import → Browse, choose BoardRaid.zip and confirm.
4. Wait for installation, then verify Minecraft 1.16.1 and Fabric before launching.
## Installing only the mod
Put the official jar in the mods folder of a 1.16.1 Fabric instance. BoardRaid requires Fabric Loader 0.15.0 or later; the pack includes Glacier, which needs 0.18.4 or later. Use the stricter pack requirement. Install a compatible Speedrun API or Fabric API.
Keep only one BoardRaid version. A jar is a mod file, not an importable instance archive.
## Java and memory
Prefer the environment supplied with the pack. Check the actual Java installation and error message under Edit instance → Settings → Java. Vanilla 1.16.1 uses Java 8 as its baseline; do not copy Java 25 or JVM arguments from unrelated tutorials.
2048 MiB is a starting memory budget, not a performance guarantee. Leave memory for the operating system.
## Updating
Close Minecraft and back up the instance. Prefer the official update prompt. When reimporting, migrate options.txt and necessary configuration carefully; keep the old instance for recovery. Do not copy account tokens or overwrite a new pack with old mods.

## MultiMC: import the official pack
1. Download from the [MultiMC website](https://multimc.org/#Download). Extract the launcher archive on Windows and run MultiMC.exe. Extracting the launcher is separate from keeping the modpack zipped.
2. Add a Microsoft account that owns Minecraft Java Edition and complete browser login. Never share authentication tokens.
3. Download BoardRaid.zip and leave the pack intact; do not unpack it or rename it to jar.
4. Select Add Instance → Import from zip → Browse, choose BoardRaid.zip and confirm. A compatible exported instance can also be dragged onto the main window.
5. Wait for installation. Under Edit Instance → Version, verify Minecraft 1.16.1 and Fabric, then launch with the correct account.
## MultiMC: Java, memory and manual installation
Check the instance-specific Java path and memory under Edit Instance → Settings → Java. Verify the detected Java choice rather than copying settings from other Minecraft versions. Start around 2048 MiB and leave memory for the system.
For a jar-only installation, create a 1.16.1 instance, install a suitable Fabric Loader from its version page, and place one BoardRaid jar plus a compatible API in that instance's mods folder. A jar is not an importable pack.
## MultiMC: common import problems
An unrecognized-pack error may mean you selected the launcher archive, a plain mods-only zip or a jar. Reselect the official BoardRaid.zip rather than renaming or repacking it. Preserve dependency-download errors and check connectivity and versions before creating more mixed instances.
Exit and back up before updating. Migrate options.txt and necessary configuration carefully instead of overwriting a new pack with old mods. See the [official import guide](https://github.com/MultiMC/Launcher/wiki/Import-Instance).
