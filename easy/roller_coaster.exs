# CHALLENGE ROLLER COASTER
# You are given a piece of text. Your job is to write a program
# that sets the case of text characters according to the following rules:

# 1. The first letter of the line should be in uppercase.
# 2. The next letter should be in lowercase.
# 3. The next letter should be in uppercase, and so on. Any characters,
# except for the letters, are ignored during determination of letter case.

defmodule RollerCoaster do
    @pattern ~r/[A-Za-z]/

    def convert(text) do
      text
      |> String.codepoints
      |> _switch(true)
      |> Enum.join("")
    end

    defp _switch([], _), do: []

    defp _switch([head | tail], true) do
      case Regex.match?(@pattern, head) do
        true -> [ String.capitalize(head) | _switch(tail, false)]
        false -> [ String.capitalize(head) | _switch(tail, true)]
      end
    end

    defp _switch([head | tail], false) do
      case Regex.match?(@pattern, head) do
        true -> [ String.downcase(head) | _switch(tail, true)]
        false -> [ String.downcase(head) | _switch(tail, false)]
      end
    end
end


ExUnit.start
defmodule Test do
    use ExUnit.Case
    test "Letters should alternate lowercase and uppercase" do
        original_text = "for example - roller coaster"

        new_text = RollerCoaster.convert(original_text)
        assert new_text == "FoR eXaMpLe - RoLlEr CoAsTeR"
    end
end
