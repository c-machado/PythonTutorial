next_stop = "lovely amsterdam"

print(len(next_stop))
print(next_stop.lower())
print(next_stop.upper())
print(str(2)+next_stop)

name = "dianacarolinamachadouseche"
l = next_stop.split()
print(l)
print(name.replace('a','A'))
print(name.replace('a','A',2))

substring = name[0:6]
step = name[0:6:2]
complete_string = name[:]
string_last_index = name[-1]
string_truncate = name[:-1]
step_whole_string = name[::2]
reverse_string = name[::-1]

print(substring)
print(step)
print('complete '+complete_string)
print(string_last_index)
print(string_truncate)
print(step_whole_string)
print(reverse_string)

#concatenate
hobby = "yoga"
place = "home"
print("I love to do " + hobby + " at my " + place)
print("I love to do % at my %" % (hobby, place))
