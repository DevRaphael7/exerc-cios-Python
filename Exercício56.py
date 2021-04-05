I, A, B, C = int(input('Digite 1, 2 ou 3: ')), float(input()), float(input()), float(input())

if I == 1:

    if A < B and B < C and A < C:
        print('Ordem crescente: {}, {}, {}'.format(A, B, C))
    elif A > B and B < C and A < C:
        print('Ordem crescente: {}, {}, {}'.format(B, A, C))
    elif A > B and B < C and A > C:
        print('Ordem crescente: {}, {}, {}'.format(B, C, A))
    elif A > B and B > C and C < A:
        print('Ordem crescente: {}, {}, {}'.format(C, B, A))
    elif A < B and B > C and A < C:
        print('Ordem crescente: {}, {}, {}'.format(A, C, B))
    elif A < B and B > C and A > C:
        print('Ordem crescente: {}, {}, {}'.format(C, A, B))

elif I == 2:

    if A < B and B < C and A < C:
        print('Ordem crescente: {}, {}, {}'.format(C, B, A))
    elif A > B and B < C and A < C:
        print('Ordem crescente: {}, {}, {}'.format(C, A, B))
    elif A > B and B < C and A > C:
        print('Ordem crescente: {}, {}, {}'.format(A, C, B))
    elif A > B and B > C and C < A:
        print('Ordem crescente: {}, {}, {}'.format(A, B, C))
    elif A < B and B > C and A < C:
        print('Ordem crescente: {}, {}, {}'.format(B, C, A))
    elif A < B and B > C and A > C:
        print('Ordem crescente: {}, {}, {}'.format(B, A, C))

elif I == 3:

    if A > B and A > C:
        print('{}, {}, {}'.format(B, A, C))
    elif B > A and B > C:
        print('{}, {}, {}'.format(A, B, C))
    elif C > A and C > B:
        print('{}, {}, {}'.format(A, C, B))

