# 他社 AI を人の手を介さず使う経路(検討中 2026-10-04)

目的: Claude の枠切れ時の逃げ道と、画像(Claude が弱い)を GPT / Nano Banana に任せること。

| 経路 | 契約 | 人の手 | 状態 |
|---|---|---|---|
| GitHub の issue / PR に `@codex` と書いて Codex に頼む | ChatGPT の定額(Codex 込み) | 要らない(最初の連携だけ人) | 要確認: Plus で使えるか、連携済みか |
| 環境の secret に API キーを置き、セッションから直接呼ぶ(OpenAI 画像 / Gemini 画像) | 従量(API) | 要らない(キーを置くのだけ人) | 推奨。キーはチャットに貼らず secret に直接 |
| ローカル PC の Codex CLI / Gemini CLI を Claude から呼ぶ | 定額のログインを PC で一度 | 要らない | PC のセッションのみ |
| Notion・Drive に依頼を書き、相手の AI が読む | 定額 | 相手側の起動に人が要ることが多い | 中継箱としては GitHub issue で足りる |

- 定額の画像生成(ChatGPT・Gemini アプリ)には公式の自動化口がない。画像を無人で回すなら API。
- 他社に渡すのはコードや素材の指示だけにし、非公開 repo の中身を渡す時は判断する。
