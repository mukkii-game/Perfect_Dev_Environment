# 12 世の中から拾う(環境自体を自作しない)

## 現状の結論

- 作品の素材・ライブラリと同じ原則を **環境そのものにも適用する**。skill.md、AGENTS.md の雛形、テンプレート repo、Actions、MCP サーバー、他の個人開発者のワークフローは、まず既存のものを探し、合うものを取り込み、足りない所だけ自作する。
- 2026-09-13: 調査を実行部隊に委託(7 分類: skills 集、AGENTS.md 実例、Vite+Phaser/Babylon/Three テンプレート、itch.io/Pages の Actions、CC0 素材と検索 API、個人開発者の AI 駆動ワークフロー、ゲーム開発向け MCP)。結果は research/ に保存する。

## 検討中の論点

1. 取り込む基準: ライセンス、更新の新しさ、依存の少なさ、AI が読んで使える形か。
2. 取り込み先: skills は雛形 repo の `.claude/skills/`、AGENTS.md は drafts/ で比較して吸収、Actions は雛形に直書き、素材検索 API は dev-tools。
3. **定期的に探し直す**。07 の定期更新 Routine に「新しい skill・テンプレート・ツール」の項目を足す。月 1。

## 調べたこと

- 2026-09-13 調査完了 → research/2026-09-13-borrowable-assets.md(7 分類、約 60 件)。要点:
  - **skills は自作不要**。Phaser 公式 repo に SKILL.md が 28 本同梱、gamedev-skills に 73 本(Phaser 4 / three.js / Godot)。`npx skills add`(vercel-labs/skills)で Claude Code / Codex / Gemini CLI に同時配布できる。
  - AGENTS.md 正本 + CLAUDE.md は `@AGENTS.md` は世の中の標準手法と一致。agent-rules-sync で自動同期も可。
  - テンプレは Phaser 公式 `template-vite-ts`(**Phaser 4**)+ Vite 公式 Pages ワークフロー + `yeslayla/butler-publish-itchio-action` で「push だけで Pages と itch.io 同時公開」。Babylon は michealparks/babylon-template(Havok 物理付き)、Three は pachoclo/vite-threejs-ts-template(Pages 対応済み)。
  - 素材: Kenney(CC0、ミラー repo を clone してローカル検索)、Poly Haven API、Freesound API(CC0 フィルタ)、ambientCG API、Quaternius / KayKit。
  - MCP: Playwright MCP を毎ビルドの実プレイ確認とスクショに。Google Sheets 公式 MCP で台帳を自動記帳。Phaser Game Agent MCP は有料クレジット制、要検証。
  - 日本語の先行事例: Zenn の aya テンプレ(Phaser 4 + 素材生成込み)、machamu の Codex/Claude 比較、乙一の Minimal Rogue(MIT)。
  - 注意: 一部 URL(zenn / note / kenney / freesound)は実行環境の proxy で未取得。採用前に人間が 1 度開く。

## 次にやること

- [x] 調査結果を research/ に保存
- [x] 提案 5 つ採用(decisions/2026-09-13-adoptions.md)
- [x] Phaser 4 に既定変更
