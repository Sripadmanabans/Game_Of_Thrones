def game_of_thrones(string):
    var = {}
    for char in string:
        if var.has_key(char):
            num = var.get(char)
            num += 1
            var[char] = num
        else:
            var[char] = 1
            
    count = 0
    for element in var.keys():
        if var.get(element)%2 == 1:
            count += 1

    if count > 1:
        print "NO"
    else:
        print "YES"

string = raw_input()
game_of_thrones(string)
