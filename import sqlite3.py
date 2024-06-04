import sqlite3



c = sqlite3.connect('expenses.db')
cursor = c.cursor()
cursor.execute('''
        CREATE TABLE IF NOT EXISTS expenses (
        id INTEGER PRIMARY KEY,
        date TEXT NOT NULL,
        category TEXT,
        amount REAL,
        description TEXT
        )
        ''')
 
expenses= [
    ('2024/3/6', 'حمل ونقل', '300','snapp'),
    ('2024/02/5','غدا','200','ناهار'),
    ('2024/03/05','بستنی','100','شکلاتی'),
    ('2024/2/29', 'سینما','75','فیلم')
]#ساخت table

cursor.executemany('''INSERT INTO expenses (date,category , amount , description)VALUES(? , ? , ? , ? )''',expenses)#اضافه کردن ستون ها 
c.commit()#ثبت تغیرات

while True:
    print('1 Add Expense     2 View        3 Update    4 Delete     5 Exit')
    choice = input("Enter choice: ")#چه عملیاتی قراره انجام بشه

    if choice == '1':
        date = input("Enter the date: ")
        category = input("Enter the category: ")
        amount = (input("Enter the amount: "))
        description = input("Enter the description: ")
        cursor.execute('''
            INSERT INTO expenses (date ,category , amount , description)
                    VALUES(?, ?, ?, ?) 
                         ''',(date , category , amount ,description))#اضافه کردن مورد جدید به table
        c.commit()
        print("done!")

    elif choice == '2':
        cursor.execute('SELECT * FROM expenses')# نشون دادن هزینه ها البته مطمئن نبودم که کل جدول باید  نش.ن داده بشه یا فقط amount
        expenses=cursor.fetchall()
        for i in expenses:
            print(i)


    elif choice == '3':
        id = int(input("Enter the ID you want to update: "))
        date = input(" new date: ")
        category = input("new category: ")
        amount = float(input("new amount: "))
        description = input("new description: ")
        cursor.execute('''UPDATE expenses 
                       SET date = ? , category = ? , amount=? , description=? WHERE id = ?
                       ''', (date , category , amount , description , id ))#اطلاعات جدید رو میگیره و ثبت میکنه
        c.commit()
        print("done!")


    elif choice == '4':
        id = int(input("Enter the ID  you want to delete: "))
        cursor.execute('DELET FROM expenses WHERE id = ?' , (id))
        c.commit()#ای دی رو مییگیره و هر جا ک ای دی برابر با عددی ک گرفته بود رو حذف میکنه
        
    elif choice == '5':
         print('bye.')
         break
    
    c.close()
