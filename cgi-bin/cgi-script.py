#!/usr/bin/python3

import cgi
form = cgi.FieldStorage()
your_name = form.getvalue('your_name')
company_name = form.getvalue('company_name')

print("Content-type:text/html\n")
print("<html>")
print("<head>")
print("<title>First CGI Program</title>")
print("</head>")
print("<body>")
print(f"<h2>Hello, {your_name} who is working in {company_name}</h2>")
print("</body>")
print("</html>")