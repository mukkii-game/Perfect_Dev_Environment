# 作品づくりのノウハウ索引(どこに何があるか)

「◯◯を作る時、何を見ればいいか」を 1 枚で。中身は各ファイル。ジャンルに固有の話は `genres/`、どのジャンルでも効く話はそれ以外。

| 知りたいこと | ジャンル固有 | どのジャンルでも |
|---|---|---|
| よく使うアセット(絵・音) | `genres/<ジャンル>.md` の 7 | `tables/assets.csv`(道具と素材の総合表)、`tables/used-assets.csv`(うちで使った素材と評価)、`catalog-tools.md` |
| よく使う UI | `genres/` の 6 | 雛形 `docs/knowledge/web-game-rules.md`(スマホ・入力・iframe)、`knowledge/promotion.md`(見た目と OGP) |
| ゲームシステムとゲームフロー | `genres/` の 2 | `tables/genres.csv`(全ジャンルの必須要素の早見表) |
| データ構造 | `genres/` の 3 | 雛形 `src/game/logic.ts`(中身と描画の分離・1/60 秒刻み)、`src/core/`(乱数・記録と再生・調整つまみ) |
| ゲームバランスの指針 | `genres/` の 4 | `game-design.md`(手応えと難しさ・近い目標・何もしないで勝てる穴)、雛形 `src/tuning.ts` と `npm run sim`(ボット比較) |
| 攻略パターン・敵の組み合わせ・レベルデザイン | `genres/` の 5 | `game-design.md` |
| 元ネタから作り始める | `genres/` の 8(参考 URL) | `start-from-reference.md`(下調べ 15 分の手順・ライセンス・逆解析) |
| 進め方・AI への頼み方 | — | `process-patterns.md`、`codex-handoff.md` |
| 実機で踏んだ罠 | `genres/` の 9 | 雛形 `docs/knowledge/web-game-rules.md` の §8(症状→原因の逆引き)・§9、`env-gotchas.md` |
| うちの作品の振り返り | `genres/` の 9 | `progress/*postmortem*`、`harvest-log.md`(作品から回収した気づきの台帳) |

**ゲームデザインの知識の蓄積**(講演・記事の要約 2,200 枚超)は非公開の知識 repo にあり、毎朝自動で集まっている。作品から直接は読まない。会議室が `genres/` と `game-design.md` に要約して移す。
