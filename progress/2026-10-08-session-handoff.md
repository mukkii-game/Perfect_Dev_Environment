# 会議室セッションの引き継ぎ(2026-10-08)

前のセッション(session_01Rjcrs5wXfyBHne4YNLSenp「個人開発環境の整備」、9/13〜)が長くなったので、次のセッションが**これ 1 枚と README から**続きを始められるようにまとめた。細部は各ファイルにある(ここは索引)。

## 会議室の 3 つの仕事(README の先頭)
1. 調べる(AI・ゲーム開発・ゲームデザイン) 2. 作る土台を極める(1 日 1 本・ユニーク) 3. Mukkii を育てる

## 動いている自動化(定期実行は Claude の Routine。作品台帳だけ GitHub Actions)
| 名前 | いつ | どこで動く | ID / 場所 |
|---|---|---|---|
| AI知見の毎日収集 | 毎朝 7:03 | 毎回新しいセッション(Sonnet) | trig_018McVEb8PhNtRwKBG9KMvQA |
| 読む相手の毎日見直し | 毎朝 8:30(木曜休み)、10/17 か 3 日変化なしで自分を止める | 会議室セッション | trig_01GdhugaDfhCaW43MFbKLtpe |
| 作品台帳(機械) | 毎朝 6:50 | GitHub Actions(利用枠を使わない) | ai-ops `works-ledger.yml` → `ledger/works.json` `ledger/needs.md` |
| 追いかける係(秘書) | 毎朝 7:41 | 会議室セッション | trig_01WGXEztbs5bBFgoiDjHKWVk |
| AI 情報の週 1 取捨 | 木曜 8:00 | 会議室セッション | trig_01KMFiFHFvZ9WiRqL3zjeZrw |
| 週次レビュー | 月曜 8:00 | 会議室セッション | trig_01CmG3KkyfJXfeC4nGspSRPV |
| 作品の気づき回収 | 毎晩 23:52 | 会議室セッション | trig_01YPF6LcmAswnpmrHS1HkCfT |
| AIへの指示の月 1 点検 | 毎月 1 日 | 会議室セッション | trig_01EbtNVm61qgavXWVVX5QgNF |

**10/8 に 2 代目(session_01DsPopicw11cBJMpc4PSd8Z)へ付け替え済み**(上の ID は新しいもの)。次にまた移す時: 「会議室セッション」で動く 6 つは persistent_session_id が古いセッションに縛られている。新しいセッションで create_trigger(同じ prompt・cron、persistent_session_id = 新しいセッション)を作り直し、古いものを delete_trigger する。prompt は get_trigger で取る。

## 置き場所
- スプシ「開発ノウハウ一覧」1L3i02WVyMPxC-_wEiy1zSnyVFsCBHfRrrD25sXJVQAg: **作品**(台帳・Drive なので私有作品も載せてよい)/ AI・心構え・TIPS・用語集(値で書いたタブ。手順は knowledge/tables/README.md)/ 他は IMPORTDATA
- スプシ「Mukkii 育成プログラム」11Dn_SjUjqVBs8fdtdJk2dHQ0RO7S35ieKWE-T6_n2Sg: 教科書・カリキュラム・テスト ほか
- ドライブ AI知見フォルダ 199f1wPF5NWyb0Wcmer2vTgpiivBD1JDN(全文版「AI知見 日付」と公開用「ゲーム開発のためのAI知見 日付」)

## 今週決まったこと(decisions/ と topics/ に本文)
- Drive は会議室が作ったファイルなら確認なしで書いてよい(decisions/2026-10-06-drive-write-trust)。削除・G: の仕事データ・ゾーン C は今まで通り。
- Claude の上限が来たら Codex に HANDOFF.md で引き継ぐ(decisions/2026-10-06-claude-limit-handoff)。
- AI 同士の自動往復(Emmichy の実験)は終了。知見は knowledge/multi-ai-relay.md。
- 置き場の使い分け: GitHub=作品と公開 / Cloudflare=サーバー(game-llm)/ Netlify=Mucky Reader と古い物(topics/05)。
- 雛形: SPEC に「ひねり」「任せ方」欄、OGP、元ネタ探しの手順(knowledge/start-from-reference.md)。
- 競合として星野創吉さんを観察(sources.md 常設、topics/17)。

## Mukkii の返事待ち
1. 作品台帳の「状態を直す」列(特に 休止?完成? 23 本)
2. 今朝の判断 3 件(おばけ提灯の続行・終わりの作り方、Emmichy の PR #3)
3. パクる候補(research/2026-10-07-ai-game-factories.md 上位 3 つを雛形へ)と資料 5 つ(knowhow-curators)を入れるか
4. ~~週 1 取捨の 5 件(10/8)を番号で~~ → **済**: 10/8「全部」。process-patterns.md 5〜7・新設 game-design.md に入れた(多くなったら後で削る、と Mukkii)
5. itch.io 自動公開のための BUTLER_API_KEY
6. X の鍵の確認(Mucky Reader の一覧読みが 10/5〜10/7 止まった。10/8 は復活)。Mucky Reader のソースの置き場所(見つかっていない)

## 進行中の実験・次の一手
- 作品台帳: 機械(Actions)+ 判断(Claude)。needs.md が「なし」の日は Claude は短く済ませる。数日見て、役に立てば続ける。
- 雛形に入れる候補: 合格条件に「気持ちいい瞬間」1 行 / 検査を Hooks で自動に / 「完成」の 6 項目判定 / 状態を文字で返す関数(research/2026-10-07-ai-game-factories.md)
- おばけ提灯: 試運転のポストモーテムは progress/2026-10-06-postmortem-obake-chochin.md(面白さを誰も確かめなかった、が最大の教訓)

## 先輩に聞く(1 代目のセッションは残してある)
- 1 代目: session_01Rjcrs5wXfyBHne4YNLSenp「個人開発環境の整備」(9/13〜10/8)。消さない・アーカイブしない。2 代目: session_01DsPopicw11cBJMpc4PSd8Z。
- **聞く時**: 記録(decisions/ topics/ progress/ knowledge/)に答えが無い時だけ。まず記録を探す。
- **聞き方**: Mukkii に「1 代目に聞いてください: <質問>」と頼むか、使えるならセッション間のメッセージで 1 代目へ送る。
- **答えの受け取り方**: 1 代目は答えを会話ではなく **progress/senpai-answers.md に追記して push** する(セッション間で返信が届かないことがあるため。ファイルなら確実に残る)。2 代目はそこを読む。
- 答えが大事な判断なら、2 代目が decisions/ か topics/ に書き移す(先輩のセッションにしか無い知識を減らしていく)。

## 2 代目の最初の宿題
- 定期実行「読む相手の毎日見直し」(trig_01GdhugaDfhCaW43MFbKLtpe)の指示文に、週 1 取捨の**古い ID**(trig_01U1KVqNyU9yDjQTfxgTPh4x)が 1 か所残っている。新しい ID は trig_01KMFiFHFvZ9WiRqL3zjeZrw。指示文の書き換えは、そのセッション(2 代目)からしかできないので、2 代目が update_trigger で直す(他の部分は 1 文字も変えない)。
- **済(10/8 2 代目)**: update_trigger で ID だけ差し替えた。他の 5 つの指示文と repo 内に古い ID が残っていないことも確認。
