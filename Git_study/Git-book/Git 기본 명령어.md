# Git 기본 명령어

## 자주 쓰이는 code

### Git 명령어

- `git init`: 새로운 Git 저장소 초기화
- `git add`: 변경된 파일을 스테이징 영역에 추가
- `git commit`: 스테이징 영역의 파일을 커밋
- `git push`: 로컬 커밋을 원격 저장소에 푸시
- `git pull`: 원격 저장소의 변경 사항을 가져와 병합
- `git clone`: 원격 저장소를 복제

## 시작 및 설정

### `git —version`

- 설치된 git 버전 확인

### `git init`

- `.git` 하위 디렉토리 생성

### `git config —global user.name"사용자이름"`

- 사용자 이름 설정

### `git config —global user.email"사용자 메일"`

- 사용자 이메일 설정

### `git status`

- 상태 확인

## 저장소

### `git remote add origin [github 저장소 주소]`

- 원격 저장소 연결

### `git remote -v`

- 저장소 확인

### `git clone/로컬/저장소/경로`

- 로컬 저장소 복제

### `git clone 이름@호스트:/원격/저장소/경로`

- 원격 저장소 복제

## commit 명령어

### `git add 파일명`

- 커밋에 변경사항 올림

### `git add .`

- 수정한 전체파일 올림

### `git commit -m “메세지”`

- 커밋 생성(변경사항 저장)

### `git log`

- 커밋 내역 확인

### `git status`

- 파일 상태 확인

## branch 명령어

### `git branch`

- 브랜치 목록 확인

### `git branch 브랜치명`

- 브랜치 생성

### `git checkout 브랜치명`

- 브랜치로 이동

### `git checkout -b 브랜치명`

- 브랜치만들고 이동

### `git checkout master`

- master 브랜치로 돌아옴

### `git branch -d 브랜치명`

- 브랜치 삭제

### `git log —coeline`

- 한 커밋씩 출력

### `git log —branches —graph`

- 커밋을 그래프로 표시

## push 명령어

### `git push origin master`

- 원격 저장소에 업로드

### `git push 저장소주소 브랜치이름`

- 커밋을 원격 저장소에 업로드

### `git push -u 저장소주소 브랜치이름`

- 커밋을 원격 저장소에 업로드

### `git remote add origin 저장소주소`

- 클라우드 주소 등록

### `git remote remove 저장소주소`

- 클라우드 주소 삭제

## merge 명령어

### `git pull`

- 원격 저장소 변경사항 가져오고 병합하기

### `git merge 다른브랜치이름`

- 현재 브랜치에 다른 브랜치 병합

### `git add 파일이름`

- 파일 병합

### `git diff 브랜치이름 다른브랜치이름`

- 병합 이전의 내용과 비교

## 로컬 명령어

### `git checkout —파일명`

- 변경 전으로 되돌림

### `git fetch origin`

- 현재 상태를 다운로드

- 
