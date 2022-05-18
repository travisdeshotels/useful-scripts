#add this function to your bashrc and create an alias

# shellcheck disable=SC2010
function finddir {
    PROJECT_DIR=""

    match_count=$(ls "$PROJECT_DIR" | grep -ic "$1")
    if [[ $match_count == 0 ]];then
        echo "No match"
    elif [[ $match_count == 1 ]];then
        cd "$PROJECT_DIR/$(ls "$PROJECT_DIR" | grep -i "$1")" || exit
    else
        lines=$(ls "$PROJECT_DIR" | grep -i "$1")
        i=1
        lines_array=()
        while IFS= read -r line
        do
            echo $i. "$line"
            lines_array[$i]="$line"
            i=$((i+1))
        done <<< "$lines"
        echo -n "Select one: "
        read -r choice
        cd "$PROJECT_DIR/${lines_array[$choice]}" || exit
    fi
}
