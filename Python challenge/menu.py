def menu (**kwargs):
    print('Menu:')
    for key, value in kwargs.items():
      print(key)
    k = input('Choose an item: ')
    if k in kwargs:
      return kwargs[k]()
    else:
      return 'Invalid'
    