#add this function to your bashrc and create an alias

function finddir {
    PROJECT_DIR=""

    match_count=$(ls "$PROJECT_DIR" | grep -ic "$1")
    if [[ $match_count != 1 ]];then
        echo "ERROR did not match one directory:"
        ls "$PROJECT_DIR" | grep -i "$1"
    else
        "cd $PROJECT_DIR/$(ls "$PROJECT_DIR" | grep -i "$1")"
    fi
}
