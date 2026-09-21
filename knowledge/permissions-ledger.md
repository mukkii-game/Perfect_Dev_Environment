# 権限の棚卸し表

> AI と外部サービスに「今どこまで許可しているか」の一覧。
> 変更したら必ずここを直す。月 1 で Routine が差分を点検する(topics/11)。
> 最終更新: 2026-09-16

## GitHub

| 対象 | 許可の範囲 | 置き場 | 状態 |
|---|---|---|---|
| Claude(GitHub App) / mukkii-game | **All repositories**。actions / checks / code / discussions / issues / pull requests / repository hooks / workflows の読み書き + コミット状態の読み取り。公開リポジトリは読み取り専用で含む | GitHub アプリ設定 | **確認済み(2026-09-16)。設定変更は不要** |
| Studio-Shimazu の repo が一覧に出る件 | **連携は入っていない**。3 本(Iwanna4Udemy / SteamLeaderboard / SoundGameOchiru)がいずれも public のため、上記の「公開リポジトリは読み取り専用」条項で見えているだけ。書き換えは不可 | — | **対応不要(2026-09-16 調査)** |
| `AI_OPS_TOKEN` | 全 repo の Administration / Contents / Pages / PR 書き込み。**最も強い** | ai-ops の Actions secret | **有効期限 2026-09-28**(fine-grained PAT)。更新は人間の手作業。使う時だけ有効化する運用に変える(topics/11) |
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
| `AI_OPS_TOKEN` | **2026-09-28** → 更新したら書き換える | 期限の 2 週間前 | ai-ops の repo 作成・Pages 設定・Topics 付与 = 新作を立てる導線 |

### GitHub App への移行(2026-09-21 着手・**PC 待ちで中断**)

期限そのものを無くすため、App 方式へ移る。App の秘密鍵には期限が無く、実行時に
発行されるトークンは 1 時間で失効するので、更新作業が消えて安全性も上がる。

- ai-ops 側は**対応済み**(`scripts/app-token.sh`)。App の secret を入れた瞬間に自動で切り替わる。
  入るまでは従来どおり `AI_OPS_TOKEN` で動くので、放置しても壊れない。
- App は作成済み。**App ID 5019353**。インストールと秘密鍵の投入が残り。
- 中断の理由: iPhone だけでは秘密鍵の `.pem` を受け取れなかった(Safari のダウンロードに現れない)。
  **PC の前に座った時に 5 分で片付ける**。鍵は作り直せるので、今ある 2 本は放置でよい。
- 残り作業: ①App を All repositories にインストール ②鍵を作り直して
  `AI_OPS_APP_ID` / `AI_OPS_APP_PRIVATE_KEY` を ai-ops の secret へ ③空打ちしてログに
  `token source: GitHub App installation ...` が出るのを確認 ④`AI_OPS_TOKEN` を削除

更新手順: GitHub → <https://github.com/settings/personal-access-tokens> → 当該トークン →
Regenerate token(**権限は広げない**・期限 90 days)→ 新しい値を ai-ops の Actions secret へ貼る。
**値をチャットに貼らないこと。** 更新したら、この表の期限と警告日を書き換える。

週次レビューは毎週この表を見て、期限の 2 週間前から警告すること。

## 直近でやること
- [x] mukkii-game は All repositories(確認済み 2026-09-16)
- [x] Studio-Shimazu は連携なし。対応不要(2026-09-16)
- [ ] **`AI_OPS_TOKEN` を 2026-09-28 までに更新する**(期限切れ間近。2026-09-21 発見)
- [ ] `AI_OPS_TOKEN` を使う時だけ有効化する運用へ
- [ ] B・C ゾーンの書き込みを止める hook
- [ ] Chrome を開発専用プロファイルに分ける
