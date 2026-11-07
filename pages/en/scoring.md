# Ranked scoring

Public points drive profiles, ranks and leaderboards. Matchmaking also maintains a separate hidden skill estimate. They are not the same number, so public score differences do not directly determine an award. Casual and private rooms remain unrated even with ranked boards or seeds.

## Starting points and outcomes

| Situation | Public points |
| --- | --- |
| New account | Starts at 1000 |
| Rated win | Positive award, minimum +2 |
| Rated loss | No public-point deduction |
| Agreed draw | Neither player gains or loses |
| Win caused by opponent forfeit, departure or disconnect | Winner still receives a win settlement |
| Casual, custom or practice | No ranked points |

## How a win award is calculated

| Opponent hidden skill relative to yours | Base award | After dither, before clipping |
| --- | --- | --- |
| At least 120 lower | 12 | 11–13 |
| Between the two outer bands | 20 | 19–21 |
| At least 120 higher | 32 | 31–33 |

The base award receives a −1, 0 or +1 dither, is clipped by a soft ceiling related to smoothed hidden skill, then receives the minimum +2 floor. A result can therefore be below its base band. Normal win awards range from +2 to +33; the middle band is not a fixed +20 every win.

## Hidden skill versus public points

Hidden skill updates from outcomes and opponent strength and affects later pairing and public-award limits. No public deduction for a loss does not mean hidden skill is unchanged. Other players’ hidden values are not a public leaderboard field. Settlement and history are authoritative over outdated guides or client messages.

## Active rules and future policies

The current implementation disables the grouped scoring switches for repeat-opponent decay, daily caps and weekly repeat-opponent caps. A guide should not claim that meeting someone a certain number of times automatically awards zero. Collusion, cheating and queue abuse remain subject to official conduct rules; future policy changes require current announcements.
