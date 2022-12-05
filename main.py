import webview
import GSHEET as GS
import time
import os

dirname = os.path.dirname(__file__)
"""
This example demonstrates evaluating JavaScript in a web page.
"""

#
# def greet():

#     val2 = GS.search()

#     result = window.evaluate_js = r"""document.getElementById("t").innerHTML = ohshitnadfasdfadf"""
#     print(result)


class Api:

    def sayHelloTo(self):
        time.sleep(0.1)
        val2 = GS.search()
        response = {'message': val2}
        return response

    def printer(self, val):
        print(val)


api = Api()

#f = open((os.path.join(dirname, 'render_pre_style.html')), "r")
#htmlval = f.read().replace('\n', '')
#f = open((os.path.join(dirname, 'css.html')), "r")
#cssval = f.read().replace('\n', '')
#val = htmlval + cssval
#f = open((os.path.join(dirname, 'render_post_style.html')), "r")
#val = val + f.read().replace('\n', '')

window = webview.create_window('Testing PyWebView',
                               'lib\\render.html',
                               js_api=api,
                               width=1100,
                               height=900)
webview.start(debug=True)
