from flask import Flask, request, jsonify, make_response
from newspaper import Article
# import nltk

# API Ref - https://programminghistorian.org/en/lessons/creating-apis-with-python-and-flask
# Lambda 1 - https://pythonforundergradengineers.com/deploy-serverless-web-app-aws-lambda-zappa.html
# Lambda 2 - https://towardsdatascience.com/deploy-a-python-api-on-aws-c8227b3799f0
# Test


# summary, reading time, video duration
# API - 1. on personal website (portfolio)
# 2. telegram bot (pass link to telegram bot, it hits this function, and returns keywords in the bot itself


app = Flask(__name__)
app.config['DEBUG'] = True


@app.route('/', methods=['GET'])
def index():
    return "<h1>Yes this works</h1>"


@app.route('/api/v1/extract', methods=['GET'])
def extract():
    if 'url' in request.args:
        url = str(request.args['url'])
        article = Article(url)

        article.download()
        article.parse()
        article.nlp()

        keywords = article.keywords
        authors = article.authors
        published_at = article.publish_date
        article_text = article.text
        word_count = len(article_text.split())

        return make_response(jsonify({
            "message": url,
            "keyword": keywords,
            "authors": authors,
            "published_at": published_at,
            'word_count': word_count,
            'article_text': article_text
        }), 400)
    else:
        return jsonify({"error": "no url present"})


if __name__ == '__main__':
    app.run()
