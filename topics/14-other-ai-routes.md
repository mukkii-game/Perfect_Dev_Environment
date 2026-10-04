# 他社 AI の使い方(GPT のセカンドオピニオンを反映 2026-10-04)

条件(ユーザー): 従量課金の API は使わない。ChatGPT Plus の定額・無料枠・ローカルの範囲で。
経緯: Claude 案 → GPT に評価させた(85〜90 点、2 点修正)→ 下に反映。

## 正式ルート(これ以外は補助)
| 状況 | 使うもの |
|---|---|
| 普段の作品づくり | Claude Code |
| Claude の枠切れ・別の実装 | **Codex Cloud / Codex CLI を直接起動**(issue に `@codex` と書く方式は公式に弱いので使わない) |
| 大きな設計判断・詰まった不具合 | **独立セカンドオピニオン**(下の手順) |
| 公開前の点検 | PR に `@codex review` |
| スマホから相談 | ChatGPT + GitHub 連携(**読む・相談するだけ**。書き換えは Codex) |
| 画像 1〜数枚(質重視) | ChatGPT の画像生成を人が使う(AI が指示文を書き、人が貼って保存。`assets/mine/` へ) |
| 画像の量産・差分・画風統一 | ローカル ComfyUI(本命) |
| クラウドの Claude から画像 | Gemini API の無料枠(支払い方法を登録しないキー)【実測待ち】 |
| 作法 | AGENTS.md に一本化(Claude も Codex も読む)。二重管理しない |

## 独立セカンドオピニオンの手順
- 議論(往復)させない。往復すると互いに引きずられて「合意ゲーム」になる。
1. Claude が自分の案を `docs/opinions/<日付>-<題>-claude.md` に保存する。
2. Codex には **Claude の結論を見せず**、同じ問題と前提だけ渡して独立に答えさせる(PC: `codex exec`、クラウド: Codex Cloud にタスク)。
3. Claude か人間が 2 つを並べ、一致・相違・おすすめを出す。
- 逆向き(Codex が `claude -p` で Claude に聞く)も PC で可能。規約上の禁止は見当たらないが、**利用上限を回避する目的の多重起動はしない**。

## 確かめていないこと(実測してから正式にする)
- **Codex CLI から Plus の範囲で画像生成できるか**: 「CLI の組み込み機能・Plus 枠で gpt-image」という報告(note 記事・gpt-image-bridge)がある一方、GPT 自身は「公式保証された CLI 画像生成は API 側(従量)で、ChatGPT の画像枠と Codex の枠は別」と言う。CLI に画像ツールが来ない不具合報告(openai/codex#37496)もある。→ **デスクトップで 1 回試す。従量課金の画面が出たら使わない。**
- `@codex review` の初期設定: ChatGPT/Codex に GitHub 接続 → GitHub App に repo の許可 → Codex Cloud で repo を有効化 → Codex 設定で Code Review をオン。接続できても review だけ認証エラーになる報告あり(openai/codex#30168)。
- Gemini 無料枠の実際の枚数。

## Codex 側に用意するもの(最小)
- `~/.codex/AGENTS.md` に全体の決まり 3 行(Codex は ~/.codex → repo → 下位の順に AGENTS.md を読む)。
- PLANS.md は作らない(雛形の HANDOFF.md・SPEC.md・QUESTIONS.md と重なる)。
- Skill は必要になったものだけ(候補: 公開前点検)。指示を増やしすぎない。

- 他社に渡すのはコードと素材の指示だけ。非公開 repo の中身を渡す時は判断する。
