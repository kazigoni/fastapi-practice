"""Details about the async def syntax for path operation functions"""
# TL;DR - TooLong, Didn't Read

"""
if any third party libraries use 'await' to call them
then, declare path operation functions with 'asynch def'
"""


# result = await some_library()
@app.get(/):
async def read_results():
    result = await some_library()
    return result
# 'await' can only be used inside async function
# it will help performance optimization

"""
Asynchronous Code
async and await
Coroutines
"""
"""Asynchronous Code
---------------------------
Asynchronous code just means that the language 💬 has a way to tell the computer / program 
🤖 that at some point in the code, it 🤖 will have to wait for something else to finish somewhere else."""

"""
wait for something else" normally refers to I/O operations that are relatively "slow" (compared to the speed of the processor and the RAM memory), like waiting for:

the data from the client to be sent through the network
the data sent by your program to be received by the client through the network
the contents of a file in the disk to be read by the system and given to your program
the contents your program gave to the system to be written to disk
a remote API operation
a database operation to finish
a database query to return the results
etc.
"""

"""
Concurrency and Burgers
-------------------------
This idea of asynchronous code described above is also sometimes called "concurrency". 
It is different from "parallelism".

Concurrency and parallelism both relate to "different things happening more or less at the same time".
"""
