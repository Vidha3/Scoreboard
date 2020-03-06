#!/usr/bin/env python3
from flask import (Flask,
                   flash,
                   render_template,
                   url_for,
                   redirect,
                   request
                   )
# from score_board.src.scoreboard import Scoreboard
from score_board.forms import DataForm
from score_board import sb

app = Flask(__name__)
app.config['SECRET_KEY'] = '8815976dfb4c5e3a124ce3cdcae89812'


@app.route('/')
@app.route('/home', methods=['get', 'post'])
def home():
    form = DataForm()
    # receive flag from HTML, save object state;
    # 0 = original, 1 = ascending, 2 = descending
    sb.ordering = request.args.get('order', default=sb.ordering, type=int)
    if sb.ordering > 0:  # ordering is ascending or descending
        rev = sb.ordering == 2  # descending
        final_sb = sorted(sb.scoreboard, key=lambda x: x[1], reverse=rev)
        scores_dict = {'score_table': final_sb}
        if form.is_submitted() and form.validate_on_submit():
            name, score = form.name.data, form.score.data
            if not sb.add_score(name, score):
                flash("You cannot modify existing scores. You can only add new ones.")
            return redirect(url_for('home'))
        return render_template('home.html', title='Scoreboard', scores=scores_dict, form=form)

    else:
        # choice is original order
        scores_dict = {'score_table': sb.scoreboard}
        if form.is_submitted() and form.validate_on_submit():
            name, score = form.name.data, form.score.data
            if not sb.add_score(name, score):
                flash("You cannot modify existing scores. You can only add new ones.")

            return redirect(url_for('home'))
        return render_template('home.html', title='Scoreboard', scores=scores_dict, form=form)


if __name__ == "__main__":
    app.run(debug=True)
