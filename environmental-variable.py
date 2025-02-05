import os

name = os.getenv("MY_NAME", "World")
print(f"Hello {name} from Python")

"""
The second argument to os.getenv() is the default value to return.

If not provided, it's None by default, here we provide "World" as the default value to use
"""
"""Here we don't set the env var yet
python main.py

💬 As we didn't set the env var, we get the default value

Hello World from Python

💬 But if we create an environment variable first
export MY_NAME="Wade Wilson"

💬 And then call the program again
python main.py

💬 Now it can read the environment variable

Hello Wade Wilson from Python"""

