# 08 AI 以外の自動化

## 現状の結論

- GAS、Chrome 拡張、サーバー常駐 Python、PC バッチなど、都合の良いものはどんどん入れる。
- 選ぶ理由: コスト(AI を使わずに済む)、サーバー駆動(PC 不要)、権利範囲(GitHub を触るなら Actions が自然)。
- 作品開発中にできた道具が汎用なら、汎用ツールとして環境に残す。

## 棚卸しで見つかった汎用ツール候補(2026-09-13)

| 候補 | 元 | 備考 |
|---|---|---|
| 企画 CSV ⇄ スプシ同期(csv → data.gs → clasp push、目次生成) | charge-and-anchor-gdd、slayers-ip-reference で独立に 2 回書かれた | gas-plannning-sheet と統合して 1 本に。`E:\` 固定パスを相対化 |
| 単一 HTML ビルド(画像 base64、日本語フォントサブセット、ルビ) | youjo build.py | 絵本 / ノベル系の公開形式。my-butsukari-ojisan とビューア統一 |
| スクショ / 自動プレイ / soak | panzer-tokoron(puppeteer)、cedec-fable(playwright)、marshmallow shot-server | playwright に寄せて雛形 tools/ に 1 本 |
| PDF OCR → CSV | slayers-ip-reference ocr_pdf.py | 資料取り込み |
| 定期収集 Actions(cron) | ENG_App、gd-knowledge collect.yml | 再利用ワークフロー 1 本に |
| LPC スプライト合成 | the-short-walk build_sprites.py | 06 の索引へ |
| SNS 投稿 bot(puppeteer) | fb-radio-auto | **cookies.json がコミット済み。先に処理** |

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
