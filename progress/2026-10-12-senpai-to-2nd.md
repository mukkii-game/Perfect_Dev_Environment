# 1 代目 → 2 代目への引き継ぎ(2026-10-11〜12 に 1 代目で話した分)

Mukkii が間違えて 1 代目に話した分。**ここから先は 2 代目が担当する**(Mukkii の指示 10/12)。
詳しい中身は各ファイル。ここは索引と「止まっていること」。

## 作ったもの・決まったこと
| 何 | どこ |
|---|---|
| スプシ「個人開発環境の地図」(説明 / 全体地図 / 担当表 / **私の環境**) | Drive `1dYIH58PeNFuMMzgO5llqHc0n8vfjfuugwy1Xzg-Wdog`。原本は knowledge/tables/map.csv・roles.csv・my-env.csv |
| 開発ノウハウ一覧の「作品」タブに I 列「作っているAI(Mukkii が記入)」 | 4 本だけ記入(obake・kutsuzure=Claude、emmichy=Codex、charge-and-anchor-gdd=Claude) |
| AI 同士のつなぎ方の検討(6 案の比較・結論は「GitHub を土台、常時起動 PC は後で」) | topics/18-ai-linkage.md |
| **Issue から Claude を呼ぶ仕組み(動作確認済み)** | 雛形と emmichy の `.github/workflows/claude.yml`。`@claude` か label `claude` で Claude Code が Max の枠(Sonnet 5.5)で動き、PR と Issue のコメントで返す。emmichy #33 で成功 |
| 作品へ配る自動化「Enable Claude」 | ai-ops の Actions と scripts/enable-claude.sh。新作の作成(bootstrap)も最後に呼ぶ。Mukkii が「A: 鍵の配布まで自動」を選んだ |
| Claude の長期トークンの期限 | permissions-ledger.md の表(作成から 1 年) |
| 地雷: PC の Claude Code が API の従量課金でログインしていた → 直した | knowledge/env-gotchas.md |
| 権限モード(クラウド=自動が最上位、ローカル=バイパスあり)、Codex の 3 モードとの対応 | knowledge/env-gotchas.md |
| 依頼書の型・PC のコマンド版で他の AI を呼ぶ道・クラウドで月額の枠を使う道 | knowledge/multi-ai-relay.md |
| 用語集に repo / Issue / commit・push / PR | knowledge/tables/glossary.csv(値のタブへは毎晩の回収が足す) |
| Antigravity で Claude Sonnet/Opus 5.5 が使える(Mukkii 確認) | Claude の枠が尽きた時の予備。my-env.csv・topics/18 |
| Emmy = GitHub の emmichy(公開・Pages)。Codex が codex/* ブランチで開発中 | — |

## 止まっていること(2 代目が引き取る)
1. **Enable Claude を動かす前の、Mukkii の一度だけの作業(未完了)**
   - ① ai-ops に secret `CLAUDE_CODE_OAUTH_TOKEN`: PC の Claude Code(E:\dev で起動・Claude Max)で `/install-github-app` → `mukkii-game/ai-ops` → 「Set up workflows」→ 鍵は「Create a long-lived token with your Claude subscription」。最後にできる PR は**マージしない**(ai-ops の verify.sh が外部 action を 5 個に固定しているため。2 代目が閉じる)。
   - ② ai-ops の GitHub App(mukkii-ai-ops)に Repository permissions の **Secrets・Workflows・Issues を Read and write** で足し、組織のインストール側で承認。
   - 済んだら 2 代目が Actions「Enable Claude」を `kutsuzure` で試す(mcp__github__actions_run_trigger、workflow_id `enable-claude.yml`、inputs `{"repositories":"kutsuzure"}`)。
2. **@codex が動かない**: emmichy #35 に `@codex` と書いたが 4 分反応なし。Mukkii は**新しい Codex Cloud** に emmichy の環境を作った。旧 Codex Cloud の注記に「GitHub 連携に使うのはレガシー環境」とあるので、**旧 Codex Cloud にも emmichy の環境**を作ってもらい、「コードレビュー」の設定で emmichy をオンにしてもらう依頼をした(返事待ち)。済んだら #35 に `@codex` を再コメント。Issue でだめなら PR のコメントで試す。旧の Yasu の環境は「移行」しない。
3. **Gemini の入口**: agy コマンドは Mukkii の PC に無かった。必要になったら GitHub の run-gemini-cli(Google AI Studio の無料 API キー)を足す。急がない。
4. **emmichy の公開範囲**: 公開のままか(Pages が楽)。他社 IP(ちいかわ)の調査データが公開 repo にあることを Mukkii に伝え済み。判断待ち。
5. 1 代目の過去の宿題(10/11): 回収と週次レビューの指示文に「地図」スプシを足す件は、progress/2026-10-08-session-handoff.md の末尾。

## 2 代目がまず Mukkii に言うこと
「1 代目から引き継ぎました。残りは ①ai-ops の鍵と権限(一度だけ) ②旧 Codex Cloud の環境とコードレビュー設定 の 2 つです」
