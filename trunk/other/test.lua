random = math.random(10000)
log_random = math.log10(random)
print(random, log_random)
print("****")
filename = "test.lua"
for line in io.lines(filename) do print(line) end
print("\n")
print("now: "os.date())
