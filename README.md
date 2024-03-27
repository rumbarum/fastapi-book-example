# 소개
한빛미디어 출판 도서, 「처음 시작하는 FastAPI」 샘플 코드 입니다.

# 동작 안내
- 챕터별로 코드가 있는 branch 가 구성되어 있습니다. 
  - ch-03 ~ ch-18 까지 챕터별로 branch 가 구성되어 있습니다.
- 챕터별로 branch 를 변경하여, 해당 챕터의 코드를 확인할 수 있습니다.


- 리포지토리 clone
    ```shell
    git clone https://github.com/rumbarum/fastapi-book-example.git
    cd fastapi-book-example
    ```

- 전체 branch 목록 보기
    ```shell
    git branch -a
    ```

- branch 변경
    ```shell
    #(git version 2.23 이상일 경우)
    $ git switch ch-03
    
    #(git version 2.23 미만일 경우)
    $ git checkout ch-03 
    ```

# 환경 안내
- 버전 
  - python 3.10 기준으로 작성 되었습니다.
  - 라이브러리들도 가능한 최신 버전으로 작성되었습니다. 버전별 동작이 상이 할 수 있습니다.
  - Pydantic의 경우 1.x 버전과 2.x 버전의 차이가 있습니다. (2.x 버전을 사용하였습니다.)

- 의존성 설치 
    - pip 사용
    ```shell
    pip install -r requirements.txt
    ```
    - poetry 사용
    ```shell
    poetry install
    ```
