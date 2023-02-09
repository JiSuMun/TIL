# 복잡도

- 알고리즘의 성능을 나타내는 척도

- 메모제이션(Memoization) 기법
    - 메모리를 더 많이 사용해서 시간을 비약적으로 줄이는 방법

- 시간 복잡도
    - 알고리즘을 위해 필요한 연산의 횟수
    - 빅오(Big-O) 표기법 사용
        - 가장 빠르게 증가하는 항만 고려
        - 항상 절대적인 것은 아니다.

- 공간 복잡도
    - 알고리즘을 위해 필요한 메모리의 양
    - 빅오(Big-O) 표기법 사용

## 측정

- 수행 시간 측정 소스코드
    ```python
    import time
    start_time = time.time() # 측정 시작

    # 프로그램 소스코드

    end_time = time.time() # 측정 종료
    print("run time: ", end_time - start_time) # 수행 시간 출력
    ```
    