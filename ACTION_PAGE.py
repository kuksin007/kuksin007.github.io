import cgi

form = cgi.FieldStorage()
text1 = form.getfirst("fname", "не задано")
text2 = form.getfirst("lname", "не задано")
text3 = form.getvalue("elems")
print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
        <html>
        <head>
            <meta charset="utf-8">
            <title>Обработка данных форм</title>
        </head>
        <body>""")

print("<h1>Обработка данных форм!</h1>")
print("<p>TEXT_1: {}</p>".format(text1))
print("<p>TEXT_2: {}</p>".format(text2))
print("<p>TEXT_3: {}</p>".format(text3))
print("""</body>
        </html>""")