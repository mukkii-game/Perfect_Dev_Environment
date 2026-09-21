# 権限の棚卸し表

> AI と外部サービスに「今どこまで許可しているか」の一覧。
> 変更したら必ずここを直す。月 1 で Routine が差分を点検する(topics/11)。
> 最終更新: 2026-09-16

## GitHub

| 対象 | 許可の範囲 | 置き場 | 状態 |
|---|---|---|---|
| Claude(GitHub App) / mukkii-game | **All repositories**。actions / checks / code / discussions / issues / pull requests / repository hooks / workflows の読み書き + コミット状態の読み取り。公開リポジトリは読み取り専用で含む | GitHub アプリ設定 | **確認済み(2026-09-16)。設定変更は不要** |
| Studio-Shimazu の repo が一覧に出る件 | **連携は入っていない**。3 本(Iwanna4Udemy / SteamLeaderboard / SoundGameOchiru)がいずれも public のため、上記の「公開リポジトリは読み取り専用」条項で見えているだけ。書き換えは不可 | — | **対応不要(2026-09-16 調査)** |
| GitHub App `mukkii-ai-ops`(App ID 5019353) | ai-ops のワークフローが使う。実行時に **1 時間で失効する**トークンを発行 | 秘密鍵が ai-ops の Actions secret(`AI_OPS_APP_ID` / `AI_OPS_APP_PRIVATE_KEY`) | **稼働中(2026-09-21 実証)**。秘密鍵に期限は無い |
| `AI_OPS_TOKEN` | 旧。全 repo の Administration ほか | — | **役目を終えた。削除する**(2026-09-21) |
| `BUTLER_API_KEY` | itch.io へのアップロード | tetrishoot の Actions secret | 有効。将来はアカウント単位に集約 |
| `CLOUDFLARE_API_TOKEN` | Pages のデプロイ | 未設定 | 未 |

## ローカル PC(3 ゾーン方式 → decisions/2026-09-13-permission-zones.md)

| ゾーン | 対象 | AI の扱い |
|---|---|---|
| A 自由 | `E:\`(ゲーム・個人開発)、`G:\マイドライブ` の個人開発フォルダ | 確認なしで読み書き |
| B 確認 | `G:` の個人の仕事データ、システム領域、仕事の SaaS にログインした Chrome | 読むのは自由、書き換え前に許可を取る |
| C 社外 | 社外ドライブ(G: 内ショートカット)、他社 SaaS | 直接触らない。outbox 経由で配達係が反映 |

未実装: B・C への書き込みを止める hook(topics/11 の次の作業)。

## 外部サービス

| サービス | 用途 | 資格情報 | 状態 |
|---|---|---|---|
| itch.io(mukkii) | ゲーム公開 | API キー → GitHub secret | 稼働 |
| Google(仕事と個人が同一アカウント) | Drive 5TB、GAS、スプシ | デスクトップ版 Drive で `G:` にマウント | 稼働。分離は第 2 段階 |
| Chrome 拡張の Claude | ブラウザ操作 | ログイン中のプロファイル | 稼働。**開発専用プロファイルに分ける予定** |
| Facebook | (fb-radio-auto 用だった) | cookie | 2026-09-14 全デバイスログアウトで無効化 |
| Render | (fb-radio-auto 用だった) | — | 2026-09-14 プロジェクト削除 |
| Newgrounds / PLiCy | ゲーム公開(自動投稿予定) | 投稿用の専用 Chrome プロファイル | 未 |
| Cloudflare | Pages / Workers / R2 | API トークン | 未 |

## 有効期限のあるもの(切れると黙って 403 で落ちる)

| 対象 | 期限 | 警告を出す日 | 切れると止まるもの |
|---|---|---|---|
| (いまは無し) | — | — | — |

`AI_OPS_TOKEN`(期限 2026-09-28)は GitHub App に置き換えて不要になった(2026-09-21)。
期限のある鍵を新たに作ったら、必ずこの表に足すこと。週次レビューは毎週この表を見て、
期限の 2 週間前から警告する。

### GitHub App への移行(2026-09-21 完了)

期限そのものを無くすため App 方式へ移行した。秘密鍵に期限は無く、実行時に発行される
トークンは 1 時間で失効するので、更新作業が消えたうえで安全性も上がった。

- 仕組み: `ai-ops/scripts/app-token.sh` が JWT を作って installation token を取る。
  外部アクションは増やしていない(curl と openssl のみ)。App が未設定なら旧 PAT へ退避する。
- 実証: 2026-09-21 の Remove Legacy Ruleset 実行で
  `token source: GitHub App installation 163455635 (expires in 1 hour)` を確認。
- 事故: 途中で秘密鍵をチャットに添付してしまい、その鍵は破棄して作り直した(未インストールのため実害なし)。

## 直近でやること
- [x] mukkii-game は All repositories(確認済み 2026-09-16)
- [x] Studio-Shimazu は連携なし。対応不要(2026-09-16)
- [x] `AI_OPS_TOKEN` を GitHub App に置き換える(2026-09-21 実証済み)
- [ ] `AI_OPS_TOKEN` を secret とトークン本体の両方から削除する(ユーザー作業)
- [ ] B・C ゾーンの書き込みを止める hook
- [ ] Chrome を開発専用プロファイルに分ける
