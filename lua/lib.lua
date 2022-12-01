-- Print a table by unpacking beforehand
function print_table(t)
	print(table.unpack(t))
end

-- Pretty Print
--
-- Unpacks tables before printing, prints everything else as expected.
-- Only takes a single argument, not API compatible with print.
function pprint(_)
	if type(_) == type({}) then
		print_table(_)
	else
		print(_)
	end
end
