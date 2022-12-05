import webview

import os

dirname = os.path.dirname(__file__)

"""
This example demonstrates evaluating JavaScript in a web page.
"""


def evaluate_js(window):
    result = window.evaluate_js(
        r"""
        document.getElementById("tasks").innerHTML = "<td>2014</td><td>2014</td><td>2014</td><td>2014</td><td>2014</td><td>2014</td><td>2014</td><td>2014</td><td>2014</td><td>2014</td>"
        """
    )

    print(result)


if __name__ == '__main__':
    f = open(dirname + "\\render_pre_style.html", "r")
    htmlval = f.read()
    f = open(dirname + "\\css.html", "r")
    cssval = f.read()
    val = htmlval + cssval
    f = open(dirname + "\\render_post_style.html", "r")
    val = val + f.read()

    window = webview.create_window('Run custom JavaScript', html=val)
    webview.start(evaluate_js, window)
