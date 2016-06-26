# CHALLENGE REVERSE WORDS
# Write a program which reverses the words in an input sentence.
#
# INPUT SAMPLE:
# The first argument is a file that contains multiple sentences, one per line.
# Empty lines are also possible.
#
#     Hello World
#     Hello CodeEval
#
# OUTPUT SAMPLE:
# Print to stdout each sentence with the reversed words in it, one per line.
# Empty lines in the input should be ignored. Ensure that there are no trailing
# empty spaces in each line you print.
#
#     World Hello
#     CodeEval Hello



defmodule Reverser do

  def words(sentence) do
    sentence
      |> String.split(" ")
      |> Enum.reverse
      |> Enum.join(" ")
  end

end



ExUnit.start
defmodule Test do
  use ExUnit.Case

  test "should reverse words" do
    reversed_words = Reverser.words("Hello World")
    reversed_words_second = Reverser.words("Hello CodeEval")

    assert reversed_words == "World Hello"
    assert reversed_words_second == "CodeEval Hello"
  end
end
