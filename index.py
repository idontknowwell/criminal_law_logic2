from flask import Flask, render_template_string, redirect, url_for

app = Flask(__name__)

@app.route("/")
def index():
    return render_template_string("""
        <h1>죄명을 선택하세요</h1>
        <ul>
            <li><a href="{{ url_for('assault') }}">폭행</a></li>
            <li><a href="{{ url_for('fraud') }}">사기</a></li>
            <li><a href="{{ url_for('indecent_act') }}">강제추행</a></li>
        </ul>
    """)

@app.route("/assault")
def assault():
    return redirect("https://idontknowwell-criminal_law_logic2-assault.streamlit.app/")

@app.route("/fraud")
def fraud():
    return redirect("https://idontknowwell-criminal_law_logic2-fraud.streamlit.app/")

@app.route("/indecent_act")
def indecent_act():
    return redirect("https://idontknowwell-criminal_law_logic2-indecent_act.streamlit.app/")

if __name__ == "__main__":
    app.run(debug=True)
