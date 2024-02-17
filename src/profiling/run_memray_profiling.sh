#!/bin/bash

if [ "$#" -lt 2 ]; then
    echo "Usage: $0 function_name file_path"
    exit 1
fi

FUNCTION_NAME=$1
FILE_PATH=$2
PROJECT_ROOT="$(git rev-parse --show-toplevel)"

# execute `memray run` with the provided arguments to generate the .bin
memray run "$PROJECT_ROOT/src/profiling/run_memray_profiling.py" $FUNCTION_NAME $FILE_PATH

# find the most recent .bin file in the profiling directory
LAST_FILE=$(ls -t $PROJECT_ROOT/src/profiling/memray*.bin | head -1)

# run memray on the bin file generated in previous step
# usage: memray [-h] [-v] [-V] {run,flamegraph,table,live,tree,parse,summary,stats,transform,attach,detach} ...
memray stats $LAST_FILE
