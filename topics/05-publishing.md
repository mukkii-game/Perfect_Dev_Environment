# 05 公開の自動化

## 現状の結論

- 公開先: itch.io、DLsite、BOOTH、pixiv、note(参考: https://note.com/kakasi4423/n/n75ec8e897da7)、X。Steam / App Store / Google Play は時々。家庭用機は後回し。
- 日英の説明文・一言コメントまで自動で作る。

## 検討中の論点

1. **自動化の可否(現時点の見立て)**
   | 公開先 | 手段 | 見立て |
   |---|---|---|
   | GitHub Pages | Actions | 完全自動 |
   | itch.io | 公式 CLI butler | 完全自動 |
   | note | 公式 API なし | 記事本文を生成し、人間が貼る |
   | X | API 有料 | 投稿文生成 + 手動、または低額 API |
   | BOOTH / DLsite / pixiv | API なし | パッケージ・説明文・画像を全部用意し、人間がアップロードのみ |
   | Steam | Steamworks SDK / steamcmd | 自動化可だが後回し |
2. 「公開パッケージ」の標準形を決める(zip 構成、スクショ枚数とサイズ、アイコン、説明文の長さ別バリエーション)
3. 公開の承認は誰がどこで押すか(GitHub の手動トリガー、スマホから)
4. 上記 note 記事の内容を研究に取り込む

## 宣伝動画の自動生成(ユーザー要望 2026-09-13)

- できる。流れ: 自動プレイ(既存の cedec-fable `tools/autoplay.mjs` や panzer-tokoron の soak ツールが元)→ Playwright の録画機能で動画取得 → ffmpeg でタイトル・字幕(日英)・BGM(CC0)を合成 → 15 秒 / 60 秒の 2 種類を出力 → itch.io のページ、X、YouTube(API で投稿可)に配る。
- 必要なもの: 作品側に「自動プレイ用の入力スクリプト or デモモード」を雛形の作法として持つ(AGENTS.md に「`?auto=1` でデモが走る」を既定にする)。
- 映像生成 AI は使わない(06 の方針)。録画 + 編集の定型処理だけで作る。

## 調べたこと

- 2026-09-13: Pages と itch.io の自動公開は ai-dev-infra の deploy-pages.yml / publish-itch.yml で実証済み(Yasu)。ユーザー評価「楽だった、踏襲」。上の表の 2 行は「実装済み」。

- (未着手)

## 次にやること

- [ ] note 記事を読んで要点を research/ に保存
- [ ] 公開パッケージ標準形の案を書く
