import cProfile
import pstats
from typing import Callable

def run(func: Callable, file_path: str, top_offending: int = 15) -> None:
    """
    Runs cProfile on a specified function and prints a summary along with the top offending code
    sections where most time was spent.

    Parameters:
    - func: The function to profile.
    - file_path: The path to the file that the function will process.
    - top_offending: The number of top offending functions to display.
    """
    profiling_dir = "profiling"

    func_name = func.__name__
    profile_file_path = f"{profiling_dir}/time_cprofile_results_{func_name}.bin"

    cProfile.run(f"{func_name}('{file_path}')", profile_file_path)
    p = pstats.Stats(profile_file_path)
    p.sort_stats("cumulative").print_stats(top_offending)