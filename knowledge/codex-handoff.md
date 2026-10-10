# Claude の上限が来た時に Codex へ渡す(貼るだけ)

決まり: decisions/2026-10-06-claude-limit-handoff。Mukkii がやるのは **下の 1 通を Codex に貼るだけ**。
GPT 側に常駐の相棒は作らない(knowledge/multi-ai-relay.md: AI 同士の自動往復は 2026-10-07 に試して「1 本に集約」が結論。止まった AI は自動で起きず、往復の管理が重くなった)。
受け渡しの場所は GitHub の repo と HANDOFF.md だけ。Codex も AGENTS.md を読むので、会議室と雛形の作法はそのまま効く。

## Codex に貼る文(作品の続き)
```
mukkii-game/<作品 repo> の続きをお願いします。
1. まだなら Game Studio プラグインを入れてください(codex plugin add game-studio@openai-curated)。
2. git pull してから AGENTS.md と HANDOFF.md を読み、HANDOFF の「次の一手」から続けてください。
3. 作り方の決まりがプラグインと AGENTS.md で食い違ったら AGENTS.md を優先してください。
4. 区切りごとに HANDOFF.md の「現状」を直して push してください。Claude が戻ったらそこから引き継ぎます。
```

## Codex に貼る文(会議室の仕事)
```
mukkii-game/Perfect_Dev_Environment の作業を引き継いでください。README.md と progress/2026-10-08-session-handoff.md を読み、
「Mukkii の返事待ち」と「進行中の実験」から私が頼んだことだけ進めてください。定期実行(Routine)は Claude 側の仕組みなので触らないでください。
終わったら progress/ に日付つきで何をしたか 1 枚書いて push してください。
```

## Claude が戻った時
- 作品: その repo の HANDOFF.md を読めば続きができる(Codex が書いたもの)。
- 気づきは毎晩の回収が HANDOFF の「全体に共有したい気づき」から拾うので、Codex が書いたものも会議室に入る。
