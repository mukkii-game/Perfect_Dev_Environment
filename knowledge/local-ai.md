# 手元の PC で動かす AI(ComfyUI・ローカル LLM)

**いつ使うか**: クラウドの AI で足りない時だけ。(1) 同じキャラを何十枚も描く(LoRA を自作して揃える)、
(2) 生成回数が多すぎてクラウドの枠や料金が気になる、(3) クラウドに無いモデル・細かい制御が要る、(4) 外に出したくない素材。
**それ以外はクラウド(GPT Image / Firefly / Canva 等)の方が速い。** 一覧表では「AI操作」に `ローカル` と付けた行が対象。

最終確認: 2026-10-03(出典は各行。【未確認】は使う前に実測)

## 1. 手元の機材

| 機械 | GPU | VRAM | 役割 |
|---|---|---|---|
| デスクトップ | RTX 4080 SUPER | 16GB | **主力**。画像・動画・3D・LoRA 学習・ローカル LLM(〜27B 量子化) |
| ノート | RTX 3080 Laptop | **8GB か 16GB(要確認)** | サブ。画像(SDXL・FLUX.2 klein 4B)、TTS、小さい LLM |

**入れた道具**(置き場所は `global/pc-setup.md`):
- VOICEVOX エンジン: `G:\マイドライブ\ai\tools\voicevox\`(2026-10-04、ナスの地上絵の作業中に導入。2 台共有)

ノートの VRAM の確かめ方: タスクマネージャー → パフォーマンス → GPU →「専用 GPU メモリ」、または `nvidia-smi`。
確かめたらこの表を直す。

## 2. AI からの動かし方(いざという時)

1. **デスクトップで Claude Code をローカル実行**し、ComfyUI を操作させる。一番素直で安全(外にポートを開けない)
   - **Comfy MCP(公式・ベータ)** を Claude Code に登録すると、ワークフロー実行・モデル検索・画像/動画/音声/3D 生成ができる。
     2026-08 からローカル ComfyUI に正式対応。[docs](https://docs.comfy.org/agent-tools/mcp) / [ローカル対応 2026-08-11](https://comfyui-wiki.com/en/news/2026-08-11-comfy-mcp-local-server)
   - MCP 無しでも、ComfyUI の API(`POST /prompt` にワークフロー JSON)を AI が直接叩ける【未確認: ポートは 8188、Desktop 版は 8000 のことあり】
2. **外出先から**: デスクトップの Claude Code で `/rc`(Remote Control)→ スマホから同じセッションを操作。
   PC は起動したまま、同時 1 セッション。[Simon Willison 2026-02-25](https://simonwillison.net/2026/Feb/25/claude-code-remote-control/)
3. **クラウドの会議室・作品セッションからは直接届かない**。生成物はデスクトップ側で作品 repo の `assets/` に push するか、Google ドライブ経由で渡す。

### 安全(必ず守る)
- **ComfyUI を `--listen 0.0.0.0` でネットに直接出さない**。API に認証が無く、カスタムノード導入やワークフロー実行は事実上なんでも実行できる。
  外から触るなら Remote Control か Tailscale のプライベート網内だけ。
- **怪しいカスタムノード・ワークフローを入れない**(過去にマルウェア入りの事例)。入れる前に Manager の評価・作者を見る。

## 3. ローカル LLM

- **Ollama** を入れれば足りる(LM Studio でも可)。**Claude Code をローカルモデルで動かせる**:
  `ANTHROPIC_BASE_URL=http://localhost:11434` / `ANTHROPIC_AUTH_TOKEN=ollama`(Ollama v0.14.0〜)。[Ollama docs](https://docs.ollama.com/integrations/claude-code)
  **ただし体験はクラウドの Claude より明確に劣る**。使うのは「枠切れ時の軽作業」「外に出せない文章の下処理」程度。
- 16GB の目安(ブログ情報 2026-09): コーディング Qwen 3.5 27B(量子化)/ 汎用 Gemma 4 26B-A4B / 推論・ツール gpt-oss-20b。
  [runaihome](https://www.runaihome.com/blog/best-local-llm-16gb-vram-2026/)

## 4. 商用ゲームに使えるか(ライセンス)

| 安全寄り | 条件付き | 非商用(作品に使わない) |
|---|---|---|
| FLUX.2 klein 4B(Apache 2.0)、Wan 2.2(Apache 2.0)、Qwen-Image【未確認】、TRELLIS(MIT)【未確認】、ACE-Step(Apache)【未確認】 | LTX-2(年商 1,000 万ドル以上は有償)、Hunyuan 系(EU・英国・韓国で不可 → 海外配信に不向き)、Stable Audio Open(年商 100 万ドル未満なら可)【未確認】、SDXL 系(OpenRAIL++。派生モデルは個別) | FLUX.2 dev / klein 9B / Kontext dev【未確認】、RMBG-2.0【未確認】 |

- **LoRA・派生モデルは配布元(Civitai 等)の許諾フラグも見る**。使ったモデル名とライセンスは作品の `CREDITS.md` に書く(雛形の規則と同じ)。

## 5. 初回にやること(人間)
1. デスクトップに ComfyUI Desktop を入れる → 2. Comfy MCP を Claude Code に登録 → 3. FLUX.2 klein 4B で 1 枚出す
→ 4. ここに「動いた設定」と 1 枚あたりの秒数を書く(実測が入るまで表のランクは仮)

## 6. 手元の GPU で足りない時: Google AI Pro 特典の Colab(A100)(2026-10-10 追記)
- Google AI Pro(Mukkii は契約済み)に Colab の上位特典が付き、**A100 40GB / 80GB** が使えるようになった(Google Gemma 公式の告知 https://x.com/googlegemma/status/2108652628590944540 、StudioYebisu の実演 https://x.com/studio_yebisu/status/2108808702577009033 、ともに 2026-10-10)。
- 月 200 CU の配布で、A100 40GB なら約 37 時間、ハイメモリなら約 26 時間(StudioYebisu の概算。未確認)。
- 手元(4080S 16GB / 3080 Laptop)との差: 16GB では量子化しないと動かない動画・画像の生成モデル(Wan2.2・LTX-Video・HunyuanVideo 等)を高い精度で回せる。30B〜70B の LLM、LoRA の学習も回せる。
- うちでの使いどころ(毎日の 1 本には要らない。**まとめて作る時だけ**):
  - キャラを揃えるための LoRA 学習(漫画・作品の主役)
  - 宣伝動画の生成
  - ゲームに入れる LLM(game-llm)の大きめのモデルの試験
- 注意: 生成物の商用利用はモデルごとのライセンス次第(§4 と同じ)。Colab はブラウザで人が開くもので、クラウドのセッションから直接は動かせない(未確認)。使う日は Mukkii の手元から。
