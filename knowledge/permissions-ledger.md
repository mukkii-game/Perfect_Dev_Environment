# 権限の棚卸し表

> AI と外部サービスに「今どこまで許可しているか」の一覧。
> 変更したら必ずここを直す。月 1 で Routine が差分を点検する(topics/11)。
> 最終更新: 2026-09-16

## GitHub

| 対象 | 許可の範囲 | 置き場 | 状態 |
|---|---|---|---|
| Claude(GitHub App) / mukkii-game | **All repositories**。actions / checks / code / discussions / issues / pull requests / repository hooks / workflows の読み書き + コミット状態の読み取り。公開リポジトリは読み取り専用で含む | GitHub アプリ設定 | **確認済み(2026-09-16)。設定変更は不要** |
| Studio-Shimazu の repo が一覧に出る件 | **連携は入っていない**。3 本(Iwanna4Udemy / SteamLeaderboard / SoundGameOchiru)がいずれも public のため、上記の「公開リポジトリは読み取り専用」条項で見えているだけ。書き換えは不可 | — | **対応不要(2026-09-16 調査)** |
| `AI_OPS_TOKEN` | 全 repo の Administration / Contents / Pages / PR 書き込み。**最も強い** | ai-ops の Actions secret | 有効。使う時だけ有効化する運用に変える(topics/11) |
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

## 直近でやること
- [x] mukkii-game は All repositories(確認済み 2026-09-16)
- [x] Studio-Shimazu は連携なし。対応不要(2026-09-16)
- [ ] `AI_OPS_TOKEN` を使う時だけ有効化する運用へ
- [ ] B・C ゾーンの書き込みを止める hook
- [ ] Chrome を開発専用プロファイルに分ける
