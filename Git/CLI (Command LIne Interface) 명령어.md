명령어 인터페이스는 터미널을 통해 사용자와 컴퓨터가 상호 작용하는 방식

# 관리자 권한으로 실행

### `sudo`

(super user do)

1. 관리자만 읽을 수 있는 파일 읽기
2. 새로운 프로그램 설치
3. Notes 새로운 프로그램 설치 시 Package Manager 이용 보편적

# 기본적인 unix/linux 명령어

### `ls`

(list)

파일보기

### `al`

(all)

파일의 세부 내용 확인

<ls - al 상세 내용 (권한)>

1. 접근권한(읽기/쓰기/실행 가능) 여부
2. 링크된 파일 갯수
3. 소유자
4. 소유 그룹
5. 파일 크기
6. 만든 날짜
7. 만든 시간
8. 파일/디렉토리 이름

### `cd`

(change directory)

디렉토리로 이동

### `pwd`

(print working directory)

full 디렉토리 path 확인 (디렉토리 위치 변경)

# 디렉토리 이동

### `cd ~`

홈 디렉토리 (현재 사용자 개인 파일 디렉토리)

### `cd /`

루트 디렉토리 (시스템 최상위 디렉토리 확인)  
(중요한 디렉토리 의미 관리자 권한 요구함)

### `cd .`

현재 디렉토리

### `cd ..`

부모 디렉토리

### `pwd`

현재 full 디렉토리 확인

### `clear`

터미널 입력 내용 지움

# 자주쓰는 명령어

### `touch [file_name]`

빈 파일 생성 / (not 디렉토리 literally 파일 생성)

### `mkdir [dir_name]`

(make directory)

디렉토리 생성

### `cat [file_name]`

(concatenate)

텍스트 형태의 파일 확인

### `mv [file_name or dic name]
[target_dir_name]`

(move)

파일 또는 디렉토리 옮기기

### `mv [file_name or dic name]`

(move)

파일 및 디렉토리 이름 바꾸기

### `cp [file] 
[target_dir_name]`

(copy)

복사

### `cp -r [folder_name]`

복사

# 즉시 삭제 (휴지통 안거침)

### `rm [file_name]`

(remove)

파일 삭제

### `re -r [dir_name]`

폴더 삭제

# 파일 소유권 변경

### `chown [owner_file]: [group_file]`

(change owner)

파일 소유권 변경

### `mkdir`

디렉토리 생성

### `rm`

삭제

# GUI 프로그램 실행

### `explorer .`

현재 폴더 windows 파일 관리자에게 보기

### `open .`

현재 폴더 macOS finder에서 보기

### `code .`

현재 폴더 VS Code 에디터로 열기
