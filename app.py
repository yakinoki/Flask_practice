import random
from flask import Flask, render_template

# Flaskアプリケーションのインスタンスを作成
app = Flask(__name__)

# カードのマークを表す文字列（カンマ区切り）
card_marks = 'star,sun,moon'

# 文字列をカンマで分割し、リストに変換
marks = card_marks.split(',')

# ルート('/')にアクセスしたときに、index.htmlをレンダリングする
@app.route('/')
def index():
    # templatesディレクトリ内のindex.htmlをクライアントに返す
    return render_template('index.html')

# '/random_mark' にアクセスしたときに、ランダムなマークを返す
@app.route('/random_mark')
def random_mark():
    # 'marks' リストの中からランダムに1つ選ぶ
    mark = random.choice(marks)
    # 選んだマークを文字列として返す（API的な使い方）
    return mark

# アプリケーションのエントリーポイント
if __name__ == '__main__':
    # Flaskアプリをデバッグモードで実行（変更があると自動リロードされる）
    app.run(debug=True)
