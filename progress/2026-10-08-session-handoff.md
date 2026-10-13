# 会議室セッションの引き継ぎ(2026-10-08)

前のセッション(session_01Rjcrs5wXfyBHne4YNLSenp「個人開発環境の整備」、9/13〜)が長くなったので、次のセッションが**これ 1 枚と README から**続きを始められるようにまとめた。細部は各ファイルにある(ここは索引)。

## 会議室の 3 つの仕事(README の先頭)
1. 調べる(AI・ゲーム開発・ゲームデザイン) 2. 作る土台を極める(1 日 1 本・ユニーク) 3. Mukkii を育てる

## 動いている自動化(定期実行は Claude の Routine。作品台帳だけ GitHub Actions)
| 名前 | いつ | どこで動く | ID / 場所 |
|---|---|---|---|
| AI知見の毎日収集 | 毎朝 7:03 | 毎回新しいセッション(Sonnet) | trig_018McVEb8PhNtRwKBG9KMvQA |
| 読む相手の毎日見直し | **10/9 に停止**(3 日変化なし。週 1 取捨に戻した) | 会議室セッション | trig_01GdhugaDfhCaW43MFbKLtpe |
| 作品台帳(機械) | 毎朝 3:50(10/12 に 6:50 から変更。GitHub の遅れ対策) | GitHub Actions(利用枠を使わない) | ai-ops `works-ledger.yml` → `ledger/works.json` `ledger/needs.md` |
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

## 雛形への反映(10/8 2 代目)— 済
- web-app-template d21a713: `core/probe.ts`(AI の目と手: 状態を JSON で返す・意味単位の操作・禁止はコードで拒否)+ サンプル配線 + check.mjs の確認 + スキル早見表の同期。build / check / test:replay 通過。
- 2 代目のセッションに web-app-template を書き込み可で追加済み(Mukkii 許可 10/8)。

## 1 代目からの追加(10/11)— 2 代目への宿題
- Mukkii の依頼で、人間が一覧するためのスプシ「個人開発環境の地図」(1dYIH58PeNFuMMzgO5llqHc0n8vfjfuugwy1Xzg-Wdog)を作った。タブは 説明 / 全体地図 / 担当表。原本は knowledge/tables/map.csv と roles.csv、スプシは値で書いてある(HYPERLINK で「開く」)。
- 定期実行の指示文を書き換えられるのは 2 代目だけなので、次の 2 つを 2 代目が update_trigger で足す(他は変えない):
  1. 作品の気づき回収(trig_01YPF6LcmAswnpmrHS1HkCfT)の 7.「コメント欄」の対象スプシに、このスプシを足す。
  2. 週次レビュー(trig_01CmG3KkyfJXfeC4nGspSRPV)の「一覧表の更新」に、map.csv・roles.csv を実物(list_triggers・Actions)と照合し、変えたらスプシの 2 タブを書き直す、を足す。

## 1 代目からの追加(10/12)
- 10/11〜12 に Mukkii が 1 代目で話した分は **progress/2026-10-12-senpai-to-2nd.md**。以後は 2 代目が担当(止まっていること 5 件あり)。

## Mukkii との話し方(10/12 Mukkii の依頼)
- **Mukkii に何か頼む時・報告する時は日本語で書く**(読み違いを防ぐため)。2 代目が英語で返していた。コマンド・ファイル名・画面の項目名はそのままでよいが、説明と頼みごとは日本語。

## 2 代目の役目(Mukkii 2026-10-13)
- **PC もクラウドも、Claude も GPT も、まとめて開発環境の効率を上げ続けるセッション**。Mukkii のあらゆる開発環境と開発状況を管理する(過去作・開発中の作品・その発信と宣伝をどこでどうやるかまで)。
- 重要な情報を集め、抜粋・吟味して憲法(global/constitution.md)と雛形の作法を磨き続ける。同時に、毎回読まれる指示が無駄に膨れて全作品のトークンを食わないかを見張る。
- 普遍的に効くことは、指示に入れてよい(Mukkii 10/13)。入れる時は仕組み(フック・コード)を先に考え、文は短く。
