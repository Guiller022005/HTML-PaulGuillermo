import json

with open('dia3/tablas.json', 'r') as f:
    data = json.load(f)
    
html_Table = """

<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Tabla JSON a HTML</title>
<style>
    table {
    width: 100%;
    border.collapse: collapse;
    }
    th, td{
      border: 1px solid #dddddd;
      padding: 8px;
      text-align: left;
    }
    th{
      background-color: #f2f2f2;
    }
</style>
</head>
<body>

<table>
    <thead>
        <tr>
            <th>ID</th>
            <th>Index</th>
            <th>GUID</th>
            <th>Balance</th>
            <th>Name</th>
            <th>Email</th>
            <th>Phone</th>
            <th>Address</th>
            <th>About</th>
            <th>Registered</th>
            <th>Latitude</th>
            <th>Longitude</th>
            <th>Tags</th>
            <th>Friends</th>
        </tr>
    </thead>
    <tbody>
"""


for item in data:
    html_Table += "<tr>"
    html_Table += "<td>{}</td>".format(item['_id'])
    html_Table += "<td>{}</td>".format(item['index'])
    html_Table += "<td>{}</td>".format(item['guid'])
    html_Table += "<td>{}</td>".format(item['balance'])
    html_Table += "<td>{}</td>".format(item['name'])
    html_Table += "<td>{}</td>".format(item['email'])
    html_Table += "<td>{}</td>".format(item['phone'])
    html_Table += "<td>{}</td>".format(item['address'])
    html_Table += "<td>{}</td>".format(item['about'])
    html_Table += "<td>{}</td>".format(item['registered'])
    html_Table += "<td>{}</td>".format(item['latitude'])
    html_Table += "<td>{}</td>".format(item['longitude'])
    html_Table += "<td>{}</td>".format(', '.join(item['tags']))
    friends_with_id = ', '.join(["{} ({})".format(friend['name'], friend['id']) for friend in item['friends']])
    html_Table += "<td>{}</td>".format(friends_with_id)  # Mostrar nombres de amigos con ID
    html_Table += "</tr>"

html_Table += """
    </tbody>
<table>
</body>
</html>
"""

with open('tabla.html','w') as f:
    f.write(html_Table)