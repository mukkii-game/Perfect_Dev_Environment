# ゲーミング PC の準備(デスクトップ・ゲーミングノート共通)

**使い方**: その PC の Claude Code(ローカル)に「会議室の `global/pc-setup.md` をやって」と頼む。
AI は各項目を「入っているか確かめる → 無ければ入れる → 動くか確かめる」の順でやり、最後に結果をユーザーに見せる。
何度やってもよい(入っているものは飛ばす)。非力なサブ PC ではやらない(クラウドか、デスクトップへの Remote Control を使う)。

AI への注意: winget の ID は入れる前に `winget search <名前>` で確かめる。ID が見つからない・公式でないものは入れずに報告する。
インストールの許可を求められたら、何を入れるか 1 行で添えて人間に聞く。

## 0. この PC のドライブ(ユーザー 10/4)
| PC | データ用ドライブ | 使い方 |
|---|---|---|
| ゲーミングデスクトップ | **E:**(D: より大きい) | 作品の repo は `E:\dev\`、Drive のキャッシュも E: |
| ゲーミングノート | **D:** | 作品の repo は `D:\dev\`、Drive のキャッシュも D: |
- PC ごとにパスが違ってよい(git と HANDOFF で引き継ぐので、パスはそろえなくてよい)。
- **C: は容量が乏しい。大きいものは全部データ用ドライブ(E: / D:)に入れる。** C: に入れてよいのは小さい道具(Git・Node・Python 本体)だけ。
- Google ドライブ(5TB)は**ストリーミング**(必要な時だけ読む)で、手元のキャッシュは既に E: / D: にある。この設定は変えない。
- AI モデルもまずは**ストリーミングのまま**使う(初回に読んだ分は E: / D: のキャッシュに残る)。**よく使うモデルが毎回読み込みに時間がかかる・途中で止まる**時だけ、そのファイル(かフォルダ)を右クリック →「オフラインで使用可能」にする。理由: キャッシュは容量に応じて消されることがあり、消えると数GBを取り直す。また ComfyUI などはモデルを一部ずつ読む読み方をするので、取ってくる途中だと遅い。マイドライブ全体はミラーにしない。
- 道具からは **G: のパスで指す**(2 台とも同じ G: なので設定を使い回せる)。
- **C: に勝手に置かれやすいもの(必ず E: / D: に向ける)**:
  - Ollama のモデル → 環境変数 `OLLAMA_MODELS` を `G:\マイドライブ\AIモデル\ollama`(または `E:\ai\ollama`)に
  - ComfyUI Desktop → インストール時の場所を `E:\ai\ComfyUI`(ノートは `D:\ai\ComfyUI`)に。モデルは `extra_model_paths.yaml` で G: を読む
  - VOICEVOX → インストール先を `E:\ai\VOICEVOX` / `D:\ai\VOICEVOX` に
  - pip / npm のキャッシュ、Hugging Face のキャッシュ(`HF_HOME`)→ 大きくなるので `E:\cache` / `D:\cache` に
- 入れ終わったら C: の空きを確認し、増え方が大きければ何が置かれたかを調べて報告する。

## 1. 道具(各 PC に入れる。Drive には置かない)
| 道具 | 入れ方の目安 | 確かめ方 |
|---|---|---|
| Git | `winget install Git.Git` | `git --version` |
| Node.js LTS | `winget install OpenJS.NodeJS.LTS` | `node -v` |
| Python 3 | `winget install Python.Python.3.12` | `python --version` |
| Codex CLI(画像生成・枠切れ時) | `npm i -g @openai/codex` → `codex` を起動し ChatGPT アカウントでログイン(**ログインは人間**) | `codex --version`、画像生成を 1 枚試す |
| Ollama(ローカル LLM) | `winget install Ollama.Ollama` | `ollama --version` |
| VOICEVOX(声) | 公式サイトのインストーラ(winget にあればそれ) | アプリを起動し、`http://localhost:50021/version` が返る |
| ComfyUI Desktop(画像) | 公式サイトのインストーラ | 起動して既定のワークフローで 1 枚出す |

## 2. 大きな AI モデルの置き場(2 台で共有する)
- モデル(.safetensors 等)は**書き換えない大きなファイル**なので、Google ドライブの `AIモデル/` に置いて 2 台で共有する(0 の設定どおり)。
- **Drive に置かないもの**: ComfyUI 本体・Python の仮想環境・node_modules・git の repo(小さいファイルが大量に書き換わり、同期で壊れる)。

## 3. 会議室のスキルと全体の決まり
`global/README.md` の 1 行を実行する(済んでいれば飛ばす)。

## 4. 終わったら
入れたもの・版・失敗したものを、`knowledge/local-ai.md` の「1. 手元の機材」に PC 名つきで 1 行ずつ足すよう、会議室のセッションに伝える(この PC から会議室へ直接 push しない)。
