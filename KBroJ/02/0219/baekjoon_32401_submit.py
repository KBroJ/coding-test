def find_ana_string(string):

    ana_number = 0

    for i in range(len(string)):

        end_a_index = -1
        n_number = 0

        if string[i] == 'A':

            for j in range(i + 1, len(string)):
                if string[j] == 'A':
                    end_a_index = j
                    break

            if end_a_index != -1:
                for k in range(i + 1, end_a_index):
                    if string[k] == 'N':
                        n_number += 1

                if n_number == 1:
                    ana_number += 1

    return ana_number


N = int(input())
S = input()
print(find_ana_string(S))
