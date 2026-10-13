# 18. AI 同士をつなぐ仕組みと、枠が尽きた時の逃げ道(2026-10-12 起案)

Mukkii の環境は `knowledge/tables/my-env.csv`(スプシ「個人開発環境の地図」の「私の環境」タブ)。

## 現状の結論(提案。Mukkii の判断待ち)
**GitHub を「連絡の場所」にして、イベントで起きる仕組み(①)を土台にする。常時起動の機械(②)はローカルの道具が要る時だけ足す。**

1. **作品は全部 GitHub に置く**(非公開でよい)。PC の中だけの作品はクラウドの AI にも作品台帳にも見えない。
2. **頼み方は Issue 1 枚 = 依頼書 1 枚**。結果は repo のファイルと Issue のコメントで返す(multi-ai-relay.md の「1 つの場所・イベントは起床ベル・黙って終わらない」)。
3. **呼べる相手(どれも月額の枠で動く)**
   - Claude: 会議室の Claude がクラウドのセッションを立てる(実績あり)/ GitHub Actions の claude-code-action に Max のトークン(`claude setup-token`)を渡す
   - Codex: PR(や Issue)に `@codex` と書く → Codex のクラウド作業が ChatGPT の枠で動く
   - Gemini: Antigravity で Claude 5.5 が使えるなら、それが Claude の予備の枠(要確認)。GitHub Actions から Gemini を呼ぶのは API キーになる(無料枠があれば無料。要確認)
4. **Claude の枠が尽きた時**: 作品は HANDOFF.md があるので Codex(@codex か Codex アプリ)か Antigravity に渡す。会議室の定期実行も Claude なので一緒に止まる。止まっても困らない作り(機械の部分は GitHub Actions)を保つ。
5. **常時起動の機械(②)は後回し**。ComfyUI を外から使いたくなった時に、ゲーミングノートを家の常時起動機にする(Tailscale のような自分だけの網で。ネットに直接公開しない)。

## 6 つの案の比較
| 案 | 良い所 | 弱い所 | 判定 |
|---|---|---|---|
| ① GitHub Actions(クラウドで常に呼べる) | 無料。家の PC が消えていても動く。Claude・Codex は月額の枠で呼べる。結果が repo に残る | 作るのに一手間。6 時間で打ち切り。GPU なし。PC の中のファイルは見えない | **土台にする** |
| ② 常時起動の PC(ゲーミングノート等) | ローカルの道具(ComfyUI・PC 版の claude/codex/gemini)を全部使える | 電気代(ノートなら月数百円程度、デスクトップはその数倍。実測していない)。故障・停電・更新で止まる。外から入る道の安全 | ComfyUI を外から使う時に足す |
| ③ 常時起動の VM(クラウドの貸しサーバー) | どこでも動く。何でも入る | 月額がかかる(GPU なしでも数百〜千円台)。②と役割が重なり GPU も無い | 今は不要 |
| ④ この会議室のセッションが中継を作る | Claude 同士はすぐできる(実績あり) | **Claude の枠が尽きると会議室も止まる**(一番欲しい場面で使えない)。Codex・Gemini には直接届かない | 補助に留める |
| ⑤ 中継役の AI プログラムが常に待機 | 待機中はトークンを使わない | 置き場所が要る(=②か③)。①のイベント式が同じことを無料でする | ①で代わりになる |
| ⑥ 複数 AI をまとめる市販のアプリ | 作らずに済む | Cursor・Manus は自社の料金と枠(手持ちの契約の枠を使わない)。Grok Bots は月 120 ドル/席(10/6 調べ)。Dots は ChatGPT Pro(月 100 ドル)が要る | 今は入れない。Antigravity(契約済み)だけ試す |

## 枠を長持ちさせる工夫(先にやる方が安い)
- 定型の仕事は Sonnet、重い判断だけ Opus(定期実行はすでにこの形)
- 大きな調べ物はサブエージェントに任せ、本体の会話を太らせない
- セッションが長くなったら引き継いで新しくする(会議室で実施済み)
- 調べ物の下ごしらえ(集める・並べる)は余っている Gemini に、判断は Claude に

## 次にやること
1. ~~Antigravity で Claude 5.5 が選べるか~~ → **済(10/12)**: Claude Sonnet 5.5・Opus 5.5・GPT-OSS 120B・Gemini 3.8 Flash・3.1 Pro が選べる。Claude の枠が尽きた時は Antigravity の Claude で続ける。
2. ~~Emmy を GitHub に上げるか~~ → Emmy は既に GitHub の emmichy(公開・Pages)だった。公開のままにするかは Mukkii(非公開にするなら公開先は Cloudflare Pages)。
3. **①の最小形を作った(10/12)**: 雛形と emmichy に `.github/workflows/claude.yml`。Issue に label `claude` を付けるか `@claude` と書くと、Claude Code が Max の枠で動き、結果をブランチと PR にして Issue にコメントする。書き込み権限のある人だけが起動できる(公開 repo でも他人は動かせない)。動かすには Mukkii が secret `CLAUDE_CODE_OAUTH_TOKEN` を入れる。label は repo ごとに要る(雛形から作った repo には付かないので、ai-ops の新作作成で作るよう後で直す)。動いたら Codex(@codex)と Gemini の入口を足す
4. ComfyUI のセットアップが進んだら、②(ゲーミングノートを常時起動)を検討する

## 動作確認(2026-10-12)
- Mukkii が PC の Claude Code で `/install-github-app`(Claude の GitHub アプリを mukkii-game に導入・鍵は「Claude の契約で長期トークン」)→ emmichy に secret `CLAUDE_CODE_OAUTH_TOKEN` が入った。workflow は会議室が入れたものを残した。
- emmichy Issue #33 に `@claude` で依頼 → 約 1 分で Actions が成功し、Issue にコメントで回答(Max の枠)。①の最小形は動く。
- 他の repo で使うには、その repo に同じ secret が要る(`/install-github-app` を repo ごとに回すか、組織の secret にする)。

## 全自動化(2026-10-12 Mukkii が「A: 鍵の配布まで自動」を選択)
- ai-ops に Actions「Enable Claude」(scripts/enable-claude.sh)。repo 名か `active`(7 日以内に更新の作品)を渡すと、label・claude.yml・secret をまとめて入れる。新作の作成(bootstrap)も最後にこれを呼ぶ。
- 一度だけ Mukkii がやること: ① ai-ops に secret `CLAUDE_CODE_OAUTH_TOKEN` を入れる ② ai-ops の GitHub App に Secrets・Workflows の書き込み権限を足して承認する。
- 鍵の期限は permissions-ledger.md の表に入れた(1 年)。

## 2026-10-13 調査: 3 者(Claude・Codex・Gemini)が呼び合う既製の仕組み
Mukkii の依頼「既に公式か誰かが作っていないか」。結論: **PC の上なら既製品で 3 者が呼び合える**。クラウド(PC が消えていても)は今の GitHub 方式(①)のまま。

| 呼ぶ側 → 呼ばれる側 | 既製の道 | 出どころ |
|---|---|---|
| Claude → Codex | OpenAI 公式プラグイン codex-plugin-cc(`/codex:review` 等) | 公式(topics/14) |
| Codex → Claude | Claude Code 自身が MCP サーバーになる `claude mcp serve` を、Codex の MCP 設定に登録 | Claude Code の機能(第三者の解説で確認。公式文書は未確認) |
| Claude・Codex → Gemini | **Gemini CLI は 2026-06-18 に個人アカウントで終了**(複数の記事で一致)。後継は Antigravity CLI `agy`。`agy -p "…"` で 1 回だけ答えさせられる(端末でないと何も出ない報告あり → 疑似端末で包む) | 第三者の記事複数 |
| Gemini(agy) → 他 | `agy mcp add` で MCP サーバーを足せる → `claude mcp serve` や Codex を登録 | Antigravity CLI の早見表 |
| **3 者まとめて** | **PAL MCP Server(旧 Zen MCP)の `clink`**: どの CLI からでも他の CLI を子として呼べる(Claude → Codex、Codex → Gemini …)。結論だけ返るので本体の会話が太らない | 有志(BeehiveInnovations)。agy 対応は未確認 |
| 規格 | ACP(エディタ ⇔ エージェント。Claude・Codex・Gemini 登録済み)、A2A(エージェント同士。Codex は 2026-05 時点で未対応)。橋渡しに a2acode | 規格団体・有志 |

- 費用: どれも PC でログインした月額の枠で動く(API キー不要)。ただし**枠を回避する目的の多重起動はしない**(topics/14)。
- 試す順(PC、【実測待ち】): ① codex-plugin-cc(Claude → Codex)② Codex に `claude mcp serve` を登録(Codex → Claude)③ agy を入れて `agy -p` が Claude から呼べるか ④ うまくいけば PAL MCP の clink で 3 者を 1 つにまとめる。
- 出典: https://github.com/kanywst/a2acode / https://www.philschmid.de/acp-overview / https://codex.danielvaughan.com/2026/05/01/codex-cli-agent-interoperability-protocols-mcp-acp-a2a/ / https://mcpservers.org/ja/servers/BeehiveInnovations/zen-mcp-server / https://www.ksred.com/claude-code-as-an-mcp-server-an-interesting-capability-worth-understanding/ / https://botmonster.com/coding/gemini-cli-dead-migrate-antigravity-cli-2026/ / https://computingforgeeks.com/wp-content/uploads/2026/09/antigravity-cli-cheat-sheet.pdf
