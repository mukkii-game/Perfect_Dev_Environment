# 04 自分専用 Web エンジン・過去作の棚卸し

## 現状の結論

- 方針: ゼロから作らず「既存ライブラリ + 薄い自前層」。自前層は毎回必ず要るものだけ(入力、シーン、セーブ、音、日英切替、タイトル、公開メタ)。
- 過去作で作った Python / GAS / エンジン的コードは棚卸しして、汎用部分を取り込む。世に落ちているものの方が早ければそれを拾う。

## 2026-09-13 決定

decisions/2026-09-13-engine-defaults.md: 2D Phaser 3、3D はアクション性が高ければ Babylon.js、見せるのが主なら Three.js、作り込みは Godot 4。

## 検討中の論点

1. 2D = Phaser 3、3D = Three.js で良いか(AI が最も正確に書けるという理由)
2. 「凝りたいもの」を Godot 4 に移す前提で良いか(無料、Web 書き出し、テキストシーン)。Unity / Unreal は Web 向きでないので後回し
3. 過去作の所在(GitHub / Drive / ローカル)と、どれを棚卸し対象にするか
4. エンジンの配布形態(→ 01 論点 1)

## 調べたこと

- 2026-09-13: 過去作は全部 GitHub org `mukkii-game` にある(47 repo)。作品 repo の一覧は research/2026-09-13-existing-infra-inventory.md。Unity 系(Unity2D_TD)、GAS 系(gas-plannning-sheet, GAS-Plannning-sheet)、Web 系多数。

- (未着手)候補ライブラリ比較、Godot Web 書き出しの現状

## 次にやること

- [x] 過去作の所在: GitHub org 全部
- [ ] 作品 repo 約 35 本を子セッションで一括スキャンし「共通化できる部品」「使った外部ライブラリ」「ジャンル」を表にする
- [ ] 棚卸し用チェックリストを作る(何を見て、何を残すか)
