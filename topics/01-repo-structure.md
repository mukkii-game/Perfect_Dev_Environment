# 01 repo 構成・命名

## 現状の結論(推奨案、未確定)

GitHub 上に以下の repo 群を持つ。

| repo | 役割 | 備考 |
|---|---|---|
| `Perfect_Dev_Environment` | 作戦会議室(この repo) | コードなし |
| `dev-template-web-game` | 作品 repo の雛形(2D Web) | GitHub の「Template repository」機能で 1 クリック複製 |
| `dev-template-web-3d` | 雛形(3D Web) | 第 2 波以降 |
| `dev-template-app` | 雛形(ゲーム以外のツール・アプリ) | |
| `dev-engine` | 自分専用の薄い Web エンジン | npm パッケージ or CDN 配信。作品 repo から参照 |
| `dev-tools` | 公開自動化、素材取得、翻訳などの汎用ツール | Python / GAS / バッチ / Actions の再利用ワークフロー |
| `dev-knowledge` | ノウハウ・ライブラリ索引・素材索引(人間も読む) | スプシと併用。会議室から分離するかは 07 で決める |
| `game-<slug>` / `app-<slug>` | 作品 | 雛形から生成。公開先の URL を README に持つ |

雛形 repo に入れるもの(案):

- `AI_RULES.md`(正本)と、それを参照するだけの `CLAUDE.md` / `AGENTS.md` / `GEMINI.md`(→ 02)
- `SPEC.md`:企画メモ。数行でよい。AI はここから作り始める
- `.github/workflows/`:ビルド → GitHub Pages 公開(プレビュー URL を自動で返す)、公開ジョブ(→ 05)
- `dev-tools` の再利用ワークフローを呼ぶだけの薄い定義
- `docs/PUBLISH.md`:日英の説明文、スクショ置き場。公開ジョブが読む

命名: すべて小文字ハイフン。作品は `game-` / `app-` 接頭辞で GitHub 上の一覧が自然にソートされる。

## 2026-09-13 追記(既存資産の反映と Q&A)

- 雛形は **既存の `web-app-template` を土台に軽量化**して使う。ゼロから作らない。repo 作成は `ai-ops/bootstrap-web-repo.sh` の経路が実証済みなので、そこを「1 コマンドで新作を生やす」の実体にする。
- **エンジンの参照方法(Q: CDN / npm とは何か)**: npm 公開 = ライブラリを npm レジストリに登録し `npm install` で入れる方式。手間と版管理が要る。CDN 直参照 = GitHub 上のファイルを jsDelivr 等が配信し、HTML の `<script src>` 1 行で読む方式。手間ゼロだが外部依存。**パイロット速度優先なら第 3 案「雛形に同梱(コピー)」が最も単純**。エンジンが育ってから CDN に移す。→ 推奨を (d) 同梱に変更。
- **public → private への切替(Q)**: いつでも GitHub の設定 1 つで可能。注意 2 点。(1) GitHub Free では private repo の Pages は使えない(Pro 以上が必要)。製品化で private にした作品は Pages 以外の配信先に移す。(2) Free の private 個人 repo ではルールセットが効かない(ai-ops の記録より)。パイロットは public、製品化で private + 必要なら Pro、という運用で問題ない。
- **Unity / UE も同 repo 内で良いか(Q)**: Godot は同 repo の `godot/` で問題ない(テキスト中心、軽い)。Unity / UE はバイナリが巨大で Git LFS が必要になり、Web 版の CI と衝突しやすい。**Unity / UE に移す時は別 repo(`game-<slug>-unity`)** を推奨。同 repo は Godot まで。

## 検討中の論点

1. エンジンを作品 repo からどう参照するか。候補: (a) npm 公開、(b) GitHub Packages、(c) CDN(jsDelivr の GitHub 直参照)、(d) テンプレート複製時にコピー。速度重視なら (c) or (d)。バージョン固定と更新のしやすさで (c) を仮推奨。
2. GitHub 無料枠で足りるか。Actions 分数(private だと月 2,000 分)は、1 日 1 本ビルド+公開なら余裕。作品を public にすれば無制限。**作品 repo は原則 public** を推奨(itch.io 等に出すものは隠す理由が薄い)。
3. 作品の「卒業」(Godot 等で作り込む段階)は同じ repo 内に `godot/` を切るか、別 repo にするか。
4. Google Drive の役割分担: ビルド成果物の保管、大容量素材、過去作アーカイブ。repo にはリンクと索引のみ。

## 調べたこと

- (未着手)GitHub Template repository の制約、jsDelivr の GitHub 参照の仕様、Actions 無料枠

## 次にやること

- [ ] 論点 1〜4 をユーザーと確認
- [ ] 決定後、`dev-template-web-game` の中身一覧を decisions に固定し、実行部隊に「雛形 repo を作れ」と出す
