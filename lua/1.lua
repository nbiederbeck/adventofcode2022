result_a = 24000
result_b = 45000
example = "examples/1.txt"
puzzle = "build/1"

function build_calories(filename)
	io.input(filename)
	calories = {}
	elf_counter = 1

	for line in io.lines() do
		if calories[elf_counter] == nil then
			calories[elf_counter] = 0
		end
		if line ~= "" then
			cal = tonumber(line)
			calories[elf_counter] = calories[elf_counter] + cal
		else
			elf_counter = elf_counter + 1
		end
	end

	return calories
end

function run_a(filename)
	calories = build_calories(filename)
	return math.max(table.unpack(calories))
end

function test_a()
	assert(run_a(example) == result_a)
end

test_a()
print(run_a(puzzle))

function run_b(filename)
	calories = build_calories(filename)
	sum = 0
	for i = 1, 3 do
		max = math.max(table.unpack(calories))
		for i, val in ipairs(calories) do
			if val == max then
				table.remove(calories, i)
				break
			end
		end
		sum = sum + max
	end
	return sum
end

function test_b()
	assert(run_b(example) == result_b)
end

test_b()
print(run_b(puzzle))
