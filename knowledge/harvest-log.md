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

## 会議室の資料の使われ方

作品の HANDOFF の `会議室: <ファイル> / 評価` 行を夜の回収が書き写す。週の見直しで件数を見る。

| 日付 | 作品 | 読んだファイル | 評価 |
|---|---|---|---|
| 2026-10-06 | obake-chochin | knowledge/start-from-reference.md, tables/genres.csv | 役立った(元ネタは骨組みだけ借りる判断の根拠) |
| 2026-10-07 | obake-chochin | tables/genres.csv | 無かった(ミサイルコマンド系の行。足した) |
