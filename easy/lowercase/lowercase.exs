# CHALLENGE LOWERCASE
# Given a string write a program to convert it into lowercase.
#
# INPUT SAMPLE:
# The first argument will be a path to a filename containing sentences,
# one per line. You can assume all characters are from the english language. E.g.
#
#     HELLO CODEEVAL
#     This is some text
#
# OUTPUT SAMPLE:
# Print to stdout, the lowercase version of the sentence, each on a new line. E.g.
#
#     hello codeeval
#     this is some text


defmodule LowerCase do
  def convert(text), do: String.downcase(text)
end



ExUnit.start
defmodule Test do
  use ExUnit.Case

  test "should convert characters in lowercase" do
    test_case1 = LowerCase.convert("HELLO CODEEVAL")
    test_case2 = LowerCase.convert("This is some text")

    assert test_case1 == "hello codeeval"
    assert test_case2 == "this is some text"
  end

end
