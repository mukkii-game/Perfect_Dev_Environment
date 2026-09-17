# 環境の落とし穴(1 層「必読」候補)

> 知らないと必ず踏むものだけ。15 行に収める。増えたらスキル(2 層)へ落とす。

| 日付 | 現象 | 対処 |
|---|---|---|
| 2026-09-17 | AI_OPS_TOKEN で workflow_dispatch が 403 | トークンに Actions 書き込みが無い(意図的)。権限を足さず、**普通の commit で push イベントを起こして**代用する |
| 2026-09-17 | 旧 bootstrap で作った repo は main に push も PR マージもできない | 旧ルールセット `protect-main` が、もう存在しないチェックを必須にしている。ai-ops の **Remove Legacy Ruleset** を repo 名指定で実行して外す |
| 2026-09-16 | 覚えのない組織の repo が Claude の一覧に出る | その repo が public なだけ。GitHub App の「公開リポジトリは読み取り専用で含む」条項。書き換えは不可なので実害なし |
| 2026-09-16 | 新しいクラウドセッションで GitHub 連携を求められる | 同じ仕組みの初回許可。連携画面では **All repositories** を選ぶ(個別だと新作 repo を毎回許可し直すことになる) |
| 2026-09-14 | 子セッション(実行部隊)が許可待ちで無言のまま止まる | 発注時に「npx -y / 任意 URL の curl / ファイル削除を使うな」と明記。既存を消す・置き換える仕事は人間が見ているセッションでやる |
| 2026-09-14 | Playwright がブラウザ版不一致で起動しない | `PW_CHROMIUM=/opt/pw-browsers/chromium` のように既存の Chromium を指定する(雛形の tools は対応済み) |
| 2026-09-15 | 会議室の実行環境から一部の外部サイトが読めない(egress 制限) | `research/_to_fetch.txt` に積み、GitHub Actions 側の収集で取得する |
| 2026-09-13 | GitHub Free では private repo に Pages とルールセットが効かない | private にしたい作品は Cloudflare Pages で公開する |
