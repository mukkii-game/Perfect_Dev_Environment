# 世の中から拾える資産の調査(実行部隊レポート、2026-09-13)

関連 topic: 12, 01, 02, 05, 06, 07

以下が調査レポートです（URL は取得可能なものは WebFetch で存在確認済み。取得できなかったもの（proxy でブロック）は「※未取得」と明記）。

---

# AI駆動ブラウザゲーム開発 環境構築のための再利用可能資産サーベイ（2026-09-13）

**3行まとめ**
1. Skills は「`npx skills add`（vercel-labs/skills）で SKILL.md を Claude Code / Codex / Gemini CLI に同時配布」が 2026 年の標準。Phaser 公式リポジトリ自体に 28 本の SKILL.md が同梱されており、gamedev-skills の 73 本（three.js / Phaser 4 対応）と組み合わせれば自作は不要。
2. 指示ファイルは **AGENTS.md を唯一の正本**にし、CLAUDE.md は `@AGENTS.md` 1 行、GEMINI.md も同様に参照（または agent-rules-sync で自動同期）。テンプレは公式 `phaserjs/template-vite-ts`（Phaser 4 / MIT）＋ `pawap90/phaser3-ts-vite-eslint` の Pages ワークフローを移植するのが最短。
3. 公開は「Vite 公式の `actions/deploy-pages` ワークフロー」＋「`yeslayla/butler-publish-itchio-action`」の 2 本で GitHub Pages と itch.io を同時自動化。素材は Kenney / Poly Haven（API あり）/ Freesound（API あり、CC0 フィルタ）で CC0 に絞る。

---

## 1. Claude Code Skills / プラグイン / マーケットプレイス

| 名前 | URL | 何か | ライセンス | 更新 | この開発者への効き方 |
|---|---|---|---|---|---|
| anthropics/skills（公式） | https://github.com/anthropics/skills | Anthropic 公式 Agent Skills リポ。spec/ template/ 同梱。`/plugin marketplace add anthropics/skills` | Apache-2.0（docx/pdf 等はソース公開のみ） | 2026（176k★） | SKILL.md の仕様と雛形の正典。自作スキルはここの template から |
| phaserjs/phaser `skills/` | https://github.com/phaserjs/phaser/tree/master/skills | Phaser 公式リポ同梱の SKILL.md 群（Scenes/Physics/Tilemaps/Tweens/V3→V4 移行など 28 本）。`npx skills add phaserjs/phaser` | MIT（Phaser 本体と同じ） | 2026 | Phaser の API 知識をエージェントに直接注入。幻覚 API 対策に最も効く |
| gamedev-skills/awesome-gamedev-agent-skills | https://github.com/gamedev-skills/awesome-gamedev-agent-skills | 73 スキル・10 エンジン（Phaser 4.2 / PixiJS / three.js r184 / Godot 等）。ルーターがエンジンと課題を自動判定して読込 | Apache-2.0 | 2026 | 1 コマンド導入で Phaser と three.js の両方をカバー。router でスキル名を覚える必要なし |
| Yakoub-ai/phaser4-gamedev | https://github.com/Yakoub-ai/phaser4-gamedev | Claude Code プラグイン：5 エージェント（architect/coder/debugger/playtester/asset-advisor）＋26 スキル。Codex 向けにも `npx skills add` 可 | MIT | 2026 | playtester / asset-advisor が「1日1本」パイプラインの QA と素材選定を担える |
| PlayableIntelligence/game-creator | https://github.com/PlayableIntelligence/game-creator | テキスト→2D(Phaser 3)/3D(Three.js) ゲーム生成プラグイン。手続き的ピクセルアート、Strudel チップチューン、Playwright QA、GitHub Pages/Netlify デプロイまで一式 | MIT（Strudel 使用時 AGPL 互換必須） | 2026（331★） | 「素材生成→QA→デプロイ」を一体化した最も近い完成形。丸ごと参考に |
| Nice-Wolf-Studio/claude-skills-threejs-ecs-ts | https://github.com/Nice-Wolf-Studio/claude-skills-threejs-ecs-ts | Three.js + ECS + TS のスキル 14 本（モバイル最適化・タッチ入力含む） | MIT | 2025-26 | Three.js 案件の日にだけ読み込む専用スキル |
| Donchitos/Claude-Code-Game-Studios | https://github.com/Donchitos/Claude-Code-Game-Studios | 49 エージェント・73 スキル・12 フック・11 ルールの「スタジオ」テンプレ（Godot/Unity/UE 中心） | MIT | 2026 | 重すぎるが hooks（コミット時アセット検証等）と rules 構成は流用価値あり |
| hoyoboy0726123/claude-skill-github-pages-deployer | https://github.com/hoyoboy0726123/claude-skill-github-pages-deployer | vite.config の base 注入→gh repo 作成→deploy.yml→Pages 有効化→Actions 監視まで無操作 | MIT | 2026 | 「デプロイして」の一言で Pages 公開。小規模だが仕組みは自作スキルの叩き台に |
| vercel-labs/skills（`npx skills`） | https://github.com/vercel-labs/skills | オープン Agent Skills のパッケージマネージャ。Claude Code / Codex / Gemini CLI 等 70+ エージェントに同時配布。`find-skills` スキル同梱 | MIT | 2026 | 3 エージェント併用の前提ツール。skills.sh で検索 |
| i18n 系スキル（mcpmarket） | https://mcpmarket.com/tools/skills/i18n-localization | JSON 翻訳構造・ICU 複数形・Intl API パターン | 各スキル依存 | 2026 | 日英同時公開の翻訳キー設計を任せる。品質は要確認 |
| ComposioHQ/awesome-claude-skills | https://github.com/ComposioHQ/awesome-claude-skills | コミュニティ awesome リスト | CC0/MIT 混在 | 2026 | 定期的に新スキルを拾う索引 |

## 2. AGENTS.md / CLAUDE.md / GEMINI.md の実例・ガイド・同期ツール

| 名前 | URL | 何か | ライセンス | 更新 | この開発者への効き方 |
|---|---|---|---|---|---|
| AGENTS.md 公式 | https://agents.md | Linux Foundation（AAIF）管理のオープン規格。Codex/Gemini CLI/Jules/Cursor 等が読む | CC/オープン | 2026 | 正本ファイルはこれ一択 |
| OpenAI Codex CLI docs | https://developers.openai.com/codex/cli | AGENTS.md の階層読込順（~/.codex → git root → cwd）、`/init` で雛形生成 | — | 2026 | Codex 側の読込ルールを把握して重複を避ける |
| Gemini CLI GEMINI.md docs | https://github.com/google-gemini/gemini-cli/blob/main/docs/cli/gemini-md.md | 階層読込・`@file` インポート構文・context file 名の変更設定 | Apache-2.0 | 2026 | `contextFileName` を AGENTS.md に設定すれば GEMINI.md 自体不要 |
| aq.dev: Keep AGENTS.md and CLAUDE.md in Sync | https://aq.dev/guides/keep-agents-md-and-claude-md-in-sync/ | AGENTS.md を正本、CLAUDE.md は `@AGENTS.md` 1 行、skills/commands は薄いラッパにする手法 | 記事 | 2026 | 推奨構成そのもの。まずこれに従う |
| inventivehq: CLAUDE.md vs AGENTS.md vs GEMINI.md | https://inventivehq.com/blog/claude-md-vs-agents-md-vs-gemini-md | 3 CLI の読込挙動比較 | 記事 | 2026 | 差分早見表 |
| dhruv-anand-aintech/agent-rules-sync | https://github.com/dhruv-anand-aintech/agent-rules-sync | rules・skills・settings・MCP 設定を Claude Code/Codex/Gemini CLI/Cursor 間で ~3 秒で自動同期するデーモン（pip） | MIT | 2026 | symlink 運用が面倒なら常駐同期。MCP 設定も同期できるのが強み |
| HermeticOrmus/claude-code-game-development | https://github.com/HermeticOrmus/claude-code-game-development | Phaser/Three/Babylon/PixiJS のワークフロー文書、100+ プロンプト、5 テンプレ | MIT | 2025 | CLAUDE.md に書く「アーキテクチャ・命名・やらないこと」の文例集 |
| Chier Hu「Claude Code for Game Development」 | https://chierhu.medium.com/claude-code-for-game-development-7a88fcd19992 | 実プロジェクト調査。CLAUDE.md＋エンジン別 Skills＋MCP（実行中ゲームの目）の三点セットを推奨 | 記事 | 2026 ※未取得 | 環境設計の指針として引用可 |

## 3. スターターテンプレート

| 名前 | URL | 何か | ライセンス | 更新 | この開発者への効き方 |
|---|---|---|---|---|---|
| phaserjs/template-vite-ts（公式） | https://github.com/phaserjs/template-vite-ts | Phaser 4 + Vite 6.3 + TS 5.7。HMR・アセット処理・本番ビルド。Pages ワークフローは無し | MIT | 2026 | ベース候補 No.1。deploy.yml だけ追加 |
| phaserjs/template-vite / template-react-ts / template-vue-ts | https://github.com/phaserjs/template-vite | 公式の JS 版 / React / Vue 連携版 | MIT | 2026 | UI を React で組みたい日の選択肢 |
| pawap90/phaser3-ts-vite-eslint | https://github.com/pawap90/phaser3-ts-vite-eslint | Phaser 3.80 + TS + Vite + ESLint + **GitHub Pages deploy.yml 同梱**（base 設定要） | 不明 | 2024-25 | deploy.yml と build.yml をそのまま公式テンプレに移植 |
| ourcade/phaser3-typescript-vite-template | https://github.com/ourcade/phaser3-typescript-vite-template | 老舗の Phaser 3 + TS + Vite | MIT | 2024 | 参考のみ |
| michealparks/babylon-template | https://github.com/michealparks/babylon-template | Vite + Babylon.js + Havok Physics + TS | MIT | 2025-26 | Babylon 用ベース。Havok 物理付きが便利 |
| GREEB/vite-babylon-ts-template | https://github.com/GREEB/vite-babylon-ts-template | Babylon 最小構成 | 要確認 | — | 最小で始めたい時 |
| pachoclo/vite-threejs-ts-template | https://github.com/pachoclo/vite-threejs-ts-template | Three.js + TS + Vite。**GitHub Actions build.yml＋Pages デモあり**。206 コミット | 要確認 | 2026-04 | Three.js 用ベース。Pages 対応済み |
| defmech/vite-threejs-ts-starter | https://github.com/defmech/vite-threejs-ts-starter | OrbitControls/Stats/影付き最小 Three.js | 要確認 | 2025 | 代替 |
| Vite 公式「Deploying a Static Site」 | https://vite.dev/guide/static-deploy | GitHub Pages 用公式ワークフロー YAML（configure-pages → upload-pages-artifact → deploy-pages） | MIT docs | 2026 | 全テンプレ共通の deploy.yml はここからコピー |

## 4. GitHub Actions（itch.io butler / Pages）

| 名前 | URL | 何か | ライセンス | 更新 | この開発者への効き方 |
|---|---|---|---|---|---|
| yeslayla/butler-publish-itchio-action（Butler Push） | https://github.com/marketplace/actions/butler-push | 入力：BUTLER_CREDENTIALS / CHANNEL / ITCH_GAME / ITCH_USER / PACKAGE（+VERSION）。v1.2.0 | 要確認（リポ参照） | 2025-26 | `dist/` を `html5` チャンネルへ push する定番。1 ジョブで itch.io 公開 |
| setup-butler 系 | https://github.com/marketplace/actions/setup-butler | butler を PATH に入れるだけの薄い Action | MIT | 2026 | 自前で `butler push` を書きたい場合（複数チャンネル等） |
| Publish to Itch.io with Butler | https://github.com/marketplace/actions/publish-to-itch-io-with-butler | セットアップ＋push 一体型 | MIT | 2025-26 | 上記の代替 |
| actions/deploy-pages（公式） | https://github.com/actions/deploy-pages | upload-pages-artifact とセットの公式 Pages デプロイ | MIT | 2026 | GitHub 推奨方式。permissions: pages/id-token だけ注意 |
| JamesIves/github-pages-deploy-action | https://github.com/JamesIves/github-pages-deploy-action | ブランチ push 型の老舗（v4.7.4） | MIT | 2026 | 1 リポで複数ゲームをサブディレクトリ公開したい時に柔軟 |
| Vite Github Pages Deployer | https://github.com/marketplace/actions/vite-github-pages-deployer | Vite 専用の 1 ステップ Action | MIT | 2025-26 | 最短 YAML |
| sitek94/vite-deploy-demo | https://github.com/sitek94/vite-deploy-demo | Vite → Pages の動くデモリポ | MIT | 2025 | 設定の答え合わせ |

## 5. CC0 / クレジット不要の素材ソースと検索 API・CLI

| 名前 | URL | 何か | ライセンス | 更新 | この開発者への効き方 |
|---|---|---|---|---|---|
| Kenney | https://kenney.nl/assets | 2D/3D/UI/SFX/フォント数万点、スタイル統一 | CC0 | 継続更新 ※未取得 | 「1日1本」の見た目を即座に揃える主力。API は無し → ETdoFresh/kenney.nl ミラー（https://github.com/ETdoFresh/kenney.nl）をローカルに置きエージェントに grep させる |
| Poly Haven Public API | https://github.com/Poly-Haven/Public-API / https://api.polyhaven.com | assets 一覧・カテゴリ・ファイル URL を返す公開 API。キー不要 | 素材 CC0 / API コード AGPL（ToS: 「Powered by Poly Haven」表記） | 2026 | HDRI・テクスチャ・小物モデルを MCP/スクリプトから直接取得可能 |
| Freesound API | https://freesound.org/docs/api/ | テキスト検索＋`license` フィルタ、プレビュー/DL（API キー、DL は OAuth2） | 音源ごと（CC0 ≈38 万件） | 2026 ※未取得 | SE 検索を自動化。フィルタ `license:"Creative Commons 0"` 固定で安全 |
| OpenGameArt + oga-go CLI | https://opengameart.org / https://github.com/numberoverzero/oga-go | 検索・DL・説明の CLI（Python 版は 2026-03 にアーカイブ、Go 版へ移行） | 素材ごと（CC0 チェックボックスあり）/ CLI MIT | 2026 | 2D スプライト・BGM の CLI 取得。公式 API は無いためスクレイプ節度に注意 |
| Quaternius / KayKit | https://quaternius.com / https://kaylousberg.itch.io | ローポリ 3D キャラ・環境・アニメ | CC0 | 2026 | Babylon/Three の 3D 日のキャラ供給 |
| ambientCG | https://ambientcg.com（API: https://docs.ambientcg.com/api/） | PBR テクスチャ・HDRI、JSON API あり | CC0 | 2026 | テクスチャ取得を自動化 |
| Sketchfab Download API | https://sketchfab.com/developers/download-api | CC ライセンスモデルの検索・glTF 取得（要トークン） | モデルごと（CC0 でフィルタ可） | 2026 | glTF で Three/Babylon に直投入 |
| Google Fonts | https://fonts.google.com | 日本語含む OFL フォント、CSS API | SIL OFL / Apache | 2026 | 和文 UI フォントの即時解決（Noto Sans JP 等） |
| Cinevva 無料素材ガイド | https://app.cinevva.com/guides/game-assets-guide | 20+ ソースの網羅と横断検索（Kenney/Quaternius/KayKit/Poly Haven/ambientCG/OGA/Freesound/Sketchfab） | 記事 | 2026 | ライセンス一覧の早見表 |

## 6. ソロ開発者の AI 駆動高速プロトタイピング事例

| 名前 | URL | 何か | ライセンス | 更新 | この開発者への効き方 |
|---|---|---|---|---|---|
| Zenn aya「グラフィックも BGM・SE も AI が作るテンプレ」 | https://zenn.dev/aya/articles/4c7ae95322ced5 | Phaser 4 + React 19 + TS + Vite。1〜2 時間規模の 2D ドットゲーム前提でアセット生成込みのテンプレ | 記事（テンプレは要確認） | 2026-06 ※未取得 | 日本語で最も近い構成。テンプレをフォークして Pages/itch.io ワークフローを足す |
| Zenn machamu「Codex ゲーム開発バズの正体」 | https://zenn.dev/machamu/articles/codex-claude-code-game-dev-comparison | 2026-04 以降の「1 プロンプト＋一晩自律実行」事例分析、Codex と Claude Code の使い分け、実務プロンプト集 | 記事 | 2026-05 ※未取得 | 3 エージェントの役割分担（Codex=長時間自律、Claude=設計/レビュー）の根拠 |
| Zenn itamoko「モンスター 78 体のブラウザ RPG を itch.io に」 | https://zenn.dev/itamoko/articles/55ccb137aa922e | Claude Code のみで育成 RPG を一人で完成・itch.io 公開 | 記事 | 2026-07 ※未取得 | 日本人ソロの itch.io 公開フロー実録 |
| 乙一『Minimal Rogue』（Claude Code + Suno、GitHub MIT） | https://gaming-st.com/news/otsuichi-claude-code-minimal-rogue-ai-game/ | 非エンジニアが Claude Code でローグライクを itch.io 無料公開、ソース MIT | MIT | 2026-08 ※未取得 | 「音楽は Suno」等、素材生成の分担例。リポを読んで CLAUDE.md を拝借 |
| note Hiro「ClaudeCode で 1 日でゲームを作る」 | https://note.com/hiro02/n/n7bb038808bf7 | 1 日完結の手順 | 記事 | 2026 ※未取得 | 1 日スケジュールの時間割参考 |
| Codex KB「Codex CLI for Game Prototyping」 | https://codex.danielvaughan.com/2026/05/10/codex-cli-game-prototyping-godot-phaser-browser-games-agent-skills/ | 設計書→プレイアブルまで Codex + Agent Skills で回す手順 | 記事 | 2026-05 ※未取得 | Codex 側のワークフロー雛形 |
| Linuxbeast「1 日で 3 本のブラウザゲーム」 | https://linuxbeast.com/blog/how-i-built-3-browser-games-in-one-day-with-claude-ai/ | Canvas ゲーム 3 本を 1 日で | 記事 | 2026 | 「1 日 1 本」の実現可能性の裏付け |
| Cinevva「Solo devs shipping, not vibing」 | https://app.cinevva.com/signals/2026-03-23-solo-devs-shipping-not-vibing | Void Balls の 8 並列 Claude Code エージェント運用等 | 記事 | 2026-03 | 並列エージェント（設計/実装/バランス/テスト）分担の実例 |
| Phaser 公式「AI-First」 | https://phaser.io/news/2026/07/phaser-game-agent-mcp-setup | Phaser Game Agent MCP の公式セットアップ | 記事 | 2026-07 ※未取得 | 下記 MCP 参照 |

## 7. MCP サーバー

| 名前 | URL | 何か | ライセンス | 更新 | この開発者への効き方 |
|---|---|---|---|---|---|
| microsoft/playwright-mcp | https://github.com/microsoft/playwright-mcp | `npx @playwright/mcp@latest`。`browser_take_screenshot` / `browser_snapshot` | Apache-2.0 | 2026 | ローカル dev サーバーの実プレイ確認・スクショを毎ビルド自動化（QA と itch.io 用画像） |
| phaserjs/phaser-game-agent | https://github.com/phaserjs/phaser-game-agent | `npx @phaserjs/game-agent`。Claude Code(HTTP MCP)/Codex/Gemini CLI 対応。コード・絵・音を生成しプレビュー URL 発行（Phaser アカウント＋クレジット制） | MIT（サービスは有料枠あり） | 2026-07 | Phaser 案件のアセット込み一気通貫。コスト要検証 |
| phaserjs/editor-mcp-server | https://github.com/phaserjs/editor-mcp-server | Phaser Editor v5 を MCP から操作 | 要確認 | 2026 | シーン配置を GUI エディタで持つ場合 |
| ahujasid/blender-mcp | https://github.com/ahujasid/blender-mcp | Blender を LLM から操作（26k★）。Poly Haven 取得統合あり | MIT | 2026 | 3D 日の簡易モデル・glTF 書き出し |
| Coding-Solo/godot-mcp | https://github.com/Coding-Solo/godot-mcp | Godot 起動・実行・デバッグ出力取得 | MIT | 2026 | Godot Web エクスポートに手を出す時のみ |
| Google Sheets 公式 MCP | https://developers.google.com/workspace/sheets/api/guides/configure-mcp-server | Google 公式リモート MCP（読み書き・batchUpdate） | — | 2026 ※未取得 | ゲーム台帳（日付/URL/素材ライセンス/翻訳キー）を Sheets で管理し、エージェントが自動記帳 |
| xing5/mcp-google-sheets | https://github.com/xing5/mcp-google-sheets | Drive + Sheets のコミュニティ MCP | MIT | 2026 | 公式が使えない環境の代替 |
| z27fang/itch-io-mcp-ts | https://github.com/z27fang/itch-io-mcp-ts | itch.io API（ライブラリ/購入/DL キー）。**ビルドのアップロードは不可** | 不明 | 2025 | 用途薄。公開は butler Action に任せる |
| github/github-mcp-server | https://github.com/github/github-mcp-server | Actions 実行状況・PR・Issue 操作 | MIT | 2026 | デプロイ失敗を検知して自動修正させる |

---

## 会議室への提案 5 つ（採用優先順）

1. **指示ファイルを AGENTS.md 正本に統一し、`npx skills` で SKILL.md を 3 エージェントに配布する**
   CLAUDE.md は `@AGENTS.md`、Gemini CLI は `contextFileName` を AGENTS.md に。skills は `npx skills add phaserjs/phaser` と `gamedev-skills/awesome-gamedev-agent-skills` の 2 本を入れれば Phaser/three.js の API 幻覚が激減し、Codex/Gemini でも同じ知識が使える。コスト 30 分、効果は毎日。

2. **「ゲームテンプレ」リポを 1 本作り、公式 `phaserjs/template-vite-ts` に Vite 公式の Pages ワークフローと `yeslayla/butler-publish-itchio-action`（channel `html5`）を同梱する**
   `git push` だけで GitHub Pages と itch.io に同時公開。Babylon 用は `michealparks/babylon-template`、Three 用は `pachoclo/vite-threejs-ts-template` を同じ deploy.yml で揃える。「Use this template」→ 1 日 1 リポ運用。

3. **Playwright MCP を QA ゲートに常設する**
   毎ビルド後にエージェントが `browser_take_screenshot` で実プレイ確認→スクショを itch.io カバー画像に流用。`game-creator` の Playwright QA スクリプトを参考に「起動・1 分間エラー無し・スコア変動」の 3 チェックを AGENTS.md に固定する。

4. **素材は CC0 限定ポリシーを AGENTS.md に明記し、Poly Haven API / Freesound API（CC0 フィルタ）/ Kenney ローカルミラーの 3 経路だけを許可する**
   ライセンス確認の判断をエージェントに委ねない。Kenney は API が無いので `ETdoFresh/kenney.nl` を clone してローカル検索させる。素材出典は自動で `CREDITS.md` に追記（CC0 でも記録は残す）。

5. **台帳を Google Sheets 公式 MCP で自動記帳し、日本語記事（aya テンプレ・乙一リポ・machamu の Codex 分析）を読んで「Codex=一晩自律実装 / Claude=設計・レビュー・公開 / Gemini=翻訳・素材探索」の役割分担を試す**
   1 日 1 本を継続するには「今日の 1 本」の決定とふりかえりの記録が律速。Sheets に日付・URL・所要時間・素材・翻訳キーを自動記録し、翌日の企画に使う。Phaser Game Agent MCP は有料クレジット制なので、まず 1 本で費用対効果を測ってから判断。

---
**未検証メモ**: zenn.dev / note.com / phaser.io / kenney.nl / freesound.org / developers.google.com は本環境の proxy で取得不可（※未取得と表記）。URL は検索結果に実在したものだが、内容は検索スニペット由来。採用前に人間側で 1 度開いて確認を推奨。