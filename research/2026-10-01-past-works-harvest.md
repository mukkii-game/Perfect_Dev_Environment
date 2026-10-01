# 過去作に埋もれたノウハウの回収(2026-10-01)

Galaxtris に「持ち出し用」の 1,565 行が眠っていた件を受けて、他の作品も洗った。

## 対象と方法

- **公開 repo 26 本**を浅く取得し、`.md` を行数順に並べ、「ハマ・罠・原因・解決・iOS・失敗」などの語で絞って読んだ。読むだけで、どの repo も書き換えていない。
- **private repo 13 本は未調査**(Otra、charge-and-anchor-gdd、SlayTheSpireLike、PilotMod、Orejanakya ほか)。必要なら個別に接続して読む。

## 結果

大半(約 20 本)は**その作品専用の企画書・仕様書**で、持ち出す種類のものではなかった。
汎用のノウハウは 6 件。

| # | 中身 | 出所 | 入れた先 |
|---|---|---|---|
| 1 | iPhone のサイレントスイッチで Web Audio だけ鳴らない → 無音の `<audio>` をループ | NeoSoukoban | 雛形 web-game-rules §9-1(**実機未確認**。確認できたら `audio.ts` へ 0 層化) |
| 2 | やり直し後に古い `setTimeout` が新しい状態を壊す → 世代カウンタ | NeoSoukoban | 雛形 §9-2 |
| 3 | スマホで横画面を強制(orientation.lock、iOS は CSS 回転と座標補正、PWA) | ImoteControllDandy | 雛形 §9-3 |
| 4 | ヘッドレスブラウザでスクショ後に rAF が凍結 | panzer-tokoron | 雛形 §9-4、env-gotchas |
| 5 | Tripo + Mixamo で 3D キャラ、GLTFLoader が骨名の `:` を落とす | ImoteControllDandy | catalog-tools(3D) |
| 6 | **GGJ2026-MASK は Godot 4.6 製**。Godot の実績があった | GGJ2026-MASK | engines |

## 気づいたこと

- **NeoSoukoban の DEVELOPMENT_LOG.md(1,360 行)は良い記録の型**。版ごとに「症状 → 原因 → 修正 → どう確かめたか → 実機で未確認な点」を書いている。ノウハウが回収しやすいのは、この形で書かれたものだった。
  → 雛形の `HANDOFF.md` の「ハマったこと」欄も、この 5 項目の形にするとよい(次の改善候補)。
- 「持ち出し用」と明示されたファイルは Galaxtris 以外になかった。今回の 6 件は、**作品の開発記録の中に混ざっていた**のを拾ったもの。
