'''
reverse_string('awesome') # 'emosewa'
reverse_string('Colt') # 'tloC'
reverse_string('Elie') # 'eilE'
'''
 # add whatever parameters you deem necessary - good luck!
def reverse_string(string):
    string = "".join(reversed(string))
    return string
 print(reverse_string('awesome'))
