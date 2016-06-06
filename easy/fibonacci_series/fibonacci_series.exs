# CHALLENGE - FIBONACCI SERIES
#
# The Fibonacci series is defined as:
# F(0) = 0; F(1) = 1; F(n) = F(n–1) + F(n–2) when n>1.
# Given an integer n >= 0, print out the F(n).
#
# INPUT SAMPLE:
# The first argument will be a path to a filename containing integer numbers,
# one per line. E.g.
#  5
#  12
#
# OUTPUT SAMPLE:
# Print to stdout, the fibonacci number, F(n). E.g.
#  5
#  144


defmodule Fibonacci do

  defp get_n_numbers(n) do
    Stream.unfold({0,1}, fn {f1,f2} -> {f1, {f2, f1 + f2}} end)
      |> Enum.take(n)
  end

  def get_number_in_position(n) do
    serie = get_n_numbers(n + 1)
    Enum.at(serie, -1)
  end

end



ExUnit.start
defmodule Test do
  use ExUnit.Case

  test "should get fibonacci number is n position" do
    first_case = Fibonacci.get_number_in_position(5)
    second_case = Fibonacci.get_number_in_position(12)

    assert first_case == 5
    assert second_case == 144
  end
end
