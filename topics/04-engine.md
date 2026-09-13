# 04 自分専用 Web エンジン・過去作の棚卸し

## 現状の結論

- 方針: ゼロから作らず「既存ライブラリ + 薄い自前層」。自前層は毎回必ず要るものだけ(入力、シーン、セーブ、音、日英切替、タイトル、公開メタ)。
- 過去作で作った Python / GAS / エンジン的コードは棚卸しして、汎用部分を取り込む。世に落ちているものの方が早ければそれを拾う。

## 2026-09-13 決定

decisions/2026-09-13-engine-defaults.md: 2D Phaser 3、3D はアクション性が高ければ Babylon.js、見せるのが主なら Three.js、作り込みは Godot 4。

## 棚卸し結果(2026-09-13、research/2026-09-13-past-works-inventory.md)

- 作品 repo 41 本、実質の作品 25 本、Web 作品 21 本。技術は **素の canvas / DOM が 13 本で最多**、Vite+TS 6、Three.js 2、Phaser 1。AI に書かせると自然に「ライブラリなし + 自前の薄い層」に収束している。
- 毎回作り直している部品: WebAudio 合成音(18 作)、キー+タッチ統合入力(16)、タイトル→プレイ→リザルト遷移(15)、DPR 対応 resize(12)、localStorage セーブ(9)、ミュート(9)、仮想パッド(8)、文字送り(6)、純ロジック分離(5)、自動スクショ(5)。
- 日英切替は 1 本だけ、ゲームパッドも 1 本だけ。
- **engine/ に入れる候補**(実装がほぼ同形): input, audio, save, video, scene, i18n, text, 公開メタ。元になる実装は cedec-fable / CassetteVisionGame / panzer-tokoron / Yasu / rare-earth-demo に既にある。
- **入れない**: 物理・衝突・TileMap(Phaser か作品ごと)、3D 一式、拍同期、通信、Godot/Unity、パレット制約。
- 雛形の構成案: `src/core/`(上記 8 部品、ES Modules 単独で動く形)+ `src/game/` + `src/ui/touch` + `tools/shot, autoplay` + `docs/SPEC, HANDOFF, CREDITS` + AGENTS.md。文書は 3 枚で足りる(md 27 本の ENG_App は過剰)。

### エンジン既定の再検討(重要)

棚卸しの事実から、当日決めた「2D は Phaser」は実態と合っていない。**提案: 2D の既定は「素の canvas + 自前 core/」、Phaser 4 は物理・TileMap・大量スプライトが要る作品でだけ選ぶ。** 3D は Babylon / Three.js のまま。理由: 過去 21 本の 13 本がこの形で最速に出ており、core/ の 8 部品は既存コードから抽出できる。Phaser の skills(公式 28 本)は Phaser を選んだ日に読み込めばよい。

## 見直し候補(2026-09-13)

- 調査で公式テンプレと skills が **Phaser 4** 主流と判明。既定を Phaser 3 → 4 に変える提案(research/2026-09-13-borrowable-assets.md)。

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
