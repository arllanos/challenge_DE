import sys
from src.q1_memory import q1_memory
from src.q1_time import q1_time
from src.q2_memory import q2_memory
from src.q2_time import q2_time
from src.q3_memory import q3_memory
from src.q3_time import q3_time


def run(func, file_path):
    if function_to_run := globals().get(func):
        result = function_to_run(file_path)
        print(result)
    else:
        print(f"Function {func} not recognized.")
        

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python memory_profiling.py [function] [file_path]")
        sys.exit(1)

    function_name = sys.argv[1]
    file_path = sys.argv[2]

    run(function_name, file_path)
