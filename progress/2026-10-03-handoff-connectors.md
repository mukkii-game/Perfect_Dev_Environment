# 引き継ぎ: Google Sheets/Docs/Slides コネクタ接続後の段取り(2026-10-03)

ユーザーが claude.ai で Google Docs / Sheets / Slides コネクタを接続済み。新しい会議室セッションで次を行う。

1. 手元に Sheets/Docs/Slides のツールが出ているか確認(出ていなければ read_documentation connectors で原因を調べて報告)
2. スプシ 2 枚を**作り直さずに**直接修正: 全タブ 1 行目にフィルタ、縦中央・折り返し・列幅(knowledge/sheet-style.md)を実際に確認
   - 開発ノウハウ一覧 1L3i02WVyMPxC-_wEiy1zSnyVFsCBHfRrrD25sXJVQAg
   - Mukkii 育成プログラム 11Dn_SjUjqVBs8fdtdJk2dHQ0RO7S35ieKWE-T6_n2Sg(古い 1Fd51… は削除済みか確認)
3. 旧会議室セッション(session_01Rjcrs5wXfyBHne4YNLSenp)に届く定期実行を新セッションへ付け替え
   (persistent_session_id は update で変えられない → 同じ指示文で作り直し、旧いものは削除):
   - trig_01Ns5fm6oP4TQypayNsPmVw8 週次レビュー
   - trig_01U1KVqNyU9yDjQTfxgTPh4x 週1取捨
   - trig_017FjzQqjTwGAwDdiiFstMEe 読む相手の毎日見直し
   - trig_01TkkE97BqwtTuft6fecvzm2 作品の気づき回収
   - trig_01YKtRwgwbXxsfMayxaU9xMQ 指示の月1点検
   - trig_018McVEb8PhNtRwKBG9KMvQA 毎朝の収集(毎回新セッション)は connectors に Google Sheets/Docs を足すだけ
4. automations.csv の管理場所欄と、knowledge/sheet-style.md の「操作のしかた」を更新

## 結果(同じ日)
- コネクタは**このセッションの途中で使えるようになった**(新セッション不要)。定期実行の付け替えも不要。
- 開発ノウハウ一覧に直接: 全タブ 1 行目フィルタ、縦中央・折り返し、道具タブの列幅と色付けの列(C→D)を修正。リンク不変。
- 残り: 育成プログラム(11Dn…)も同様に確認。毎朝の収集(新セッション型)に Sheets/Docs の権限を足すかは、使う場面が出てから。
