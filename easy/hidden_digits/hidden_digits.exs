# CHALLENGE HIDDEN DIGITS
# In this challenge you're given a random string containing hidden and visible digits. The digits are hidden
# behind lower case latin letters as follows: 0 is behind 'a', 1 is behind ' b ' etc., 9 is behind 'j'.
# Any other symbol in the string means nothing and has to be ignored. So the challenge is to find all visible
# and hidden digits in the string and print them out in order of their appearance.
#
# INPUT SAMPLE:
# Your program should accept as its first argument a path to a filename. Each line in this file contains a
# string. You may assume that there will be no white spaces inside the string. E.g.
#
#     abcdefghik
#     Xa,}A#5N}{xOBwYBHIlH,#W
#     (ABW>'yy^'M{X-K}q,
#     6240488
#
# OUTPUT SAMPLE:
# For each test case print out all visible and hidden digits in order of their appearance. Print out NONE in
# case there is no digits in the string. E.g.
#
#     012345678
#     05
#     NONE
#     6240488


defmodule HiddenDigits do

  defp get_digit_value(digit) do
    visible_digits = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    hidden_digits = %{
      a: 0, b: 1, c: 2, d: 3, e: 4, f: 5, g: 6, h: 7, i: 8, j: 9
    }

    case {hidden_digits[String.to_atom(digit)], digit in visible_digits} do
      {nil, false} -> ""
      {_, false} -> hidden_digits[String.to_atom(digit)]
      {_, true} -> digit
    end
  end


  def there_digits?(digits) do
    case {digits == ""} do
      {true} -> "NONE"
      {_} -> digits
    end
  end


  def get_digits(line) do
    String.codepoints(line)
      |> Enum.map(&get_digit_value(&1))
      |> Enum.join("")
      |> there_digits?()
  end
end



ExUnit.start
defmodule Test do
  use ExUnit.Case

  test "shoul get hidden digits" do
    test_case1 = HiddenDigits.get_digits("abcdefghik")
    test_case2 = HiddenDigits.get_digits("Xa,}A#5N}{xOBwYBHIlH,#W")
    test_case3 = HiddenDigits.get_digits("(ABW>'yy^'M{X-K}q,")
    test_case4 = HiddenDigits.get_digits("6240488")

    assert test_case1 == "012345678"
    assert test_case2 == "05"
    assert test_case3 == "NONE"
    assert test_case4 == "6240488"
  end

end
