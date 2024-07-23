# 새 저장소 생성

### git init

.git 하위 디렉토리 생성   
(폴더 만든 후, 그 안에 명령 실행 → 새로운 git 저장소 생성)

# 저장소 복제/다운로드(clone)

### git clone<링크>

기존 소스 코드 다운로드/복제

### git clone /로컬/저장소/경로

로컬 저장소 복제

### git clone 사용자명@호스트:/원격/저장소/경로

원격 서버 저장소 복제

# commit

### git add <파일명> 
git add *

커밋에 단일 파일의 변경 사항 포함 (인덱스에 추가된 상태)

### git add -A

커밋 파일의 변경 사항 한번에 모두 포함

### git commit -m “커밋 메시지”

커밋 생성

### git status

파일 상태 확인

# branch 작업

### git branch

브랜치 목록

### git branch <브랜치이름>

새 브랜치 생성(local에서 만듬)

### git checkjout -b <브랜치이름>

브랜치 생성 & 이동

### git checkout master

master branch 되돌아 옴

### git branch -d <브랜치이름>

브랜치 삭제

### git push origin <브랜치이름>

만든 브랜치 원격 서버 전송

### git push -u <remote> <브랜치이름>

새 브랜치 원격 저장소로 push

### git pull <remote> <브랜치이름>

원격 저장된 git 프로젝트 현재 상태 다운받고 + 현재 위치 브랜치 병합

# push 변경 사항 발생

### git push origin master

변경사항 원격 서버 업로드

### git push <remote> <브랜치이름>

커밋 원격 서버 업로드

### git push -u <remote> <브랜치이름>

커밋 원격 서버 업로드

### git remote add origin <등록된 원격 서버 주소>

클라우드 주소 등록 및 발행   
(git 새로운 원격 서버 주소 알림)

### git remote remove <등록된 클라우드 주소>

클라우드 주소 삭제

# merge 갱신 및 병합

### git pull

원격 저장소 변경 내용 현재 디렉토리 가져오기(fetch) 병합(merge)

### git merge <다른 브랜치이름>

현재 브랜치에 다른 브랜치의 수정사항 병합

### git add <파일명>

파일 병합

### git dff <브랜치이름> <다른 브랜치이름>

변경 내용 merge 전 바뀐 내용 비교

# tag 작업

### git log

현재 위치 브랜치 커밋 내용 확인 및 식별자 부여

# 로컬 변경사항 return 작업

### git checkout —<파일명>

로컬 변경 사항 변경 전으로 되돌림

### git fetch origin

원격 저장된 git 프로젝트 현 상태 다운로드
