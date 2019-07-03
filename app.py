# from flask import Flask, render_template
# app = Flask(__name__)

# print(__name__)

# @app.route('/')
# def home():
#     try:
#         with open('SPOON.html', 'r') as f:
#             return f.read()
#     except Exception as e:
#         return 'error: ' + str(e)

class Circle(float):
    def compare(self, ls):
        bigger = [other for other in ls if self < other]
        smaller = [other for other in ls if self > other]
        same = [other for other in ls if self == other]

        return {a: b for a, b in zip(['bigger', 'smaller', 'same'], [bigger, smaller, same])}

a = Circle(2)
b = Circle(3)
print(a+b)