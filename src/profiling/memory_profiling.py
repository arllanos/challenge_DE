import sys
from q1_memory import q1_memory
from q1_time import q1_time

def run(func, file_path):
    result = []
    if func == "q1_memory":
        result = q1_memory(file_path)
    elif func == "q1_time":
        result = q1_time(file_path)
    else:
        print("Function not recognized.")
    
    print(result)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python memory_profiling.py [function] [file_path]")
        sys.exit(1)

    function_name = sys.argv[1]
    file_path = sys.argv[2]

    run(function_name, file_path)
