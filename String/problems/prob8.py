def minimumString(s, b, c):
    mother = []
    list_ = [s,b,c]

    for str_ in list_[1:]:
        

        print(str_)




    # for str_ in list_:
    #     if str_ not in mother:
    #         return False
    

    return mother

    ...

""" 
    abc
     bca
  aaa
--------
  aaabca

  ab
   ba
  aba
--------
  aba

 """


print(minimumString( "abc","bca","aaa"))