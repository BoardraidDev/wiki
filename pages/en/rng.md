# Shared RNG and loot adjustments

RNG means random outcomes. BoardRaid gives supported match events reproducible random substreams and reduces extreme failure streaks for selected drops. It does not disable every vanilla random event or promise identical inventory at the same wall-clock second.

## Event order, not wall-clock time

Sequences depend on the world seed, event group, enchantment tier and position in that group’s stream. The Nth eligible attempt in the same context is reproducible. Resources and subevents use separate streams so unrelated actions do not consume a goal’s randomness. Spatial events may also include location anchors.

A group is not always one entity type: related resources from different sources can share a group. Different kill order, enchantments, tool conditions or consumed attempts can produce different immediate outcomes. One apparent mismatch alone does not prove synchronization failed.

## Main covered systems

| System | Treatment |
| --- | --- |
| Target drops | Flint, blaze rods, pearls and wither skulls use target and enchantment contexts |
| Basic resource groups | Leather, bones and arrows use their resource models; probability and quantity are separate |
| Interactions | Supported taming, eyes of ender, composting, villager trade and equipment events use dedicated substreams |
| Piglin bartering | Keeps separate table and bonus streams; no other platform’s trade-count guarantee applies |
| Structure containers | Use each container’s loot seed, followed by the selected adjustments below |

## Soft and hard pity

Eligible targets track consecutive failures. A calibrated initial probability applies first, then increases after a soft threshold; reaching the hard cap guarantees the next eligible attempt. Success clears that target/tier failure counter. Parameters are calibrated against vanilla probabilities for the matching enchantment tier to reduce extremes while preserving the model’s long-run average. Initial probability is not the overall drop rate.

| Example: unenchanted tier | Vanilla non-empty probability baseline | Consecutive failure cap | Next guaranteed attempt |
| --- | --- | --- | --- |
| Gravel → flint | 10% | 19 | 20th eligible attempt |
| Blaze → rod | 50% | 3 | 4th eligible attempt |
| Enderman → pearl | 50% | 3 | 4th eligible attempt |

An eligible attempt must satisfy the event’s vanilla context. Silk Touch, shears, explosions and ineligible kills are not universally counted toward the same pity counter. Fortune and Looting have separate tiers; unenchanted counters do not describe every tool. Quantity randomness is separate from the drop decision.

## Container loot adjustments

| Loot source | Current adjustment |
| --- | --- |
| Shipwreck supply chest | Gunpowder total normalized to 5–11; if TNT is absent, 50% chance to add 1–2; existing TNT capped at 2 |
| Desert temple chest | Top up iron to a sampled 1–2 and gunpowder to a sampled 2–4 when below those targets |
| Jungle temple chest | At least 4 iron; top up rotten flesh to a sampled 2–4 |
| Village weaponsmith chest | At least 5 iron in taiga/snowy biome contexts; otherwise at least 7 |
| Village toolsmith / armorer chest | At least 7 iron |
| Bastion chest | Vanilla chest tables; no extra guaranteed obsidian injection |
| Iron golem iron | Adjusted to 4–5 in eligible match worlds |

Except for explicitly capped shipwreck items, top-ups are not extra grants of the same amount and do not trim larger vanilla totals. Only selected tables are adjusted, and additions require free slots. Containers do not all share one universal loot table. Normalization is once per chest, not a new reward on every opening.

## Saving, reconnecting, resetting and scope

Managed RNG state is persisted with the world; reconnecting normally is not a fresh reroll. A personal world reset recreates the same world and consumes sequences from the new world’s starting point, without changing the opponent or completed cells. Ordinary saves, modded entities and unsupported contexts do not inherit these guarantees.

> Shared events, container adjustments and golem floors have separate world eligibility checks. Main-game match worlds are the primary scope, with additional shared-event integration for Most%. Do not assume every race world or ordinary vanilla save enables the entire system.
