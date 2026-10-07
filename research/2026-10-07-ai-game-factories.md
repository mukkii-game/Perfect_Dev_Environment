# AI でゲームを量産している人・仕組みの調査(2026-10-07)

前回 `research/2026-09-13-borrowable-assets.md` に載せたもの
(Phaser 公式 skills、gamedev-skills、Yakoub-ai、PlayableIntelligence、Claude-Code-Game-Studios ほか)は繰り返さない。
数字は 2026-10-07 に GitHub 検索 API で見た値。`gh api` はこの session では 403 だったので、GitHub MCP 検索で代用した。

## 3行まとめ

1. 「AI が自分で遊んで確かめる」型の仕組みが標準になった。OpenAI 公式の `develop-web-game` skill は、`window.render_game_to_text` と `window.advanceTime(ms)` の 2 つの hook が要。うちの replay/bot と同じ発想で、しかも agent 側の共通語になりつつある。
2. 一番近い先行例は `majidmanzarpour/threejs-game-skills`(MIT、2.4k★、6月開始)。director skill が全体を振り分ける。決定論 hook、seed 固定、bot playtest、canvas の画素チェック、証拠 manifest の検査まで揃っている。
3. `zenstory-ai/novel-to-game` の QA 規約(1 回の通しプレイで launch/render/input/coreLoop/outcome/restart の 6 項目を見る。「面白さ」は PASS にせず limitation に書く)は、うちの「完成の定義」にそのまま使える。日本語で「1日1本を仕組みで回している」公開例は見つからなかった。

## 同じことをしている人・仕組み

| 名前 | URL | 誰 | 何か | 活動 / ライセンス | 確認 |
|---|---|---|---|---|---|
| openai/skills `develop-web-game` | https://skills.sh/openai/skills/develop-web-game | OpenAI | Web ゲームの作り方の skill。実装→操作→待つ→観察→直す、を回す。Playwright client、action payload JSON、`render_game_to_text`、`advanceTime` を使う | repo 27.9k★、2026-02 初出、1.1k install。ライセンスは repo 次第(未確認) | skills.sh で本文の冒頭を読んだ。GitHub 上のパスは 404(場所が変わった可能性) |
| majidmanzarpour/threejs-game-skills | https://github.com/majidmanzarpour/threejs-game-skills | Majid Manzarpour | Three.js ゲームの skill 9 本。director が gameplay/graphics/UI/QA/素材生成に振り分ける。Vite+TS の雛形入り。テスト hook `__THREE_GAME_TEST_HOOKS__`、seed 固定 RNG、smoke・画像回帰・bot playtest の雛形、canvas 検査スクリプト、`check_evidence.py`、API キー有無の probe | MIT、2,444★、2026-06 作成、10/07 も更新 | README を読んだ |
| zenstory-ai/novel-to-game | https://github.com/zenstory-ai/novel-to-game | ZenStory AI(中国) | 小説からゲームを作る skill 7 本。工程ごとに文書が 1 つ(PRODUCT_BRIEF → CONCEPT → GAME_DESIGN → ART_DIRECTION → BUILD_BRIEF → qa/verification.json)。`_progress.md` から再開できる | MIT、832★、2026-07 作成 | README を読んだ |
| DY-2026/GameDesignOS | https://github.com/DY-2026/GameDesignOS | DY-2026 | AI agent 用のゲーム設計 OS。セッションを証拠・実験・判断記録に変える。人の承認ゲートと巻き戻しがある | 411★、2026-05 作成。ライセンスは未確認 | 説明文だけ見た |
| holger1411/game-dev-pipeline | https://github.com/holger1411/game-dev-pipeline | holger1411 | moodboard →「目標スクショ」を先に決める → 素材パイプライン(kie.ai/Meshy/ElevenLabs/Blender)→ 目標画像に合うまで直す | 0★、2026-09-25 作成 | 説明文だけ見た |
| chongdashu/phaserjs-oakwoods | https://github.com/chongdashu/phaserjs-oakwoods | chongdashu | Phaser の vibe coding 実例。`phaser-gamedev` skill と Playwright テスト skill を一緒に使う | 86★、2026-09 更新 | 説明文と vibeindex の掲載だけ見た |
| MartinDelophy/awesome-gpt-6-astra | https://github.com/MartinDelophy/awesome-gpt-6-astra | MartinDelophy | 1 モデルで作ったゲームを、ソース・デモ・プロンプト付きで集めた一覧 | 338★、2026-09 作成 | 説明文だけ見た |
| Eurekaleo/awesome-ai-for-games | https://github.com/Eurekaleo/awesome-ai-for-games | Eurekaleo | ゲーム AI 研究(playtesting、PCG)の論文一覧 | 359★、2026-09 作成 | 説明文だけ見た |
| Capcom CEDEC 2026 自動プレイ AI | https://book.st-hakky.com/news/capcom-efficient-ai-driven-testing | Capcom | 人と同じ環境で遊ぶ自動 playtest agent。成功した行動をコードとして保存する | 2026 | 二次記事だけ見た |
| Playwright Agents(v1.56〜) | https://azukiazusa.dev/blog/playwright-agents | Microsoft / 解説 azukiazusa | Planner・Generator・Healer の 3 agent。Claude Code から呼んで、テストを作り、壊れたら直す | 2025〜 | 解説記事のタイトルだけ見た |
| ライブラリ記事「本の要約 400 本をカードゲーム化」 | https://library.libecity.com/articles/01KRDJMQ3JXA51XQ8KY6JKTCTH | 個人 | Claude Code で 1 日で作り、静的サイトとして公開 | 2026 | 検索結果の要約だけ見た |

## パクる候補 上位10(効果の大きい順)

| # | 何を | 出典 | どこに入れるか | 手間 |
|---|---|---|---|---|
| 1 | `window.render_game_to_text()` と `window.advanceTime(ms)` を、dev build だけで出す。AI は画面を状態テキストで読み、時間を決定論的に進める | openai develop-web-game | 雛形 `src/core/`(replay/tuning の隣に test-hooks を置く)。AGENTS.md には 1 行だけ書く | 小 |
| 2 | 「完成」を 6 項目の通しプレイで判定する:launch / render(空白でない、変化する)/ input / coreLoop / outcome / restart。状態は NOT_RUN・FAIL・PASS の 3 つ。面白さは limitations に書き、PASS にはしない | novel-to-game `qa/verification.json` | 雛形の bot tests と publish kit(公開前のゲート)。結果は `qa/verification.json` に残す | 小〜中 |
| 3 | canvas の非空白チェック(色の多さ、エッジ密度)と、desktop/mobile 両方の viewport スクショを 1 コマンドで撮る | threejs-game-skills `inspect-threejs-canvas.mjs` | 雛形 tools(Phaser 用に移植) | 中 |
| 4 | 証拠 manifest:今回の run ID と撮るべき状態の一覧を宣言し、古いスクショで「済み」と言わせない | threejs-game-skills `check_evidence.py` | 雛形 tools か ai-ops | 中 |
| 5 | director 型の skill を 1 本にまとめる。入口を 1 つにして、専門 skill は director が呼ぶ。小さい修正には小さい検証だけ、と比例させる | threejs-game-skills | war-room `skills/`(今日のゲームを作る skill の構成の型) | 中 |
| 6 | 工程ごとに文書 1 つ+`_progress.md` で再開。「BUILD は設計を勝手に変えない」というルール | novel-to-game | 1日1本の Routine の手順(企画メモ → 実装 → QA の受け渡し) | 小 |
| 7 | 企画を複数案出し、名前のついた「却下条件」で落とす(例:固有名詞を外すと汎用テンプレしか残らない、など) | novel-to-game `CONCEPT.md` | 「今日のお題」生成の Routine / skill | 小 |
| 8 | 「目標スクショを先に決め、合うまで直す」流れ | holger1411/game-dev-pipeline | 見た目を磨く skill の手順。knowledge に技法として 1 行 | 小 |
| 9 | API キーの有無を値を出さずに `KEY=SET|MISSING` で調べる probe。無ければ手続き生成に落とすと決めておく | threejs-game-skills `probe_asset_credentials.sh` | ai-ops / dev-tools | 小 |
| 10 | 「ジャンルの外枠」チェック表:各ジャンルらしさの部品(導入、目標表示、成長、また遊ぶ理由)を、実装・縮小・省略に分けて理由を書く | novel-to-game `GAME_DESIGN.md` | war-room `knowledge/`(ジャンル別の表、csv) | 小 |

## 見送り

| 何 | 理由 |
|---|---|
| GameDesignOS | Python 製の別 OS。うちの decisions/topics と役割がかぶる。中身は未確認 |
| threejs-game-skills の素材生成 skill(Tripo/Gemini/ElevenLabs) | 有料 API 前提。1日1本の固定費が増える。probe と代替手段の考え方だけ借りる |
| Capcom の自動 playtest、Ziva の full-game-tester | 大規模・商用・非公開。参考の話にとどめる |
| awesome-gpt-6-astra、awesome-ai-for-games | 一覧なので直接使える部品はない。月に 1 回見る索引として ai-news Routine に入れる程度 |
| Playwright Agents(Healer) | canvas ゲームは DOM が薄いので効きにくい。#1 の hook の方が確実 |
| 日本語の「1 日で作った」系の記事(libecity、classmethod など) | 単発の体験談で、仕組みとして使えるものはない |

## 未確認

- openai/skills の develop-web-game の現在のパスとライセンス。`github.com/openai/skills/blob/main/skills/.curated/develop-web-game/SKILL.md` は 404 だった。skills.sh では見られた。
- `gh api` が 403(この session では外部 repo の許可がない)。★と日付は GitHub 検索 API の値。ライセンスは README の記載から。
- GameDesignOS、game-dev-pipeline、phaserjs-oakwoods、awesome-gpt-6-astra は説明文しか見ていない。
- X、note、Zenn で「AI で毎日 1 本」を仕組みとして公開している日本の人は、今回の検索では見つからなかった。いないとは言い切れない。次は X 検索で探す。
- threejs-game-skills の「bot playtest metrics」が何を測っているかは、README だけでは分からない。手順書(`threejs-qa-release`)は読んでいない。
