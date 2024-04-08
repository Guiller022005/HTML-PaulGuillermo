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

