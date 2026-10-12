# プラットフォーマー(横スクロールのジャンプアクション。近縁: 精密プラットフォーマー・メトロイドバニア)

使い方: プラットフォーマーを作る前に 1 回通して読む。数値は「つまみ候補」として `src/tuning.ts` に入れ、F2 で人が直す前提の初期値。最終更新: 2026-10-12。
確かさの印: 【実測】うちの作品で確かめた /【定説】複数の出典が一致 /【一説】1 出典だけ(または出典がプレイヤーの経験談)。印の無い数値は、このファイルが置いた仮の値。
用語: 自キャラ = プレイヤーが動かすキャラ。コヨーテタイム = 足場から落ちた直後でもジャンプを受け付ける猶予。先行入力(ジャンプバッファ)= 着地の少し前に押したジャンプを覚えておき、着地の瞬間に出す仕組み。可変ジャンプ = ボタンを押す長さで高さが変わるジャンプ。タイル = 地形を作る正方形のマス(16px 角など)。

---

## 1. 芯と、1 日で作るパイロットの最小構成

### 芯(これがあればプラットフォーマーと感じる)
- **跳ぶ手触り**: 押した瞬間に跳び、押す長さで高さが変わり、上りはふわっと・下りは速い。手触りの大半は見えない猶予(コヨーテタイム・先行入力・角の補正)で決まる。【定説】GDC「Forgiveness Mechanics: Reading Minds for Responsive Gameplay」/ Celeste の公開コード(NoelFB/Celeste `Player.cs`)/ GMTK のジャンプ解説(https://www.youtube.com/watch?v=ep_9RtAbwog)
- **届くか届かないかの読み**: 足場の間隔とジャンプの届く距離がちょうど同じくらいで、「行けそう」と思わせて跳ばせる。ジャンプの届く範囲が全部の地形の物差しになる。【定説】Kyle Pittman「Building a Better Jump」(GDC 2016)/ Rodrigo Monteiro「The guide to implementing 2D platformers」
- **すぐやり直せる失敗**: ミスしたら 1 秒以内に直前の場所から再開。ミスの重さが軽いほど、難しい場所に何度も挑める。【定説】GMTK「Are Lives Outdated Game Design?」/ GDC「Level Design Workshop: Designing Celeste」(Matt Thorson, 2018)
- **1 つの動詞を使い倒す**: キャラの芯の動き(マリオのジャンプ、ショベルナイトの下突き、Celeste のダッシュ)を 1 つ決め、移動にも攻撃にも仕掛けにも同じ動きを使う。【一説】GMTK「Shovel Knight's Signature Moves」(https://www.youtube.com/watch?v=8fjCKMIE1Pg)
- **地形で教える**: 文字の説明なしに、安全な場所で 1 回試させ、次に少し危ない形で使わせ、ひねりを入れ、最後に腕前を見せる場を置く。【定説】林田宏一(Super Mario 3D Land)の「4 段階」インタビュー(Gamasutra 2012、Nintendo Life の紹介記事)/ GDC「Designing Celeste」

### 1 日パイロットの最小構成(この順で作る)
1. 自キャラ: 左右移動(加速・減速あり)、ジャンプ(可変 + コヨーテ + 先行入力)。判定は四角 1 つ。
2. 地形: タイルの格子 1 枚(固い / 空 / トゲ / ゴール の 4 種)。画面 3〜5 枚分の横長 1 面を文字列で書く(§3)。
3. ミス: トゲに触れる・画面の下に落ちる → 0.5 秒の演出 → 最後に通った旗から再開。残機なし、ミス回数だけ数える。
4. 敵 2 種: 左右に歩いて端で折り返す / 一定間隔で跳ねる。上から踏むと倒せ、横から触るとミス。
5. 集める物(コイン)を少し寄り道に置き、ゴールでタイムとミス数とコイン数を出す。記録は `core/save`。
6. カメラ: 横は進む向きに少し先を見せ、縦はジャンプ中は動かさない(§6)。
7. `?auto=1` で右へ走って穴の手前で跳ぶ bot、`?seed=` で再現(`core/rng`・`core/replay`)。
- 後回しでよいもの: 坂、動く足場、壁ジャンプ、ダッシュ、ボス、複数面、地図。坂と動く足場は当たり判定の手間が一番かかる。

---

## 2. よく使うゲームシステムとゲームフロー

- **フロー**: タイトル → 面選択(またはワールド地図)→ 面(始点 → 中間の旗 → ゴール)→ リザルト(タイム・ミス数・集めた物)→ 次の面。1 面 1〜3 分が目安。パイロットは 1 面で十分。
- **中間地点(チェックポイント)を段に分ける**: 「面の始め(本当のやり直し地点)」と「中間の旗(一時的な再開地点)」の 2 段にすると、旗の間隔だけで難しさとストレスを調整できる。ショベルナイトは旗を壊すと宝が出る代わりに再開地点が遠くなる(自分で難しくする選択)。【一説】GMTK「Are Lives Outdated Game Design?」
- **残機をやめて記録の目標にする**: 無限に再開できるようにし、ミス数やタイムを結果画面に出す。上手い人は「ミス 0」を自分の目標にする。残機制なら 1UP の発見が強いご褒美になる、という裏表がある。【一説】同上
- **見えない難易度の道を 3 本**: 誰でも通れる真ん中の道、困った人の下の道(遠回りだが安全)、上手い人の上の道(危ないが速い・ご褒美)を同じ面に重ね、どれを通るかはプレイヤーが決める。1UP やコインを「危ない所にだけ」置くと、取るかどうかが自分で選ぶ難しさになる。【一説】GMTK「Super Mario's Invisible Difficulty Settings」(https://www.youtube.com/watch?v=gkvyYTSKTQY)
- **見えない補正**: 押したジャンプの高さを「届くのに要る高さ」へ気づかれない程度に寄せる。267 人の実験で、補正を強めても「上達した感じ」は下がらなかった(違和感とは独立)。初心者向けの難易度に使える。【一説】CEDEC2015 簗瀬洋平・鳴海拓志「誰でも神プレイできるジャンプアクションゲーム」
- **パワーアップ**: 1 回当たっても大丈夫になる(マリオのキノコ型)か、動きが増える(二段ジャンプ・ダッシュ)。動きが増える型は、取った直後にそれを使わないと進めない場所を置く(§5 メトロイドバニア)。
- **精密プラットフォーマー**(Celeste・Super Meat Boy 型): 1 画面 = 1 つの課題、ミスで即その画面の頭から。面の長さではなく画面の数で量を出す。集める物(イチゴ)は取ってから安全な地面に着いて初めて確定する。【一説】GDC「Designing Celeste」
- **メトロイドバニア**(近縁): 一続きの地図を、手に入れた能力で少しずつ開けていく。フローは「探索 → 行き止まり(鍵が要る所)を覚える → ボス → 能力 → 覚えていた行き止まりへ戻る」の繰り返し。詳しくは §5 の最後。

---

## 3. よく使うデータ構造(この雛形での書き方)

雛形の決まり: ゲームの中身は `src/game/logic.ts` の `step(state, input, cfg)` で **1/60 秒(TICK)ずつ**進め、Phaser・DOM・`Math.random` を使わない。描画は state を読むだけ。`core/fixedstep.ts` が画面の Hz に関係なく step を回す。

### Phaser の Arcade 物理を使うか、自分で書くか
- Phaser 4 の Arcade 物理 + Tilemap なら当たり判定は数行で済む(`layer.setCollisionByProperty({ collides: true })`、片側だけ当たる足場は `body.checkCollision.up` など。雛形 `docs/phaser/reference/physics-arcade`)。ただし中身が Phaser の中に入るので、`npm run sim` の描画なしの bot 比較と `?replay=` の再現が効かなくなる。
- **既定は「当たり判定も自分で書いて logic.ts に置く」**。四角 × タイルの格子だけなら 100 行前後で書け、bot で面を何百回も回せる。坂や回転する物が要る時だけ Arcade(または Matter)に乗り換える。仮
- Arcade を使う場合: 速く落ちると薄い床をすり抜ける。`tileBias`(既定 16)を上げると直るが、上げ過ぎると横から床の上に乗り上がる。【一説】Phaser の文書・フォーラムの経験談

### 入力(人・bot・記録の再生が同じ口を通る)
```ts
export interface Input { dx: number; jump: boolean; jumpPressed: boolean; down: boolean; act: boolean }
// jump: 押し続けているか(可変ジャンプ用) / jumpPressed: この tick に押された瞬間か(先行入力用)
// encodeInput: 'L','R','J','P','D','A' の組み合わせ 1 文字ずつ(core/replay.ts で ?replay= に載る)
```
- 「押した瞬間」は入口で 1 tick だけ立てる。押してすぐ離すタップを取りこぼさない(雛形 `web-game-rules.md` §2-5)。【実測】Galaxtris

### 地形はタイルの格子(文字列で書く)
```ts
// src/game/stage1.ts(中身側。描画と無関係)。1 文字 = 1 タイル(TILE = 16px)
export const STAGE1 = [
  '                                        ',
  '                    oo          F       ',
  '        ooo        ###         ###     G',
  '  S    #####   e          ^^          ##',
  '##########   ######   #############  ###',
];
// S 始点 / G ゴール / F 中間の旗 / # 固い / ^ トゲ / o コイン / e 歩く敵 / = 下から抜けられる足場
export const SOLID = new Set(['#']);
```
- 大きくなったら Tiled(`tables/assets.csv` A ランク)で描いて JSON を読む。AI が JSON を書くことも、人が描き直すこともできる。
- 地形の固さは `tileAt(tx, ty)` 1 つで引く。画面外は「固い」(左右と上)/「空」(下。落ちたらミス)と決めておく。

### 当たり判定(四角 × 格子。Celeste / TowerFall の作り方)
- 自キャラは**絵より少し細い四角**。Celeste は 8×11px(絵は 1 タイル 8px の世界)。【一説】Celeste `Player.cs` の `normalHitbox`
- **位置は整数 px、端数は別に持つ**。速さ × TICK を端数に足し、整数になった分だけ 1px ずつ動かして、ぶつかったら止める。横と縦を別々に動かす(先に X、次に Y)。すり抜けが起きず、坂の無い格子なら必ず正しい。【一説】Maddy Thorson「Celeste & TowerFall Physics」(maddymakesgames.com)
```ts
function moveX(s: Body, amount: number): boolean { // 戻り値: 壁に当たった
  s.remX += amount; let move = Math.round(s.remX); s.remX -= move;
  const sign = Math.sign(move);
  while (move !== 0) {
    if (collides(s.x + sign, s.y, s.w, s.h)) { s.remX = 0; return true; }
    s.x += sign; move -= sign;
  }
  return false;
}
```
- 地形 = 動かない「Solid」、キャラ・敵・弾 = 動く「Actor」。動く足場は Solid 側が自分の上に乗った Actor を一緒に運ぶ。【一説】同上
- **角の補正**: 上へ跳んで天井の角に頭が 1〜4px かかったら、横へずらして通す。ダッシュも同じ。Celeste は 4px。【一説】Celeste `Player.cs`(`UpwardCornerCorrection = 4`)。判定を移動の向きで縮める(横移動中は足元を持ち上げて小さな段差を越える、跳んだ時は細くして隙間を抜ける)手もある。【一説】GDC「Forgiveness Mechanics」
- 接地は「足元 1px 下に固い物があるか」で毎 tick 調べる。壁は「左右 1〜2px 先」。Celeste の壁ジャンプは壁から 3px 離れていても出る。【一説】Celeste `Player.cs`(`WallJumpCheckDist = 3`)/ AUTOMATON の紹介記事(2020-03)

### 状態機械(自キャラの「今なに中か」)
```ts
type PState = 'ground' | 'air' | 'wallSlide' | 'dash' | 'hurt' | 'dead';
interface Player { st: PState; x: number; y: number; remX: number; remY: number; vx: number; vy: number;
  coyote: number;   // 残りコヨーテ時間(秒)。接地中は毎 tick 満タンに戻す
  buffer: number;   // 残り先行入力時間(秒)。jumpPressed で満タン
  varJump: number;  // 可変ジャンプの残り時間(秒)
  facing: 1 | -1; }
```
- 状態ごとに「重力・左右の効き・出せる技」を表にする。Celeste は 23 個の状態(StNormal〜StAttract)を持つが、パイロットは上の 6 つで足りる。
- 猶予はフレーム数ではなく**秒で持ち、TICK ずつ減らす**(画面が 120Hz でも同じ)。【実測】雛形 `logic.ts` の決まり
- ジャンプの判定は 1 か所に集める: `if (p.buffer > 0 && (p.st === 'ground' || p.coyote > 0)) jump()`。跳んだら buffer と coyote を 0 に(二重に跳ばない)。

### 固定刻みの更新の順番(1 tick)
入力を読む → 猶予タイマーを減らす → 状態ごとに速さを決める(加速・重力)→ moveX → moveY → 接地・壁を調べ直す → 敵・トゲ・コイン → 出来事(`'jump'` `'land'` `'die'`)を返す。描画側は出来事で音と粒を出す。

---

## 4. よく使うゲームバランスの指針

### ジャンプは「高さ」と「頂点までの時間」で決める
- 重力と初速を直接いじらず、**最高点の高さ h と頂点までの時間 t** をつまみにして計算で出す: `g = 2h / t²`、`v0 = 2h / t`。横の届く距離は `走る速さ × 滞空時間`。地形の設計(何タイル跳べるか)からジャンプが決まる。【一説】Kyle Pittman「Math for Game Programmers: Building a Better Jump」(GDC 2016)
- **下りの重力を強く**: 上りより下りを 1.5〜3 倍重くすると「ふわっと上がって、すとんと落ちる」。ボタンを早く離したら重力を上げて上昇を切る(可変ジャンプ)。【定説】同上 / GMTK のジャンプ解説 / Ultimate-2D-Controller(早く離した時の重力 3 倍)
- **頂点で重力を半分に**: 上下の速さが小さい間(頂点付近)だけ重力を半分にすると、空中で向きを直す余裕ができる。Celeste はジャンプを押している間だけ、上下の速さが 40px/秒 未満で重力 ×0.5。【一説】Celeste `Player.cs`(`HalfGravThreshold`)

### 参考になる実物の数値(公開コードの定数)
| 項目 | Celeste(1 タイル 8px、320×180 の画面) | Ultimate-2D-Controller(Unity、単位はワールド) |
|---|---|---|
| 走る最高速 | 90px/秒(約 11 タイル/秒) | 14 |
| 加速 / 減速 | 1000 / 400 px/秒²(空中は ×0.65) | 120 / 地上 60・空中 30 |
| 重力 / 落下の上限 | 900px/秒² / 160px/秒(下を押すと 240) | 110 / 40 |
| ジャンプ初速 | 105px/秒、押していれば 0.2 秒その速さを保つ | 36(早く離すと重力 ×3) |
| コヨーテタイム | 0.1 秒(6 tick) | 0.15 秒 |
| 先行入力 | (入力側の設定。このファイルでは未確認) | 0.2 秒 |
| 角の補正 | 4px | なし |
- Celeste の定数から計算すると、押しっぱなしのジャンプは高さ約 28px(3.5 タイル)、頂点まで約 0.37 秒、着地まで約 0.68 秒。最高速なら横に約 61px(7.6 タイル)届く。【一説】`Player.cs` の定数をこのファイルで 60Hz で計算(実機では未確認)

### この雛形での初期値(つまみ候補。1 タイル 16px の場合)
| 項目 | 初期値 | 根拠・印 |
|---|---|---|
| 走る最高速 | 160px/秒(10 タイル/秒) | Celeste の 11 タイル/秒に合わせた仮の値 |
| 加速 / 減速(地上) | 0.1 秒で最高速 / 0.07 秒で止まる | 加速は速く、止まりはさらに速く。仮 |
| 空中の左右の効き | 地上の 0.65 倍 | 【一説】Celeste `AirMult` |
| 最高点の高さ | 3.5 タイル(56px) | 【一説】Celeste の約 3.5 タイル |
| 頂点までの時間 | 0.35 秒 | 【一説】Celeste の約 0.37 秒 |
| 下りの重力 | 上りの 1.8 倍 | 「1.5〜3 倍」の中間。【定説】(§4 冒頭) |
| 早く離した時の重力 | 上りの 3 倍 | 【一説】Ultimate-2D-Controller |
| 落下の上限 | 1 tick で 1 タイルを超えない(16px × 60 = 960px/秒 未満)。320px/秒から | 1 tick の移動が判定の大きさを超えるとすり抜け(§3 の 1px ずつ動かす作りなら起きない) |
| コヨーテタイム | 0.1 秒 | 0.1〜0.15 秒が多い。【定説】Celeste / GDC「Forgiveness Mechanics」(最大 0.1 秒)/ Ultimate-2D-Controller |
| 先行入力 | 0.1〜0.15 秒 | 「4〜6 フレーム」〜「最大 0.2 秒」まで幅あり。【定説】GMTK / GDC「Forgiveness Mechanics」/ Ultimate-2D-Controller。長いと「勝手に跳んだ」と感じるので短めから |
| 角の補正 | 4px(1/4 タイル) | 【一説】Celeste |
| 自キャラの判定 | 絵の幅の 70〜80%、高さ 85% | 細くすると壁際で引っかからない。仮 |
| ミスから再開まで | 0.5〜1.0 秒 | 「すぐやり直せる」【定説】(§1)。秒は仮 |

- **浮いた感じの原因は 3 つに分けて見る**: 重力が弱い(現実の 9.8m/s² ではゲームでは遅く見える)/ 当たりの押し戻しが段階的でがたつく / 質量の比がおかしい。物理エンジン任せで「ふわふわする」時の切り分け。【一説】GDC「Designing with Physics: Bend the Physics Engine to Your Will」
- **判定は少しプレイヤーに有利に**: 踏みつけは敵の上半分に触れれば成功、トゲの判定は見た目より小さく。ソニックフォースは「意図が読めたら成功させる」方針で、判定を横に広げてトゲの手前のミスを減らした。【定説】CEDEC2017 神谷聖子「高速『体験』を生み出すレベルデザイン ～ソニックフォースの『セット』手法～」/ GDC「Forgiveness Mechanics」
- **難しさの出どころを 2 つに分ける**: 「地形と敵の複雑さ」と「操作の難しさ(技の入力)」。片方ずつ上げる。両方を同時に上げると急な崖になる。【一説】GMTK「Shovel Knight's Signature Moves」
- **bot で測る**(雛形 `src/game/bots.ts` + `tools/sim.mjs`): idle(何もしない)/ random / 「右へ走り、穴と敵の手前で跳ぶ」think / think の 0.2〜0.6 秒遅れ を並べ、ゴール率・ミスした場所・タイムを見る。
  - think がほとんどの所で死ぬ → 跳べない幅がある(ジャンプの届く距離と地形の物差しがずれている)。遅れ版だけが死ぬ所 → 反射神経の山。そこに中間の旗を置く。【実測】反射神経を遅れで測る型はおばけ提灯(シューティング)。プラットフォーマーでは未実測
- **つまみ候補の一覧**(`src/tuning.ts` に入れる): `move.maxSpeed` `move.accelTime` `move.decelTime` `move.airControl` `jump.height` `jump.timeToApex` `jump.fallGravityMul` `jump.cutGravityMul` `jump.apexHalfGrav` `fall.maxSpeed` `jump.coyote` `jump.buffer` `collide.cornerPx` `player.hitW` `player.hitH` `death.respawnDelay` `camera.lookAhead` `camera.damping` `audio.sfx` `audio.bgm`。曖昧な注文(「もっと軽快に」)は、このどれを何から何へ動かすかに直して返す(例: `jump.timeToApex` 0.35 → 0.30、`move.accelTime` 0.1 → 0.06)。

---

## 5. よく使う攻略パターン・敵の組み合わせ・レベルデザイン

### 1 つの仕掛けを 4 段で使う(起承転結)
- 1) 安全な所で試させる(落ちても死なない穴の上の動く足場)→ 2) 少し危なくする(下がトゲ)→ 3) ひねる(足場が途中で消える、別の仕掛けと組み合わせる)→ 4) 腕前を見せる場(連続で使う)。1 面 = 1 つの仕掛け、で作ると面が覚えやすい。【定説】林田宏一インタビュー(Gamasutra 2012)/ GMTK の Super Mario 3D World 解説
- 最初は「たまたまそうなった」と感じる形で体験させ(仕掛けを意識させない)、後の面で「それを使わないと越えられない」場所を出す。気づいた瞬間が自分の手柄になる。【一説】GDC「Designing Celeste」(勢いを使ったジャンプの例)

### 面の「話」を 1 行で決める(精密プラットフォーマー)
- 「崩れるブロックの横をよじ登り、落ちる前に跳んで上の足場へ」のように、各画面で何をさせたいかを 1 行で書く。話に関係ない跳び方の違いは許し(届くように手伝う)、話を飛ばす抜け道は確実に塞ぐ。【一説】GDC「Designing Celeste」
- **安全な足場の密度で緊張を作る**: 立って休める場所が多い区間は緩く、少ない区間は張りつめる。休める場所にも段階がある(ただの地面 / 崩れる足場 / トゲの間の狭い足場)。【一説】同上
- 同じ目的地に 2〜3 通りの行き方を用意すると、上手い人の工夫が生まれる。【一説】同上
- 面を作る前に、新しい動き 1 つにつき使い道を紙に 20〜30 個書き出し、良いものだけ残す。【一説】GMTK の Ori 制作解説(https://www.youtube.com/watch?v=gIdHTL18kTU)

### 敵と地形の型
- **歩く敵**(端で折り返す / 落ちる): 踏む練習と、ジャンプの「着地点」を塞ぐ役。
- **跳ねる敵・飛ぶ敵**: 空中の軌道を塞ぐ。真上を通る時が危ない。
- **砲台**(一定間隔で弾): リズムを読ませる。弾の間に跳び込む。
- **トゲ・穴**: 動かない罰。敵より公平(読めば必ず避けられる)。
- **動く足場・消える足場・バネ・一方通行の足場(下から抜けられる)**: 動きの幅を増やす地形。動く足場は「乗った時に足場の速さを引き継ぐ」かどうかを決めておく。
- **予告してから動く**: 敵の攻撃・落ちる足場は、揺れる・光るを 0.3〜0.5 秒見せてから。予告なしは理不尽に感じる。【定説】GDC「Boss Up: Boss Battle Design Fundamentals」/ CEDEC2023『FINAL FANTASY XVI』コンバットデザイン講演(秒は仮)
- **画面外から撃たせない**: 見えない所からの攻撃は理不尽に感じる。カメラの外の敵は止めるか、撃たない。【一説】CEDEC2023『FINAL FANTASY XVI』講演
- 「何とかぎりぎり逃げ切れた」を作る(追ってくる壁・崩れる床を、プレイヤーより少し遅く)。実際より難しく感じさせ、抜けた時の達成感を大きくする。【一説】GDC「Unravel: Using Empathy as a Game Mechanic」

### 面の流れと寄り道
- 1 面の中で「速く走れる区間 → 止まって考える区間 → また走る」を交互に。ソニックフォースは数秒単位の「セット」(認識 → 入力 → 反応)を並べて面を作り、ユーザーテストで入力のずれを見て直した。【一説】CEDEC2017 ソニックフォース講演
- 小さなご褒美(コイン・集める物)を道しるべに並べ、言葉なしで行き先を教える。【定説】GMTK の Metroid Dread 解説(https://www.youtube.com/watch?v=5pop-cc9kmY)/ GMTK「Super Mario's Invisible Difficulty Settings」
- 隠し部屋は「隠し過ぎない」。ひび割れ・色の違う壁など、よく見ていれば気づく手がかりを置く。【一説】GMTK の Ori 制作解説
- 登れる・壊せる物は色や形でそろえる(「この色の壁は登れる」)。【一説】GMTK(https://www.youtube.com/watch?v=KW4JlxAEAE0)
- 面の自動生成をするなら、地形を直接ばらまかず、先に「ボタンを押すリズム(いつ跳ぶか)」を作ってから地形に直すと遊びやすい。【一説】CEDEC2015「Adaptable Game Experience through PCG」(元は Gillian Smith らの Rhythm-based level generation)

### メトロイドバニア(近縁)
- **鍵と錠**: 新しい能力(鍵)を取ったら、それで開く障害(錠)を同じ地域のすぐ先に置く。能力が開ける錠は他にもあるが、本筋の錠だけを近くに置くと、迷路に見えても自然に一本道を進める。【定説】GMTK の Hollow Knight: Silksong 解説(https://www.youtube.com/watch?v=l7xXW0EbK4g)/ GMTK の Metroid Dread 解説
- **一方通行で今の探索範囲を絞る**: 戻れない滑り台・落下・自動で閉まる扉を挟み、「今探すべき所」を狭める。広がり続ける地図で迷わせない。【一説】GMTK の Metroid Dread 解説
- 逆に、崩れる足場のように「一度しか通れない」仕掛けは、後で戻れる手段とセットにする(Ori は崩れた足場が元に戻る + 掘って戻れる)。【一説】GMTK の Ori 制作解説
- **詰まったら別の場所へ**: 1 体のボスに詰まった人が、別の地域を探索して強くなってから戻れるよう、行ける場所を常に 2 か所以上残す。死ぬとお金を落とす仕組みは、この回り道を邪魔することがある。【一説】GMTK の Silksong 解説
- 遠い鍵と錠はワープでつなぐ。進めない場所が多い時期は、地図に「まだ行けない印」を付ける。【一説】GMTK の Metroid Dread 解説 / Ori 制作解説
- 全体の設計は、能力 → 開く場所の依存関係を図(依存グラフ)に描いて確かめる。【一説】GMTK「Boss Keys」シリーズ(メトロイドバニア編、2018〜)
- パイロットでは地図 1 枚(10〜15 部屋)、能力 2 つ(二段ジャンプ・壁ジャンプなど)、ボス 1 体まで。部屋は 1 画面 = 1 部屋の格子にすると地図が自動で描ける。仮

---

## 6. よく使う UI

- **HUD は最小限**: 集めた物の数・タイム・(あれば)体力を上の隅に小さく。精密プラットフォーマーは HUD なし、止めた時だけ出す型が多い。
- **カメラ**(このジャンルの UI の主役):
  - 横は**進む向きに先を見せる**(自キャラを画面の中央より後ろに置く)。中央に固定すると画面の半分が後ろの景色になり、前から来る物に驚かされる。【定説】GMTK の 2D カメラ解説(https://www.youtube.com/watch?v=TdWFzpgnljs)/ Itay Keren「Scroll Back: The Theory and Practice of Cameras in Side-Scrollers」(GDC 2015)
  - 縦は**ジャンプ中は動かさず、着地した高さで追い直す**。跳ぶたびに画面が上下すると酔い、着地点が見えなくなる。【定説】同上
  - 細かい動きで揺れないよう、**遊び(この枠の中なら動かない)と、なめらかな追従**を入れる。追従が遅すぎると先が見えなくなる。【定説】同上
  - 横と縦を別のルールで動かしてよい。【一説】GMTK の 2D カメラ解説
  - 面の高さを画面 1 枚に収めれば、縦のカメラは要らない(ショベルナイト)。パイロットはこれが一番楽。【一説】同上
- **ミスの演出**: 一瞬止めて(0.1 秒)、はじける粒、画面の小さな揺れ、すぐ再開。長い演出は繰り返すと苦痛になる。仮
- **着地・ジャンプの手応え**: 跳ぶ瞬間に縦に伸び、着地で横につぶれる(数 tick)。足元の土ぼこり。音は短く。仮
- **地図**(メトロイドバニア): 行った部屋・まだ行けない扉・ボスの場所を出す。最後の目的地を最初から地図に出すと、自由に探させても迷子にならない。隠しの印は最初は出さず、後半に出す切り替えもある。【一説】GMTK の Silksong 解説
- **スマホの操作**:
  - 左半分を左右移動(左下に仮想スティックか ← → の 2 ボタン)、右下にジャンプ(大きく)。ジャンプの長押しで可変ジャンプが効くようにする。精密な操作はスマホに向かないので、猶予(コヨーテ・先行入力)を PC より少し長くする選択肢を調整パネルに。仮
  - ボタンは指で隠れる位置を避け、押した時に光らせる。最後の砦に本物の DOM の `<button>` を置く(雛形 `web-game-rules.md` §2-4)。
  - 入力リスナーを `window` だけに付けない(雛形 AGENTS.md)。【実測】Galaxtris
  - 横画面が前提になるので、横に回す仕組みを先に入れる(雛形 `web-game-rules.md` §9-3、アプリ内ブラウザは §9-8)。【実測】ImoteControllDandy / おばけ提灯
- **縦横比**: 横長の 16:9 前後に固定して黒帯(雛形 §9-5)。画面が広いと先が見えすぎて難しさが変わるので、見える範囲(タイル数)は作品で 1 つに決める。仮

---

## 7. よく使うアセット(絵・音)

### 会議室の表に既にあるもの(先に使う)
- **Kenney**(`tables/assets.csv` S ランク、CC0、クレジット任意「Kenney (www.kenney.nl)」)。セットごとに題材が限られるので、先に中身を見る。【実測】metopon 2026-10-05
- **Pixel Adventure(Pixel Frog、itch.io)**(`assets.csv` A ランク「横スクロールのドット絵一式」)https://pixelfrog-assets.itch.io/pixel-adventure-1 — itch.io の表示は CC0(クレジット不要)だが、OpenGameArt の同じ素材は CC-BY 4.0 表記。**ZIP の中のライセンスを見てから使う**。作品が被りやすい。
- **Tiled Map Editor**(`assets.csv` A ランク)— 地形を描いて JSON。Phaser がそのまま読める。
- **ぴぽや / itch.io 無料素材**、**PixelMplus / まるきやフォント**(`assets.csv`)— ドット絵と日本語のドット文字。
- **Kenney Impact Sounds**(足音・着地・ぶつかる音)https://kenney.nl/assets/impact-sounds — CC0。くつずれで使用。【実測】`used-assets.csv`
- **WebAudio 合成**(`src/core/audio.ts`)/ **Bfxr・jsfxr** — ジャンプ音・コイン音はファイル不要で作れる。【実測】過去作
- **魔王魂**(BGM)— 直接 URL は 403、配布ページを Referer にすると取れる。【実測】おばけ提灯

### プラットフォーマー向けの追加候補(2026-10-12 に検索結果で CC0 表示を確認。中身は未確認)
- **Kenney Pixel Platformer** https://kenney.nl/assets/pixel-platformer — CC0。地形タイル・ブロック・アイテム・HUD・キャラと敵、200 枚超。タイルシートと 1 枚ずつの両方。
- **Kenney Pixel Platformer Blocks** — CC0。80 タイル × 4 色(白は色を塗り替えやすい)。上と組み合わせる。
- **Kenney New Platformer Pack**(2025)— CC0。タイル・キャラ・敵・HUD・背景・効果音。
- **Kenney 1-Bit Platformer Pack** — CC0。白黒 1 色。抽象的な見た目にしたい時。
- **Kenney Platformer Art Deluxe(Pixel)** — CC0。380 枚超(古い版)。
- 使ったら必ず `CREDITS.md` と会議室の `used-assets.csv` に書く。

### 音の作り方
- **ZzFX**(https://github.com/KilledByAPixel/ZzFX、MIT)— 1 行の数値配列で効果音。ジャンプ(上がる音程)・着地(低く短い)・コイン(高く 2 音)・ミス(下がる音程)の 4 つがあれば足りる。
- **jsfxr / bfxr2** — 「Jump」「Pickup/Coin」「Hit/Hurt」のボタンで作れる。
- ジャンプ音は毎回鳴るので、短く、音程を少し揺らす。足音は走る速さに合わせて間隔を変える。仮
- 音量は控えめから(`audio.sfx` / `audio.bgm` 既定 0.45)。AI は聴かずに大きめを選ぶ。【実測】おばけ提灯

---

## 8. 参考 URL(雛形が要る時に見る所)

スター数・最終更新(最後の push)は 2026-10-12 に GitHub で確認。ライセンス「なし」は読むだけにして、コードを写さない。

### コード
- https://github.com/NoelFB/Celeste — ★3,996 / 2022-10(アーカイブ済)/ MIT(コードのみ。ゲーム本体と絵は対象外)。Celeste の `Player.cs`(約 5,500 行)。重力・可変ジャンプ・コヨーテ・角の補正・壁ジャンプ・ダッシュの定数と処理がそのまま読める。§4 の数値の出典。
- https://github.com/Matthew-J-Spencer/Ultimate-2D-Controller — ★2,172 / 2023-10 / MIT。Unity の 2D キャラ操作。コヨーテ・先行入力・早く離した時の重力などのつまみが名前と説明つきで並ぶ。つまみの一覧づくりの手本。
- https://github.com/KilledByAPixel/LittleJS — ★4,206 / 2026-10 / MIT。素の JS の小さなエンジン。タイルの当たり判定つきの横スクロールの例がある(例の中身は未確認)。
- https://github.com/godotengine/godot-demo-projects — ★9,638 / 2026-10 / MIT。Godot の公式サンプル集。2D プラットフォーマーの例(状態機械・敵・弾)を設計の参考に。
- https://github.com/deepnight/gameBase — ★710 / 2025-10 / MIT。Dead Cells の作者の 1 人(Sébastien Bénard)の Haxe の雛形。格子の上の当たり判定と、画面の揺れ・一瞬止める演出の作り方。
- https://github.com/SebLague/2DPlatformer-Tutorial — ★710 / 2017-04 / MIT。Unity。光線で当たりを調べるキャラ操作(坂・すり抜け床・壁ジャンプ)の講座の完成コード。
- https://github.com/nkholski/phaser3-es6-webpack — ★704 / 2023-01 / なし。Phaser 3 のスーパーマリオ風の面(Tilemap + Arcade)。構成の参考だけ。
- https://github.com/mikewesthad/phaser-3-tilemap-blog-posts — ★284 / 2023-10 / なし。Phaser 3 の Tilemap の講座(Tiled の読み込み・当たり・プラットフォーマー)。
- https://github.com/yandeu/phaser3-typescript-platformer-example — ★88 / 2026-04 / MIT。Phaser 3 + TypeScript の小さなプラットフォーマー。雛形に近い構成。
- https://github.com/EXOK/Celeste2 — ★547 / 2021-01 / なし。Celeste Classic 2(PICO-8、Lua)の作者自身のコード。小さな精密プラットフォーマーの全部。読むだけ。

### 解説・設計
- https://maddymakesgames.com/articles/celeste_and_towerfall_physics — Maddy Thorson「Celeste & TowerFall Physics」。Solid と Actor、整数 px + 端数で 1px ずつ動かす方法。§3 の当たり判定の元。短い。まずこれ。
- https://gdcvault.com/play/1023148/Math-for-Game-Programmers-Building — Kyle Pittman「Building a Better Jump」(GDC 2016)。高さと距離からジャンプを逆算する式。
- https://www.gamedev.net/tutorials/programming/general-and-gameplay-programming/the-guide-to-implementing-2d-platformers-r2936/ — Rodrigo Monteiro「The guide to implementing 2D platformers」(2012)。実装の 4 つの型(タイル単位 / タイル + 滑らか / ビットマスク / 線分)と、坂・はしご・すり抜け床の扱い。
- https://www.gamedeveloper.com/design/scroll-back-the-theory-and-practice-of-cameras-in-side-scrollers — Itay Keren「Scroll Back」。横スクロールのカメラの技を名前つきで総覧。
- https://www.youtube.com/watch?v=TdWFzpgnljs — GMTK の 2D カメラ解説(先を見せる・ジャンプ中は止める・遊びとなめらかさ)。
- https://www.youtube.com/watch?v=ep_9RtAbwog — GMTK のジャンプの手触り解説(二段の重力・先行入力・コヨーテ・可変ジャンプ)。
- https://gmtk.itch.io/platformer-toolkit — GMTK「Platformer Toolkit」(2022、ブラウザで遊べる)。30 以上のつまみを動かして手触りが変わるのを体験できる。開発記「Behind The Code」にコードあり。数値を決める前に 10 分触る。
- https://www.youtube.com/watch?v=4RlpMhBKNr0 — GDC「Level Design Workshop: Designing Celeste」(Matt Thorson, 2018)。面の話・安全な足場・地形で教える。
- https://www.youtube.com/watch?v=HCnZhs-92j0 — GDC「Forgiveness Mechanics: Reading Minds for Responsive Gameplay」。コヨーテ・先行入力・判定を縮める補正。
- https://www.youtube.com/watch?v=gkvyYTSKTQY — GMTK「Super Mario's Invisible Difficulty Settings」。3 本の道・危ない所のご褒美。
- https://www.nintendolife.com/news/2012/04/super_mario_3d_land_director_shares_level_design_inspirations — 林田宏一の 4 段階(起承転結)の紹介記事。元は Gamasutra のインタビュー(未読)。
- https://www.youtube.com/watch?v=l7xXW0EbK4g ・ https://www.youtube.com/watch?v=5pop-cc9kmY — GMTK の Silksong / Metroid Dread 解説。鍵と錠・一方通行・ご褒美の道しるべ。GMTK「Boss Keys」(メトロイドバニア編)も同じ系統。
- CEDEC2015 簗瀬洋平・鳴海拓志「誰でも神プレイできるジャンプアクションゲーム」/ CEDEC2017 神谷聖子「高速『体験』を生み出すレベルデザイン ～ソニックフォースの『セット』手法～」(https://cedil.cesa.or.jp/cedil_sessions/view/1599)。日本語の講演。

---

## 9. うちの作品での実例と、踏んだ罠

**プラットフォーマーの作品はまだ無い。** 下は他のジャンルの作品で確かめた、このジャンルにも当てはまるもの。

- **固定刻みと乱数・再現**: 中身を 1/60 秒刻みの step にし、乱数は `core/rng`、入力の記録は入口で丸める。記録の再生がずれた原因は「記録は整数、本番は小数」と「bot が中身と同じ乱数を引いた」。プラットフォーマーは位置の端数(§3 の remX)を持つので、端数も state に入れて記録の再生で一致するか確かめる。【実測】おばけ提灯(雛形 `web-game-rules.md` §9-6)
- **bot を並べて芯を測る**: 動くか・壊れていないかしか確かめずに出したら「つまらない」と言われた。何もしない・でたらめ・考える・指の遅れる bot を並べる型はここから。プラットフォーマーでは「跳べない幅が無いか」「idle が安全に待てる場所(敵が届かない所)が無いか」を見る。【実測】おばけ提灯・くつずれ(`knowledge/game-design.md` 6)
- **入力**: itch.io の iPhone 埋め込みで、押した瞬間が同じフレームの `pointercancel` で消えた(ショットが出なかった)。ジャンプも同じ罠を踏む。タッチは Touch Events を主にし、押した瞬間を 1 tick 保持。【実測】Galaxtris(雛形 `docs/knowledge/itch-mobile.md`)
- **横画面**: スマホで横画面を強制する(全画面 + orientation.lock、だめなら CSS で 90° 回してタッチ座標も回す)。アプリ内ブラウザでは横にならない。【実測】ImoteControllDandy・おばけ提灯(雛形 §9-3・§9-8)
- **縦横比**: canvas を縦横別々に引き伸ばして絵が伸びた → 縦横比を保って黒帯。プラットフォーマーは見える範囲が難しさに効くので必須。【実測】雛形 §9-5
- **判定の関数に演出を混ぜない**(画面外の敵から粒が出続けた)。トゲ・敵の判定とミスの演出を分ける。【実測】Galaxtris(雛形 §6-4)
- **Kenney は題材が限られる**(Pixel Shmup に砂漠が無かった)。Pixel Platformer も中身を先に見る。【実測】metopon

---

## 10. 未確認・これから調べること

- スーパーマリオブラザーズの実際の数値(歩き・走りの速さ、ジャンプの初速と重力、押す長さでの重力の切り替え)。解析資料はサブピクセル単位で公開されているが未読。
- Celeste の先行入力の秒数(入力側の `Input.cs` は公開リポジトリに無い。0.08 秒という話があるが未確認)。
- Phaser 4 の Arcade 物理と、logic.ts に自分で書いた当たり判定の、スマホでの重さと書きやすさの比較。1 本作って【実測】にする。
- スマホの仮想ボタンの配置・大きさ・猶予を何秒延ばすと良いか(経験談も見つかっていない)。
- 坂・動く足場・すり抜け床を logic.ts の格子方式でどう書くか(Monteiro の記事と Thorson の記事の実装を試す)。
- メトロイドバニアの地図を部屋の格子から自動で描く方法と、bot で「全部の部屋に行けるか」を確かめる方法。
- 日本語の一次資料(任天堂・セガの講演)をもう少し。CEDEC のアーカイブで「ジャンプ」「レベルデザイン」の講演を引く。
- このファイルの GMTK の動画のうち、題名を確認していないもの(ep_9RtAbwog・TdWFzpgnljs・KW4JlxAEAE0)は URL だけで書いた。
