# PC の Claude Code に入れる設定(2026-10-13)

雛形の作品には `.claude/settings.json` で入っているが、PC 全体(雛形を使わない作品・企画・MOD も)に効かせるために PC にも入れる。
**入れ方**: PC の Claude Code(どのフォルダでもよい)に「会議室の global/pc-claude-settings.md を読んで、その通りに設定して」と頼む。
既にある `~/.claude/settings.json`(Windows は `%USERPROFILE%\.claude\settings.json`)は消さず、`hooks` に足すだけにする。

## 1. 圧縮・/clear のあとに申し送りを読み直す
作業フォルダに HANDOFF.md(無ければ docs/50_resume.md)があれば、先頭 80 行を会話に戻す。Windows でも動くよう node で書く。
```json
{
  "hooks": {
    "SessionStart": [
      {
        "matcher": "compact|clear",
        "hooks": [
          { "type": "command", "command": "node -e \"const fs=require('fs');for(const f of ['HANDOFF.md','docs/50_resume.md']){try{console.log('--- '+f+'(圧縮のあとに自動で読み直し)---\\n'+fs.readFileSync(f,'utf8').split('\\n').slice(0,80).join('\\n'));break}catch(e){}}\"" }
        ]
      }
    ]
  }
}
```

## 2. 全体の決まり(憲法)を最新にする
`global/README.md` の 1 行コマンドをもう一度流す(war-room-knowhow スキルと憲法 `~/.claude/war-room-constitution.md` を取り直す)。

## 確かめ方
新しいセッションで何か作業をして `/compact` → 返事の最初に HANDOFF の中身が見えていれば成功。
