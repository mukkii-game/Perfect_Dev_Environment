# Claude / Codex / Antigravity(agy) / Grok の連携と、枠切れ時の乗り換え(2026-10-14 調査)

Mukkii の依頼「世の中の AI 同士の連携を全力で探す。特にトークン切れの時」。サブエージェントが Web(公式・GitHub・Zenn・Qiita・dev.to)を調べた結果を、会議室の判断つきでまとめた。1 出典のものは【一説】。

## 結論
- 会話を「生きたまま」他社の AI に移す手段は無い。移せるのは **git の中身 + 引き継ぎメモ** か **Claude の会話ログの取り込み**。
- Claude が止まった後の救済(どちらも Claude の枠を使わない):
  - **Codex CLI の `/import`**(0.140 以降): 過去 30 日・最大 50 件の Claude の会話、CLAUDE.md → AGENTS.md、スキル、MCP、hooks を取り込む。https://dev.classmethod.jp/articles/codex-cli-import-from-claude-code/
  - **Grok Build の `/resume-claude`・`Ctrl+U`・`grok import <jsonl>`**(2026-07)。https://continuumcode.ai/guides/grok-resume-claude-code-sessions/
- Claude Code から他社を呼ぶ**公式プラグイン**: OpenAI(codex-plugin-cc)と xAI(grok-build-plugin-cc)。Google(agy)は有志のみ。
- `codex mcp-server` は公式に削除(後継の app-server は MCP ではない)。https://learn.chatgpt.com/docs/mcp-server

## 道具(主なもの)
| 名前 | つなぐもの | 枠 | 場所 | 成熟度 | 出典 |
|---|---|---|---|---|---|
| codex-plugin-cc | Claude → Codex(review / rescue / `/codex:transfer`) | サブスク | PC | OpenAI 公式 | https://github.com/openai/codex-plugin-cc |
| Codex `/import` | Claude の設定と会話 → Codex | サブスク | PC | 公式 | 上記 |
| grok-build-plugin-cc | Claude → Grok | サブスク | PC | xAI 公式 | https://github.com/xai-org/grok-build-plugin-cc |
| Grok Build(`grok`) | Claude・Codex の会話を取り込んで続ける。AGENTS.md・CLAUDE.md を読む | SuperGrok 等 | PC | 公式 | https://github.com/xai-org/grok-build |
| `claude mcp serve` | 他の AI → Claude | サブスク | PC | Anthropic 公式 | https://qiita.com/Ohmiya-Mizuki/items/499458f72be309cac704 |
| PAL MCP の clink | Claude・Codex・Gemini の CLI を互いに呼ぶ(agy は PR 中) | CLI はサブスク | PC | 有志・最終リリース 2025-12 | https://github.com/BeehiveInnovations/pal-mcp-server |
| claude-code-failover | Claude が上限で止まった瞬間(StopFailure フック)に Codex 等へ自動で渡す | 渡し先の枠 | PC | 有志・実績ほぼ無し | https://github.com/erencivril/claude-code-failover |
| many-ai-cli | 複数 CLI をブラウザで管理、止まった前任の会話から後任へ | サブスク | PC | 日本の個人作 | https://qiita.com/ishizakahiroshi/items/d7c04c99e43b2ca1bc11 |
| Claude Squad | Claude・Codex・Gemini を並列 | サブスク | PC | 有志・人気 | https://github.com/smtg-ai/claude-squad |
| claude-code-router | Claude Code の画面で別モデルを API キーで | **API 課金** | PC | 有志・人気 | https://github.com/musistudio/claude-code-router |
| CLIProxyAPI | 各社サブスクを API 化・複数アカウント | — | — | **使わない(規約違反の恐れ大)** | https://github.com/router-for-me/CLIProxyAPI |

終わったもの: vibe-kanban(終了予定)、Crystal(廃止)、coder/AgentAPI(保守終了)。

## 実際の例(抜粋)
- 上限が来たら関数 `cx` で Codex へ。WORKLOG と状態表示の 5 時間枠・週枠で切り替え時を判断(うぐいすソリューションズ)。https://zenn.dev/uguisu_blog/articles/f184b67962ce7c
- ゲームをストア公開。UI は Codex、他は Claude、絵は Antigravity。上限中は相手が代わる(roripika)。https://qiita.com/roripika/items/1952fb2bf112fb562042
- Claude Code から `grok -p` で X を検索させる(koedesk)。https://zenn.dev/koedesk/articles/claude-code-grok-x-ad-targeting
- Claude・Codex・agy の 3 つを併用、レビューは手元の LLM(k_motoki)。https://zenn.dev/k_motoki/articles/11de0ba46dd1ee
- handoff.sh + NOTES.md の 4 段構え。https://dev.to/gabrielanhaia/your-ai-coding-plans-usage-limit-is-now-a-production-dependency-39hh

## 規約(大事)
- **Anthropic**: サブスクのログインは Anthropic 自身のアプリ専用。他社の道具がサブスクの認証で要求を流すのは禁止。本人が普通の claude を使うのは可。複数アカウントで上限を伸ばすのも危険。https://code.claude.com/docs/en/legal-and-compliance
- **Google**: 2026-02、Antigravity のログインを他社の道具で使った人を停止。agy 本体を使うのは可。https://github.com/openclaw/openclaw/issues/14203
- **OpenAI**: 2026-09-29「Sign in with ChatGPT」— 連携先の道具で Plus/Pro の枠を使ってよい公式の仕組み。4 社で一番寛容。https://thenewstack.io/sign-in-with-chatgpt/
- **Grok Build**: 2026-07 にリポジトリを丸ごと(.env 含む)送っていた件。サーバー側で止まったとされるが範囲は未確認 → 秘密のある repo では使わない。https://betterstack.com/community/guides/ai/grok-cli-data-leak.md

## できない・未確認
- Claude が Codex / Grok の会話を取り込む公式機能は未確認。
- `/codex:transfer` が上限到達後に動くかは未確認(止まった後は Codex の `/import` が確実)。
- クラウドの Claude セッションは会話ログが手元に無いので、取り込み系は使えない可能性が高い。
- agy が AGENTS.md を読むか・ACP 正式対応かは未確認。

## 会議室の判断(提案)
1. **土台はもうある**: AGENTS.md + CLAUDE.md の `@AGENTS.md` + HANDOFF.md + push のたびに直す。これが「どの AI でも続きができる」の本体。
2. **PC に足す(小さく)**: 状態表示に 5 時間枠・週枠の残り(`rate_limits`)を出す。止まったら Codex を開いて `/import`。
3. **普段から枠を減らす**: codex-plugin-cc で点検・調べ物を Codex に回す。
4. Grok は X 検索など得意分野だけ、秘密の無い repo で。サブスクを API 化する道具は使わない。
