puzzles/day%.txt:
	curl \
		--silent \
		https://adventofcode.com/2023/day/$*/input \
		--cookie "session=$$AOC_SESSION" \
		--output $@
