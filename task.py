from flask import Flask, request

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

NAME_LIMIT_SYMBOL = 10


@app.route('/likes')
def likes_treatment():
    query_params = request.args.get('names')
    if not query_params:
        return {
            "error": False,
            "data": "Это никому не нравится",
            "error_message": None
        }

    names = query_params.split(',')

    for name in names:
        if len(name) > NAME_LIMIT_SYMBOL or not name.isalpha():
            return {
                "error": True,
                "data": None,
                "error_message": "*Введены недопустимые символы*"
            }

        if len(names) == 1:
            word = 'лайкнул'
        else:
            word = 'лайкнули'

        return {
            "error": False,
            "data": f"{', '.join(names)} {word} это" if len(
                names) <= 3 else f"{', '.join(names[:2])} и еще {len(names[2:])} человека {word} это",
            "error_message": None
        }


if __name__ == '__main__':
    app.run(debug=True)