import pygsheets
client = pygsheets.authorize(service_file='service_account.json')
 

sh = client.open('Bases')
wks = sh.sheet1
wks.update_value('A1', "Numbers on Stuff")

# # https://www.youtube.com/watch?v=bu5wXjz2KvU
# sa = gspread.service_account(filename="service_account.json")
# sh = sa.open('Bases')
# global wks
# wks = sh.worksheet('Bases')


# class WorkSheet:
#     def __init__(self, wks):
#         self.wks = wks

#     def action(self):
#         print('Rows: ', self.wks.row_count)
#         print('Cols: ', self.wks.col_count)

#         # print(wks.acell('A9').value)
#         print(self.wks.cell(3, 4).value)
#         val = (self.wks.get_all_records())
#         print(type(val))


# def search(val):
#     global wks
#     games = {}
#     x = 0
#     VL = wks.col_values(1)
#     STID = wks.col_values(3)
#     for i in VL:
#         x = x + 1
#         if val.casefold() in i.casefold():
#             games[STID[x]] = i

#     with open("myfile1.txt", "w+") as file:
#         for key, val in games.items():

#             file.write("{} =  ==steam ID== {}'\n'".format(val, key))



# global w
# w = WorkSheet(wks)
# w.action()
# # w.action()


# # @#####################################
# # print(wks.get_all_records())
# # print(wks.get_all_values())

# # wks.update('A3', 'Anthony')
# # wks.update('D2:E3', [['Engineering', 'Tennis'], ['Business', 'Pottery']])
# # wks.update('F2', '=UPPER(E2)', raw=False)
