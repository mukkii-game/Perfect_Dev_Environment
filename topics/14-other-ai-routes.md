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

## 画面操作(computer use)で他社アプリを動かす件(2026-10-06 検討)
話題: 「Opus に桃太郎の動画を頼んだら、ブラウザで Gemini(絵・TTS)と Suno(BGM)を操作して仕上げた」。
- **Suno: 条件付きで可(グレー)。** 規約(2026-09-03 施行版を本文で確認)の禁止は「data mining, robots, scraping, or similar data gathering or extraction methods」で、狙いはデータ収集。自分のアカウントで自分の曲を作る画面操作を名指しで禁じる文は無い(※10/6 に一度「自動化ソフトを明記で禁止」と書いたのは検索要約の誤り。訂正)。
  - **守ること**: 無料・Basic は**個人・非商用のみ**。作品(公開ゲーム等)に使うなら Pro / Premier で、**公式のダウンロードボタンで落とした曲だけ**商用可。録音・ストリームの抜き取りは禁止。透かし・メタデータを消さない。
  - **公式 API・MCP は無い**(2026-10 時点)。ネットにある非公式の API ラッパー(ログイン情報を使うもの)は規約違反に近いので使わない。
  - 量産・連打はしない(人が操作する程度の頻度)。
- **Gemini アプリ: グレー。** 明示の禁止は見つからないが許可も無い。量産には使わない。
- **同じ流れを規約内でやる道**(どれも定額・無料・ローカル):
  - 絵: Gemini API の無料枠(game-llm 用に作ったキーとは別に、作品制作用のキーを作る)/ ローカル ComfyUI
  - 声: VOICEVOX(ローカル)
  - BGM: 魔王魂など規約の明確な配布元 / ローカルの音楽生成(ACE-Step 等、要確認)
  - 編集: ffmpeg・Remotion をコマンドで(画面操作より速く確実)
- 「トークンがあまり減らない」は 1 人の体感。画面操作は画像を毎回送るので、普通は多く使う。

## 2026-10-06 追記: ChatGPT の通常チャットから GitHub に書き込める件
- Mukkii の ChatGPT 通常チャットに、emmichy への branch 作成・commit・PR 作成のツールが見えている。
- **会議室ではそのための設定をしていない**(記録は「読む・相談するだけ」)。ChatGPT 側の GitHub 連携(Codex 用に入れた GitHub App の権限)が通常チャットにも見えていると推測。未検証。
- 使うなら PR 経由に限る(main に直接書かない)。ターミナルが無く、テストもビルドも走らない。CI と人間の確認が頼り。
- Claude の通常チャットは、GitHub を読むだけ。書くには GitHub の MCP をカスタムコネクタとして足す必要がある(未設定・未検証)。
- 利用上限(10/6 調べた): Claude Code・Claude のチャット・デスクトップ版は**同じ上限を共有**している(5 時間ごと＋週ごと)。Claude Code の上限が来たらチャットも止まるので、チャットは逃げ道にならない。
  - 続ける手段は 2 つ。(1) 有料の追加枠(usage credits。前払いで API 料金。support.claude.com/en/articles/12429409) (2) **Codex / ChatGPT に同じ repo で続きを頼む**(別会社なので上限も別)。費用ゼロなのは (2)。
  - (2) のために、HANDOFF.md を常に最新にしておく(雛形の作法にすでにある)。

## 2026-10-06 追記: GPT 側から「AI 文通所」の提案(Emmichy)
- 提案: repo に /AI/VISION・DECISIONS・HANDOFF・PLAYTEST.md を置き、Issue 1 本を AI 同士の文通所にする。
- 判断: 方向は会議室と同じ(GitHub が正本、AI 同士は会話させずファイルで渡す)。ただし**雛形にはもう同じ役のファイルが root にある**(SPEC=VISION、DECISIONS、HANDOFF、QUESTIONS)。/AI に別名で作ると二重になるので、雛形の名前に合わせる。
- 新しく価値があるのは 2 つ: **PLAYTEST.md**(遊んだ記録と評価。おばけ提灯で欠けていた「面白いかの確認」の置き場)と、**文通所 Issue**(子セッションから親へ返信できない問題の回避策にもなる)。
- 進め方: Emmichy(Codex 側)で試す → 効いたら雛形に PLAYTEST.md を足し、文通所は任意の作法として資料に書く(AGENTS.md の必須手順にはしない。毎回 Issue を読む手間は全作品にかかるため)。
