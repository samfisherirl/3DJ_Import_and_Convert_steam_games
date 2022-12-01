
strings = "asdkfjnladsjngflasdgladsnffnadfjkandskjflasfjklnadsjkfnajksldfnadjklsfajklndsfnkljadnfjklakjnsfjklasd"


def trimmer(val):
  if (len(val)) > 10:
    amount = (len(val)) - 10
    val = val[:-(int(amount))]
  return val
    
val = trimmer(strings)
print(val)