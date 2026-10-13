# 圧縮で続けるか、新しいセッションに引き継ぐか(2026-10-13)

対象: Claude Code(CLI・デスクトップ・クラウドのセッション)。公式ドキュメントは WebFetch で本文を読んだ(◎)。
実践者の記事は直接つなげないサイトが多く、検索結果の要約しか見ていない(○)。

## 結論
- **同じ作業を続けていて、流れがまだ良い間 → 圧縮**(`/compact <残すもの>`)。公式も自動圧縮を前提にしており、
  「会話のやり取りが多い長い作業」に向くとしている。
- **作業が変わる・同じ指摘を 2 回以上した・失敗した案で会話が汚れた → 新しいセッション**(申し送りを書いてから
  `/clear`、クラウドではサイドバーで新しいセッション)。公式は「直しが 2 回を超えたら /clear して、学んだことを
  入れた良い指示で始め直せ。たいていそちらが勝つ」と明言している。
- **数日にまたがる・別の PC/AI が拾う → 申し送りファイル必須**(圧縮は会話の中にしか残らない)。
  Anthropic の長時間エージェントの記事は「圧縮だけでは足りない」とし、進捗ファイル + git で新しい窓へ渡す形を採った。
- 圧縮の前に、**残したい決めごとは先にファイルへ書く**。こうすれば圧縮でも新セッションでも同じものが残る。

## 根拠
### 圧縮の仕組みと落ちるもの
- 自動圧縮はまず古いツール出力を消し、足りなければ会話を要約する。「依頼と主要なコード片は残る。
  会話の初めの方の細かい指示は失われうる。常設のルールは CLAUDE.md に置け」(how-claude-code-works ◎)。
- 要約が残すもの: 依頼と意図・技術的な要点・見た/直したファイルと重要なコード片・エラーと直し方・残りの作業・
  今の作業。**ツール出力の全文と途中の考えは消える**。Claude は経緯を参照できるが正確な中身は持たない(context-window ◎)。
- 圧縮後に読み直されるもの(context-window「What survives compaction」◎):
  - ルート直下の CLAUDE.md(AGENTS.md も同様の扱いと理解)・パス指定のないルール・自動メモリ・plan モードの計画 → ディスクから再注入
  - 最近触ったファイル最大 5 本(5,000 トークン超は場所だけ)。使ったスキル本体(1 本 5,000・計 25,000 トークンまで、古い順に落ちる)
  - **落ちるもの**: 会話の中だけで言った指示、サブフォルダの CLAUDE.md と `paths:` 付きルール(該当ファイルを触るまで戻らない)、
    スキル一覧、フックが前に足した文脈(要約に混ざる)
- 実践者の報告(○): エラー文・ファイルパス・行番号・決めた理由・制約の正確な言い回しが短い説明に縮む。
  CLAUDE.md が圧縮後も文脈にあるのに守られなくなった、という報告もある(公式の記載ではない)。
- 自動圧縮の発動点: 1M 窓のモデル(Fable・Sonnet 5 以降・Opus 4.7 以降など)は約 967K、200K のモデルは上限付近。
  **クラウドのセッションは窓の途中で早めに圧縮**するよう `CLAUDE_AUTOCOMPACT_PCT_OVERRIDE` が固定で入る(model-config・claude-code-on-the-web ◎)。
- 性能は窓が埋まるほど落ちる(「context rot」)。1M 窓でも同じで、圧縮点が遠いぶん劣化した状態で長く走りうる
  (best-practices ◎・Anthropic Engineering ◎。後半は推論)。

### 圧縮に指示を渡せるか
- `/compact <指示>` で残すものを指定できる(例 `/compact focus on the auth bug fix`)。クラウドでも使える。
- CLAUDE.md に「Compact Instructions」節、または「圧縮するときは変更ファイルの一覧とテストコマンドを必ず残せ」のように書ける。
- `/rewind`(Esc 2 回)で「ここから要約」「ここまで要約」と部分だけ圧縮もできる。
- 保証はない。指示しても落ちることがある(実践者 ○)。

### 公式の使い分け
- 無関係な作業の間は `/clear`。「キッチンシンク」な会話は性能を落とす(best-practices ◎)。
- 仕様を詰めたら**新しいセッションで実装**せよ。きれいな文脈と書かれた仕様が手に入る(best-practices ◎)。
- 深い一つの問題に取り組み中で、経緯そのものに価値がある時は溜めてよい(best-practices「Develop your intuition」◎)。
- Anthropic Engineering: 圧縮=やり取りの多い長い会話、メモを取る=節目のある反復開発、サブエージェント=調べ物(◎)。
- 実践者の目安(○): 「前の 1 時間を新人に説明する必要がないなら /clear、短い申し送りで足りるなら /compact」。
  「壊れてから圧縮すると誤解も要約に残る。良い状態のうちに区切れ」。

## 仕組みにする方法
- **使用率を見える化**: ステータスラインに `context_window.used_percentage` を出せる(statusline ◎)。`/context` で内訳。
- **早めに圧縮させる**: `/autocompact 300k`、設定 `autoCompactWindow`、環境変数 `CLAUDE_CODE_AUTO_COMPACT_WINDOW`(model-config ◎)。
  1M 窓のまま 967K まで走らせない方がよい、という使い方ができる。
- **PreCompact フック**(matcher `manual`/`auto`): 圧縮の直前にスクリプトを走らせられる。入力は `trigger` と
  `custom_instructions`(手動 /compact の指示文)と `transcript_path`。exit 2 か `decision:"block"` で圧縮を止められる
  (自動で上限エラーから回復中に止めるとリクエストが失敗する)。用途例: 会話ログから申し送りの下書きを書き出す・止めて「先に HANDOFF を書け」と促す。
- **PostCompact フック**: 入力に `compact_summary`(要約本文)。ファイルに保存すれば申し送りの材料になる。判断は変えられない。
- **SessionStart フック(matcher `compact` / `clear`)**: 圧縮後・/clear 後に、標準出力が文脈に足される。
  `cat HANDOFF.md` や `git log --oneline -5` を流せば、どちらで続けても同じ申し送りが入る(hooks-guide 公式例 ◎)。
- **新しいセッションを立てる道具**: `claude --cloud "HANDOFF.md を読んで続きを"`、`claude -p`、デスクトップ/クラウドの
  サイドバー、Claude Code Remote の create_session。`/branch`・`--fork-session` は会話を複製するだけで軽くはならない。
- **できないこと(見た範囲)**: フックから `/clear` や新セッション作成を直接起こす公式の口は見当たらない。
  「使用率 X% で自動的に新セッションへ」は、ステータスライン/フックで知らせる → 人か AI が申し送りを書いて立て直す、が現実的。

## 指示文の案(AGENTS.md / CLAUDE.md に 1〜2 行)
- 案 A(中身を残す型。圧縮でも新セッションでも効く):
  「決めたこと・数値・ファイルの場所は、決めた時点で HANDOFF.md に書け(会話だけに置くな)。圧縮するときは HANDOFF.md・変更したファイル一覧・未解決の問題を必ず残せ。」
- 案 B(切り替えの合図型):
  「作業が変わった時、同じ直しを 2 回した時は、HANDOFF.md の次の一手を更新してから新しいセッションで続けるよう人間に言え。同じ作業の途中なら /compact でよい。」
- 推し: A。B は AI が自分で /clear できないので「言え」止まりになる。A の前半は既存の「push のたびに HANDOFF を直せ」と重なるので、
  足すなら後半(圧縮時に残すもの)だけで足りる可能性が高い。仕組みで補うなら SessionStart(compact|clear)で `cat HANDOFF.md`。

## 未確認
- AGENTS.md を CLAUDE.md の `@AGENTS.md` で読み込んでいる場合も、圧縮後に読み直されるか(仕組み上はルート CLAUDE.md 扱いのはずだが実測していない)。
- デスクトップアプリ固有の差(クラウドは /clear 不可・早め圧縮を確認済み。ローカルのデスクトップは CLI と同じと推定)。
- PreCompact で block した後、AI に「申し送りを書け」と伝える確実な経路(block の reason が Claude に届くかは文書で読めていない)。
- 実践者記事の本文(morphllm・dev.to・lilting.ch は接続不可で検索要約のみ)。
- API 側のサーバー圧縮(platform.claude.com の compaction)は今回読んでいない。

## 出典
- https://code.claude.com/docs/en/best-practices
- https://code.claude.com/docs/en/context-window (What survives compaction / When your context fills up)
- https://code.claude.com/docs/en/how-claude-code-works (When context fills up)
- https://code.claude.com/docs/en/memory (Instructions seem lost after /compact)
- https://code.claude.com/docs/en/hooks (PreCompact / PostCompact / SessionStart)
- https://code.claude.com/docs/en/hooks-guide (Re-inject context after compaction)
- https://code.claude.com/docs/en/model-config (auto-compact window / thresholds)
- https://code.claude.com/docs/en/statusline (context_window fields)
- https://code.claude.com/docs/en/claude-code-on-the-web (Manage context)
- https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
- https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents
- ○ https://lilting.ch/articles/claude-code-context-window-rot ・ https://dev.to/stacknotice/claude-code-compact-vs-clear-2026-managing-long-sessions-without-losing-quality-4dhm ・ https://www.morphllm.com/claude-code-auto-compact
