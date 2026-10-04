# 他社 AI を人の手を介さず使う経路(検討中 2026-10-04)

目的: Claude の枠切れ時の逃げ道と、画像(Claude が弱い)を良いモデルに任せること。
**条件(ユーザー 10/4): 従量課金は使わない。定額(ChatGPT Plus・Gemini)・無料・ローカルの範囲で。**

## 画像
| 経路 | 費用 | 人の手 | 使える場所 | 状態 |
|---|---|---|---|---|
| **Codex CLI の画像生成(gpt-image)を Claude Code から呼ぶ** | ChatGPT Plus の範囲 | PC で `codex` に一度ログイン | PC のセッション | 本命。ただし CLI に画像ツールが来ない不具合報告あり(openai/codex#37496)。PC で実測する |
| **Gemini API の無料枠(Flash Image)** | 0 円。**請求先を登録しないキーなら課金されようがない** | キーを作って環境の secret に置く(1 回) | クラウド・PC | 二次情報で 1 日 500 枚・毎分 2 枚程度。Pro は無料枠なし。実測する |
| **ローカル ComfyUI(デスクトップ 4080S)** | 0 円 | なし(起動だけ) | デスクトップのセッション / Remote Control | 量産・差分・同じ画風の繰り返しに強い。`knowledge/local-ai.md` |
| ChatGPT・Gemini のアプリで人が作る | 定額 | AI がプロンプトを書き、人が貼って保存(1 枚 1 分) | どこでも | 最高品質の 1 枚が要る時の逃げ道。`assets/mine/` に置けば作品が最優先で使う |
| ブラウザ自動操作でアプリを動かす | 定額 | なし | PC | **やらない**(規約上グレー、凍結リスク) |

## コード(Claude の枠切れ時)
- GitHub の issue / PR に `@codex` と書けば Codex クラウドが Plus の範囲で動く(連携は最初に 1 回、人が ChatGPT 側で GitHub をつなぐ)。
- PC なら Codex CLI を Claude Code から直接呼べる。

- 他社に渡すのはコードや素材の指示だけ。非公開 repo の中身を渡す時は判断する。

## Codex で作業させる時の作法(2026-10-04)
- 雛形・作品の指示書は `AGENTS.md`(CLAUDE.md はそれを読み込むだけ)。**Codex は AGENTS.md を自分の指示書として読む**ので、作品の作法はそのまま通じる。
- 全体の決まり(global/constitution.md)は Claude 用の場所に入れているので、Codex には届かない。PC では `~/.codex/AGENTS.md` にも同じ 3 行を置けば届く【未実施】。
- 資料のスキル(war-room-knowhow)を Codex が読めるかは未確認。読めなくても、AGENTS.md の資料の場所(会議室の URL)を辿ればよい。

## セカンドオピニオン(Claude ⇄ Codex)
| 方法 | 自動か | 場所 | 費用 |
|---|---|---|---|
| Claude が PC の Codex CLI に `codex exec "<この差分をレビューして>"` で聞き、答えを読む | **自動** | PC | Plus の範囲 |
| Claude が PR を作り、コメントに `@codex review` と書く → Codex がレビューを返す → Claude が読んで直す | **自動**(最初に ChatGPT 側で GitHub 連携だけ人) | クラウド・PC | Plus の範囲 |
| 逆向き: Codex が PC の Claude Code に `claude -p "<質問>"` で聞く | **自動**(Codex はコマンドを打てる) | PC | Claude の定額の範囲 |
| 議論させる: Claude が `codex exec` で意見を取り、反論を返す…を 2〜3 往復して、両論と結論をユーザーに出す | **自動** | PC | 両方の定額 |
- 使い所: 大きな設計判断、詰まった不具合、公開前の点検。毎回やると遅くなるので、迷った時だけ。

## 頼み方(人間)
- 「GPT にも聞いて」「セカンドオピニオン取って」→ PC なら `codex exec`、クラウドなら PR に `@codex review`。
- 「GPT と議論させて」→ PC で 2〜3 往復。結果は「一致した点・割れた点・おすすめ」で返す。
- Notion を仲介にする方法もあるが、GitHub の issue / PR か PC のコマンドで足りる(記録が repo に残る)。
