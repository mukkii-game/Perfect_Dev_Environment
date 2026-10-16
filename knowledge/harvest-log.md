# 気づきの回収台帳

作品セッションの「全体に共有したい気づき」(各作品の `HANDOFF.md`)を毎日回収し、全作品へ配った記録。
**同じ気づきを二度取り込まないための台帳。** 新しいものを下に足す。

| 日付 | 作品 repo | 気づき | 取り込み先 |
|---|---|---|---|
| 2026-10-03 | (ユーザーが会議室に持ち込み) | 縦長・横長モニタで画面が引き伸ばされる → 縦横比を保って黒帯 | 雛形 `docs/knowledge/web-game-rules.md` §9-5・§8 |
| 2026-10-03 | metopon | VOICEVOX はアクセントが崩れる → 1語ずつ東京式に付け直す。Docker の cpu イメージで動く | `tables/assets.csv` VOICEVOX 行 |
| 2026-10-03 | metopon | 使った素材: Twemoji / 魔王魂 / VOICEVOX:春日部つむぎ(評価なし) | `tables/used-assets.csv` |
| 2026-10-03 | metopon | iPhone 消音で無音 → 無音 audio を最初のタップで鳴らす | 既に §9-1 にあり、取り込みなし |
| 2026-10-03 | (スプシのコメント欄) | 2 シートとも記入なし | — |
| 2026-10-05 | metopon | VOICEVOX を Windows で動かす手順(vvpp を展開して run.exe、Docker 不要) | `global/pc-setup.md` |
| 2026-10-05 | metopon | Kenney Pixel Shmup は題材が限られる(砂漠なし) | `tables/assets.csv` Kenney 行 |
| 2026-10-05 | metopon(格上げ) | 作品が Esc を一時停止に使う → 雛形の調整パネルの Esc と衝突 | 雛形 `src/core/tuning.ts` を F2 に変更 |
| 2026-10-05 | (スプシのコメント欄) | 未確認(回収を簡略化) | — |
| 2026-10-06 | obake-chochin | 記録→再生がずれる(丸め・bot の乱数を分ける)+ bot に lag を付けて反射神経依存を測る | 雛形 `web-game-rules.md` §9-6・§8 |
| 2026-10-06 | obake-chochin | Phaser 4 Graphics の arc が直線でつながる → lineBetween で区切る | 雛形 `web-game-rules.md` §9-7・§8 |
| 2026-10-06 | obake-chochin | 元ネタの芯を 3〜5 個の仕組みに分ける。説明のサインを足しすぎない。タイマーは物の距離で見せる | `start-from-reference.md` 地雷・`tables/mindset.csv` |
| 2026-10-06 | obake-chochin | viewport 固定・Chromium 予備 | 雛形 07a110a で対応済み |
| 2026-10-06 | (他の repo) | emmichy・game-llm・私有 repo 3 つ・my-rss に全体向けの気づきなし。素材は自作のみ | — |
| 2026-10-06 | (スプシ) | コメント欄・☑ ともに記入なし。AI知見 10-07 はまだ無く TIPS 0 件 | — |
| 2026-10-07 | obake-chochin | 「◯◯みたいな」の芯を移す手順(動詞→仕組み→ひねりは 1 ルールに合体→情報は絵の中の出来事→bot で芯を測る) | `start-from-reference.md` 手順 2・`tables/mindset.csv` 出典 |
| 2026-10-07 | obake-chochin | genres.csv にミサイルコマンド系が無かった(使用記録「無かった」) | `tables/genres.csv` に 1 行 |
| 2026-10-07 | (他の repo) | emmichy は記録済み。my-rss は自動更新のみ。私有 repo 2 つに全体向けの気づきなし。素材の追加なし | — |
| 2026-10-07 | (スプシ・格上げ) | 値の 4 タブはコメント・☑ ともに記入なし。AI知見 10-07 は収集失敗で 0 件、TIPS・用語 0 件。格上げ 0 件 | — |
| 2026-10-08 | obake-chochin | アプリ内ブラウザで横向きにならない / Phaser の字欠け・Web フォント / 写しと状態の上書き順(bot の崖) / BGM の拍合わせ | 雛形 `web-game-rules.md` §9-8〜9-11・§8 |
| 2026-10-08 | obake-chochin(格上げ) | AI が決める音量は大きめ(人間の指摘「いつもでかめ」) | 雛形 `src/core/audio.ts` + `src/tuning.ts` に `audio.sfx` / `audio.bgm`(既定 0.45)。4a3580f |
| 2026-10-08 | obake-chochin | 動詞で混ぜる・ひらめきの採点・形と模様をサインに・通り道の線・置く前に見せる・格子とマス・敵の連鎖・弾の補充・出口の待ち伏せ・型ごと×やり方の bot・欲張らない bot・手本と自動の確かめ・選択の意味 | `knowledge/game-design.md` 3〜6 |
| 2026-10-08 | kutsuzure | bot で歩き方 5 通り × 最後まで + 辛口ディレクター役の別 AI | `knowledge/game-design.md` 6 |
| 2026-10-08 | obake-chochin | pyopenjtalk + HTS Voice Mei(クラウドで日本語の声)/ 魔王魂は Referer で取れる・効果音は選べない | `tables/assets.csv` |
| 2026-10-08 | kutsuzure | VSCO-2-CE(CC0 の楽器 1 音、一部 1 オクターブずれ) | `tables/assets.csv` |
| 2026-10-08 | obake-chochin / kutsuzure | Pages を開けない・URL の直後・素材サイトの通る通らない・GitHub 検索 API 403・SVG→PNG | `env-gotchas.md` |
| 2026-10-08 | obake-chochin / kutsuzure | 使った素材 8 件(魔王魂 BGM・Mei・Kenney・VSCO-2-CE・OGA の CC0・Google Fonts)。評価なし、★ 無しで素材庫の保存なし | `tables/used-assets.csv` |
| 2026-10-08 | (非公開の企画 repo) | 画面レイアウトをスライドで人が直し、スクリプトで定義に書き戻す往復 | `process-patterns.md` 8(一般化して記載) |
| 2026-10-08 | (他の repo) | emmichy・game-llm・my-rss に HANDOFF の気づき欄なし。非公開の知識 repo は自動収集のみ。ai-ops は台帳の自動更新 | — |
| 2026-10-08 | (スプシ) | 値の 4 タブはコメント・☑ ともに記入なし。TIPS 3 件(AI知見 10-08)・AI タブに Gemini 画像・音楽の行を追記。用語 0 件(新しい名前は未確認のものだけ) | `tables/tips.csv`・`tables/ai.csv` |
| 2026-10-08 | kutsuzure | 絵・BGM を専門 AI に直接頼めない(鍵が無い) | 憲法候補として受領済み → `topics/06-assets.md`(Mukkii に GEMINI_API_KEY を依頼中) |
| 2026-10-09 | obake-chochin | Canvas の切り抜き(destination-out)は切る形を不透明に | 雛形 `web-game-rules.md` §9-12・§8 |
| 2026-10-09 | obake-chochin(格上げ) | Facebook でリンクに絵が出ない(ほかの作品でも)。og:image:width/height が無い・古い結果を覚える | 雛形 `index.html` に width/height/type/secure_url/alt と twitter:image、AGENTS.md の「公開」の行を直す(行数は同じ)、§9-13。0a36c34 |
| 2026-10-09 | obake-chochin | 難しさは指の遅れる bot で測る(0.6 秒遅れで 7 割 → 3 割) | `knowledge/game-design.md` 6 |
| 2026-10-09 | obake-chochin | platforms.md の itch.io「全自動」が誤解を生んだ(使用記録「食い違い」) | `knowledge/platforms.md` を「更新は全自動、初回のページ作成と secret は人間」に |
| 2026-10-09 | (他の repo) | kutsuzure・metopon・emmichy・game-llm・my-rss に新しい気づきなし。非公開 3 つは自動更新・企画書のみ。素材の追加なし | — |
| 2026-10-09 | (スプシ) | 値の 4 タブはコメント・☑ ともに記入なし。TIPS 3 件・用語 1 件(Claude Haiku 5.5)をスプシにも追記 | `tables/tips.csv`・`tables/glossary.csv` |
| 2026-10-10 | (非公開の作品) | 自動テストで曲の時計を差し替えるのは開始処理の後 | 雛形 `web-game-rules.md` §9-14・§8 |
| 2026-10-10 | (非公開の作品) | 物理合体の連鎖が隙間で切れる → 生まれる位置を寄せる | `knowledge/game-design.md` 7 |
| 2026-10-10 | (非公開の作品) | 考えて置く bot と適当に押す bot を同時に測る(3 本目の作品で同じ結論) | `knowledge/game-design.md` 6 を直した。格上げの保留「雛形に bot 比較の道具」を後押し |
| 2026-10-10 | (他の repo) | 公開の作品(おばけ提灯・metopon・emmichy・game-llm 等)に新しい気づきなし。非公開の MOD・企画書・自動更新にも全体向けなし。素材の追加なし | — |
| 2026-10-10 | (スプシ) | 値の 4 タブはコメント・☑ ともに記入なし。TIPS 3 件・用語 1 件(Claude Motion) | `tables/tips.csv`・`tables/glossary.csv` |
| 2026-10-11 | (全体) | 新しい気づき 0 件(非公開の MOD・企画書は作品固有の話のみ。公開の作品に追記なし)。my-rss は直したあと成功が続く。スプシのコメント・☑ なし。AI知見 10-11 は収集失敗(本文まで読めた記事 0 件)で TIPS・用語 0 件。格上げ 0 件 | — |
| 2026-10-12 | emmichy | Issue から呼ぶ Claude(Actions)が調べ物をしても、許可が無く Web を取れない。「迷ったら仮決め」の決まりのせいで、調べた事実まで推測で埋めかけた | 雛形の `.github/workflows/claude.yml` に GitHub の閲覧の許可と「調べ物の事実は推測で埋めず不明と書く」を入れた(**今日の格上げ**、雛形 1f81f0a)。`env-gotchas.md` |
| 2026-10-12 | (知識カード 1〜10 枚目) | ピース 2 個(台詞の間を操作で守る・移動そのものを技にする)。LLM による QA 自動化の講演 5 枚は、ピースでなく AI テストプレイの型として `process-patterns.md` 6 に足した | `tables/pieces.csv`・`process-patterns.md` |
| 2026-10-13 | obake-chochin | 同じ道の敵を足すとまとめ倒しが増えて易しくなる。別の向きから来る組 + 間隔で難しくする | `tables/pieces.csv` SH-011(実測) |
| 2026-10-13 | obake-chochin | bot 100 回以下だと ±5 ポイント揺れる。案の比較は各 400 回 | `game-design.md` §6 |
| 2026-10-13 | obake-chochin | まとめ倒しは ×n 表示・音・30ms の止めで連鎖数と別に見せる。数えは中身のイベントに | `tables/pieces.csv` ACT-082(実測)、ACT-038 を実測に |
| 2026-10-13 | emmichy | スマホで文字入力を始めると絵が縮む(visualViewport の高さ比例・縦専用 CSS) | 雛形 `web-game-rules.md` §9-15 と §8 |
| 2026-10-13 | emmichy | LLM キャラは正確な知識 bot を先に作り、人格を上に重ね、別々に評価する | `ai-in-games.md` |
| 2026-10-13 | emmichy | テストが通っても楽しいとは言わない。評価の種類を分けて記録 | `tables/mindset.csv` |
| 2026-10-13 | emmichy | X の元投稿は 403、Threads・Instagram は公開検索で本文も反応も取れない | `env-gotchas.md` |
| 2026-10-13 | metopon | getGamepads を偽のパッドに差し替えると Playwright からコントローラを押せる | 雛形 `web-game-rules.md` §9-16 と §8 |
| 2026-10-13 | (非公開の作品 2 本) | 全要素モックは「デモ固定ルート」で全部に必ず出会わせ、自動テストで通す。作りかけは「ハリボテ」と表示。担当を分け、つなぎ口を先に決める | `process-patterns.md` §10 |
| 2026-10-13 | (非公開の作品) | 版権ものは ID に原作の名前を入れず役割の語にする(差し替えやすく) | `process-patterns.md` §10 |
| 2026-10-13 | kutsuzure・(非公開の作品) | 使った素材: ChatGPT の画像生成、ローカル画像生成(Animagine XL 4.0) | `tables/used-assets.csv` |
| 2026-10-13 | (AI知見) | TIPS 3・用語 1(Claude Code の更新)。雛形への格上げ 0 件(出典 1 つ) | `tables/tips.csv`・`glossary.csv` |
| 2026-10-13 | (スプシ) | コメント・わかったチェックとも 0 件。育成プログラム「関連リンク」A1 が #REF! | 報告のみ |
| 2026-10-14 | ImoteControllDandy | 曲のオマージュの線引きと、似すぎの測り方(音程の動き + リズム、8 音一致で書き直し) | `process-patterns.md` §11 |
| 2026-10-14 | ImoteControllDandy | Suno の商用条件(生成時に有料プラン)、ComfyUI の API テンプレートは有料、PLATEAU で実在の街 | `tables/assets.csv`・`local-ai.md` §7 |
| 2026-10-14 | ImoteControllDandy | 生成 AI に入れるのは自分のラフだけ、LoRA は商用可のみ | `tables/mindset.csv` |
| 2026-10-14 | ImoteControllDandy | 昭和アニメ風の仕上げを 1 枚のシェーダーで | `tables/pieces.csv` ALL-085(実測) |
| 2026-10-14 | ImoteControllDandy | 使った素材(Kenney City Kit・VRM サンプル・VOICEVOX 2 人・効果音ラボ・Tripo・Dela Gothic One) | `tables/used-assets.csv` |
| 2026-10-14 | emmichy・game-llm | LLM の構造化出力の崩れ、429 で再試行を止めてオフライン再生、気持ちと事実を分ける | `ai-in-games.md` |
| 2026-10-14 | emmichy | Cloudflare 公開直後は一部のファイルが古い | `env-gotchas.md` |
| 2026-10-14 | emmichy | キーボードで絵を動かさず顔中心に固定、アプリ内ブラウザの初回案内 | 雛形 `web-game-rules.md` §9-15・§9-8 に追記 |
| 2026-10-14 | (非公開の作品 2 本) | 合意してから作らせる、監修用の画面写真を自動で撮る、社内版と外向け版を 1 つの元から、試遊の感想の 1 行形式、JSON Schema を添える | `process-patterns.md` §10 |
| 2026-10-14 | (非公開の作品) | 既存ゲームの MOD の画面写真と描画順の罠 | `env-gotchas.md` |
| 2026-10-14 | (AI知見) | ピース候補 10 → 8 個(手触り補助・放置の転生と新通貨・デッキ構築の演出と地図・AI テストプレイ)。TIPS 3・用語 2。Gemini 4 Argon の一般公開で ai.csv を直した。格上げ 0 件(出典 1 本) | `tables/` 各所 |
| 2026-10-14 | (スプシ) | コメント・わかったチェックとも 0 件 | — |
| 2026-10-15 | game-creator-life | 小ネタは 1 人生 2 回まで、イベントに時代の鍵、並走する他人は bot で | `tables/pieces.csv` MNG-015〜017(実測) |
| 2026-10-15 | game-creator-life | ファイルを分けたサブエージェント並列、bot のログを文字で通読、司令塔を 2 つ立てない、数値の置き場は 1 本 | `process-patterns.md` §10 |
| 2026-10-15 | game-creator-life | 実名を笑いに出す前に後年の不祥事まで調べる | `tables/mindset.csv` |
| 2026-10-15 | game-creator-life | 魔王魂の効果音は説明で選べる(古い記述を直した)、ぴぽや・効果音ラボはクラウドから 403、AUTOMATON は読めない | `tables/assets.csv`・`env-gotchas.md` |
| 2026-10-15 | game-creator-life | 和文の Web フォントは描く前に使う字を読ませる、iOS の音量は GainNode、日本語の折り返しで 1〜2 字だけ残さない | 雛形 `web-game-rules.md` §9-9・§9-17・§9-18 |
| 2026-10-15 | game-creator-life | 雛形の Cloudflare の公開が Pages 前提で初回に落ちる | 10/15 昼に雛形を Workers 方式へ直し済み |
| 2026-10-15 | (非公開の作品) | 紙芝居はデータで、見せるだけの分かれ道、Sheets は必要な列だけ読む | `pieces.csv` STO-025・`process-patterns.md`・`env-gotchas.md` |
| 2026-10-15 | game-creator-life | 使った素材: 魔王魂の BGM 8・効果音 19、DotGothic16 | `tables/used-assets.csv` |
| 2026-10-15 | (AI知見) | TIPS 3・用語 1。ピース候補は既出 3・取り込み済み 2。格上げ 0 件 | `tables/` |
| 2026-10-15 | (スプシ) | コメント・チェック 0 件。育成プログラム「関連リンク」A1 は #REF! のまま(Mukkii の手作業待ち) | — |
| 2026-10-15 | (Mukkii が持ち込み: PC Gamer の新作 Castlevania 評) | 操作の割り当てと手触りの地雷(トリガーに連打操作を付けない・溜めを短く・狙いを吸い付かせる・最初の回避は確実に・長押しの終わりを知らせる)、高リフレッシュの画面で壊れる | 雛形 `docs/knowledge/controls.md`・`test:replay` に 144/240Hz・`pieces.csv` ACT-087〜089 |

## 会議室の資料の使われ方

作品の HANDOFF の `会議室: <ファイル> / 評価` 行を夜の回収が書き写す。週の見直しで件数を見る。

| 日付 | 作品 | 読んだファイル | 評価 |
|---|---|---|---|
| 2026-10-06 | obake-chochin | knowledge/start-from-reference.md, tables/genres.csv | 役立った(元ネタは骨組みだけ借りる判断の根拠) |
| 2026-10-07 | obake-chochin | tables/genres.csv | 無かった(ミサイルコマンド系の行。足した) |
| 2026-10-08 | obake-chochin | topics/14-other-ai-routes.md, knowledge/local-ai.md, tables/assets.csv | 役立った(クラウドから ComfyUI に届かない・魔王魂と Kenney が使える) |
| 2026-10-08 | obake-chochin | tables/ai.csv | 無かった(クラウドの作品セッションで使える画像生成の手段。→ ai.csv に注記、topics/06 で鍵を用意中) |
| 2026-10-08 | kutsuzure | knowledge/process-patterns.md | 役立った(企画の多角審査をそのまま Workflow に。16 案 → 5 審査 → 3 案で 25 分) |
| 2026-10-08 | kutsuzure | tables/assets.csv | 役立った(Kenney・OGA を先に当たれた)。古かった: 効果音ラボ等はクラウドから通らない → assets.csv・env-gotchas に注記 |

| 2026-10-09 | obake-chochin | knowledge/platforms.md, tables/procedures.csv | 食い違い(itch.io の「全自動」。platforms.md を直した) |
| 2026-10-10 | (非公開の作品) | tables/assets.csv, genres.csv | 役立った(画像生成の推奨、パズルは素の canvas + 自作ロジックが向く) |
| 2026-10-13 | obake-chochin | genres/shmup.md(§4) | 役立った(速さより数と並びで難しくする) |
| 2026-10-13 | obake-chochin | tables/pieces.csv | 無かった(まとめ倒し専用のピース → ACT-082 を足した) |
| 2026-10-15 | game-creator-life | start-from-reference.md | 役立った(芯を仕組みに分けて合体、を PLAN の骨に) |
| 2026-10-15 | game-creator-life | game-design.md §6・§8 | 役立った(原理でひねりの狙いを書けた。bot で同じ小ネタの連発などを数字で発見) |
| 2026-10-15 | game-creator-life | process-patterns.md §1・§6・§10 | 役立った(3 案から絞る、つなぎ口を先に固定して 4 パート同時) |
| 2026-10-15 | game-creator-life | genres/README.md | 役立った(層の考え方)。人生シミュの 1 枚は無かった |
| 2026-10-15 | game-creator-life | tables/pieces.csv | 一部役立った。人生シミュ・ランダムイベントのピースが薄い → MNG-015〜017 を足した |
| 2026-10-15 | game-creator-life | tables/refs.csv | 無かった(人生シミュの参考コード。ink / inkjs が候補) |
| 2026-10-15 | game-creator-life | tables/assets.csv | 役立った(魔王魂の取り方)。古かった: 魔王魂の効果音の記述、ぴぽやの 403 → 直した |

## 格上げの保留

週の見直しが判断する。

| 日付 | 出所 | 候補 | 保留の理由 |
|---|---|---|---|
| 2026-10-08 | obake-chochin | CI からブラウザ確認を外し(約 76 秒 → 30 秒)、手元の確認を「毎回 tsc・build・bot / 描画を変えた時だけブラウザ / 文書だけは build」に分ける。雛形の build-and-deploy.yml と AGENTS.md へ | 1 作品の実測のみ。人が直接 push した時にブラウザ確認が抜ける |
| 2026-10-08 | obake-chochin | 雛形に絵の差し替えの道(キー → 画像の manifest + ComfyUI 一括 + 背景抜き、作品の tools/art/) | 鍵の経路(topics/06)と合わせて決める |
| 2026-10-08 | obake-chochin | 雛形の tools/sim.mjs に「面ごと・やり方ごと」の bot 比較 | 雛形に sim.mjs がまだ無い。probe.ts の上に作るか要検討 |
| 2026-10-09 | obake-chochin | 雛形 AGENTS.md の「終わったら HANDOFF を更新」を「push のたびに HANDOFF の現状を 1 行直す(該当行だけ)」に。十数回分ずれた実例あり | 指示の文の変更。今日の格上げ枠は OGP に使った。週の見直しで判断 |
| 2026-10-09 | obake-chochin | 雛形の sim に「指の遅れる bot」を既定で並べる(10/8 の「面ごと・やり方ごとの比較」と同じ道具の話) | 雛形に sim.mjs がまだ無い。probe.ts の上に作る時に合わせて |
| 2026-10-10 | 3 作品 | 「やり方の違う bot を並べて比べる道具」を雛形に(おばけ提灯・くつずれ・非公開 1 本で同じ結論。10/8・10/9 の保留と同じ話) | **条件は満たした**(複数の作品で同じ結論)。ただし雛形の見本シーンは中身と描画が分かれておらず、作るには見本の作り直しが要る。週の見直しで「作るか」を決める |
| 2026-10-12 | 会議室 | shmup.md の 5 節(攻略パターン・敵の組み合わせ)を pieces.csv に `SH-` で 15〜25 個起こす | 夜の回収で 1 日 10 個まで(10/15 に SH-027 まで済み。§5 は出し切った) |
| 2026-10-12 | 会議室 | `_families.md`・game-design §8 の記憶だけで書いた数値(Celeste のコヨーテタイム、ヒットストップのフレーム数)と講演 2 本(Into the Breach の振り返り、Pecorella の放置ゲームの数学)の実在を Web で確かめる | 週次レビューで |
| 2026-10-14 | AI知見(note 1 本) | 雛形の依頼に「手触りの補助」(コヨーテ・先行入力・判定の大小・最初の一発・最後の一撃)の一覧を入れる | 出典 1 本。genres/platformer・shmup にはある。作品で効いたら入れる |
| 2026-10-15 | game-creator-life | genres/人生シミュ(ランダムイベント型)を起こす。refs.csv に同じ型の参考コード(ink / inkjs など)を足す | 週次レビューで(1 週 1 枚) |
| 2026-10-15 | game-creator-life | 雛形 AGENTS に「始める前に同じ repo で動いているセッションが無いか確かめる」 | 1 件のみ。会議室側の手順(前のセッションを止めてから立てる)で先に防ぐ |

週の見直し 2026-10-12 の判断: bot 比較(10/8・10/9・10/10 の 3 行)は**作る**(見本シーンを中身と描画に分けてから `tools/sim.mjs`)。HANDOFF を push ごと(10/9)は**格上げ済み**(雛形 1106276)。CI の軽重分け・絵の差し替えの道は保留のまま。

2026-10-12 追記: bot 比較の道具は**入れた**(雛形 55f4c2b。`src/game/logic.ts`・`bots.ts`・`npm run sim`。あわせて 1/60 秒刻みにして、60Hz と 120Hz で結果が同じになることを test:replay で確かめる)。

知識カードのピース化: 40 枚目まで(ファイル名順。2026-10-12 の初回はジャンル別に約 450 枚を読んで 304 個にした。夜の回収は重複を飛ばしながら先頭から進める)
- 2026-10-16: X(iritec_jp 経由の Sac 氏の記事)AI で 3D ゲームを作る流れ → process-patterns §12、assets に Auto-Rig Pro・Unity 公式 MCP を監視で追加。翌週の GitHub 公開を見て、コードが出たら refs.csv に足すか判断
- 2026-10-16: 仕事の案件(デッキ構築の MOD・仕様書)を初回まとめて回収(Mukkii 指示で以後も毎晩対象)→ env-gotchas に MOD の罠 15 項目と Windows パスの罠、process-patterns §13(大きな仕様書を AI とまとめる)と §9・§10 の追記、sheet-style に仕様書の色と書き方、genres/roguelike に B 型の設計 6 項目、start-from-reference に jar 解析の実測。固有名は伏せた。非公開 3 repo は手元に無く未読
- 2026-10-16: X(my_syumi_game、欧米ゲームデザイン理論の用語が AI 動画で広まる話)→ 照合: 緩急・手応え・ゲームフローは既にあり。コアループ・視線誘導・タメツメフォロースルーを game-design.md §8 の原理に追加、英語名の対応を付けた
