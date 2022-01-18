from flask import Flask,request,jsonify
import csv

with open('articles.csv',encoding='utf-8') as f:
  arreader = csv.reader(f)
  data = list(arreader)
  all_articles = data[1:]

liked_articles = []
unliked_articles = []

app = Flask(__name__)

@app.route('/get-article')
def get_article():
  return jsonify({
    'data' : all_articles[1:],
    'status':'Success'
  }),201

@app.route('/liked-articles',methods=['POST'])
def liked_article():
   articles = all_articles[0]
   all_article = all_articles[1:]
   liked_articles.append(articles)
   return jsonify({
    'status' : "Success"
  })

@app.route('/unliked-articles',methods=['POST'])
def unliked_article():
   articles = all_articles[0]
   all_article = all_articles[1:]
   unliked_articles.append(articles)
   return jsonify({
    'status' : "Success"
  })

if __name__ == '__main__':
  app.run()