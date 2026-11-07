# Custom room settings

## Creating, joining and player counts
Choose solo, two-player or multiplayer before creating a room. Friends join with its code. Solo is local practice; two-player rooms are private duels. Multiplayer capacity is configurable from 3 to 32. Room-family controls lock after creation.
## Editing, applying, cancelling and conflicts
Before creation, settings describe your local preference. In an existing room, only the host in the waiting lobby can edit rules; members inspect them read-only. Apply changes and wait for confirmation. Cancel or Esc discards the draft. Reopen current settings when a stale-rule conflict is reported.
## Room management
Room management provides room-name and related management controls. The name identifies the room but does not replace its join code. Editing depends on ownership and room state.
## Hide the room code locally
Hide the join code on your own screen for streaming or screenshots. This does not change the actual code, access permissions or other players' displays.
## Allow spectating
This is currently an unsupported read-only setting. It does not promise spectator admission. Inspecting the world after a match is a separate feature.
## Multiplayer rules: deathmatch
Players compete individually on a shared task board. Deathmatch skips two-sided drafting because that allocation method does not fit this room type. Use automatic allocation or a host-authored custom board.
## Multiplayer rules: teams and cooperation
Team battle divides players into A and B, with task progress shared within each team. The first team to satisfy the win rule wins. Each team allows up to 16 players, with at most 32 combined; assign seats in the lobby UI. A zero-player side represents cooperation: everyone works together instead of competing against an empty team.
## Deathmatch finish target
Wait for X finishers controls when the whole deathmatch ends. X=1 ends it at the first completion; larger values allow later finishes. Valid values depend on room capacity. This does not change the task condition each player must complete.
## Activity: standard, exclusive drafting and races
Solo and private duels can select standard play, portal race or treasure hunt. A 5×5 duel also offers exclusive drafting: a cell cannot belong to both sides, the first to 13 wins, and meta goals are absent. It is not available in solo, multiplayer or other board sizes. Invalid combinations are normalized. Races hide the following Bingo-specific settings and use their own rules.
## Board size
Available sizes are 3×3, 4×4, 5×5, 6×6 and 7×7: 9, 16, 25, 36 and 49 cells. Size affects task count, full-board targets and legal win conditions. Shrinking a custom board can truncate cells, so review it or save a preset first.
## Board difficulty
Ranked difficulty uses the main task mix; casual difficulty reduces overall difficulty for practice. Difficulty determines the automatic task pool, while allocation determines who chooses the board. Difficulty is hidden for a manually authored board because automatic selection does not replace its cells.
## Board allocation: random, draft and custom
Random allocation assigns tasks using the seed and difficulty without drafting. Draft allocation lets participating sides select goals; solo can practice selection, but deathmatch does not offer it. Custom allocation uses host-authored cells without the automatic board or the same draft flow.
## Custom board contents
This appears only with Custom allocation. Open the editor to select or clear each goal and check the filled count. Empty cells stay empty rather than receiving random tasks. Recheck after resizing, especially whether the win target is attainable. Members cannot overwrite the host's board.
## Win condition
The Ranked win condition means first to 15 tasks; it does not make a private room award ranked points. It is unavailable on a 3×3 board with only 9 cells. BINGO Line requires a line; Challenge requires the full board. Exclusive duel drafting uses its own 13-cell target.
## Seed source
Ranked source draws from the ranked seed library. Random source generates a non-fused random seed. Custom source exposes separate Overworld, Nether and End inputs. Ranked here describes the seed source, not ranked matchmaking.
## Custom seed inputs
The three fields appear only for Custom source. Enter signed decimal 64-bit integers, not text seed names or out-of-range values. Blank and 0 mean unspecified rather than a fixed zero seed; leaving all three blank falls back to random. Invalid input blocks the settings transaction instead of silently randomizing it.
## Opening seed type
This applies only to Ranked-library source. Choose an unrestricted library entry or a desert, island, taiga, jungle or snowy opening from the expanded list. Unrestricted library selection differs from a random world. An unavailable requested type does not silently become another type. With non-library sources, this setting is read-only and inactive.
## Artificial lava pools
This local creation preference enables additional artificial lava pools; island openings always skip them. It is not a synchronized rule sent to every member and is absent from the existing-room rule editor. Races hide it. Turning it off does not remove naturally generated lava.
## Rule presets: built-ins, saving, import and export
Start from built-ins for standard/casual duels, lines, small challenges, deathmatch or teams/cooperation, or inspect the last custom match. Preview, fill the draft, then Apply: importing alone does not update the room. Confirm replacements of authored boards. Presets respect room-family compatibility and do not silently change player counts or teams. Save locally, copy JSON for export or paste for import. Fixed seeds are excluded by default unless explicitly included in the UI. Restore defaults resets the rule draft for the current room family and still requires Apply. Overwriting a named preset asks for confirmation. Store at most 20 local presets with names of 1–32 characters.
## Suggested combinations and release scope
For practice, try solo, a small board and casual difficulty. For a friendly duel, try 5×5, draft allocation and the ordinary 15-task target. For deathmatch, use random/custom allocation and agree on the finish target. Multiplayer and preset details describe the current development branch; actual released UI availability takes precedence over this handbook.
