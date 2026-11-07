# Seed pool and structure distances

Ranked seeds combine Overworld, Nether and End components. The dimensions may use different underlying seeds, so entering a single number in vanilla Minecraft does not necessarily reproduce the full world. The opening types below belong to the main-game pool, not the round routes of treasure races.

## Five opening categories

| Overworld opening | Target weight | Main features |
| --- | --- | --- |
| Desert | 30% | Village and desert temple |
| Island | 20% | Buried treasure, shipwreck and monument |
| Taiga | 20% | Taiga village and smithies |
| Jungle | 20% | Jungle temple and nearby outpost |
| Snowy | 10% | Snowy village and basement igloo |

The system selects a category before a dimension combination within it. A larger category inventory does not directly increase its opening probability. Empty categories are excluded and remaining weights normalized. Legacy libraries without recognized categories use a compatibility path. These weights describe normal five-category selection, not a fixed sequence every ten matches.

## Overworld: measured from spawn

| Opening | Nearby primary structures | Other screening conditions |
| --- | --- | --- |
| Desert | Village and desert temple each ≤6 chunks (96 blocks) | Outpost ≤32 chunks (512 blocks) |
| Island | Generated buried treasure ≤5 chunks (80 blocks); complete shipwreck ≤6 chunks (96 blocks) | Ocean monument ≤32 chunks (512 blocks); separate downstream ravine verification |
| Taiga | Taiga-style village ≤5 chunks (80 blocks) | Non-zombie; ≥2 loot-bearing smithies including ≥1 weaponsmith; generated outpost ≤32 chunks |
| Jungle | Jungle temple ≤5 chunks (80 blocks) | Jungle spawn biome; temple terrain height ≤72; generated outpost ≤32 chunks |
| Snowy | Snowy-style village ≤5 chunks (80 blocks) | Non-zombie; ≥1 loot-bearing smithy and ≥1 weaponsmith; basement igloo ≤32 chunks; no required outpost |

An island opening is not accepted merely for having a shipwreck: pool rechecks also require real treasure, a complete ship and a nearby monument. Snowy openings do not require an outpost. Screening uses structure locator positions and horizontal distances; one chunk is 16 blocks. These are not walking distances or distances to the nearest structure edge.

## Nether: near the planned entry point

| Target | Screening limit | Reference |
| --- | --- | --- |
| Bastion remnant | ≤6 chunks (96 blocks) | Planned Nether entry derived from spawn |
| Nether fortress | ≤10 chunks (160 blocks) | The same planned entry |
| Bastion to fortress | ≤16 chunks (256 blocks) | Between structure locator positions |

Additional checks cover openness, nearby footing and access. Target bastions in basalt deltas are excluded, and hoglin-stable bastions have template requirements. Building a portal far from spawn changes the actual entry position; these limits do not promise nearby structures at every possible portal.

## Outer End: near the first gateway exit

Within 32 chunks (512 blocks) of the projected outer-island exit of the first gateway, screening requires a generated End city with an assembly-confirmed ship. The reference is not the central obsidian platform or an arbitrary later gateway. More than one qualifying city may exist.

## Scope and exceptions

> These numbers describe current pool-screening criteria, not a fresh world-generation audit of every production inventory row. Historical inventory, manually supplied seeds, random worlds and empty-pool fallbacks are not certified by this table. Report anomalies with a match identifier for rechecking.

Selecting a category in custom play restricts selection to that available category. Choosing random or manual seeds instead disables this opening policy. Screening may be refined during maintenance; current official rules and announcements take precedence.
