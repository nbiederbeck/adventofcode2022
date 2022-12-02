#!/usr/bin/env lua
require("lua/lib") -- make functions from lib.lua accessible

for _, day in ipairs(arg) do
	if tonumber(day) then
		part = {}

		require("lua/" .. day) -- "import" functions into `part`
		ex = "examples/" .. day .. ".txt"
		puzzle = "build/" .. day

		assert(part.a(ex) == result.a)
		print(part.a(puzzle))

		assert(part.b(ex) == result.b)
		print(part.b(puzzle))

		local part, result
	end
end
