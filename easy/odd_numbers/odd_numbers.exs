# ODD NUMBERS
# 
# Print the odd numbers from 1 to 99.
#
# INPUT SAMPLE:
# There is no input for this program.
#
# OUTPUT SAMPLE:
# Print the odd numbers from 1 to 99, one number per line.

Stream.unfold({1}, fn {f1} -> {f1, {f1 + 2}} end)
  |> Enum.take(50)
  |> Enum.each(&IO.puts/1)
