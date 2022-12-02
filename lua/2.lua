result = {}
result.a = 15
result.b = 12

shape = {}
shape.rock = 1
shape.paper = 2
shape.scissors = 3

outcome = {}
outcome.lose = 0
outcome.draw = 3
outcome.win = 6

function roshambo(me, op)
	if me == op then
		return outcome.draw
	elseif me == "rock" and op == "scissors" then
		return outcome.win
	elseif me == "rock" and op == "paper" then
		return outcome.lose
	elseif me == "paper" and op == "scissors" then
		return outcome.lose
	elseif me == "paper" and op == "rock" then
		return outcome.win
	elseif me == "scissors" and op == "paper" then
		return outcome.win
	elseif me == "scissors" and op == "rock" then
		return outcome.lose
	end
end

opponent = {}
opponent.A = "rock"
opponent.B = "paper"
opponent.C = "scissors"

me = {}
me.X = "rock"
me.Y = "paper"
me.Z = "scissors"

function parse_line(line)
	_, _, _op, _me = string.find(line, "(%a+)%s(%a+)")
	return opponent[_op], me[_me]
end

function part.a(filename)
	io.input(filename)

	total = 0
	for line in io.lines() do
		_op, _me = parse_line(line)
		total = total + roshambo(_me, _op)
		total = total + shape[_me]
	end

	return total
end

function roshambo_outcome(op, outcome)
	local o = nil
	if outcome == "draw" then
		o = op
	elseif outcome == "win" then
		if op == "scissors" then
			o = "rock"
		elseif op == "rock" then
			o = "paper"
		else
			o = "scissors"
		end
	else -- outcome == "lose"
		if op == "scissors" then
			o = "paper"
		elseif op == "rock" then
			o = "scissors"
		else
			o = "rock"
		end
	end
	return o
end

game = {}
game.X = "lose"
game.Y = "draw"
game.Z = "win"

function parse_line_outcome(line)
	_, _, _op, _me = string.find(line, "(%a+)%s(%a+)")
	return opponent[_op], game[_me]
end

function part.b(filename)
	io.input(filename)

	total = 0
	for line in io.lines() do
		_op, _outcome = parse_line_outcome(line)
		_me = roshambo_outcome(_op, _outcome)
		total = total + outcome[_outcome]
		total = total + shape[_me]
	end

	return total
end
