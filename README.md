# hana-fuku_auto-reserve: 鼻・副鼻腔クリニック大宮の自動入力・予約ツール
 [鼻・副鼻腔クリニック大宮](https://hana-fuku.com)の自動新規予約ツールです。  
 新規予約では毎回、氏名やメールアドレスなどの個人情報の入力が必要となり、煩わしいために開発しました。
 
## Getting Started: 使い方
 お使いの環境に下記の利用サードパーティライブラリをインストール。  
 personal_info.jsonファイルのサンプルデータを、ご自身のデータに変更してからmain.pyをご利用ください。  
 Python3.x系での利用を想定しています。  
 最後の予約確定ボタンは自動クリックさせない設定となっています。確定ボタンのクリックまで自動化させたい場合はコメントを外してください。
 
## Required Libraries: 利用サードパーティライブラリ
* Selenium
* webdriver_manager

## Discraimer: 免責事項
* サンプルデータのまま利用することは絶対におやめください。  
 （最悪の場合、威力業務妨害に問われる可能性もあります。その場合でも当方は責任をもてませんので、自己責任にてお願いいたします。）
* 2023/04/15時点でのWebフォームUIに基づいて開発しています。UI等に変更が生じた場合には動作保証いたしかねます。
* Sleep関数の数値を削除したり、極端に短い値を設定するなど、DoS攻撃を疑われるような行為はおやめください。

## Recommendation: おすすめの利用方法
MacおよびLinuxの場合、Cronを利用すると新規予約枠が開放される毎日0時に自動的にスクリプトを立ち上げることが可能です。  
下記の記事を参考にしてください。
* [Pythonスクリプトをcronで定期実行させる｜こはた｜note](https://note.com/kohaku935/n/ne0957479c819)
* [cronでPythonスクリプトを自動実行する | masayanblog](https://maasaablog.com/development/backend/python/737/)
* [venv環境でpythonスクリプトをcronで周期実行 - Qiita](https://qiita.com/gao_gao/items/12a1e9620bddbff7463f)

