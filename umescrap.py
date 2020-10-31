import pandas #pandasをインポート
import pprint

#取得したいページのurlを入力
url = 'http://www.jma.go.jp/jp/amedas_h/today-83431.html'

#urlを読み取る
fetched_daraframes = pandas.io.html.read_html(url)

#to_json関数で文字列をjsonに変換し，UmeNoAme.jsonで保存
fetched_daraframes[4].to_json('UmeNoAme.json',force_ascii=False)

#プリントしたい場合
ret = fetched_daraframes[4].to_json(force_ascii=False)
pprint.pprint(ret)