# global/ — どのセッションにも入る決まりの正本

`constitution.md` は全セッションが毎回読む。**3 行を超えて増やさない**(全部の作業に課税される)。
足したくなったら、スキルか作品の AGENTS.md に置けないかを先に考える。毎月の指示書監査の対象。

入れ方(クラウドはセットアップ用スクリプト、PC はその PC で 1 回。既存の ~/.claude/CLAUDE.md は消さず、読み込み行を足すだけ):

```
mkdir -p ~/.claude/skills/war-room-knowhow && R=https://raw.githubusercontent.com/mukkii-game/Perfect_Dev_Environment/main && curl -sfL $R/skills/war-room-knowhow/SKILL.md -o ~/.claude/skills/war-room-knowhow/SKILL.md; curl -sfL $R/global/constitution.md -o ~/.claude/war-room-constitution.md && (grep -qs war-room-constitution ~/.claude/CLAUDE.md || echo '@~/.claude/war-room-constitution.md' >> ~/.claude/CLAUDE.md); true
```
