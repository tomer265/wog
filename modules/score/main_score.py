from flask import Flask, render_template
from utils import SCORES_FILE_NAME
from common import try_parse

app = Flask('wog_score')


@app.route('/')
def score_server():
    try:
        with open(SCORES_FILE_NAME, 'r') as file:
            score_to_present = file.read()
            if not try_parse(score_to_present):
                raise ValueError
            return render_template('/views/index.html', SCORE=score_to_present)
    except FileNotFoundError:
        return render_template('/views/error.html', ERROR='Could not find scores file.')
    except ValueError:
        return render_template('/views/error.html', ERROR='Could not cast score to an integer.')
    except:
        return render_template('views/error/html', ERROR='Could not load score page.')


score_server()
