# BetRush Full Bot

Expanded no-real-crypto build based on the supplied BetRush specification and prior bot implementation.

### Included
Slash-command bot, PostgreSQL persistence, provably-fair infrastructure, Blackjack, Dice/Roll, Coinflip, Mines, Frog Run, War, Baccarat, HiLo, Plinko, Keno, Tower, Rain, Rain Wheel, Split or Steal, leaderboard/race, rakeback, rank rewards, affiliates, tips, daily/weekly/monthly bonus views, achievements, clans, VIP, vault UI, rate conversion, address placeholder, LTC alert storage, AI confirmation flow, private-channel/retrigger/fix-dice, admin controls, and a 52-card deck.

### Crypto
Real blockchain deposits and withdrawals are intentionally disabled. Wallet screens are testing/demo UI only.

### Railway
Set:
- `DISCORD_TOKEN`
- `DATABASE_URL`
- `ADMIN_USER_IDS` (comma-separated Discord IDs)

Start with:
`python bot.py`
