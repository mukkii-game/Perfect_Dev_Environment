# ローグライク・ローグライト(ターン制ダンジョン、デッキ構築、サバイバー系)

使い方: 作る前に 1〜2 と、作る型(A/B/C)の節を読む。数値は「つまみ候補」として `src/tuning.ts` に入れ、F2 で人が直す前提の初期値。最終更新: 2026-10-12。
確かさの印: 【実測】うちの作品で確かめた /【定説】複数の出典が一致 /【一説】1 出典だけ(または攻略 wiki・ファンの解析)。印の無い数値は、このファイルが置いた仮の値。
3 つの型: **A. ターン制ダンジョン**(Rogue・不思議のダンジョン・Brogue)/ **B. デッキ構築**(Slay the Spire 系。以下 StS)/ **C. サバイバー系**(Vampire Survivors 系。以下 VS。自動で撃ち、移動とレベルアップの選択だけ)。
用語: ラン = 1 回の挑戦(死ぬかクリアで終わる)。メタ進行 = ランをまたいで残る成長・解放。レリック = ラン中ずっと効く持ち物。ビルド = ラン中に集めた組み合わせ。アセンション = クリア後に 1 段ずつ解放される高難度。インテント = 敵が次に何をするかの表示。

---

## 1. 芯と、1 日で作るパイロットの最小構成

### 芯(これがあればこのジャンルと感じる)
- **毎回ちがう、でも読める**: 地形・報酬・敵の並びがランごとに変わる。ただし規則は毎回同じなので、上手くなるのは知識と判断。【定説】Berlin Interpretation(2008、高価値の要素に「ランダム生成」「永久死」「資源管理」「探索と発見」)/ GMTK「The Two Types of Random in Game Design」
- **運は選ぶ前に置く**: 配られた手札・出た報酬・地図(入力の運)に対して計画を立てさせる。行動の後に結果が揺れる運(命中判定)は少なめに。【定説】GMTK 同上 / `../game-design.md` §8「運の置き場」
- **選ぶ = ビルドが育つ**: 報酬は「全部取る」ではなく「数個から 1 つ」。何を取らないかがその回の個性になる。【定説】`../game-design.md` §8「選択の重み」(Sid Meier「Interesting Decisions」)/ 電撃オンラインの VS 紹介(3 つから 1 つ)
- **死んでも、すぐもう 1 回**: 1 ランが短く、負けの理由が見え、次のランに知識(とローグライトなら少しの強化)が残る。【定説】GDC「Roguelikes And Narrative Design With Hades」(Greg Kasavin)/ `../game-design.md` §8「失敗の安さ」「公平な負け」

### 1 日パイロットの最小構成(型ごと。この順で作る)
- **A. ターン制ダンジョン**: ① 40×25 マスの部屋と通路(rot.js `Map.Digger`)② 主人公 1 歩 = 敵 1 歩 ③ 敵 3 種(近づいて殴る / 遠くから撃つ / 遅いが硬い)④ 体力と回復薬、階段で次の階、3 階で終わり ⑤ 視界(rot.js FOV)⑥ 持ち物 4 種(回復・投げる・巻物で全体攻撃・装備 1 つ)。後回し: 識別、満腹度、店、罠。
- **B. デッキ構築**: ① 初期デッキ 10 枚(攻撃 5・防御 4・特別 1)、手札 5 枚、エネルギー 3 ② 敵 4 種 + エリート 1 + ボス 1、全部インテント表示 ③ 勝つとカード 3 枚から 1 枚(取らないも可)④ 地図 1 幕 = 10〜15 階の分岐 ⑤ 休憩所(回復 or 強化)⑥ 状態異常 2 つ(弱体・脆弱)と筋力。後回し: 店、イベント、ポーション、レリック 10 個以上。
- **C. サバイバー系**: ① 自機は移動だけ、武器は自動 ② 敵は画面外から湧き、まっすぐ寄る(3 種)③ 倒すと経験値の玉、拾うとバーが溜まり、レベルアップで 3 択(新しい武器 / 今の武器の強化 / 受け身の強化)④ 武器 4 種 × 5 段階 ⑤ 10 分で終わり(最後に強い敵)⑥ 結果画面でお金 → 次のランの強化 1 種。後回し: 進化、キャラ選択、宝箱、複数ステージ。
- 3 型とも: `?seed=` で同じランが出る / `?auto=1` で bot が最後まで遊ぶ / 1 ランの記録(seed + 選んだ番号の列)を `?replay=` で再生(§3)。

---

## 2. よく使うゲームシステムとゲームフロー

### ランの形
- **フロー**: タイトル → (キャラ・難易度を選ぶ)→ ラン(地図 → 戦闘 → 報酬 → 地図 …)→ ボス → 次の幕 or 結果画面 → メタ進行の画面 → もう一度。結果画面からもう一度までは 1 タップ。
- **ローグライクとローグライト**: Berlin Interpretation は「どれだけローグらしいか」を点で測るもので、条件の表ではない(欠けても失格ではない)。低価値の要素に「ASCII 表示」「ダンジョン」「数値の表示」。ランをまたいで強くなる要素(メタ進行)があるものを今は「ローグライト」と呼び分けることが多い。【定説】Wikipedia「Roguelike」/ PC Gamer フォーラム
- **永久死の重さを選ぶ**: 全部消える(Rogue)/ 知識と解放だけ残る(StS)/ 通貨で強くなる(Hades・VS)。重いほど 1 手の緊張が増し、軽いほど気軽に周回できる。Darkest Dungeon はセーブのやり直しを封じ、育てたキャラが一度で消える重さを芯にした。【一説】GDC「Darkest Dungeon: A Design Postmortem」(Tyler Sigman, 2017)
- **死を物語にする**: 主人公が死んでも戻る設定にすると、繰り返しがそのまま話になる。ボスが「また来たか」と覚えていると、負けたランにも意味が残る。【一説】GDC Hades(Kasavin)

### メタ進行・アンロック
- **解放は「強さ」より「種類」から**: 新しいカード・武器・キャラを少しずつ混ぜると、毎回の新鮮さと学びの順番が同時に作れる。最初から全部入れると、1 ラン目の選択肢が多すぎて読めない。KeyForge はレア度を「強さ」ではなく「理解に要る知識の量」に合わせた(よく出るものほど単純)。【一説】GDC Board Game Design Day「KeyForge: Creating the World's First Unique Deck」
- **数値の永続強化はインフレに注意**: 永続強化があると後半は一方的に有利になる。進み具合(全体の何 % を解放したか)に合わせて敵側にも新しい危険を足す。【一説】GMTK の Prey: Mooncrash 分析
- **リセットで加速**: 伸びが鈍ったら全部を戻す代わりに次の伸びを速くする(放置ゲームのプレステージ)。ローグライトのメタ通貨と同じ形。【一説】GDC「Idle Games: The Mechanics and Monetization of Self-Playing Games」
- **偽の締め切りを出さない**: 制限が無いのに「◯日目」と数を出すと、焦りだけが生まれる。【一説】GMTK「Blue Prince: Can a random puzzle game actually work?」
- **複数の小さな目標**: ランの勝ち負け 1 つだけだと運が悪い回に何も残らない。「エリートを 3 体」「この武器で 10 分」など小さな目標(実績・解放条件)を並べる。【一説】GMTK Blue Prince

### 地図の分岐(B 型の要。A・C にも持ち出せる)
- **StS の地図**: 1 幕 = 縦 15 階 × 横 7 列の格子に、交わらない道を何本か引く。1 階は全部ふつうの戦闘、9 階は宝箱、15 階は全部休憩所、その上にボス。エリートと休憩所は 6 階より下に置かない。エリート・店・休憩所は続けて並べない。【一説】ファンの解析「Slay the Spire: Map Generation Guide」(kosgames)/ Slay the Spire wiki「Map Generation」(部屋の割合の表は未確認)
- **見せるのは種類だけ**: 部屋の種類(戦闘・エリート・休憩・店・イベント)は地図で先に見せ、中身は入るまで隠す。「どの道を通るか」が 1 幕ぶんの計画になる。
- **本道と寄り道**: 生成した地図で、入口からゴールまでの最短の道(本道)は敵も報酬も少なめ、外れた所に強い敵と大きな報酬。急ぐか寄るかの判断が生まれる。【一説】GDC「Game Design Case Studies - One Designer」(Shattered Planet の例)

### 戦闘の流れ(B 型)
- 自分の番: 山札から 5 枚引く → エネルギー 3 の範囲で出す → 残りは捨て札へ → 敵の番(表示どおりに行動)→ 敵が次のインテントを出す。山札が尽きたら捨て札を混ぜ直す。【一説】StS の遊び方(Slay the Web も同じ)
- **カードを減らせる**: 店やイベントで弱いカードを抜けると、デッキ(自分の山)の運を自分で操れる。運に振り回されている感じが減る。【一説】GMTK Blue Prince(山を自分で調整できる仕組みの比較)

### サバイバー系の流れ(C 型)
- 移動 → 武器が自動で撃つ → 玉を拾う → レベルアップ(時間を止めて 3〜4 択)→ 数分ごとに強い敵・宝箱 → 終了時刻に最後の敵。武器を最大まで上げ、対応する受け身の持ち物があると「進化」する。進化の条件(レベルアップの選択肢に出るか、ボスの宝箱か)は攻略記事で食い違う。【一説】攻略記事複数(未整理)
- 30 分で 1 ラン、のちに 20 分・15 分にする速度の選択肢が足された。【一説】Superjump Magazine の振り返り記事(2025)/ 30 分生存でクリアの例(20 Minutes Till Dawn の紹介、Inside Games)

---

## 3. よく使うデータ構造(この雛形での書き方)

雛形の決まり: 中身は `src/game/logic.ts` の `step(state, input, cfg)` で進め、Phaser・DOM・`Math.random` を使わない。乱数は `core/rng.ts` の `Rng`(mulberry32)。記録は `core/replay.ts`(seed + 「何フレーム目に何を入力したか」の文字列)。

### ターン制を tick の雛形に載せる(A・B 型)
- step は 1/60 秒ごとに呼ばれるが、**行動が来た tick だけ盤面を進める**。演出(移動のアニメ・ダメージの数字)は描画側が出来事の列(step の戻り値)を見て勝手に流す。中身は待たない。
- 入力は「意味単位の行動 1 つ」。replay は同じフレームの入力を連結するので、1 フレーム 1 行動にする。
```ts
// A 型: 'h' 'j' 'k' 'l' 'y' 'u' 'b' 'n'(8 方向)/ '.' 待つ / 'g' 拾う / 'i3' 持ち物 3 番を使う / '>' 降りる
// B 型: 'p2t1' 手札 2 番を敵 1 に / 'e' ターン終了 / 'r1' 報酬 1 番 / 'rs' 報酬を取らない / 'm4' 地図の 4 番へ
export type Input = { act: string | null };   // null = この tick は何もしない
export function encodeInput(i: Input) { return i.act ?? ''; }
```
- **1 ランの記録 = seed + 行動の列**。B 型なら数百文字。結果画面に「この回を共有」ボタン(`?replay=`)を置くと、バグ報告と自慢の両方に使える。

### 乱数は用途ごとに分ける(全型)
- 地図・報酬・戦闘のシャッフル・敵の行動・ドロップを **1 本の乱数で回すと、1 回の選択の違いで地図まで変わる**(同じ seed で比べられない)。seed から用途ごとの `Rng` を作る。StS も用途別に乱数を持つ(カード報酬・敵・イベント・シャッフル…)。【一説】StS の改造コミュニティの解析(ゲーム本体のコード)
```ts
const sub = (seed: number, tag: string) => new Rng((seed ^ [...tag].reduce((h, c) => Math.imul(h ^ c.charCodeAt(0), 16777619), 2166136261)) >>> 0);
state.rng = { map: sub(seed, 'map'), reward: sub(seed, 'reward'), shuffle: sub(seed, 'shuffle'), ai: sub(seed, 'ai'), loot: sub(seed, 'loot') };
// 階・戦闘ごとに作り直すとさらに安定: sub(seed, `floor${n}`)
```
- ボットの乱数はゲームと別(雛形 `bots.ts` の注意と同じ)。

### ダンジョン生成(A 型。B・C の地図にも)
- **rot.js**(npm `rot-js` 2.2.1、BSD-3-Clause)に部屋と通路(`Map.Digger` / `Map.Uniform`)・洞窟(`Map.Cellular`)・迷路・視界(`FOV.PreciseShadowcasting`)・経路(`Path.AStar` / `Path.Dijkstra`)・行動順(`Scheduler.Speed`)がそろう。`assets.csv` で A ランク。
- 罠: rot.js は自前の乱数 `ROT.RNG` を使う。**生成の直前に毎回 `ROT.RNG.setSeed(state.rng.map.int(1, 2**31))`** して、生成の順番を固定する。これを忘れると `?seed=` で同じ階が出ない。
- **作ったら必ず歩けるか確かめる**: 入口から塗りつぶし(flood fill)か経路探索で、階段・鍵・必須の部屋に届くか。届かなければ作り直し(seed を 1 進めて再生成)。【定説】GDC「Game Design Case Studies - One Designer」/ GDC「Procedural Level Design in Eldritch」
- **部屋と迷路**: 部屋を置く → 隙間を迷路で埋める → 部屋と迷路をつなぐ → 行き止まりを削る → 少し壁を抜いてループを作る。ループがあると逃げ道と回り込みが生まれる。【定説】Bob Nystrom「Rooms and Mazes」(2014)/ GDC Eldritch(生成後に壁を消してループ)
- **洞窟**: セルの周り 8 マスの壁の数で壁か床かを決める(セル・オートマトン)を数回かける。四角い部屋の縁だけにかけると「崩れた部屋」になる。【一説】GDC One Designer
- **手作りの部品をつなぐ**: 部屋の型を手で作り、外周の「必ず開いている帯」を決めておくと、どれを隣に置いても通れる。回転・反転で型の数を減らす。部品にテーマの札(廃墟・洞窟)を付け、階ごとに主テーマを優先すると見た目がまとまる。【一説】GDC Eldritch
- まず手で「見本の階」を 1 つ作り、それに近いものが出るように生成を書く。【一説】GDC One Designer

### カードと効果の定義(B 型。C の武器・A の持ち物も同じ形)
```ts
// src/game/cards.ts — データだけ。文章(i18n キー)と数値を分ける
type Effect = { op: 'damage' | 'block' | 'draw' | 'apply' | 'energy'; n: number; status?: string; target?: 'enemy' | 'all' | 'self' };
type Card = { id: string; cost: number; type: 'attack' | 'skill' | 'power'; rarity: 'starter' | 'common' | 'uncommon' | 'rare';
              target: 'enemy' | 'none'; effects: Effect[]; up: Partial<Card>; tags: string[] };  // tags: 'block' 'poison' 'draw' … ビルドの軸
export const CARDS: Card[] = [
  { id: 'strike', cost: 1, type: 'attack', rarity: 'starter', target: 'enemy', effects: [{ op: 'damage', n: 6 }], up: { effects: [{ op: 'damage', n: 9 }] }, tags: [] },
];
```
- 効果は小さな命令の列にして、1 つの関数(解釈器)で順に実行する。カードを足す = データを足す、にする。
- 状態異常・レリックは「割り込みの口」(ターン開始・攻撃の計算・ダメージを受けた時・カードを出した時)に関数を登録する形。**計算の順番を決めて書く**: 足し算 → 掛け算、を固定するか、取った順に適用する(Balatro・Word Play は持っている順で倍率がかかり、並べ替えが遊びになった)。【一説】GMTK の Word Play 分析
- カードに「どの戦略を支える札か」のタグを付けておくと、bot の記録から「この戦略の札が足りない」が数えられる。【一説】GDC「Board Game Design Day」の Cavemen の例

### ターン順・行動順(A 型)
- 速さの違う敵は、速さに比例して順番が来る予定表(rot.js `Scheduler.Speed`、または「次に動ける時刻」が一番早いものから動かす)。主人公の番で止まり、入力を待つ。
- B 型の敵: 毎ターンの行動を表(パターン)か重み付きの抽選で決め、**決めた時点で表示**(インテント)。抽選は前のターンに決めて、プレイヤーはそれを見て手を考える。

### C 型の中身
- 敵・弾・経験値の玉は固定長の配列で使い回す(object pool)。敵の数は数百、当たり判定は格子で分ける(`shmup.md` §3 と同じ)。
- 湧き方は「開始からの分」の表: `{ t: 60, enemy: 'bat', every: 0.5, ring: false }`。武器は段階の表: `{ id: 'knife', lv: [{ dmg: 10, every: 1.0, count: 1 }, …] }`。

### ボットで「選ぶ意味」を測る(雛形 `npm run sim` / `src/game/bots.ts`)
雛形のボットは idle / random / think / think+遅れ。このジャンルでは「何を選ぶか」の質を比べる形に替える。勝率・到達した階・残り体力・時間を並べる。
- **報酬の選び方で比べる**: `rs`(報酬を一度も取らない)/ `first`(いつも 1 番目)/ `random`(でたらめに選ぶ)/ `greedy`(数字が一番大きい札)/ `think`(今のデッキの軸のタグに合う札、なければ取らない)。
  - random と think の勝率差が小さい → 報酬の選択に意味が無い(どれも同じ強さ、または多すぎて薄まる)。雛形の警告(random が think の 8 割以上)をそのまま使える。
  - `rs` が random より強い → 取るほど弱くなる(デッキが薄まる)設計。狙いならよいが、報酬が「罰」に見えていないか確かめる。
  - greedy が think より強い → 組み合わせより単体の強さが勝つ。ビルドの面白さが出ていない。
- **戦闘の手の打ち方で比べる**(B 型): `random`(出せる札をでたらめ)/ `attack`(攻撃だけ)/ `think`(インテントを見て、攻撃が来るなら防御、来ないなら攻撃)。attack が think と同じ → インテントを見る意味が無い。
- **札 1 枚ごとの勝率**: 取ったランと取らなかったランの勝率の差を全カードで出す(StS はプレイ結果を集めるサーバーで、使用率と勝率からバランスを直した)。差が飛び抜けた札は強すぎ、どの bot も取らない札は役目が無い。【一説】GDC「Slay the Spire: Metrics Driven Design and Balance」(Anthony Giovannetti, 2019)
- **A 型**: `core/probe.ts` に意味単位の操作(「階段へ向かう」「3 番を使う」「一番近い敵を殴る」)を登録し、bot も AI も同じ口で遊ぶ。トルネコを AI に 134 回遊ばせた記録では、AI は慎重すぎて持ち物を抱えたまま死にがちで、「危険を取ってよい」と伝えて改善した。【一説】`../process-patterns.md` §6(giginet)
- **C 型**: idle(立ったまま)の生存時間、random(でたらめに歩く)、think(敵の少ない方へ逃げつつ玉を拾う)、think の 0.4 秒遅れ。idle が終了時刻まで生きる → 敵が届いていない。
- 固定の動き方の bot で、難易度の穴(楽に勝てる道)が見つかった例がある(アクション・ローグライク)。【一説】fugudaro(`../sources.md`)

---

## 4. よく使うゲームバランスの指針

| 項目 | 初期値(つまみ候補) | 根拠・印 |
|---|---|---|
| 1 ランの長さ | パイロット 10〜15 分(B: 1 幕 10〜15 階 / C: 10 分) | VS は 30 分、のちに 20・15 分の速度を追加【一説】Superjump。StS は 3 幕 + 最終幕 |
| 報酬の選択肢の数 | 3(取らないも可) | StS のカード報酬は 3 枚【一説】StS wiki「Card Rewards」。VS 系のレベルアップは 3〜4 択【一説】電撃オンライン |
| カードのレア度(ふつうの戦闘) | 普通 60% / 珍しい 37% / レア 3% | StS【定説】StS wiki「Card Rewards」/ Steam コミュニティの計算式 |
| 〃(エリート / ボス / 店) | 50/40/10 / ボスは全部レア / 54/37/9 | 同上 |
| レアの天井(救済) | レアの確率を −5% から始め、普通が出るたび +1%、レアが出たら −5% に戻す(上限 +40%) | StS【定説】同上。「しばらく出ないと出やすくなる」で、体感の不公平を減らす |
| 初期デッキ・手札・エネルギー | 10 枚・5 枚・3 | StS の最初のキャラ(攻撃 5・防御 4・特別 1)【一説】StS wiki |
| 難易度の段階 | 5 段(パイロット)。1 段ずつ解放、下の段の効果は全部重なる | StS は 20 段、StS2 早期アクセスは 10 段。1 段目は両方とも「エリートが増える」【定説】PCGamesN / Untapped / TrueAchievements |
| 1 戦闘の長さ(B) | 3〜6 ターン | 仮 |
| 階ごとの敵の強さ | 体力・攻撃 ×1.1/階(A)、幕ごとに敵の表を入れ替え(B) | 仮 |

- **アセンションの足し方**: 数値を硬くする段(敵の体力・攻撃)と、ルールを変える段(回復が減る、呪いのカードを持って始まる、ボスが 2 体)を交互に。数値だけだと同じ遊びの作業になる。【一説】StS2 の段の一覧(PCGamesN / Untapped)
- **壊れたビルドは許す**(1 人用): 狙って作れた強すぎる組み合わせはご褒美。直すのは「どのランでも同じ札を取れば勝てる」状態(支配戦略)だけ。苦情の「この札が強すぎる」は、実は代わりの選択肢が無いだけのことが多い。【定説】GDC「Balancing Cards in Clash Royale」/ GDC「Puzzle Strike A Design Diary」
- **弱くするより強くする**: 強い札を弱くすると使っていた人が怒る。弱い札を強くする方が角が立たない(対戦の話だが、配布後の調整に効く)。【一説】GDC Clash Royale
- **どの札にも輝く場面を**: 常に一番の札も、常に無駄な札も作らない。札ごとに「これが最高になる状況」を 1 つ決める。新しい札は既存の強化版ではなく、空いている役目を埋める。【定説】GDC Clash Royale / GDC Puzzle Strike
- **無限の組み合わせ**: 1 ターンに何度でも回る組み合わせは、見つけた人の自慢になる一方、bot が見つけると戦闘が終わらない。1 ターンの行動数に上限(例 100)を置き、超えたら敵を倒した扱いにする。仮
- **攻め・守り・経済の三すくみ**: 守りが強すぎる環境には、守りを無視する攻撃(貫通・毒)を 1 系統入れる。【一説】GDC Puzzle Strike
- **選んだ後の運は小さく**: B 型のダメージは固定(乱数なし)、A 型の命中も高め(85〜95%)。外れが続いた時の体感の悪さは、実際の確率以上に大きい。不思議のダンジョンの開発者も「実際の確率と体感の確率の差」を語っている。【一説】電ファミニコゲーマー「不思議のダンジョン」中村光一・長畑成一郎インタビュー(見出しと要約のみ確認)
- **時間の圧で最適解に落ち着かせない**: 何もしないで守りを固めるのが最善になったら、敵の「数ターンで強くなる」・時間制限を足す。【一説】GMTK の Prey: Mooncrash 分析
- **つまみ候補の一覧**(`src/tuning.ts` に入れる): `run.floors` `run.minutes` `reward.choices` `reward.skipAllowed` `rarity.common` `rarity.uncommon` `rarity.rare` `rarity.pityStep` `deck.handSize` `deck.energy` `player.hp` `enemy.hpMul` `enemy.dmgMul` `floor.scale` `map.eliteRate` `map.restRate` `rest.healRate` `shop.removeCost` `ascension.level` `C: spawn.rateMul` `C: xp.curve` `C: pickup.radius` `audio.sfx` `audio.bgm`。

---

## 5. よく使う攻略パターン・敵の組み合わせ・レベルデザイン

### B 型: 敵とインテント
- **インテントは毎ターンの小さなパズル**: 「次は 12 ダメージ」と見えるから「防御 2 枚か、倒し切るか」を考えられる。無いと当てずっぽうになる。【定説】GMTK「The Power of Video Game HUDs」(StS の敵行動表示)/ 電ファミニコゲーマーの StS 紹介(先読みは有利だが手札が行動を縛る)
- **敵の役割**: 殴る役 / 自分を強くする役(放っておくと危ない)/ 弱らせる役(状態異常・呪いのカードを混ぜる)/ 仲間を呼ぶ役 / 時間で強くなる役(早く倒す圧)。2〜3 体の組で「どれから倒すか」を作る。
- **最初の数戦は弱い組から**: 1 幕の始めは弱い敵の表、その後に強い表。エリートは「勝てば良い報酬、でも体力が減る」の賭け。仮(StS の構造に倣う)
- **ボスは事前に見せる**: 幕の最初に地図でボスの顔を見せると、そのボスに向けたデッキ作りが 1 幕の目標になる。【一説】StS

### A 型: 階の作り
- **行き止まりに宝、通り道に罠**: 生成でも配置の決まりで意味が出る。行き止まり = 寄り道してよい印、複数の出口がある通路の罠 = 「どの道を行くか」の判断。【一説】GDC Eldritch
- **本道は易しく、寄り道は危なく豊か**(§2)。【一説】GDC One Designer
- **部屋に役目**: 宝の部屋・敵の巣・店・泉。階に 1 つ「名物の部屋」を置くと、ランの話のタネになる。
- **敵の組み合わせ**: 近接と遠隔を混ぜる / 足の速い敵を 1 体 / 通路で 1 体ずつ戦えば勝てる群れ(地形を使う判断)。
- **一貫した場所 + 変わる中身**: 地形は毎回同じで、敵・宝・仕掛けだけ変えると、探索の習熟と毎回の新鮮さを両立できる(Prey: Mooncrash・Hades の部屋の型)。【一説】GMTK Prey: Mooncrash 分析

### C 型: 湧き方と山場
- 1 分ごとに敵の種類か数を変える。数分ごとに「囲む輪」「横から群れが走り抜ける」の山場。強い敵は宝箱を落とす。最後に倒せない敵を出してランを締める。仮(VS の構造に倣う)
- プレイヤーの強化と敵の増加を並べて進める(インフレの気持ちよさ)。【一説】電撃オンライン
- 画面の物が増えすぎると状況が読めない。敵の弾は少なく、敵の体当たりが主な脅威に。

### ビルドの組み合わせ
- **軸のタグ**: 毒・防御・手札を引く・連打 など 3〜5 系統。報酬 3 枚のうち 1 枚は今の軸に合うものが出やすくする(完全な乱数だと軸が育たない)。仮
- **取得順で計算が変わる**仕組みは、並べ替え自体が攻略になる。【一説】GMTK Word Play 分析

---

## 6. よく使う UI

- **カードの文章は今の数値で**: 筋力や弱体を反映した「実際に入るダメージ」をカード上に出し、増えたら緑・減ったら赤。キーワード(毒・脆弱)は太字にして、押す・長押しで説明の吹き出し。【一説】StS / Slay the Web
- **ダメージ予告**: 敵の頭上にインテント(剣の絵 + 数字、盾、矢印)。自分の体力バーには「この後に受けるダメージ」を薄い色で重ねる。【一説】GMTK HUD(ゲージとプレビューの 2 役)
- **隠すか見せるか**: Balatro は点の予告をわざと出さず、手を離す瞬間のドキドキを作ったが、計算できる情報なので外部の計算ツールが広まった。Isaac の持ち物の説明を隠した結果、wiki を開きながら遊ぶのが当たり前になった。隠すなら計算で戻せない情報だけに。【一説】GMTK の Balatro 情報設計の回
- **山札・捨て札・デッキ全体はいつでも見られる**。地図は幕全体を見渡せ、通った道に印。
- **A 型**: 文字の記録(「スライムに 4 ダメージ」)を下に 3 行。視界の外は暗く、一度見た所は薄く。スマホはタップした所へ経路で歩き、敵が見えたら止まる。
- **C 型**: 上に経験値バーと経過時間、レベルアップは時間を止めて大きなボタン 3 つ(説明 1 行 + 今の段階 → 次の段階)。
- **スマホのカード**: ドラッグで敵へ投げる + タップで選んでから敵をタップ、の両方。吹き出しは長押し、指で隠れない位置(上)に。入力リスナーを `window` だけに付けない(雛形 AGENTS.md)。【実測】雛形の決まり
- **結果画面**: 到達した階・倒した敵・取った札の一覧・死因。「ここで負けた」が分かると次のランへ向かう。

---

## 7. よく使うアセット(絵・音)

### 会議室の表に既にあるもの(先に使う)
- **rot.js**(`tables/assets.csv` A ランク、BSD-3-Clause)— 生成・視界・経路・行動順。見た目は自作(§3)。
- **Kenney**(`assets.csv` S ランク、CC0)。**Twemoji**(CC-BY 4.0、metopon で使用)— 絵文字は A 型の「文字の代わりの絵」に向く。
- **ぴぽや / itch.io 無料素材**(ドット絵、A ランク)。**PixelMplus**(ドット絵風の日本語フォント)。
- **Kenney Impact Sounds / RPG Audio**(CC0、くつずれで使用)— 斬る・当たる・扉・コイン。
- **WebAudio 合成**(`src/core/audio.ts`)/ **Bfxr / jsfxr** — ファイル不要。カードを出す音・ヒット音。
- **魔王魂**(BGM、obake-chochin・metopon で使用)/ **DOVA-SYNDROME** — ダンジョン・戦闘曲。
- **画像生成**(GPT Image 2 ほか、`assets.csv`)— B 型のカード絵。枠と文字はコードで描き、絵だけ生成する。

### このジャンル向けの追加候補(2026-10-12 に Kenney のページで CC0 を確認)
- **Kenney 1-Bit Pack** https://kenney.nl/assets/1-bit-pack — CC0、2021。1 色のマス目絵。A 型の一式(壁・床・キャラ・持ち物)。
- **Kenney Micro Roguelike** https://kenney.nl/assets/micro-roguelike — CC0、2021。ごく小さいローグライク用タイル。
- **Kenney Tiny Dungeon** https://kenney.nl/assets/tiny-dungeon — CC0、2022。16px のダンジョンとキャラ。
- **Kenney Playing Cards Pack** https://kenney.nl/assets/playing-cards-pack — CC0、2020。トランプの絵柄。B 型の枠の参考にも。
- **Kenney Boardgame Pack** / **Game Icons** https://kenney.nl/assets/boardgame-pack ・ https://kenney.nl/assets/game-icons — CC0、2014。駒・さいころ・アイコン。インテントや状態異常の絵に。
- **game-icons.net**(4,000 超の単色アイコン、CC BY 3.0 と記憶。ページは今回取得できず未確認)— 状態異常・レリックの絵。使うなら作者名のクレジットが要る。
- 使ったら必ず `CREDITS.md` と会議室の `used-assets.csv` に書く。
- Word Play は 160 個の強化に専用の絵を描かず、単純なアイコンで済ませて 7 か月で出した。パイロットのレリック・強化はアイコン + 名前で十分。【一説】GMTK の Word Play の回

---

## 8. 参考 URL

スター数・最終更新(最後の push)は 2026-10-12 に GitHub で確認。ライセンス「なし」「その他」は読むだけにして、コードを写さない。

### コード
- https://github.com/ondras/rot.js — ★2,721 / 2024-11 / BSD-3-Clause。JS のローグライク道具箱(生成・FOV・経路・行動順・乱数)。npm `rot-js` 2.2.1。対話式の説明書付き。
- https://github.com/oskarrough/slaytheweb — ★317 / 2026-05 / AGPL-3.0。ブラウザの StS 風デッキ構築。状態を「行動」で進める作りで、中身と画面が分かれている(README の説明。コードは未読)。**AGPL なので写さず設計だけ読む**。
- https://github.com/ondras/sleeping-beauty — ★148 / 2021-04 / なし。rot.js の作者が 7 日で作った短いローグライク。規模感の参考。
- https://github.com/munificent/rooms-and-mazes — ★148 / 2025-10 / その他。「部屋と迷路」生成の動くデモ(Dart)。
- https://github.com/munificent/hauberk — ★2,173 / 2026-09 / その他。『Game Programming Patterns』の著者の Web ローグライク(Dart)。
- https://github.com/tmewett/BrogueCE — ★1,487 / 2026-10 / AGPL-3.0。Brogue の共同版(C)。少ない操作で深い判断の見本。
- https://github.com/00-Evan/shattered-pixel-dungeon — ★6,658 / 2026-10 / GPL-3.0。スマホ向けローグライクの代表(Java)。タップ操作・UI の参考。
- https://github.com/guladam/deck_builder_tutorial — ★456 / 2024-10 / MIT。Godot 4 のデッキ構築の講座の完成コード。カード・効果・状態の分け方。
- https://github.com/DesirePathGames/Slay-The-Robot — ★289 / 2026-10 / MIT。Godot のデッキ構築の枠組み。
- https://github.com/BigJk/end_of_eden — ★205 / 2024-09 / MIT。端末で動く StS 風(Go + Lua でカードを書く)。データで札を書く例。
- https://github.com/KeJunMao/emoji-survival-game — ★18 / 2022-01 / なし。Phaser 3 + TS の VS 風(絵文字)。小さい。読むだけ。
- サバイバー系は JS の公開実装でスターの多いものが見つからなかった(Unity・Godot が中心)。

### 解説・設計
- https://journal.stuffwithstuff.com/2014/12/21/rooms-and-mazes — Bob Nystrom「Rooms and Mazes」。部屋 → 迷路 → つなぐ → 行き止まりを削る。
- https://en.wikipedia.org/wiki/Roguelike — Berlin Interpretation(2008、ベルリンの国際ローグライク開発会議)の要約。原文は RogueBasin の「Berlin Interpretation」(今回は取得できず)。
- RogueBasin https://www.roguebasin.com/ — ローグライク開発の記事集(生成・FOV・行動順のアルゴリズム)。今回は接続できず、中身は未確認。
- https://www.youtube.com/watch?v=7rqfbvnO_H0 — GDC 2019「Slay the Spire: Metrics Driven Design and Balance」(Anthony Giovannetti)。プレイ結果を集めて札の勝率・使用率で直す、日次ビルドと気軽な感想の集め方。
- https://www.youtube.com/watch?v=BYN0PJOdvzs — GDC「Procedural Level Design in Eldritch」(David Pittman)。部品・外周の帯・テーマの札・ループ・罠と宝の置き方。
- https://www.youtube.com/watch?v=5UdVNmbIClM — GDC「Game Design Case Studies - One Designer」。本道と寄り道、セル・オートマトン、生成後の到達確認。
- https://www.youtube.com/watch?v=Rnlax6eATVY — GDC「Roguelikes And Narrative Design With Hades」(Greg Kasavin)。
- https://www.youtube.com/watch?v=0IUaGQhlPwo — GDC「Darkest Dungeon: A Design Postmortem」(Tyler Sigman, 2017)。
- https://www.youtube.com/watch?v=dwI5b-wRLic — GMTK「The Two Types of Random in Game Design」。
- https://www.youtube.com/watch?v=zk3S3o1qOHo — GMTK の Balatro の情報設計の回(点の予告を隠す)。
- https://www.youtube.com/watch?v=bHLQQh8Ctu4 — GDC「Balancing Cards in Clash Royale」。
- https://www.gdcvault.com/play/1025772/ — GDC 2019「Into the Breach Design Postmortem」(Matthew Davis)。敵の攻撃を先に見せる戦術の設計(中身は未視聴)。
- https://news.denfaminicogamer.jp/projectbook/dungeon — 「不思議のダンジョン」中村光一・長畑成一郎インタビュー(バランスを 1 枚の表で作る、体感の確率)。今回は本文を取得できず。

---

## 9. うちの作品での実例と、踏んだ罠

- **この会議室の流れで作ったローグライクは、まだ無い。**
- 過去作(非公開、`../../research/2026-09-13-past-works-inventory.md`): デッキ構築の企画書(CSV → スプシ、戦闘シミュレータ付き)と、Unity のデッキ構築(決定論の乱数、純粋なルールエンジン + 自動テスト、カードの文面を別の CSV に分けて IP を切り離す)がある。作る時は設計を読み直す価値がある。
- 他ジャンルで分かった、そのまま効く話:
  - bot で「考える / でたらめ」の差を測ると、選択に意味があるかが数字で出る(3 作品で同じ結論)。【実測】`../game-design.md` §6
  - 「選択に意味があるか」はルールの細部で消える。わざと間違えた手を流して、結果に差が出るかを見る。【実測】同上
  - 記録の再生がずれた: bot がゲームと同じ乱数を使っていた。bot に別の `Rng`。【実測】おばけ提灯(`shmup.md` §9)
  - 動くか・壊れていないかだけ確かめて公開し「つまらない」と言われた。面白さを bot で測る型を最初から入れる。【実測】おばけ提灯
- 作ったら、ここに「1 ランの長さ」「報酬 3 択の random と think の勝率差」「レアの率」の実測を書く。

---

## 10. 未確認・これから調べること

- StS の地図の部屋の割合(戦闘・イベント・エリート・休憩・店の %)。ファンの解析にあるが今回は取得できず。
- StS1 のアセンション 20 段の全一覧(今回確認できたのは 1 段目と StS2 の 10 段)。
- VS の進化の正確な条件(レベルアップの選択肢か宝箱か)、最後の敵の出る時刻、武器・受け身の枠の数(攻略記事が食い違う)。開発者 poncle の一次資料(講演・インタビュー)は見つからなかった。
- 不思議のダンジョンのバランス設計(満腹度・識別・店)の一次資料。電ファミのインタビュー本文を読んで §4 に足す。
- Brogue の作者の設計の話(今回の検索は靴の Brogue に埋もれた)。「Brian Walker interview roguelike」で再検索。
- game-icons.net の今のライセンス表記、Dungeon Crawl Stone Soup のタイル(OpenGameArt、CC0 と記憶)の確認。
- RogueBasin・StS wiki・電ファミは、この環境の取得ツールからは名前解決できなかった。別の経路で読む。
- B 型の 1 戦闘のターン数・1 幕の階数の実際の分布。作ったら bot で測って【実測】に置き換える。
