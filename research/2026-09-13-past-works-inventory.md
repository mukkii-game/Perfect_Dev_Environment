# 過去作の棚卸し(mukkii-game org 作品 repo 41 本、2026-09-13 時点)

出典: https://github.com/mukkii-game の全 47 repo から環境系 6 本(ai-dev-infra, web-app-template, ai-ops, gd-knowledge, gas-plannning-sheet / GAS-Plannning-sheet, Perfect_Dev_Environment)を除いた 41 本。各 repo を `--depth 1` でクローンし、README / package.json / 主要ソースを読んだ。読めなかった repo はなし(空 repo は「空」と記載)。

要点 3 行:
- 実質的な作品は 25 本。うち Web 作品 21 本の技術は「素の canvas/DOM JS(ビルドなし)」が 13 本で最多、Vite+TS が 6 本、Phaser は 1 本、Three.js は 2 本。AI に書かせた結果として自然に「ライブラリなし + 自前の薄い層」に収束している。
- 毎回作り直している部品は、入力(キー+タッチ統合)、WebAudio の合成音、localStorage セーブ、タイトル/ポーズ/ミュート、DPR 対応 resize の 5 つ。日英切替は 1 本(cedec-heat-dash-2026-fable)にしか無く、ゲームパッド対応も 1 本(CassetteVisionGame)のみ。
- 企画・データ系では「CSV を正本にして Python で data.gs を生成し clasp でスプシへ同期する」型が 2 repo で独立に発生しており、GAS 汎用ツールの最有力候補。空・重複・スモーク残骸の repo が 8 本ある。

## 一覧(41 本)

種類: ゲーム / アプリ / ツール / 企画資料 / GAS / その他。「素 JS」= ビルドツールなしの素の canvas または DOM。公開先は README・ワークフローから判る範囲。

| repo | 公開 | 種類 | ジャンル | 技術 | 外部ライブラリ | 公開先 | 共通化できそうな部品 | 一言メモ |
|---|---|---|---|---|---|---|---|---|
| youjo | 公開 | その他(絵本) | SF 絵本 24 頁 | Python → 単一 HTML + PDF | fontTools, PyMuPDF, ReportLab | 未公開(output は git 外) | 単一 HTML 生成、日本語フォントのサブセット化、ルビ付与 | manuscript.md が正本。画像プロンプト JSON 同梱 |
| ImoteControllDandy | 公開 | ゲーム | 3D アクション(巨大な妹) | Vite + React + Three.js(R3F) | @react-three/fiber, drei, rapier, @pixiv/three-vrm, zustand, oxlint | Pages(Actions)。itch.io 想定 | 3D 入力(WASD + スティック + マウスロック)、仮想パッド、VRM 読込、トゥーン描画 | 唯一の React 構成。docs/SPEC.md、CLAUDE.md あり |
| -Navier-Stokes | 公開 | ゲーム | タイポグラフィ探索(関係性) | 素 JS(canvas) | なし | Pages(Actions) | ポインタ追従移動、文字単位の衝突 | README が英語。5 頁構成。repo 名の先頭 `-` は clone 時に要 `--` |
| minogashi-game | 公開 | ゲーム | 文字入力クイズ(ネタ) | 素 JS(DOM、11 行) | なし | Pages(.nojekyll) | なし(超最小) | 「1 日 1 本」の最小形の見本 |
| ttekoto | 公開 | ゲーム | 2 択会話 ADV(スマホ) | 素 JS(DOM、dist 直置き) | なし(chika フォント) | Pages(Actions) + ChatGPT app hosting(.openai/hosting.json) | 文字送り、合成 SE、既読結末の保存 | 仮画像は権利物。dist のみ管理 |
| tetrishoot | 公開 | ゲーム | パズル × 全方向 STG | Vite + TS + canvas | Google Fonts | Pages(Actions) | Input、Sound、GameManager の状態遷移、RetroFont | HANDOFF.md、SPECIFICATION.md あり |
| tetrishooter | 公開 | その他 | ― | README のみ | ― | ― | ― | tetrishoot の重複。削除候補 |
| GGJ2026-MASK | 公開 | ゲーム | 見下ろし体当たりアクション | Godot 4.2(GDScript) | ForlornU TopdownStarter、m3x6 font | 不明(Web 書き出しなし) | Godot の FSM(player/enemy)、TileMap | GGJ 作。README はスターターのまま。docs/SPEC.md は自前。.cursor/rules あり |
| weed | 公開 | ゲーム | スマホ海中アクション(コンブ) | 素 JS(canvas) | なし(BGM: 魔王魂) | 不明(build.mjs で dist 生成) | マルチタッチ、Audio 要素プール、PWA manifest、DPR resize | check-game.cjs で node テスト。唯一の PWA |
| the-short-walk | 公開 | ゲーム | デスゲーム・リズム(1 ボタン) | 素 JS(canvas) + WebSocket サーバ | ws(node)、Cloudflare Workers(wrangler)、LPC 素材 | 未公開(itch.io / unityroom 検討中) | 1 ボタン入力、入力遅延計測、WebAudio 合成、ラウンド単位ロックステップ通信 | Python で群衆スプライト合成。企画書.md 同梱。唯一のマルチプレイ |
| Yasu | 公開 | ゲーム | 8bit 推理 ADV | Vite + TS + DOM(256×240) | vitest, playwright, DotGothic16 | Pages + itch.io(ai-dev-infra 経由) | 固定解像度の整数倍スケーリング、50 音パネル入力、状態を純関数化 | 全自動公開の実証例。CI が重い(既知) |
| bolero_ball | 公開 | ゲーム | 音楽アクション(ま～るタイプ) | 単一 HTML(canvas、2,433 行) | なし | 不明 | WebAudio unlock、タッチ | README 1 行。mp3 同梱 |
| web-app-bootstrap-smoke | 公開 | その他 | 雛形検証 | Vite + TS | vitest, playwright | Pages(雛形のまま) | ― | ai-ops のスモーク残骸。削除候補 |
| web-app-bootstrap-actions-smoke-20260829 | 公開 | その他 | 雛形検証 | Vite + TS | vitest, playwright | Pages(雛形のまま) | ― | 同上 |
| sayounara | 公開 | ゲーム | 下校会話 ADV(表情選択) | 素 JS(DOM) | なし | 不明 | 文字送り、表情 6 択、WebAudio で 3 拍子 BGM を作曲 | BGM をコードで作曲した例 |
| OneWordHorrorNovel | 公開 | ゲーム | 一文字ホラー | 単一 HTML(DOM/CSS、540 行) | Twemoji, game-icons | 不明 | WebAudio 短音 | 1 枚完結 |
| marshmallow-build-demo | 公開 | ゲーム | 音楽同期落ちものパズル(体験版) | 素 JS(canvas) | Google Fonts | Pages | input.js(キー + タッチ)、music.js 拍同期、sfx.js 合成、util.js(save) | private 版の公開切り出し |
| panzer-tokoron | 公開 | ゲーム | 3D レールシューター | Three.js(CDN importmap) + 素 JS | three 0.166、Kenney SFX(CC0) | Pages | Input(マウス + タッチ)、AudioSys(合成 + ファイル、失敗時フォールバック)、tools(puppeteer スクショ / soak) | 3D モデルは全てコード生成。HANDOFF.md、SPEC.md |
| rare-earth-demo | 公開 | ゲーム | 見下ろし ARPG | 素 JS(canvas) | OpenGameArt CC0 | Pages | engine.js(Game / Input / Camera / TileMap / 衝突 / Sheet)、audio.js(beep / sfx / bgm) | 素 JS で最も「エンジン」らしい。キャラ交代あり |
| CassetteVisionGame | 公開 | ゲーム | レトロ制約アクション | Vite + TS 自前エンジン | なし | Pages(gh-pages ブランチ) | CVEngine、Renderer(パレット制約)、Input(キー + ゲームパッド + タッチ)、Sound、Scene 型、touch UI | 制約付き自前エンジンの先行例。AGENTS.md あり |
| CEDEC-HEAT-DASH-2026 | 公開 | ゲーム | ランアクション | Vite + TS + Phaser 3 | phaser 3.87、playwright | Pages + Netlify(base 切替) | Phaser シーン 6 本(Boot/Title/Op/Play/Result/Ed)、sound.ts、storage.ts | 唯一の Phaser 作。GAME_SPEC.md |
| cedec-heat-dash-2026-fable | 公開 | ゲーム | 同題材の別実装 | Vite + TS + canvas | playwright、Yusei Magic | Netlify(単発デプロイ) | core/(font, i18n 日英, input, save, video)、audio/(engine, music)、scenes | 日英切替の唯一の実装。Playwright 48 本。autoplay / catalog 撮影ツール |
| my-butsukari-ojisan | 公開 | その他(絵本) | Web 絵本 | 素 JS(DOM) | Google Fonts | 不明 | ページ送り、自動再生、SE | 絵本ビューアの 2 例目(youjo と別実装) |
| known-quest-demo | 公開 | アプリ | 英語学習(スワイプ) | 素 JS(DOM) | なし(speechSynthesis) | Pages | localStorage 進捗(マイグレーション付き)、スワイプ、WebAudio | ENG_App/prototype/game-first と同一ファイル |
| NeoSoukoban | 公開 | ゲーム | 倉庫番パズル | 素 JS(DOM/canvas) | なし | Pages 可(ビルド不要) | engine.js 純ロジック(UMD、DOM 禁止)、undo、ソルバ、browsertest | ロジック分離の模範。CLAUDE.md で禁止事項を明示 |
| doroneko | 公開 | その他 | ― | 空 repo | ― | ― | ― | 空 |
| SoundGameOchiru | 公開(fork) | ゲーム | 音ゲー教材 | Unity 2020.3 | klak MIDI、FadeManager | unityroom(元作者) | ― | fork。参照のみ |
| Unity2D_TD | 公開(fork) | ゲーム | TD サンプル | Unity 5 | Tiled TMX | ― | ― | 2015 年の fork。参照のみ |
| charge-and-anchor-gdd | 非公開 | 企画資料 | デッキ構築ローグライク GDD | md 74 + csv 81 + GAS + Python | clasp | Google スプシ | csv→data.gs 変換(build_gas.py)、スプシ目次生成 GAS、duo_sim.py(戦闘シミュレータ)、pitch.html | Agents.md、AI_HANDOVER あり。パスが `E:\` 固定 |
| PilotMod | 非公開 | その他(MOD) | Slay the Spire 改造ベース | Java 8 + Maven、ModTheSpire / BaseMod | BaseMod | 非公開厳守 | ― | build.ps1。tools/ に実機自動テスト |
| Orejanakya | 非公開 | その他 | ― | README のみ | ― | ― | ― | 空 |
| slayers-ip-reference | 非公開 | 企画資料 | IP 資料の隔離 | csv 51 + Python 18 + GAS | clasp、PyMuPDF、pytesseract | Google スプシ | csv→GAS 同期(build_gas.py の 2 例目)、PDF OCR、リスト整形 | IP 隔離ルールの実例 |
| SlayTheSpireLike | 非公開 | ゲーム | デッキ構築 RL(Unity) | Unity 6000.3 + 純 C# ルールエンジン + Web プロト | DOTween、UniTask | ― | 決定論 RNG、ルールエンジン + EditMode テスト、kendo/engine.js(UMD 純 JS シミュレータ) | CSV フレーバー層で IP 分離。CLAUDE.md |
| ENG_App | 非公開 | アプリ | 英語学習データ基盤 | Python 142 本 + csv 98 + Actions cron | 標準ライブラリのみ(csv, argparse, sqlite3, hashlib) | Pages(known-quest-demo として) | CSV パイプライン、定期収集 Actions、md 正本体系(AGENTS/DECISIONS/HANDOFF) | 文書が md 27 本と重い。xlsx は編集 UI 扱い |
| CasterMod | 非公開 | その他(MOD) | StS キャラ MOD | Java + Maven | BaseMod | 非公開厳守 | 日英 localization JSON(語彙表方式) | PilotMod の前身 |
| marshmallow-build | 非公開 | ゲーム | 音楽同期落ちもの(α) | 素 JS(canvas) | Google Fonts | ― | demo と同じ + tools(dev-server, shot-server, analyze.html) | docs/GAME_DESIGN.md。.claude/launch.json |
| cursed-labyrinth-base | 非公開 | その他(教材) | 購入講座アーカイブ | Unity 2021.3 | DOTween | 非公開厳守 | ScriptableObject データ駆動、SimpleTranslation | 参照のみ。再配布禁止 |
| My-project | 非公開 | その他 | Unity 6 空テンプレ | Unity 6000.3 URP | ― | ― | ― | 中身なし |
| PanzerTokoron | 非公開 | その他 | Unity 6 空テンプレ | Unity 6000.3 URP | ― | ― | ― | 中身なし。Web 版 panzer-tokoron に移行済みと見られる |
| fb-radio-auto | 非公開 | ツール | FB グループ自動投稿 | Node + express + puppeteer(Render 想定) | puppeteer, express, axios | Render | ヘッドレスブラウザで投稿 | cookies.json(FB の datr/fr 等 6 件)がコミット済み。要確認 |
| GGJ2025 | 非公開 | その他 | ― | .gitignore のみ | ― | ― | ― | 空 |

補足: `ENG_App` は「アプリ」だが実体はデータ工場(Python + CSV)で、公開 UI は known-quest-demo に切り出されている。`GGJ2026-MASK` の README は元スターターのもので作品説明がない。

## 横断所見

### 1. 繰り返し出てくる部品トップ 10(Web 作品 21 本中の出現数)

| 順位 | 部品 | 出現 | 代表実装 | 備考 |
|---|---|---|---|---|
| 1 | WebAudio 合成音(beep / tone / unlock) | 18 | rare-earth-demo audio.js、weed tone()、panzer-tokoron AudioSys | ほぼ全作で書き直している。ファイル再生へのフォールバックは panzer-tokoron のみ |
| 2 | キー + タッチ統合入力 | 16 | cedec-fable core/input.ts、rare-earth engine.js Input、marshmallow input.js | 「左半分ドラッグ = 移動、右半分タップ = ボタン」型が 4 作で同形 |
| 3 | タイトル画面 → プレイ → リザルトの状態遷移 | 15 | tetrishoot GameManager、CEDEC Phaser scenes、cedec-fable scenes.ts | 文字列 enum で自前実装が多数 |
| 4 | DPR 対応 resize / 固定論理解像度スケーリング | 12 | Yasu(256×240 整数倍)、cedec-fable core/video.ts、CassetteVisionGame Renderer | レトロ作は固定解像度、それ以外は全画面 |
| 5 | localStorage セーブ(ベスト / 設定 / 既読) | 9 | cedec-fable core/save.ts(DEFAULTS マージ + try/catch)、known-quest(マイグレーション付き) | キー名の衝突対策・版管理は 2 作のみ |
| 6 | ミュートトグル(M キー / 🔊 ボタン) | 9 | CEDEC、NeoSoukoban、marshmallow | save と結合している例は cedec-fable のみ |
| 7 | 画面上の仮想ボタン / 仮想パッド | 8 | CassetteVisionGame ui/touch.ts、Imote VirtualPad.tsx、cedec-fable 縦画面デッキ | スマホ前提の作品が多い |
| 8 | 文字送り(タイプライタ演出) | 6 | Yasu、sayounara、ttekoto、OneWordHorrorNovel、minogashi | ADV 系で毎回作り直し |
| 9 | 純ロジック分離 + Node テスト / ソルバ | 5 | NeoSoukoban engine.js(UMD)、SlayTheSpireLike kendo/engine.js、Yasu game.ts、weed check-game.cjs | AI に「DOM 禁止」と書くと分離が守られる(NeoSoukoban CLAUDE.md) |
| 10 | 自動スクショ / 自動プレイ検証ツール | 5 | panzer-tokoron tools/、marshmallow shot-server、cedec-fable tools/autoplay.mjs、the-short-walk ?auto= | puppeteer と playwright が混在 |

次点: ポーズ(7)、BGM のコード作曲(sayounara、the-short-walk、panzer-tokoron の 3)、日英切替(1)、ゲームパッド(1)、PWA(1)、マルチプレイ(1)。

### 2. 繰り返し使われる外部ライブラリ・素材

- ビルド / テスト: Vite(8)、TypeScript(8)、Playwright(6)、Vitest(3)、puppeteer / puppeteer-core(3)。
- 描画: Phaser 3(1)、Three.js(2、うち 1 は CDN importmap、1 は React Three Fiber)。素の canvas が 13 と圧倒的。
- フォント: DotGothic16(最多、Yasu ほか)、M PLUS 系、Yusei Magic、Zen Maru Gothic、m3x6。Google Fonts の CDN 読込が 4 作。
- 音・絵の素材: Kenney(CC0)、OpenGameArt(CC0、LPC)、魔王魂、効果音ラボ。CREDITS.md / CREDITS.txt を置く習慣は 6 作で定着している。
- Unity 側: DOTween(2)、UniTask(1)、URP(空テンプレ 2)。
- 企画側: clasp + GAS(2)、PyMuPDF(2)、fontTools(1)。

### 3. 雛形にすべき共通構成

過去作から自然に出てきた最小構成は次の通り。web-app-template(Vite + TS + Vitest + Playwright)の上に載せる。

```
src/
  core/    input.ts  save.ts  audio.ts  video.ts(resize/論理解像度)  i18n.ts  scene.ts
  game/    (作品固有。scenes/ と data)
  ui/      touch.ts(仮想ボタン)
tools/     shot.mjs(スクショ)  autoplay.mjs(自動プレイ)
docs/      SPEC.md  HANDOFF.md  CREDITS.md
AGENTS.md  (CLAUDE.md は @AGENTS.md の 1 行)
```

- ビルドなし派(13 作)にも対応できるよう、core/ は ES Modules の単独ファイルで動く形にし、Vite は「使ってもよい」に留める。
- ドキュメントは SPEC.md + HANDOFF.md + CREDITS.md の 3 枚で足りている(tetrishoot、panzer-tokoron、Yasu の実績)。ENG_App のような md 27 本体系はパイロット版には過剰。
- 純ロジック分離は AGENTS.md に「engine には DOM / audio / 乱数 / 時刻を書かない」と書くだけで守られている(NeoSoukoban、SlayTheSpireLike)。

### 4. エンジン(engine/)に入れる候補と入れない候補

入れる(毎回要る + 実装がほぼ同形):
- input: キー + ポインタ + ゲームパッドの統合、左右半面のドラッグ / タップ役割分け、最初のジェスチャで audio unlock。元: cedec-fable core/input.ts + CassetteVisionGame input.ts。
- audio: WebAudio 合成(tone / beep / noise)、ファイル再生プール、失敗時の合成フォールバック、ミュート永続化。元: panzer-tokoron AudioSys + rare-earth audio.js。
- save: 名前空間つき localStorage、DEFAULTS マージ、版番号、try/catch。元: cedec-fable save.ts + known-quest の移行処理。
- video: 論理解像度 + DPR resize、整数倍 / 連続倍率の切替。元: Yasu + cedec-fable video.ts + CassetteVisionGame Renderer。
- scene: Scene インタフェース(enter / update / draw / exit)と Title / Result の最小実装。元: CassetteVisionGame types.ts + cedec-fable scenes.ts。
- i18n: key → [ja, en] テーブルと lang 永続化。元: cedec-fable i18n.ts(唯一の実装)。
- text: 文字送り、ルビ。元: Yasu + sayounara + youjo build.py。
- 公開メタ: base パス切替(Pages / Netlify / itch)、CREDITS 雛形。元: CEDEC-HEAT-DASH-2026 vite.config + weed build.mjs の絶対パス検査。

入れない(作品固有、または既存ライブラリで足りる):
- 物理・衝突・TileMap・カメラ(rare-earth engine.js)。Phaser 3 か素の実装で作品ごとに変える方が速い。
- 3D 一式(Three.js、R3F、rapier、VRM)。Three.js 側の作法が強く、薄い層を挟む利点が小さい。
- 拍同期・リズム判定(marshmallow music.js、the-short-walk judge.js)。ジャンル固有。
- マルチプレイ通信(the-short-walk server/)。汎用化するなら engine ではなく別ツール。
- Godot / Unity のコード。Web エンジンとは別系統。凝りたい作品を Godot に移す時に改めて棚卸しする。
- パレット制約レンダラ(CassetteVisionGame)。面白いが用途限定。「レトロ制約プリセット」として video に薄く残す程度。

### 5. GAS・Python の汎用ツール候補

- csv → data.gs → clasp push → スプシ一括書き込み(目次シート自動生成、メタ列のグレー化)。charge-and-anchor-gdd と slayers-ip-reference で独立に 2 度書かれている。gas-plannning-sheet と統合し「企画 CSV ⇄ スプシ同期」の汎用 GAS にする(topic 08)。パスが `E:\` 固定なので相対パス化が必要。
- 単一 HTML ビルド(画像 base64 + 日本語フォントサブセット + ルビ)。youjo build.py。絵本 / ノベル系の公開形式として汎用化できる。my-butsukari-ojisan とビューアを統一できる。
- スクショ / 自動プレイ / soak テスト。panzer-tokoron tools(puppeteer)、cedec-fable tools(playwright)、marshmallow shot-server。playwright に寄せて 1 本にし、雛形の tools/ に置く。
- PDF OCR → CSV(slayers-ip-reference ocr_pdf.py、PyMuPDF + pytesseract)。資料取り込みの汎用ツール。
- 定期収集 Actions(ENG_App entertainment-collection.yml、cron 毎日)。gd-knowledge collect.yml と同型。1 つの再利用ワークフローにできる。
- 戦闘シミュレータ(duo_sim.py、kendo/engine.js)。汎用ではないが「ルールを純関数で書いて Node / Python で回す」型として AGENTS.md の作法に残す。
- LPC スプライト合成(the-short-walk build_sprites.py)。素材加工ツールとして topic 06 の索引に載せる。
- fb-radio-auto(puppeteer 投稿 bot)は SNS 投稿の雛形になり得るが、cookies.json のコミットを先に処理する。

### 6. 整理候補(棚卸しで見つかった片付け)

- 空 / README のみ: doroneko、Orejanakya、tetrishooter、GGJ2025、My-project、PanzerTokoron。アーカイブか削除。
- スモーク残骸: web-app-bootstrap-smoke、web-app-bootstrap-actions-smoke-20260829。
- 同一内容の二重管理: known-quest-demo と ENG_App/prototype/game-first、marshmallow-build と marshmallow-build-demo、CEDEC-HEAT-DASH-2026 と cedec-heat-dash-2026-fable(別実装なので残す価値あり)。
- 要確認: fb-radio-auto の cookies.json。

関連 topic: 04, 06, 08
