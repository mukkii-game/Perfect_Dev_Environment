# 決定: 2D 既定は Phaser 4、拾う提案 5 つを採用、片付け 8 repo、cookie 処理

日付: 2026-09-13(ユーザー承認「ぜんぶあなたのいうとおりでいい」)

## 2D エンジンの既定(engine-defaults の改訂)
- **2D は Phaser 4 を既定**にする。見た目の映えと融通(パーティクル、トゥイーン、タイルマップ、物理、カメラ)を優先。公式 skills 28 本で API の誤りを抑える。
- テキスト中心の ADV、超小型(数百行)の作品は素 canvas / DOM でよい。SPEC.md で指定。
- core 層(save、i18n、公開メタ、自動プレイ用デモモード)はどちらでも共通。
- 3D は変更なし(Babylon.js / Three.js)。

## 採用した提案(research/2026-09-13-borrowable-assets.md)
1. AGENTS.md 正本 + `npx skills add` で Phaser 公式 skills と gamedev-skills を Claude / Codex / Gemini に配布。
2. 雛形は Phaser 公式 template-vite-ts + Vite 公式 Pages ワークフロー + itch.io butler Action。Babylon / Three 版も同じ deploy.yml。
3. ビルドごとの実プレイ確認とスクショ。**AI が操作するのではなく、決定的なスクリプト(Playwright)が CI で走る。トークンは消費しない。** 失敗した時だけ結果とスクショが AI に渡る。
4. 素材は CC0 優先(海外 CC0 → 日本発は索引の規約範囲 → 契約済み有料)。CREDITS.md 必須。
5. Sheets 台帳の自動記帳。Phaser Game Agent MCP は保留。

## 片付け(任意、優先度低)

実害はない。理由は一覧の見やすさと、空 repo を AI が誤って使うのを防ぐことだけ。作品 repo の機械判定は接頭辞(game- / app-)で行う設計なので、やらなくても困らない。

- アーカイブ: Orejanakya, tetrishooter, My-project, PanzerTokoron(空 / README のみ)。**doroneko と GGJ2025 は除外**: 2025-03-03 の GGJ 作品で、本体が push されていない(ローカルにある可能性)。見つけたら push する。tetrishooter は一度除外したが、Gemini が更新中なのは **tetrishoot**(別 repo、作品として存続)と判明し候補に戻した(2026-09-13)、web-app-bootstrap-smoke, web-app-bootstrap-actions-smoke-20260829(残骸)。
- 会議室のセッションからは GitHub のアーカイブ操作が API で行えないため、**ユーザーが各 repo の Settings → Archive this repository で実施**(削除ではなく読み取り専用化、戻せる)。

## fb-radio-auto の cookie
- 2026-09-13 に会議室が `cookies.json` を repo から削除し `.gitignore` に追加して push 済み。アプリ本体は Render の Secret Files から読む設計なので動作に影響なし。
- 2026-09-13 ユーザーが Facebook の全デバイスログアウトを実施済み。履歴の cookie は無効化された。
- 追加決定: fb-radio-auto は作りかけ(投稿未実装)のため **repo と Render サービスを削除**する(ユーザー実施)。
