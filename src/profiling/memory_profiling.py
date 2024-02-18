import sys
from src.q1_memory import q1_memory
from src.q1_time import q1_time
from src.q2_memory import q2_memory
from src.q2_time import q2_time
from src.q3_memory import q3_memory
from src.q3_time import q3_time


def run(func, file_path):
    result = []
    if func == "q1_memory":
        result = q1_memory(file_path)
    elif func == "q1_time":
        result = q1_time(file_path)
    elif func == "q2_memory":
        result = q2_memory(file_path)
    elif func == "q2_time":
        result = q2_time(file_path)
    elif func == "q3_memory":
        result = q3_memory(file_path)
    elif func == "q3_time":
        result = q3_time(file_path)
    else:
        print(f"Function {func} not recognized.")
    
    print(result)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python memory_profiling.py [function] [file_path]")
        sys.exit(1)

    function_name = sys.argv[1]
    file_path = sys.argv[2]

    run(function_name, file_path)
