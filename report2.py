# 20250975 지용건
A = [1, 2, 3, 4, 5]
N = 5


# 조건 1. 관계행렬 입력
# 추가 기능 1. 입력 오류 및 예외 처리
def input_matrix():
    R = []

    print("\n5 x 5 관계행렬을 입력하세요.")
    print("각 원소는 0 또는 1이며 공백으로 구분합니다.")

    for i in range(N):
        while True:
            try:
                row = list(map(int, input(f"{i+1}행 입력: ").split()))

                if len(row) != N:
                    print("입력 오류: 원소를 5개 입력하세요.")
                    continue

                if any(x not in [0, 1] for x in row):
                    print("입력 오류: 0 또는 1만 입력하세요.")
                    continue

                R.append(row)
                break

            except ValueError:
                print("입력 오류: 숫자만 입력하세요.")

    return R


# 조건 1. 관계행렬 출력
def print_matrix(R):
    for row in R:
        print(" ".join(map(str, row)))


# 조건 2. 반사성 판별
def is_reflexive(R):
    for i in range(N):
        if R[i][i] != 1:
            return False

    return True


# 조건 2. 대칭성 판별
def is_symmetric(R):
    for i in range(N):
        for j in range(N):
            if R[i][j] != R[j][i]:
                return False

    return True


# 조건 2. 추이성 판별
def is_transitive(R):
    for i in range(N):
        for j in range(N):
            for k in range(N):
                if R[i][j] == 1 and R[j][k] == 1:
                    if R[i][k] == 0:
                        return False

    return True


# 조건 2. 동치 관계 판별
def is_equivalence(R):
    reflexive = is_reflexive(R)
    symmetric = is_symmetric(R)
    transitive = is_transitive(R)

    print("\n[관계 판별 결과]")
    print("반사성:", "만족" if reflexive else "불만족")
    print("대칭성:", "만족" if symmetric else "불만족")
    print("추이성:", "만족" if transitive else "불만족")

    result = reflexive and symmetric and transitive

    print("동치 관계:", "만족" if result else "불만족")

    return result


# 조건 3. 각 원소의 동치류 계산
def equivalence_class(R, i):
    group = []

    for j in range(N):
        if R[i][j] == 1:
            group.append(A[j])

    return group


# 조건 3. 동치류 출력
def print_classes(R):
    print("\n[각 원소의 동치류]")

    for i in range(N):
        group = equivalence_class(R, i)
        result = ", ".join(map(str, group))

        print(f"[{A[i]}] = " + "{" + result + "}")


# 조건 4. 반사 폐포
def reflexive_closure(R):
    C = [row[:] for row in R]

    for i in range(N):
        C[i][i] = 1

    return C


# 조건 4. 대칭 폐포
def symmetric_closure(R):
    C = [row[:] for row in R]

    for i in range(N):
        for j in range(N):
            if C[i][j] == 1:
                C[j][i] = 1

    return C


# 조건 4. 추이 폐포 (Warshall 알고리즘)
def transitive_closure(R):
    C = [row[:] for row in R]

    for k in range(N):
        for i in range(N):
            for j in range(N):
                if C[i][k] == 1 and C[k][j] == 1:
                    C[i][j] = 1

    return C


# 조건 4. 폐포 변환 전후 출력
def show_closure(name, before, after):
    print(f"\n[{name} 변환 전]")
    print_matrix(before)

    print(f"\n[{name} 변환 후]")
    print_matrix(after)


# 추가 기능 2. 관계 불만족 원인 분석
def print_errors(R):
    print("\n[관계 불만족 원인]")

    for i in range(N):
        if R[i][i] == 0:
            print(f"반사: ({A[i]}, {A[i]}) 관계가 없습니다.")

    for i in range(N):
        for j in range(i+1, N):
            if R[i][j] != R[j][i]:
                print(f"대칭: ({A[i]}, {A[j]})와 "
                      f"({A[j]}, {A[i]})가 다릅니다.")

    for i in range(N):
        for j in range(N):
            for k in range(N):
                if R[i][j] == 1 and R[j][k] == 1 and R[i][k] == 0:
                    print(f"추이: ({A[i]}, {A[j]}), "
                          f"({A[j]}, {A[k]})는 존재하지만 "
                          f"({A[i]}, {A[k]})는 없습니다.")


# 추가 기능 3. 집합의 분할 및 중복 동치류 제거
def print_partition(R):
    groups = []

    for i in range(N):
        group = []

        for j in range(N):
            if R[i][j] == 1:
                group.append(A[j])

        if group not in groups:
            groups.append(group)

    result = []

    for group in groups:
        result.append("{" + ", ".join(map(str, group)) + "}")

    print("\n[집합의 분할]")
    print("{" + ", ".join(result) + "}")
    print("분할된 부분집합의 개수:", len(groups))


# 메인 프로그램
def main():
    print("=" * 45)
    print("이산수학 Report 2")
    print("동치 관계 판별 및 폐포 변환 프로그램")
    print("집합 A = {1, 2, 3, 4, 5}")
    print("=" * 45)

    # 추가 기능 4. 프로그램 반복 실행
    while True:

        # 조건 1. 관계행렬 입력 및 출력
        R = input_matrix()

        print("\n[입력된 관계행렬]")
        print_matrix(R)

        # 조건 2. 동치 관계 판별
        if is_equivalence(R):

            # 조건 3. 동치류 출력
            print_classes(R)

            # 추가 기능 3. 집합의 분할
            print_partition(R)

        else:

            # 추가 기능 2. 불만족 원인 분석
            print_errors(R)

            print("\n[폐포 변환 시작]")

            # 조건 4. 반사 폐포
            R1 = reflexive_closure(R)
            show_closure("반사 폐포", R, R1)

            # 조건 4. 대칭 폐포
            R2 = symmetric_closure(R1)
            show_closure("대칭 폐포", R1, R2)

            # 조건 4. 추이 폐포
            R3 = transitive_closure(R2)
            show_closure("추이 폐포", R2, R3)

            print("\n[최종 관계행렬]")
            print_matrix(R3)

            print("\n[폐포 변환 후 관계 판별]")

            if is_equivalence(R3):
                print_classes(R3)
                print_partition(R3)

        # 추가 기능 4. 반복 실행 및 종료
        while True:
            again = input("\n다시 실행하시겠습니까? (y/n): ")
            again = again.strip().lower()

            if again in ["y", "n"]:
                break

            print("입력 오류: y 또는 n을 입력하세요.")

        if again == "n":
            print("프로그램을 종료합니다.")
            break


if __name__ == "__main__":
    main()
