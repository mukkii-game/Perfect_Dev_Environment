# クラウド環境の許可ドメイン(素材サイト)

クラウドの「環境」は全作品のセッションで共有(既定 env_01Hnx6…)。許可は環境に足せば全作品に効く。
足し方: セッションの題名欄の環境メニュー → 編集 → ネットワーク → Allowed domains(「パッケージマネージャを許可」は付けたまま)。手順: https://code.claude.com/docs/en/cloud-environments#network-access
素材を新しく使う時に拒否されたら(curl が 000 / connect_rejected)、ここに足して Mukkii に頼む。

## 実測(2026-10-16、会議室のセッションから curl)
- 通る: pipoya.net / maou.audio / dova-s.jp / kenney.nl / opengameart.org / github.com / raw.githubusercontent.com / fonts.gstatic.com
- 拒否(足す候補): 下の貼り付け用リスト

## 貼り付け用(足す候補)
```
soundeffect-lab.info
otologic.jp
pocket-se.info
taira-komori.jp
kurage-kosho.info
on-jin.com
amachamusic.chagasi.com
musmus.main.jp
www.hmix.net
www.irasutoya.com
1.bp.blogspot.com
itch.io
img.itch.zone
game-icons.net
quaternius.com
polyhaven.com
dl.polyhaven.org
ambientcg.com
www.ac-illust.com
freesound.org
cdn.freesound.org
pixabay.com
cdn.pixabay.com
fonts.google.com
drive.google.com
drive.usercontent.google.com
docs.google.com
```
- ぴぽやの zip は Google Drive 経由(drive.* が要る。未確認)。
- itch.io の配布ファイルは別ホストに飛ぶことがある(足した後に実測して追記する)。
