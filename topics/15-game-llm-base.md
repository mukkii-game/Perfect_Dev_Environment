# ゲーム共通の LLM 会話基盤(検討 2026-10-04)

出発点: ChatGPT 側で Emmichy(mukkii-game/emmichy, branch pilot-audio-readable-retro)に試作。
構成: GitHub Pages(静的)→ Cloudflare Worker(キーを隠す中継)→ Groq 無料枠 → 失敗時 Workers AI → 失敗時ゲーム内ルール会話。

## 評価: 骨格は正しい。共通化の前に直す所
| # | 問題(試作のコードで確認) | 直し方 |
|---|---|---|
| 1 | キャラ設定(system プロンプト)が Worker に直書き → 作品ごとに Worker が増える | **Worker は 1 本**。`/api/chat/<game>` で作品を選び、キャラ設定は Worker 側の `games/<game>.js` に置く |
| 2 | 守りが Origin 判定だけ。Origin は curl で偽装できる → 無料枠を他人に使い切られる | 1 IP あたりの回数制限(Cloudflare の Rate Limiting)+ 作品ごとの 1 日上限。**クライアントからプロンプトを受け取らない**(受け取ると誰でも使える無料 LLM 窓口になる) |
| 3 | Groq の返答が検証で落ちると、Workers AI を試さず 502 | 各プロバイダの結果を検証し、だめなら次へ進む(順番を配列で持つ) |
| 4 | 失敗の理由が見えない | provider・失敗理由・所要時間だけ数える(Workers Analytics)。**プレイヤーの文章は保存しない** |
| 5 | 課金の事故 | Cloudflare は Free プラン、Groq はカード未登録で使う。超えたら止まるだけで請求は来ない形にする |

## 共通化する部分 / 作品ごとの部分
| 共通(1 か所) | 作品ごと |
|---|---|
| Worker 本体: CORS・回数制限・プロバイダ順・タイムアウト・出力検証の枠・計測 | キャラ設定・口調・文字数・使ってよい文字(Emmichy はカタカナのみ)・禁止語 |
| クライアント `core/chat.ts`: 送信・タイムアウト・ヘルスチェック・失敗時のルール会話への切り替え・「AI/ルール」表示 | ルール会話エンジン、状態値(名前・好み・感情)、どの場面で LLM を使わないか |
| デプロイ(GitHub Actions + wrangler)、secret の置き方 | `games/<game>.js` 1 ファイル |

## 開発環境への組み込み
- **共通 Worker の repo を 1 つ**(案: `mukkii-game/game-llm`)。新作は `games/<game>.js` を足して push するだけ。キーは `wrangler secret put GROQ_API_KEY`(人間が 1 回)。
- **雛形に `src/core/chat.ts`**(`chat(game, input, state, {fallback})`)。LLM が無くても必ずルール会話で遊べることを既定にする。
- **再現性との両立**: `?auto=1`・`?seed=`・`?replay=` の時は LLM を呼ばずルール会話(雛形の自動確認と再生を壊さない)。
- 作法(AGENTS.md)は 1 行: 「LLM 会話は core/chat.ts と game-llm の games/<作品>.js。プロンプトをクライアントに置かない」。
- 調整つまみ(`src/tuning.ts`)に「LLM を使う / 使わない」「返答の長さ」を置けば、ESC で切り替えて比べられる。

## 他の候補(足すなら)
- **Gemini API 無料枠(Flash)** を 2 番手に足すと、Groq と Workers AI が同時に落ちても粘れる。
- ブラウザ内 LLM(WebLLM 等)は数百 MB〜GB の読み込みでスマホに不向き。採らない。

## 無料枠(2026-10 時点、二次情報)
- Groq gpt-oss-120b: 毎分 30 回・**1 日 1,000 回**。**組織単位で共有**(キーを分けても全作品で 1,000 回)。
- Workers AI: **1 日 10,000 Neurons**(UTC 0 時リセット)。Free プランなら超えるとエラーで止まり、請求は来ない。
- → 全作品合計で 1 日数百〜千回の会話が上限。試作・小規模公開には十分、バズったらルール会話に落ちる前提で作る。

## 役割分担(2026-10-04 決定)
- 共通 Worker(game-llm)と雛形の core/chat.ts は**会議室側(Claude)が作る**。
- Emmichy の移行は ChatGPT/Codex 側が進める。会議室は使い方と games/emmichy.js の雛形を渡す。

## 未確認
- Groq の規約で、ゲームの公開サービスとして無料枠を使ってよいか。

## 実装(2026-10-04)
- `mukkii-game/game-llm` を作成・push。Groq → Gemini(無料枠)→ Workers AI → 502(ゲーム側でルール会話)。テスト 6 本通過、wrangler の dry-run 通過。
- 公開済み: https://game-llm.mucky-totoro.workers.dev (/health で groq・gemini・workers-ai の 3 つとも鍵あり、10/4 確認)
- Emmichy の移行は Codex 側に依頼(会議室は使い方と games/emmichy.js を用意済み)。
- 雛形への `core/chat.ts` 組み込みは、Emmichy で実際に動いてから。
