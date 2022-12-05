import gspread

# https://www.youtube.com/watch?v=bu5wXjz2KvU
sa = gspread.service_account(filename="service_account.json")
sh = sa.open('Bases')
global wks
wks = sh.worksheet('Bases')


class WorkSheet:
    def __init__(self, wks):
        self.wks = wks

    def action(self):
        print('Rows: ', self.wks.row_count)
        print('Cols: ', self.wks.col_count)

        # print(wks.acell('A9').value)
        print(self.wks.cell(3, 4).value)
        val = (self.wks.get_all_records())
        print(type(val))

def trimmer(val):
  if (len(val)) > 30:
    amount = (len(val)) - 30
    val = val[:-(int(amount))]
  return val


def search():
    global wks
    games = f'''<tr class="warning no-result">
              <td colspan="12"><i class="fa fa-warning"></i>&nbsp; No Result !!!</td>
            </tr>'''
    x = 0
    VL = wks.col_values(1)
    STID = wks.col_values(3)
    EXE = wks.col_values(6)
    for (a, b, c) in zip(VL, STID, EXE):
      a = trimmer(a)
      b = trimmer(b)
      c = trimmer(c) 
      x = x + 1
      if x > 1:
        games = games + f'''<tr id="tasks{x}" ><td>{a}</td><td>{b}</td><td>{c}</td><td>{x}</td><td><button class="btn btn-success" style="margin-left: 5px;" type="submit"><i class="fa fa-check" style="font-size: 15px;"></i></button><button class="btn btn-danger" style="margin-left: 5px;" type="submit"><i class="fa fa-trash" style="font-size: 15px;"></i></button></td></tr>''' 
    return games


#global w
#w = WorkSheet(wks)
#w.action()
# w.action()


# @#####################################
# print(wks.get_all_records())
# print(wks.get_all_values())

# wks.update('A3', 'Anthony')
# wks.update('D2:E3', [['Engineering', 'Tennis'], ['Business', 'Pottery']])
# wks.update('F2', '=UPPER(E2)', raw=False)
