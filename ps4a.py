# Problem Set 4A
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''
    if len(sequence) == 1:
        return [sequence]
    
    first_char = sequence[0]
    rest_permutations = get_permutations(sequence[1:])
    permutations = []
    
    for perm in rest_permutations:
        for i in range(len(perm) + 1):
            new_perm = perm[:i] + first_char + perm[i:]
            permutations.append(new_perm)
            
    return permutations
    
    
if __name__ == '__main__':
#    #EXAMPLE
#    example_input = 'abc'
#    print('Input:', example_input)
#    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
#    print('Actual Output:', get_permutations(example_input))
    
#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)

#example1: 
    example_input1 = 'a'
    print('Input:', example_input1)
    expected_output_1 = ['a']
    print('Expected Output:', expected_output_1)
    actual_output_1 = get_permutations(example_input1)
    print('Actual Output:', actual_output_1)
    
    #example2:
    input2 = 'ab'
    print('Input:', input2)
    expected_outpur_2 = ['ab', 'ba']
    print('Expected Output:', expected_outpur_2)
    actual_output_2 = get_permutations(input2)    
    print('Actual Output:', actual_output_2)
    
    #example3: 
    input3 = 'abc'
    print('Input:', input3)
    expected_output_3 = ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
    print('Expected Output:', expected_output_3)
    actual_output_3 = get_permutations(input3)
    print('Actual Output:', actual_output_3)
    
