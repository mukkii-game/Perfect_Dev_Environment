# 02 全 AI 共通の作法(agent.md 系)

## 現状の結論(推奨案、未確定)

**正本は 1 つ、入口は AI ごと。**

```
AI_RULES.md      ← 正本。全 AI が読む共通の作法
CLAUDE.md        ← 「AI_RULES.md を読め」+ Claude 固有の 2〜3 行
AGENTS.md        ← 同上(Codex / Cursor / 汎用)
GEMINI.md        ← 同上(Gemini CLI)
```

AI_RULES.md に入れる内容(章立て案):

1. **このプロジェクトは何か**: SPEC.md を読め。ジャンル別の追加指示は `rules/<genre>.md` を読め(例: `rules/puzzle.md`, `rules/3d.md`)
2. **作業の型**: まず動くモックを最短で。複数案を求められたら `variants/a`, `variants/b` に並べる。完成より公開優先
3. **技術の既定値**: 2D は Phaser 3、3D は Three.js、エンジンは `dev-engine` を使う。ビルドは Vite。TypeScript 可だが型で止まるな
4. **素材**: 自作より外部素材優先。クレジット不要のものを優先し、`ASSETS.md` に出典とライセンスを必ず書く。自動生成した場合はどの AI で作ったかも書く
5. **公開**: `docs/PUBLISH.md` を日英で埋めてから公開ジョブを叩く
6. **道具**: 検索・一括処理は `dev-tools` のスクリプトを使え(例: `tools/search.py`)。自前で同じものを作るな
7. **記録**: 汎用的に使える道具ができたら `dev-tools` に出す PR を提案する。環境の説明(STATUS 等)に影響する変更をしたら書き換える
8. **禁止**: テストのスキップ、ライセンス不明素材の使用、秘密情報のコミット

**書き方の原則**(モデル進化への対応): 細かく書きすぎない。「何を」「なぜ」を書き、「どうやって」は AI に任せる。モデルごとの癖は `knowledge/ai-models.md`(→ 07)に日付つきで置き、AI_RULES.md には入れない。

## 検討中の論点

1. `.skill` / スキルの単位をどう切るか。候補: 「新作を生やす」「公開する」「素材を探す」「複数案を出す」「英語化する」。Claude は skills、Codex は AGENTS.md 内の手順、Gemini は GEMINI.md で同じ内容を読ませる。**同じ手順書を 3 形式に変換するスクリプト**を `dev-tools` に置く案。
2. Claude と Codex を GitHub Actions 経由で同じ手順にする件。ユーザーが別セッションで相談済み。その結論を `research/` に取り込んでからここを詰める。
3. 人間の介入点をどこに置くか。案: SPEC 承認 → 公開承認 の 2 点のみ。それ以外は自律。
4. ルールの検証方法。雛形で実際に 1 本作らせ、どの AI でも同じ動きになるか試す。

## 調べたこと

- 各 AI の設定ファイル名: Claude Code = `CLAUDE.md` + `.claude/skills/`、Codex = `AGENTS.md`、Gemini CLI = `GEMINI.md`、Cursor = `.cursor/rules/`。共通で読めるのは AGENTS.md 系が最も広い(要再確認)

## 次にやること

- [ ] ユーザーの別セッション(Claude と Codex の統一相談)の結論を受け取り research/ に保存
- [ ] AI_RULES.md の初稿を書き、雛形 repo に入れる
