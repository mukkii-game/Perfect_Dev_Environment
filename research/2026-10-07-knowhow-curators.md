# ノウハウをまとめている人・資料(2026-10-07)

調べた範囲: AI でものを作る話(Claude Code・Codex・エージェント・文脈設計)と、ゲームデザイン・売り方。
`knowledge/sources.md` と `research/2026-09-13-borrowable-assets.md` に載っているものは除いた。
この環境は多くのサイトへ直接つなげない(egress で遮断)。確認は WebSearch・WebFetch・Mucky Reader の `read_web` で行った。
「確認」欄: ◎=中身を読んだ / ○=検索結果で存在と時期を確認 / △=名前のみ(要確認)。

## 3行まとめ
- AI 側の芯は **Simon Willison の Agentic Engineering Patterns**(章立ての生きた手引き)と **Anthropic Engineering ブログ**。どちらも一次情報で、教科書にそのまま入る。
- ゲーム側の芯は **How To Market A Game(Zukowski)**・**GameDiscoverCo**(売り方)、**Game Maker's Toolkit**(設計)、**Game Programming Patterns**(無料の本)。
- 両方をまたぐ良い人はまだ少ない。日本語は Zenn の topic(claudecode・gamedev)と CEDiL(CEDEC 資料庫)を入口にするのが現実的。

## まとめている人・資料(表)

| 名前 | URL | 誰 | 中身 | 更新 | 言語 | ライセンス | 使い道 | 確認 |
|---|---|---|---|---|---|---|---|---|
| Agentic Engineering Patterns | https://simonwillison.net/guides/agentic-engineering-patterns/ | Simon Willison | 原則・Git・サブエージェント・TDD・手動テスト・注釈付きプロンプト。デザインパターン本の形 | 2026-02 開始、章を追加中 | 英 | 著作権あり(引用のみ) | (1)(3)(4) | ◎ |
| Simon Willison's Weblog | https://simonwillison.net/ | 同上 | AI ツールの実使用メモ。毎日数本 | 毎日 | 英 | 同上 | (1) | ○ |
| Anthropic Engineering | https://www.anthropic.com/engineering | Anthropic | 文脈設計・エージェントの作り方・Claude Code の使い方の一次記事 | 月数本 | 英 | 引用のみ | (1)(3) | ◎(200 応答) |
| hesreallyhim/awesome-claude-code | https://github.com/hesreallyhim/awesome-claude-code | コミュニティ | スキル・フック・コマンド・オーケストレータの索引。5.5 万★、約 2000 コミット | 継続 | 英 | LICENSE あり(種類未確認) | (1)週1で差分 (4) | ◎ |
| Latent Space | https://www.latent.space/ | swyx・Alessio Fanelli | AI エンジニア向け。エージェント・道具の深掘りと対談 | 週数本 | 英 | 引用のみ | (1) | ○ |
| Addy Osmani(Substack / 本) | https://addyo.substack.com/ | Google の Addy Osmani | 仕様先行・小さく刻む・必ずテスト、の LLM コーディング手順 | 2026 も継続 | 英 | 引用のみ | (3) | ○ |
| 12-Factor Agents | https://github.com/humanlayer/12-factor-agents | HumanLayer | エージェントを壊れにくく作る 12 原則 | 2025 | 英 | 要確認 | (3)(4) | △ |
| Prompt Engineering Guide | https://www.promptingguide.ai/ | DAIR.AI | 技法の網羅カタログ | 継続 | 英・日あり | MIT(リポ) | (2)用語集 | △ |
| How To Market A Game | https://howtomarketagame.com/ | Chris Zukowski | Steam ページ・ウィッシュリスト・メール。週1メール。入門記事集あり | 週1 | 英 | 引用のみ | (1)(2)tips (3) | ◎ |
| GameDiscoverCo newsletter | https://newsletter.gamediscover.co/ | Simon Carless | 客がどう見つけて買うかのデータ分析。無料版あり | 週数本 | 英 | 引用のみ | (1)(2)genres の売れ筋 | ○ |
| Game Maker's Toolkit | https://www.youtube.com/@GMTK / https://gmtk.substack.com/ | Mark Brown | 仕組み 1 つずつの設計分析。GMTK Game Jam も | 月1前後 | 英 | 引用のみ | (2)genres・tips (3) | ○ |
| Game Programming Patterns | https://gameprogrammingpatterns.com/contents.html | Robert Nystrom | ゲーム用設計パターン。全文無料 | 古典(更新なし) | 英(和訳書あり) | Web 版は無料閲覧 | (3)通読 (4)章の形 | ○ |
| GDC Vault 無料枠 | https://gdcvault.com/free | GDC | 講演動画・スライドの無料分 | 年1追加 | 英 | 閲覧のみ | (3)選んで視聴 | ○ |
| Red Blob Games | https://www.redblobgames.com/ | Amit Patel | 経路探索・六角マス・手続き生成を動く図で | 不定期・古典 | 英 | 引用のみ | (3)(4)動く図の説明 | △ |
| AI Gamechangers | https://aigamechangers.substack.com/ | — | ゲーム業界 × AI の対談 | 要確認 | 英 | — | (1)候補止まり | ○ |
| CEDiL(CEDEC 資料庫) | https://cedil.cesa.or.jp/ | CESA | CEDEC の資料 1700 件超。無料会員で DL・動画 | 年1追加 | 日 | 閲覧のみ | (3)AI・個人開発の回を選ぶ | ○ |
| Zenn topic: claudecode / gamedev | https://zenn.dev/topics/claudecode | 各書き手 | 日本語の実践記事。新顔探しの入口 | 毎日 | 日 | 記事ごと | (1)既に方針あり→仲間の輪の入口 | ○ |
| 『レベルデザインをはじめよう』 | https://gamebiz.jp/news/428624 | M. Salmond 著・ボーンデジタル | レベル設計 10 原則 | 2026-08 発売 | 日 | 有料書籍 | (3)買うかはユーザー判断 | ○ |

## 毎朝の収集に足す候補
`sources.md` の「候補」に入れる想定。すぐ試用にはしない。
- **Simon Willison's Weblog**: AI ツールの一次の実使用。量が多いので「Claude Code・Codex・agent」の語を含む記事だけ拾う。
- **Anthropic Engineering**: 月数本。出たら必ず拾う。
- **How To Market A Game**: 週1。売り方の欄に。
- **GameDiscoverCo(無料版)**: 週1。ジャンルの売れ方の数字が取れる。
- **Latent Space**: 長いので見出しだけ。中身があれば拾う。
- 注意: 上の多くはこの環境から直接読めない。`read_web` で読めるかを毎朝の初回で確かめる(howtomarketagame と simonwillison は読めた)。

## 教科書に足す候補(通読)
1. Agentic Engineering Patterns(全章。短い)
2. Anthropic「Effective context engineering for AI agents」 https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
3. Game Programming Patterns(全章。特に Game Loop・Update・Command・State)
4. How To Market A Game の入門記事集(サイトの「Read my favorites」)
5. GMTK の定番回(Platformer Toolkit など、game feel の回)
6. CEDiL から AI・個人開発の講演を年 2〜3 本

## 表の作りで真似したい点
- **章=パターン 1 つ**(Willison・Nystrom): 名前 / どんな時 / やり方 / 避けること の順。tips.csv に「場面」「避けること」列を足す案。
- **アンチパターンを別章に分ける**(Willison): mindset.csv や gotchas と同じ考え。良い例と並べる。
- **「注釈付きプロンプト」**(Willison): 実際のプロンプトと追い指示を全文で残し、横に注釈。progress の記録の形として使える。
- **入口を 1 本に絞る**(Zukowski の STEP 1〜6): README の「まず読む 3 本」を明示する形。
- **awesome リストの分類**(awesome-claude-code): スキル / フック / コマンド / オーケストレータ / MCP。knowledge のカタログの見出しに揃えると照合しやすい。

## 見送り
- sorceress.games のブログ: 自社ツールの宣伝が中心。
- 「Awesome Claude Code 11 選」系のまとめ記事(claudefa.st 等): まとめのまとめで一次情報なし。
- Mega Cat の Juice Guide: 2017 年。古典ほどの評価はない。GMTK と既存の game-feel スキルで足りる。
- 日本語の「ゲームデザインまとめサイト」: 検索で中身のある個人の常連が見つからず、ニュースサイトのタグ一覧のみ。

## 未確認
- 多くのサイトがこの環境から直接つながらず、最終更新日を実測できていない(Latent Space・GMTK・GameDiscoverCo・Red Blob・promptingguide・12-factor-agents・CEDiL)。
- awesome-claude-code と 12-factor-agents のライセンス種類。
- AI Gamechangers の更新頻度と中身の質。
- 日本語で「AI × ゲームデザイン」を継続して書く個人は今回見つけられず。既存の候補(roripika・tokoharusame・うきょう)の参照先をたどる方が早い。
