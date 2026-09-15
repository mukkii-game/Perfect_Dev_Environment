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

## itch.io 公開の実地(2026-09-14、tetrishoot → mukkii.itch.io/galaxtiris)

- 作品 repo に `publish-itch.yml` を 1 本足した(main push と手動実行で butler が dist を html5 チャンネルへ push)。ai-dev-infra 版から認可ゲートを外した最軽量版。雛形にこのまま入れる。
- 人間の手間の切り分け:
  | 作業 | 今後 |
  |---|---|
  | itch.io の作品ページ新規作成(API なし) | **毎作 1 回、人間**。入力内容は docs/PUBLISH.md から AI が用意し貼るだけ |
  | Metadata タブの Languages と AI 生成の申告 | 同上(ページ保存後に出る) |
  | BUTLER_API_KEY を secret に入れる | **不要にする**。アカウントで 1 つ。組織 secret か雛形作成時に自動設定 |
  | ワークフロー追加 | 不要。雛形に同梱 |
- itch.io の設定メモ(HTML ゲーム): Embed in page、Viewport はゲームの論理解像度(縦長 540×720 等)、Mobile friendly / Fullscreen / Auto start オン、Draft で保存 → butler push → Public。

## 同人 Web ゲーム公開場所の広げ方(2026-09-15、要規約再確認)

- 複数投稿は原則可(itch.io / Newgrounds / GameJolt / PLiCy / ふりーむ は非独占)。独占条項はコンテストや一部パブリッシャー系(CrazyGames, Poki 等)のみ。
- 2 段階運用: **全作品 → Pages + itch.io(自動)**。1 週間の反応を見て **手応えのあるものだけ → Newgrounds(英語圏)+ PLiCy か ふりーむ(日本語圏)**(半自動)。
- **2026-09-15 ユーザー判断: Newgrounds と PLiCy はブラウザ自動操作で投稿まで自動化する。** 明示的な禁止が見当たらないこと、審査に日数がかかることから、まず入れて問題が出たら考える方針。会議室の留意点(実行前に把握しておく): アカウント停止のリスクはゼロではない、UI 変更で壊れる、実行には PC が要る、ログイン情報の扱い。→ 対策として「投稿用の専用 Chrome プロファイルを人間が一度ログインしておき、スクリプトはそのプロファイルを使う(パスワードをスクリプトに持たせない)」「1 日の投稿数を絞る」「失敗したらリトライせず人間に報告」を設計に入れる。
- YouTube Playables は招待申し込み中。通ったら対象に追加。
- 場所別: Newgrounds = 自然流入最強、メダル / スコア API あり(組み込み可)。GameJolt = 同系小規模。PLiCy = 日本 HTML5、収益分配。ふりーむ = 審査あり日数要。夢現 = DL 型中心で効果薄。unityroom = Unity WebGL 専用(Godot 不可)。YouTube Playables = 招待制、対象外。
- dev-tools 候補:
  - `package_for.py <site>`: 各サイトの要件(zip 構成、画像サイズ、文字数)に合わせた一式を `tools/out/<site>/` に出力。
  - `post_newgrounds.mjs` / `post_plicy.mjs`: Playwright の persistent context(専用プロファイル)でフォームを埋めて送信。入力は `docs/PUBLISH.md` と `tools/out/<site>/`。結果 URL を標準出力に返す。失敗時はスクショを残して停止。
  - 実行場所は自宅 PC(ログイン済みプロファイルが要るため)。GitHub Actions からは動かさない。

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
