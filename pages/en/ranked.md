# Ranked rules and match controls

Ranked matchmaking is the rated two-player main game. Players share a 5×5 board and dimension seeds while competing in separate worlds. The first player to complete 15 goals wins. Both may complete the same goal; this differs from exclusive-cell DRAFTOUT.

## Match flow

1. Sign in, pass client checks and join the ranked queue; wait for world loading after pairing.
2. Complete drafting, setup and the countdown; do not inspect hidden world information before the start.
3. Complete goals according to their cell descriptions. Confirmed board state is authoritative.
4. Reaching the goal, forfeiting or agreeing a draw leads to settlement, then the lobby or history.

## Task difficulty distribution

| Board preset | Easy | Medium | Hard | Total |
| --- | --- | --- | --- | --- |
| Ranked 5×5 | 6 (24%) | 11 (44%) | 8 (32%) | 25 |
| Casual 5×5 | 15 (60%) | 10 (40%) | 0 (0%) | 25 |

These are quotas for 25 task groups, not independent probabilities rolled for each cell. Other sizes scale and round the counts, so small boards cannot reproduce every percentage exactly. Manually authored boards bypass these quotas. Task difficulty is also separate from Minecraft world difficulty.

## Resetting your own world

A world reset is a personal decision, not a vote, and does not reset the opponent. It recreates your world with the same Overworld, Nether and End seeds. Inventory, world state and unfinished accumulated progress restart. Completed green cells and confirmed opponent progress remain, while the match clock continues.

It is neither a new seed nor a pause. The opponent may continue while your world reloads. Ordinary resets do not make the same opponent vanilla advancement notification appear again. Treasure races reset round advancement state separately; see [Race rules](#races).

## Agreeing a seed change

After a duel starts, one player requests a seed change from Esc and the opponent must agree within 30 seconds. Without agreement the request expires. An accepted vote enters synchronized replacement, reloads worlds and starts a fresh board and preparation flow. The old world and its task progress do not carry over.

New seeds follow the [seed-pool policy](#seeds). Requesting from the Nether or End does not alter Overworld category weights. Ordinary seed changes are unavailable during drafting, the pre-start countdown or after the match. Stronghold and route replacements are separate race-specific controls.

## Draws, forfeits and disconnections

A draw requires the opponent’s agreement. Forfeiting creates a win/loss result, with the rated winner still receiving public points. Reconnect with the same account after an unexpected disconnect; a disconnect is not a pause or proof of world recovery. Preserve sanitized logs for persistent failures. See [Scoring](#scoring).
