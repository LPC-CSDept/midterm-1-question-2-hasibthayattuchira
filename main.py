def main():
    """
    ########################################
    Code Your Program here
    ########################################
    """
    i = 0
    longest = shortest = ''
    while True:
        word = input('Enter a word: ')
        if word.lower() == 'stop':
            break
        if len(word) > len(longest):
            longest = word
        elif len(word) < len(shortest) or shortest == '':
            shortest = word

    ########################################
    # Do not delete the return statement
    ########################################
    return longest, shortest
##


if __name__ == '__main__':
    main()
