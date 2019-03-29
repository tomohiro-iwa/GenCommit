# データセットの作り方（うろ覚え）

## 全体

ほとんどのpythonスクリプトは
引数としてレポジトリ名　ディレクトリパス　ファイル名　などをとり
その結果をリダイレクトします。
例）
~~~
./get_issu_list.py <ユーザ名>/<レポジトリ名> > リダイレクト先ファイル
~~~
これをデータセットとして使用する各リポジトリに対して行っています。
get_api900.shなどのシェルスクリプトは各レポジトリに対してpythonスクリプトを実行し
それをリダイレクトする処理書かれています。
これらのshはxargsとechoとvimを使って、そのつど生成していたため、shを生成するコードは
ありません。

大体のスクリプトにおいて
python = 1レポジトリに対する処理
sh     = pythonをすべてのレポジトリに対して適用する処理

### 備考
- get_api900.sh などshのファイル名についている数字はアバウトなコーパスの規模をあらわしています
- pythonスクリプトと使い方は名前が同じshを見ると推測しやすいかも

## 流れ
まずapi.jsonを作成します
これらのファイルはそれぞれ./corpus/<ユーザ名>/<レポジトリ名>/内に作成します。

説明を簡略化するために1レポジトリのみの場合で記述します。
今回コーパスを作成するために以下のファイルを順に作成しました。
試行錯誤を繰り返していたので、うろ覚えですが。。。

### 備考
最終的にはhash2corpus2.pyでコーパスが生成されています。
（hash2corpus.pyは古いファイルです）
以下の手順はこのスクリプトが必要としているファイルを生成するための手順です。




### api.json 


~~~
get_issue_list.py <ユーザ名>/<レポジトリ名> > corpus/<ユーザ名>/<レポジトリ名>/api.json
~~~
で作成します。
これはapiから習得したjsonをそのままテキストとして保存しているものです。

### summary.json 
これはsummary.pyによって作成します。
このファイルはapi.jsonから必要な情報だけを抜き出し整理したjsonです。

### url2body.json
url2body.pyにapi.jsonを渡して生成します。

### hash.json
get_hash.pyにapi.jsonを渡して生成します。
これはpullのURLからpullに含まれるhashをスクレイピングで取得しています。

### corpus.json
issue,msg,diff が含まれたjsonです。hash2corpus2.pyで作成します。
hash2corpus2.pyではsummary.json,url2body.json,hash.jsonの3つが含まれたディレクトリのパスを
引数で指定します
このファイルをdrip_corpus.pyによって抽出することでwseq2seqに入力するコーパスが作成できます。


## 最後に

殴り書きのため分かりにくい部分が多々あると思います。
質問等はお気軽にメール(tomo1996722@gmail.comまで)でお問い合わせください。



## 自分用MEMO
api.json   hash_msg.txt  mrg_and.txt     msg2issue_nom.json
api2.json  hoge          mrg_hash.txt    msg_nom.txt
diff.txt   hoge.json     msg.txt         summary.json
hash.json  issu.txt      msg2issue.json  url2body.json
