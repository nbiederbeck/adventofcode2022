result = {}
result.a = 24000
result.b = 45000

function build_calories(filename)
	io.input(filename)
	local calories = {}
	local elf_counter = 1

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

function part.a(filename)
	local calories = build_calories(filename)
	return math.max(table.unpack(calories))
end

function greater(a, b)
	return a > b
end

function part.b(filename)
	calories = build_calories(filename)
	table.sort(calories, greater)
	sum = calories[1] + calories[2] + calories[3]
	return sum
end
