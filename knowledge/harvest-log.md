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

## 格上げの保留

週の見直しが判断する。

| 日付 | 出所 | 候補 | 保留の理由 |
|---|---|---|---|
| 2026-10-08 | obake-chochin | CI からブラウザ確認を外し(約 76 秒 → 30 秒)、手元の確認を「毎回 tsc・build・bot / 描画を変えた時だけブラウザ / 文書だけは build」に分ける。雛形の build-and-deploy.yml と AGENTS.md へ | 1 作品の実測のみ。人が直接 push した時にブラウザ確認が抜ける |
| 2026-10-08 | obake-chochin | 雛形に絵の差し替えの道(キー → 画像の manifest + ComfyUI 一括 + 背景抜き、作品の tools/art/) | 鍵の経路(topics/06)と合わせて決める |
| 2026-10-08 | obake-chochin | 雛形の tools/sim.mjs に「面ごと・やり方ごと」の bot 比較 | 雛形に sim.mjs がまだ無い。probe.ts の上に作るか要検討 |
