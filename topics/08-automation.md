# 08 AI 以外の自動化

## 現状の結論

- GAS、Chrome 拡張、サーバー常駐 Python、PC バッチなど、都合の良いものはどんどん入れる。
- 選ぶ理由: コスト(AI を使わずに済む)、サーバー駆動(PC 不要)、権利範囲(GitHub を触るなら Actions が自然)。
- 作品開発中にできた道具が汎用なら、汎用ツールとして環境に残す。

## 検討中の論点

1. 候補の洗い出し(公開パッケージ生成、スクショ自動撮影、翻訳、索引更新、Drive 同期、X 投稿文生成)
2. 実行場所の使い分け: GitHub Actions / GAS(Google 系と相性) / 自宅 PC(GPU が要る時だけ)
3. `dev-tools` repo の構成と、作品 repo からの呼び方(再利用ワークフロー)

## 調べたこと

- 2026-09-13: 既存の自動化資産。ai-dev-infra(再利用ワークフロー 4 本)、ai-ops(repo 作成スクリプト)、gd-knowledge/scripts(収集 Python 57 本)、gas-plannning-sheet(企画スプシ GAS)。詳細は research/2026-09-13-existing-infra-inventory.md。
- ai-dev-infra は 2026-09-04 に「1 人 + AI では安全弁が手間」として既に軽量化済み。さらに削る余地: verify-web の playwright e2e をパイロットでは任意にする等(05 と合わせて検討)。

- (未着手)

## 次にやること

- [ ] 候補一覧を作る
