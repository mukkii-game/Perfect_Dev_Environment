# クラウド環境の許可ドメイン(素材サイト)

クラウドの「環境」は全作品のセッションで共有(既定 env_01Hnx6…)。許可は環境に足せば全作品に効く。
足し方: セッションの題名欄の環境メニュー → 編集 → ネットワーク → Allowed domains(「パッケージマネージャを許可」は付けたまま)。手順: https://code.claude.com/docs/en/cloud-environments#network-access
素材を新しく使う時に拒否されたら(curl が 000 / connect_rejected)、ここに足して Mukkii に頼む。

## 実測(2026-10-16、会議室のセッションから curl)
- 通る: pipoya.net / maou.audio / dova-s.jp / kenney.nl / opengameart.org / github.com / raw.githubusercontent.com / fonts.gstatic.com
- 拒否(足す候補): 下の貼り付け用リスト

## なぜ拒否されるか(2026-10-16 公式文書で確認)
- 環境のネットワークは「Trusted(既定: パッケージ置き場だけ)/ Custom(自分のリスト)/ Full(どこでも)/ None」の 4 段階。今の環境は Custom で、ぴぽや・魔王魂など足した分だけ通る。
- 変えられるのは Mukkii だけ(環境の設定画面)。AI からは変えられない。GitHub と MCP コネクタ(Mucky Reader 等)はこのリストを通らない。
- 先頭の `*.` で全サブドメインに効く。
- 抜け道(GitHub Actions で代わりに落として repo に置く)は、auto mode が「安全の弱体化」として止めた(10/16)。作るなら Mukkii の明示の許可が要る。

## 貼り付け用(価値ありと判断した素材・資料サイト全部。1 行 1 つ)
```
*.pipoya.net
pipoya.net
soundeffect-lab.info
*.soundeffect-lab.info
otologic.jp
pocket-se.info
taira-komori.jp
kurage-kosho.info
on-jin.com
amachamusic.chagasi.com
musmus.main.jp
www.hmix.net
maou.audio
dova-s.jp
*.dova-s.jp
youfulca.com
*.youfulca.com
www.irasutoya.com
*.bp.blogspot.com
*.ac-illust.com
*.illust-ac.com
kenney.nl
*.kenney.nl
opengameart.org
*.opengameart.org
itch.io
*.itch.io
*.itch.zone
game-icons.net
quaternius.com
*.quaternius.com
polyhaven.com
*.polyhaven.com
*.polyhaven.org
ambientcg.com
*.ambientcg.com
sketchfab.com
*.sketchfab.com
3dyasan.com
freesound.org
*.freesound.org
pixabay.com
*.pixabay.com
fonts.google.com
fonts.googleapis.com
fonts.gstatic.com
*.googleusercontent.com
drive.google.com
drive.usercontent.google.com
docs.google.com
automaton-media.com
news.denfaminicogamer.jp
gamesindustry.biz
www.gamedeveloper.com
www.4gamer.net
```
- 「パッケージマネージャを許可」のチェックは付けたまま(npm 等が止まる)。
- ぴぽやの zip は Google Drive 経由なので drive.* を入れてある。
- 記事サイト(AUTOMATON 等)は読めなかった実績があるので一緒に入れた。
- 新しい素材サイトを使う時に拒否されたら、ここに足して Mukkii に 1 行で頼む。

## Full にする選択肢
- どこでも通るので「使いたい時に使えない」は無くなる。代わりに、読んだページに仕込まれた指示で AI が外へ情報を送る危険の歯止めが無くなる。この環境には秘密の鍵を置いていない(鍵は GitHub の secrets)ので被害は小さいが、会議室はリスト方式を勧める。
