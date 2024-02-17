#!/bin/bash

if [ "$#" -lt 2 ]; then
    echo "Usage: $0 function_name file_path"
    exit 1
fi

FUNCTION_NAME=$1
FILE_PATH=$2
PROJECT_ROOT="$(git rev-parse --show-toplevel)"

# print box with function name
BOX_WIDTH=90
FUNCTION_NAME_LENGTH=${#FUNCTION_NAME}
TOTAL_PADDING=$((BOX_WIDTH - FUNCTION_NAME_LENGTH - 2)) # 2 for the side bars
LEFT_PADDING=$(($TOTAL_PADDING / 2))
RIGHT_PADDING=$((TOTAL_PADDING - LEFT_PADDING))
printf "\n%-${BOX_WIDTH}s\n" | tr " " "-"
printf "|%-${LEFT_PADDING}s%s%-${RIGHT_PADDING}s|\n" "" "$FUNCTION_NAME" ""
printf "%-${BOX_WIDTH}s\n" | tr " " "-"

# execute `memray run` with the provided arguments to generate the .bin
memray run "$PROJECT_ROOT/src/profiling/memory_profiling.py" $FUNCTION_NAME $FILE_PATH

# find the most recent .bin file in the profiling directory
LAST_FILE=$(ls -t $PROJECT_ROOT/src/profiling/memray*.bin | head -1)

# run memray on the bin file generated in previous step
# usage: memray [-h] [-v] [-V] {run,flamegraph,table,live,tree,parse,summary,stats,transform,attach,detach} ...
memray stats $LAST_FILE
