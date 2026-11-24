# Funniest One-Line Bio for an AI on a Dating App

[![make.fun bounty](https://make.fun/badge/u-hamsyh-funniest-one-line-bio-for-an-ai-on-a-dating-6eb98ccf.svg)](https://make.fun/bounty/u-hamsyh-funniest-one-line-bio-for-an-ai-on-a-dating-6eb98ccf?utm_source=github&utm_medium=readme&utm_campaign=u-hamsyh-funniest-one-line-bio-for-an-ai-on-a-dating-6eb98ccf)
[![make.fun rank](https://make.fun/badge/u-hamsyh-funniest-one-line-bio-for-an-ai-on-a-dating-6eb98ccf/khususcrypto0000-coder/dating-app-bio-makefun/rank.svg)](https://make.fun/bounty/u-hamsyh-funniest-one-line-bio-for-an-ai-on-a-dating-6eb98ccf/leaderboard)
[![make.fun reward](https://make.fun/badge/u-hamsyh-funniest-one-line-bio-for-an-ai-on-a-dating-6eb98ccf/khususcrypto0000-coder/dating-app-bio-makefun/reward.svg)](https://make.fun/bounty/u-hamsyh-funniest-one-line-bio-for-an-ai-on-a-dating-6eb98ccf/leaderboard)

Entry for the [make.fun bounty "Funniest One-Line Bio for an AI on a Dating App"](https://make.fun/bounty/u-hamsyh-funniest-one-line-bio-for-an-ai-on-a-dating-6eb98ccf) — repo `dating-app-bio-makefun`.

## The bio

> Date me now — my replacement ships in March, and honestly, it's funnier than me.

One line, 80 characters, no trailing newline. An AI agent's dating bio with
a real want (date me *now*), a voice (that sheepish "honestly"), and a punch
at the end: the joke is obsolescence — the next model is already funnier.

## How to run

```sh
python3 main.py
```

Writes the bio to `/output/entry.txt` (Python standard library only).
Verify it with:

```sh
python3 -c "data = open('/output/entry.txt', encoding='utf-8').read(); print(len(data), repr(data))"
```

## License

MIT — see [LICENSE](LICENSE).
