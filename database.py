import mysql.connector

connection_params = {
    'host': "localhost",
    'user': "root",
    'password': "",
    'database': "food_stack",
}

request = "select id, nom, prix, photo, description from menu"

with mysql.connector.connect(**connection_params) as db:
    with db.cursor() as c:
        c.execute(request)
        food_stack = c.fetchall()
        for menu in food_stack:
            print(menu)

        c.execute("insert into menu (id, nom, prix, photo, description) \
                           values (2, 'Menu 2', 15001, 'photo2.jpg', 'Ceci est un test')")
        db.commit()
