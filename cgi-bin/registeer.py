import cgi
import html
cabinet=""
pas="l4oxr"

form = cgi.FieldStorage()

password = form.getfirst("password", "")
password = html.escape(password)

code="""<!DOCTYPE HTML>
<html>
<head>
<meta charset="utf-8">
<title>Стена</title>
</head>
<body>
    <form>
        Пароль: <input type="password" name="password">
        <input type="submit">
    </form>
    
    {cabinet}
    
</body>
</html>"""

if pas==password:
    cabinet="""<p>Hello Python!</p>"""

else:
    cabinet="no"

print('Content-type: text/html\n')
print(code.format(cabinet=cabinet))
