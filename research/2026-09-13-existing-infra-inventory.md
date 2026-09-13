# 既存資産の棚卸し(mukkii-game org、2026-09-13 時点)

出典: https://github.com/mukkii-game(47 repo)、セッション「Web app共通GitHub Actions基盤」(session_013QYmJuNe564wCoQgPScjHX)

要点 3 行:
- 環境系 repo が既に 5 つある。CI/公開基盤(ai-dev-infra)、雛形(web-app-template)、repo 作成自動化(ai-ops)、知識工場(gd-knowledge)、企画スプシ GAS(gas-plannning-sheet)。
- Yasu で「雛形 → repo → CI → 自動マージ → Pages → itch.io」の全自動経路が実際に動いた。ユーザー評価は「公開自動化は良い、それ以外は重すぎた」。
- gd-knowledge は 4,629 ファイル、カード 2,281 枚。収集は Actions で無人稼働、加工は AI の 3 階層(司令塔 / 現場監督 / 作業員)。

## 環境系 repo

| repo | 公開 | 中身 | 会議室での扱い |
|---|---|---|---|
| ai-dev-infra | public | 再利用ワークフロー 4 本: verify-web(tsc/vitest/build/playwright)、merge-guard(自動マージ)、deploy-pages、publish-itch(butler)。DECISIONS.md に設計判断 7 件 | **踏襲**。ただし軽量化(05・08) |
| web-app-template | public | Vite+TS の雛形。AGENTS.md が正本、CLAUDE.md は `@AGENTS.md` の 1 行。SPEC.md / DECISIONS.md / e2e smoke | **土台として再利用**(01・02) |
| ai-ops | private | `bootstrap-web-repo.sh`: 雛形から repo 作成 → ルールセット → PR → Guard → CI → bot マージ → Pages まで検証。PAT 必要 | 「新作を 1 コマンドで生やす」の実体候補(01・08) |
| gd-knowledge | private | RSS 15 / CEDiL / YouTube 7ch を毎朝収集(collect.yml)。carder/curator/critic/scout/snipper のエージェント定義。STATUS.md で人間向け現況 | 07 の先行実装。**同じ型を AI ノウハウ・ライブラリ索引にも適用できる** |
| gas-plannning-sheet | private | スプシを方眼キャンバス化、Markdown 入出力、画像配置。clasp でデプロイ | 08 の GAS 資産。企画メモ → SPEC の入口候補 |

## Yasu セッションから得た教訓(ユーザー評価)

- 失敗: チェック時間が異常に長い。パイロット版に過剰なセキュリティ検査。md と文脈の肥大化でトークン増(そのセッションだけで約 $505 相当、73 万トークン使用)。
- 失敗: Codex を無理にクラウド対応させた。Claude は元からクラウドが充実。GPT 側を使いたい時は Codex ではなく、ChatGPT 側のクラウド実行機能を使う決まりにすれば「クラウド共通化ルール」自体が不要だったかもしれない。
- 成功: itch.io と Pages の自動公開は楽。踏襲する。

## ai-dev-infra の設計判断で会議室が引き継ぐべきもの

- 「1 人 + AI」では安全弁がマージの手間を増やすだけ。2026-09-04 に immutable tag と canary を廃止し `@main` 参照に戻した(過剰品質から軽量化へ既に舵を切っている)。
- 残した原則: fork 拒否、書き込み権限のある runner ではチェックアウトしない、secret は明示、Pages と itch の認可ゲートは同一。

## 過去作 repo(作品側、棚卸し対象)

public: youjo, ImoteControllDandy, -Navier-Stokes, minogashi-game, ttekoto, tetrishoot(er), GGJ2026-MASK, weed, the-short-walk, Yasu, bolero_ball, sayounara, OneWordHorrorNovel, marshmallow-build-demo, panzer-tokoron, rare-earth-demo, CassetteVisionGame, CEDEC-HEAT-DASH-2026(+fable), my-butsukari-ojisan, known-quest-demo, NeoSoukoban, doroneko
private: charge-and-anchor-gdd, PilotMod, Orejanakya, slayers-ip-reference, SlayTheSpireLike, ENG_App, CasterMod, marshmallow-build, cursed-labyrinth-base, My-project, PanzerTokoron, fb-radio-auto, GGJ2025
fork: SoundGameOchiru, Unity2D_TD

関連 topic: 01, 02, 04, 05, 07, 08
