factorial()
{
    if (( $1 <= 1 )); then
        echo 1
    else
        last=$(factorial $(( $1 - 1 )))
        echo $(( $1 * last ))
    fi
}

for (( n=1; n<=20; n++ ))
do
    echo factorial de $n
    factorial $n
done

