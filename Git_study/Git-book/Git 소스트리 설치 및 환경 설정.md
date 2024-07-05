# 첫 번째 Git 실행

Git 기본 사용 환경 터미널

## 터미널

터미널 환경.  
예전 MS-DOS 또는 셸(shell)처럼 텍스트 명령어 입력, 실행 환경을 의미.  
터미널 이용 Git 작업 다양함. GUI 많이 사용하는 기능 위주로 동작 구현했기 때문에 터미널 정밀한 작업은 하기 어려움.

## Git 명령어 실행

Git 프로그램 이름은 Git.  
터미널에서 Git 명령어 입력하면 Git 동작 → Git 이름만 입력하면 실행.

git 명령어 사용법 간단히 요약

```
$gitusage: git [--version] [--help] [-C <path>] [-c <name>=<value>]           [--exec-path[=<path>]] [--html-path] [--man-path] [--info-path]           [-p | --paginate | -P | --no-pager] [--no-replace-objects] [--bare]           [--git-dir=<path>] [--work-tree=<path>] [--namespace=<name>]           <command> [<args>]
These are common Git commands used in various situations:
start a working area (see also: git help tutorial)   clone              Clone a repository into a new directory   init               Create an empty Git repository or reinitialize an existing one
```

**환경 변수 경로 설정**

git 명령어 입력 제대로 실행되지 않음.  
윈도우 호나경 변수 경로(PATH)를 추가. 기본적으로 모든 디렉터리 경로 Git 실행 환경 변수 경로 설정.

윈도 제어판 실행 후 시스템→ 고급 시스템 설정 선택, 시스템 속성 창 열기 고급 → 환경 변수


시스템 변수 항목 Path 더블 클릭

환경 변수 편집 창에 C:\Program Files\Git\cmd 경로를 추가


Git 명령어 하나로만 동작 방법과 옵션 같이 사용하여 동작하는 명령어로 나뉨.  
기본적 Git 독립된 명령어로 구성. but. 독립적인 명령어들 외 하위 명령어 같이 이용 동작 기능을 세분화. → Git 명령어 옵션 지정하면 됨.

**$ git 명렁어 또는 옵션**

하위 명령어 외 추가 옵션도 같이 지정. 일부 옵션 생략.  
옵션은 짧은(-)과 긴 옵션(—)구분.  
help 옵션 입력 전체 명령어 확인.

`$ **git help --all**`

Git 배시 실행하여 간단한 실습.  
`git —version` 입력.

`$ **git --version**`

Git 버전 정보 확인.  
`Git —version` 명령어 사용 시 버전 확인 외에 Git이 정상적으로 동작하는지 확인 가능.

Git 명령어 명령어를 여러 개 묶어서 사용. 명령어 묶어 입력할 때는 세미콜론(;) 구분.  
ex. 태그 명령어와 브랜치 명령어 같이 묶어 실행.

`$ **git tag; git branch` (**세미콜론 구분**)**

```
0.0.10.0.2  footer* master
```

# 환경 설정

## config 명령어

Git 환경 설정 위해 별도 `config` 명령어 제공.  
`config` 명령어 환경 설정 파일 직접 수정X, 환경 설정을 쉽게 할 수 있도록 도움

`$ git config 설정값`

`config` 명령어 실행하면 새로운 `config` 파일 생성.  
→ 이전 설정한 환경 파일있음 기존 파일 수정.

`config` 명령어 옵션 사용,  `-help` 명령어 확인 가능.

`$ git config -help`

삭제하는 명령어. `—unset` 옵션 사용

`$ git config —unset 이메일 주소`

## 로컬 사용자

Git  여러 사람과 함께 개발할 수 있는 협업 도구.  
프로젝트 하나를 다수의 개발자와 함께 작업할 때 대비하여 각 개발자를 구분.  
→ Git은 각 개발자의 작업을 구분. 사용자를 등록하는 과정 거친다.  
로컬 저장소에서 사용자 등록은 별도의 웹 사이트에서 회원가입 X, 소스 코드의 변경 내용을 기록할 때 구분할 수 있는 사용자 설정값만 등록.  

→ 최초 Git 사용 or commit 할 때

사용자 등록은 두가지로 구분

**로컬(local)** 저장소에만 적용되는 로컬 사용자 설정 값과 모든 로컬 저장소에 공통으로 적용되는 글로벌 사용자 설정 값.  
Git 사용자를 구분할 때 ‘사용자 이름’과 ‘이메일 주소’ 사용, `config` 명령어 환경 설정 파일 등록

로컬 저장소 사용자 등록  
→ 사용자 이름과 이메일 주소는 한글로 입력하면 오류 발생 → 영문 작성.  
이메일 주소는 주로 사용하는 이메일 주소 입력.

`$ git 저장소 폴더` (깃저장소 폴더)

`$ git config user.name` ‘사용자 이름’

`$ git config user.email` ‘이메일 주소’

Git  사용자 구분하는데 쓰는 ‘사용자 이름’, ‘이메일 주소’ 중 이메일 주소는 Git 갭라자를 구별하는 고유 Key 사용.  
→ 자신의 저장소 외부로 공개 등록 이메일 주소도 외부에 공개, 공개해도 무관한 이메일 주소 사용 권장.

## 글로벌 사용자

로컬 사용자 등록은 로컬 저장소를 생성할 때 설정. 저장소마다 다르게 설정.  
but. 저장소를 생성할 때 사용자 등록을 하는 것은 불편

혼자 사용하는 컴퓨터면 글로벌(공통된) 사용자 등록하는 것이편리.  
글로벌 사용자 등록을 할 때는 `—global` 옵션과 함께 사용.  
설정된 모든 값은 글로벌(global)(전역) 영역 설정.

`$ git config —global user.name` “사용자 이름”

`$ git config —global user.email` “이메일 주소”

자동으로 글로벌 사용자 등록 적용하려면 생성된 저장소에 별도로 로컬 사용자 등록을 하지않아야한다.

## 환경 설정 파일 확인 및 직접 수정

`config` 명령어 사용하여 간단히 사용자 등록.  
`config` 명령어로 만든 환경 설정 파일은 Git 저장소 안에 `.git/config` 파일 형태로 저장.  
→ 환경 설정 파일을 찾아 `config` 명령어 등록

로컬 저장소 생성 → 해당 저장소 이동 (로컬) 사용자 등록 후 설정 파일 찾음

**ex.**

---

`$ mkdir gitstudy02`

gitstudy02 폴더 만들기

`$ cd gitstudy02` 

만든 gitsutdy02 폴더 이동

`infoh@hojin1 MINGW64 /e/gitstudy02`

`$ git init` 

git  초기화

`Initialized empty Git repository in E:/gitstudy02/.git`

`infoh@hojin1 MINGW64 /e/gitstudy02 (master)`

`$ git config user.name “hea97”`

`$ git config user.email “s24054@gsm.hs.kr”`

`infoh@hojin1 MINGW64 /e/gitstudy02 (master)`

`$ Is .git`

Git 목록 보기

`config description FETCH_HEAD hooks info objects refs`

해당 위치 이동 간단히 다음 명령어 실행 환경 설정 파일 여부 

`$ Is .git`

.git/config 파일 로컬 저장소 직접 로컬 사용자 등록할 때만 찾음.  
글로벌 사용자 등록 저장소 .git/config 파일 존재X   
대신, 개인 계정 루트에 파일 생성 후 다음 명령어 실행

`$ Is ~/.gitconfig`

.gitconfig 폴더 경로 보기

글로벌 환경 설정 파일과 로컬 설정 파일이 모두 있을 때도 있음.  
→ 로컬 환경 설정 파일 내용을 우선.

**ex.**

---

$ cat .git/config

[core]

`repositoryformatversion = 0`

`filemode = false`

`bare = false`

`logallrefupdates = true`

`symlinks = false`

`ignorecase = true`

[user]

`name = hea97`

`email = s24054@gsm.hs.kr`

---

환경 설정 파일을 직접 열어 수정 시 다음 명령어 실행 VScode 편집기 활용

`$ code .git/config`

환경 설정 파일을 직접 수정하면 절차 오류 등 여러 가지 이유 때문에 정상적으로 동작하지 않을 수도.  
→ `config` 명령어 사용 권장

### 깃 상태 컬러로 보기

Git 전용 터미널(배시) 다음 옵션 설정 Git 상태를 컬러로 볼 수 있음

`$ git config —global color.ui.auto`

## VScdoe

VScode 터미널 명령어로 실행

`$ code 파일이름`

## 정리

Git 기본적 설치 방법과 환경 설정.
