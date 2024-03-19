from flask import Flask, render_template
from utils import SCORES_FILE_NAME_API_CONTEXT


app = Flask('main_score', template_folder='template')
app.app_context().push()


@app.route('/')
def score_server():
    with app.app_context():
        try:
            with app.app_context():
                with open(SCORES_FILE_NAME_API_CONTEXT, 'r') as file:
                    score_to_present = file.read()
                    return render_template('index.html', SCORE=score_to_present)
        except FileNotFoundError:
            return render_template('error.html', ERROR='Could not find scores file.')
        except ValueError:
            return render_template('error.html', ERROR='Could not cast score to an integer.')
        except:
            return render_template('error.html', ERROR='Could not load score page.')


score_server()
