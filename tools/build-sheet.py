"""一覧表スプレッドシート(xlsx)を作る。各タブは GitHub の CSV を IMPORTDATA で読むだけ。
タブを増やす時はここに 1 行足し、出力を Drive に作り直す(リンクは変わる)。"""
import openpyxl,sys
from openpyxl.styles import Font,PatternFill
from openpyxl.formatting.rule import FormulaRule
base="https://raw.githubusercontent.com/mukkii-game/Perfect_Dev_Environment/main/knowledge/tables/"
wb=openpyxl.Workbook();ws=wb.active;ws.title="説明"
for r in [["開発ノウハウ一覧(閲覧用)"],["原本は GitHub の knowledge/tables/*.csv。各タブは自動で読み込んで表示するだけ(初回だけ各タブで「アクセスを許可」)"],
 ["学ぶこと: あなたのカリキュラム。毎週月曜に1単元が課題で出る。終わったら会議室に「テストして <単元名>」"],
 ["道具: 分野(絵/音/3D/映像/文字/コード/ローカル基盤/公開・手続き)→ 工程(入手/作る/加工/組む/確かめる/出す)の順"],
 ["区分: 優先 / 条件付き / 外した。AI操作: ◎AIだけで完結 / ○MCP・APIでAIが操作 / △人間の手が要る。ランク: S 迷ったらこれ / A 第一候補 / B 補助 / C ほぼ使わない"],
 ["手続き: 公開・販売の手順。使った素材: 作品のCREDITS.mdを毎晩集計(★=また使いたい)。自動化: 動いている仕組み全部。AIへの指示: AIが読むお作法と行数"],
 ["直したい時: 会議室に一言、または GitHub で CSV を編集。ここを直接書き換えても次の更新で消えます"],
 ["原本: https://github.com/mukkii-game/Perfect_Dev_Environment/tree/main/knowledge/tables  /  素材庫: https://drive.google.com/drive/folders/1OZ7xNZnWZYF-rwGX2QAQdhZt3O2ZOg3d"]]: ws.append(r)
ws["A1"].font=Font(bold=True,size=14);ws.column_dimensions["A"].width=130
tabs=[("学ぶこと","curriculum.csv","H",[14,4,20,40,40,30,16,6,11],{"合格":"C6EFCE","挑戦中":"FFF2CC"}),
("心構え","mindset.csv","B",[12,6,34,60,30],"rank"),
("AI","ai.csv","C",[20,10,6,10,30,34,34,34,18,11],"rank"),
("道具","assets.csv","C",[11,8,6,12,30,9,22,32,32,30,18],"rank"),
("ジャンル","genres.csv","J",[8,12,22,36,28,24,32,26,22,14],{"◎":"C6EFCE","○":"DDEBF7","△":"FFF2CC","×":"D9D9D9"}),
("手続き","procedures.csv","H",[18,4,44,22,30,14,36,10,11],{"実績あり":"C6EFCE","要確認":"FFF2CC"}),
("使った素材","used-assets.csv","A",[6,8,30,30,16,24,24,8,12,11,11],{"★":"C6EFCE","✕":"D9D9D9"}),
("自動化","automations.csv","B",[26,14,18,18,20,40,26,30,22,26,16,11],{"全自動":"C6EFCE","半自動":"DDEBF7","—":"F2F2F2"}),
("AIへの指示","rules.csv","C",[24,26,26,6,70,16],{})]
rankc={"S":"C6EFCE","A":"DDEBF7","B":"FFF2CC","C":"F2F2F2","外した":"D9D9D9"}
for name,f,rc,w,mode in tabs:
  s=wb.create_sheet(name);s["A1"]=f'=IMPORTDATA("{base}{f}")';s.freeze_panes="A2"
  for i,x in enumerate(w): s.column_dimensions[openpyxl.utils.get_column_letter(i+1)].width=x
  for c in range(1,len(w)+1): s.cell(1,c).font=Font(bold=True)
  R=f"A2:{openpyxl.utils.get_column_letter(len(w))}300"
  if mode=="rank":
    for k,v in rankc.items(): s.conditional_formatting.add(R,FormulaRule(formula=[f'${rc}2="{k}"'],fill=PatternFill("solid",fgColor=v)))
  else:
    for k,v in mode.items(): s.conditional_formatting.add(R,FormulaRule(formula=[f'LEFT(${rc}2,{len(k)})="{k}"'],fill=PatternFill("solid",fgColor=v)))
wb.save(sys.argv[1])
