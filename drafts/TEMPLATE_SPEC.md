# 雛形 repo `game-template-web` の中身(01 最終形、v1.0 案)

> 実行部隊への発注書。決定(2026-09-13)に基づく。これが完成したら「Use this template」→ SPEC.md を書く → push の 3 手で新作が公開される状態になる。

## 土台
- Phaser 公式 `phaserjs/template-vite-ts`(Phaser 4、Vite、TypeScript、MIT)をフォークではなくコピーして起点にする。
- Vite の `base` は `./`。ビルド出力 `dist/`。
- Node は LTS。`package-lock.json` をコミット。

## ディレクトリ
```
AGENTS.md              全 AI 共通の作法(drafts/AGENTS.md v0.3)
CLAUDE.md              「@AGENTS.md」の 1 行
SPEC.md                企画。人間が書く。数行でよい。冒頭に「読む追加ルール」欄
QUESTIONS.md           AI が仮決めした事項と人間への質問を溜める場所
DECISIONS.md           設計判断の追記専用(3 行ずつ)
HANDOFF.md             次のセッション(別 AI 含む)への引き継ぎ。現状・次の一手・既知の問題
CREDITS.md             使った素材の出典・規約・クレジット文。空でも置く
LICENSE                2 段書き: コードは MIT、assets/ と自作の絵・音・文は All rights reserved
docs/PUBLISH.md        公開用テキスト(日英): タイトル、一言、説明、操作、タグ。公開ジョブが読む
src/
  main.ts              Phaser 起動。core を組み込む
  core/
    save.ts            名前空間つき localStorage、DEFAULTS マージ、版番号、try/catch
    i18n.ts            key → {ja, en}、言語の永続化、?lang= で切替
    audio.ts           ミュート永続化、最初の操作で unlock、合成音のフォールバック
    input.ts           キー + ポインタ + ゲームパッド統合、左右半面ドラッグ/タップ
    demo.ts            ?auto=1 で自動プレイ(宣伝動画・CI 確認用)。作品側が update() を実装
    meta.ts            base パス、バージョン、ビルド日時
  scenes/
    Boot.ts Title.ts Play.ts Result.ts   最小の 4 シーン。Title に言語・ミュート切替
  ui/touch.ts          仮想ボタン(スマホ)
public/                favicon、OGP 画像の雛形
assets/                素材。inbox/ は未整理、使ったものだけ assets/ 直下へ
tools/
  check.mjs            Playwright: 起動 → 60 秒エラーなし → スコア変動 → スクショ 3 枚(dist を対象)
  record.mjs           Playwright 録画で ?auto=1 を 60 秒 → tools/out/*.webm
  promo.sh             ffmpeg: 録画 + タイトル + 日英字幕 + CC0 BGM → 15 秒 / 60 秒
.github/workflows/
  build-and-deploy.yml main push → npm ci → build → tools/check.mjs → Pages 公開。失敗時はスクショを artifact に
  publish-itch.yml     workflow_dispatch(手動ボタン)→ dist を butler で itch.io html5 チャンネルへ。secret は BUTLER_API_KEY
.claude/skills/        `npx skills add phaserjs/phaser` と gamedev-skills を導入した状態をコミット(Codex / Gemini も同じ内容を読む)
.gitignore             node_modules, dist, tools/out, assets/inbox, .env
```

## 作法(AGENTS.md に含める。ここは要点のみ)
- 止まらずゴールまで。仮決めは QUESTIONS.md へ。複数案は variants/。
- 素材は CC0 優先、CREDITS.md 必須。
- 公開前に docs/PUBLISH.md を日英で埋める。
- `.github/` を変える時は理由を QUESTIONS.md に書いてから。

## repo 作成時に自動で付くもの
- Topics: `game`, `web`, `phaser`(ジャンルは SPEC から後付け)。
- 説明文: SPEC.md の 1 行目。
- Pages 有効化(Actions 経由)。

## 受け入れ条件(実行部隊の完了判定)
1. template から新 repo を作り、SPEC.md に 3 行書いて push すると、5 分以内に Pages で遊べる。
2. tools/check.mjs が CI で通り、スクショが artifact に残る。
3. ?auto=1 でデモが走り、record.mjs で webm が出る。
4. ?lang=en で英語表示、リロードしても保持。
5. itch.io へ手動ボタン 1 回で公開できる(BUTLER_API_KEY を入れた状態で検証)。
6. AGENTS.md は 80 行以内、SPEC.md の雛形は 15 行以内。

## やらないこと(パイロット用)
- 型検査の強制、単体テスト、E2E の網羅、PR、自動マージ、ルールセット、セキュリティ監査。
