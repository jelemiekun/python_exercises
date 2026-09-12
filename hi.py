import buffer
import second

buffer.greeting("from hi.buffer!")
second.buffer.greeting("from hi.second.buffer!")

print(buffer.var_buffer)
print(second.var_buffer)

print(dir(buffer))

print(__file__)
