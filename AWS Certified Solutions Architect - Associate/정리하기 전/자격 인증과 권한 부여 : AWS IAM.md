# 개요

AWS 리소스는 비즈니스 위해 소중한 자원이므로 안전하게 보호해야한다.  
너무 엄격하게 접근을 제한할 경우 어드민 또는 고객 접근해야 하는 리소스 접근하지 못하는 문제 발생

안정성과 접근성 균형 맞추는 일은 쉽지 않음. 접근 필요한 사용자 등록하거나 특정인 접근 권한 허용 또는 불허하는 시스템 갖추기 위해서는 많은 노력 필요. 하지만 AWS 사용자 Identity and Access Management(IAM) 통해 리소스 관리 필요한 신분확인 및 권한부여 업무 처리

6장에서는 스스로 신분 증빙(principals) 부르는 IAM 대해 함께 살펴봄. AWS 리소스 접근하기 위한 신분 유저 또는 롤로 나태날 수 있음, 그 중 롤은 서비스, 다른 유저, 그룹에 할당 할 수 있는 임시 신분

AWS에서 Kerberos, Microsoft Active Directory 또는 Lightweight Directory Access Protocol(LDAP) 등 다양한 외부 신분 확인 및 권한 부여 서비스 연계한 연합 신분 체계(federated identities) 이용 유저 또는 애플리케이션 접근권한 증명할 수 있다.

AWS 사용자의 ID, 즉 신분 간단하게 정의한 정책(policles) 부착하는 방식 특정 리소스 상호작용. → 정책 신분 단위로 부착(ID 기반 정책)하거나 리소스 단위 부착(리소스 기반 정책) 사용

6장 중심 내용

- 계정 내에 ID 기반 접근성 긴밀히 제어하는 정책 생성
- 다양한 유형의 키와 토큰 이용 자신 신분 증명
- AWS 외부 연합 신분 서비스 이용 IAM 연계 가능한 통합 로그인(single sign-on) 솔루션 제공
- 리소스 안전한 관리 위한 계정 및 롤 환경설정 베스트 프랙티스 파악

# IAM 기반의 신분 관리

AWS 계정 생성 루트 유저(root user) 신분 만들어짐. 루트 유저 계정 내에 모든 서비스와 리소스 접근할 수 있는 권한 지니고 있음, 다른 신분으로는 결코 할 수 없는 작업 오직 루트 유저 권한으로만 할 수 있음. 바로 이런 이유로 막강한 권한 지닌 루트 유저 ID 패스트워드가 해킹 공격 목표가 되기도 함.  
해커는 루트 유저 ID, 패스워드 또는 액세스 키만 지니면 AS 계정 내에 무슨일이든 할 수 있음

루트 유저 관련된 다양한 위험 노출 가능성 피하기 위해 AWS 루트 유저 계정 엄격히 보호, 대신 다른 계정 생성 일상적인 업무 사용할 것을 권장.  
IAM 홈페이지에서 제공되는 보안 상태(Security Status) 색션, 루트 유저 접근 가능성에 대한 경고 제공

권장 사항 따르기 위한 방법과 그 이유 이해하는 것이야말로 AWS 계정 안전하게 보호하는 가장 중요한 첫 걸음

## IAM 정책

IAM 첫 번쨰 중요 요소 AIM 신분관리 정책(policies) 어떻게 사용되는지 알아보기.  
IAM 정책 하나 이상의 AWS 리소스 관련된 일련 허용 동작 및 불허 동작 정리한 문서 할 수 있음. 정책 문서에 의해 특정 사용자는 해당 리소스에 접근해서 원하는 작업 수행.    
정책에서는 효과(effect)라는 속성으로 허용 또는 불허 나타냄. 이를 위해 각각 Allow 또는 Deny라는 속성 값 사용

예를 들어, 특정 사용자 S3라는 리소스(resource)에서 버킷 생성이라는 액션(action) 허용하는 효과(effect)  추가. 해당 리소스 이용하는 다양한 액션 방식 지정

사용자 IAM Dashboard 통해 수백 여 개의 사전 정의된 정책 확인, 키워드 이용해 자신의 목적 맞는 정책 찾아 활용. Dashboard의 정책 생성(Create policy) 페이지 정책 생성 JSON 포맷 텍스트 직접 정책 작성

IAM Dashboard 인터페이스 제공하는 JSON 포맷 Administrator Access 정책 문서.  
계정에서 모든 리소스(*) 대해 모든 액션(*) 할 수 있는 정책 정의 돼 있음을 알 수 있다

```markdown
{
"Version": "2012-10-17",
"Statement": [
	{
	"Effect": "Allow",
	"Action": "*"
	"Resource": "*"
	}
]
}
```

정책 문서 의해 명시적 정의되지 않은 모든 동작 불허. 기본적으로 모든 동작 불허됨. Deny라는 속성 명시적 사용할 필요 없음.  
Deny 속성은 모든 리소스가 아닌 대부분 리소스 접근하는 정책 작성할 때 특히 유용.  
ex. 기본적으로 접근 제약 없는 리소스 하지 말아야 할 단 하나의 액션 정의할 때 Deny 사용

IAM 이용 리소스 정책 연계, 해당 신분은 정책 권한 및 제약 조건에 영향 받게 됨.  
하나의 IAM 정책 다수 신분 연계할 수 있음, 하나의 신분에는 최대 10개의 정책(6,144자 미만 정책 문서) 연계할 수 있음.

만일 하나의 신분 연결된 두 개의 정책 서로 상반된 내용 담고 있으면 어떻게 될까?  
ex. 하나의 정책 S3 버킷 생성 허용, 다른 정책 S3 버킷 생성 불허하는 경우 어떻게 될까? AWS 이외 같은 상충이 발생하는 경우, ‘불허’ 기준 따르도록 함

이 외에도, 특정 리소스 액션 대해 명시적인 불허 정의된 경우 다른 곳 허용 했더라도 결과적으론 불허 적용

## 유저 루트 계정

루트 계정 보호 위한 최선 방법 보인하는 것, 다음 절차

- 루트 계정과 연계된 모든 액세스 키 삭제
- 길고 복잡한 패스워드 작성해 안전한 패스워드 볼트 저장
- 루트 계정 다중 인증(MFA, Multi-Factor Authentication) 기능 활성화
- 일상적인 어드민 작얿에서 루트 계정 사용 자제

루트 계정 봉인, 어드민 작업 위해 새 계정 생성하고 어드민 적합한 권한 부여.  
보통의 경우 AdministratorAccess 정책 적용, 다른 유저, 그룹, 롤 생성하고 업무 수행 필요한 권한 부여

참고 | 루트 계정을 봉인하면서 그에 준하는 AdministratorAccess 권한 계정 생성하는 데는 어떤 실익?  
즉, 루트 계정, 어드민 권한 계정이든, 리소스 대한 모든 접근 권한 가졌다는 사실은 동일하지 않은가?  
사실 루트 계정과 모든 권한 부여받은 어드민 계정에는 매우 큰 차이점 존재함. 특히 전계정에 대한 예산 관리 권한 특정 S3 버킷 대한 MFA Delete 권한 오직 루트 계정만 지님

새 IAM 유저 생성할 때 패스워드 정책 적용 옵션 제시, 사용자는 최소 길이 및 복잡성 제약 조건과 패스워드 재설정 최대 주기 적용. 이 때 어드민 가급적 팀원이 좀 더 높은 수준 패스워드 사용 해 보안 수준 높일 수 있다

사용자는 콘솔 사용자 이름 아래 필침목록 메뉴의 My Security Credentials 페이지 보안 설정 내역 변경

My Security Credentials 페이지 여섯 개 아이템

- 패스워드 업데이트
- MFA 활성화 및 관리
- AWS CLI 또는 프로그래밍 SDK 통해 AWS 리소스 관리하기 위한 액세스 키 생성 및 삭제
- Amazon CloudFront 배포 위한 서명 URL 인증용 키페어 생성
- Amazon 서비스 대한 SOAP(Simple Object Access Protocol) 요청 위한 X.509 인증서 생성

참고 | S3와 Amazon Mechanical Turk 대한 SOAP 요청 위 규칙 예외. → 서비스가 X.509 인증서 대신 보통 액세스 키 사용하기 때문

- 기존 S3 ACL 사용하기 위해 12자리 AWS Account ID와 대포 유저 ID 인출

위 아이템 모두가 생성하는 모든 유저와 관련되지는 않음.

## IAM 액세스 키 관리

액세스 키 프로그래밍 기법 또는 CLI 기반 접근 시 권한 인증 기능 제공. 기존 유저네임 및 패스워드 방식 사용 X, 로컬 환경에서 액세스 키 ID와 시크릿 액세스 키 이용해 특정 리소스 대한 접근 권한 부여받을 수 있는 것. 애플리케이션 또는 실행 명령 액세스 키 정보 이용해 요청 필요한 데이터 제공

## 미사용 키 비활성화하기

활성화된 키 언제든 해킹 등에 악용 될 수 있음, 생성한 유저 해당 키 이용해 어떤 작업을 하는지 확인할 필요 있음. 일정 기간 사용되지 않은 키 발견하면 비활성화시키고, 조만간 사용할 계획 없다면 삭제하는 것이 좋다.

## 키 로테이션

오래된 액세스 키 정기적으로 삭제하는 것이 좋음 오래 사용한 키일수록 위험에 노출됐을 가능성 더 큼. ex. 30일간 같이 키 사용 기한 정해두는 것이 좋고, 이 기한 넘은 키는 삭제하거나 다른 키로 교체해야함

EC2 리소스 다른 AWS 서비스 접근할 때 IAM 롤을 위해 자동으로 키를 로테이션할 수 있지만, 특정 애플리케이션에만 사용되는 키가 있는 경우 키 자동 로테이션 기능 사용하는 일 좀 더 복잡해짐. 하지만 이를 위한 좋은 키 로테이션 방법 존재

1. 각 유저별 새 액세스 키 생성. 유저 스스로 자신 키 관리하도록 해도 됨
2. 애플리케이션 키 정보 새 키에 맞춰 업데이트
3. 오랜된 키는 비활성화 또는 삭제
4. 키 업데이트 후 애플리케이션 실행에 문제가 없는지 며칠간 관찰. 아래CLI 명령으로 애플리케이션 중 구형 키 사용하는지 여부 확인
    
    aws iam get-access-key-last-used —access-key-id ABCDEFGHIJKLMNOP
    
5. 모든 일 순조롭다면 구형 키 삭제

액세스 키 로테이션과 함께 IAM 계정 패스워드 정책 로테이션 추가해 키와 관련된 보안 수준 더욱 높일 수 있음

## IAM 그룹

개별 유저 생성할 떄는 AWS 작업 안전하고 효율적 수행할 수 있는 만큼만 접근권한 부여.   
계정 관리 복잡해지고 바빠질수록 개별 유저 일일이 관리하는 것은 불가능

ex. 여섯 명에게만 어드민 권한 부여, 또 다른 여섯 명에게 개발자 권한 부여한 경우.  
일일이 적절한 작업 권한 부여하려면 꽤 많은 시간 소요. 따라서 개별 사용자가 아닌, 팀 단위 권한 부여하는 방법 대해 생각해 보자. 팀 단위 접근권한 부여하면 변경 사항 생겼을 때도 일관적 적용할 수 잇어 편리

이러한 필요 충족시키기 위한 것이 바로 IAM 그룹 → 개별 유저가 아닌, 업무 영역별, 조직 업무 내용별 권한 부여 가능. 위와 같은 경우 개발 그룹, 어드민 그룹, 디자인 그룹 생성해 체계적 구너한과 작업 내역 관리

특정 그룹 대한 액세스 프로필 변경해야 하는 경우 개별 유저 단위 아닌 관련 그룹 단위로 변경 작업 수행.  
ex. 개발자 그룹 Elastic Beanstalk 워크로드 추가해야 하는 경우 한 번의 조작 개발팀원 전체 관련 권한 부여 할 수 있음.  
또한 디자인 부서에서 더 이상 Amazon Elastic Transcoder 이용 비디오 콘텐츠 변환 작업 수행하지 않는 경우 디자인 그룹 해당 권한 삭제

## IAM 롤

IAM 롤 유저 또는 서비스 리소스 대한 접근 요청 할 때 이용할 수 있는 임시 신분, 롤을 이용 서비스와 관련된 다양한 논리 문제 해결. ex. IAM 유저 가운데 주기적으로  EC2 인스턴스 종류, 업데이트 작업 후 재시작하는 경우 있을 수 있음. 이 때 우발적인 인스턴스 종료 막으려면, 애당초 해당 유저 EC2 인스턴스 종료할 수 있는 권한 주지 않는 것이 좋음.  
이와 같은 기능 프로그래밍 업게에서 Linux 또는 macOS는 sudo 작업 방식, Windows에서는 runas 명령 구현해 특정 리소스 대한 가능 작업 내역 세분화해서 관리

다른 예로 Elastic Container Service(ECS) 서비스 통해 다른 리소스 연계된 AWS 서비스 시작하는 경우 ECS 사용하려면 먼저 컨테이너 이미지 가져올 수 있는 Elastic Container Registry(ECR) 대한 접근 권한 갖고 있어야 한다. 즉, ECS 사용 위해 ECR에서 데이터 가져올 수 있는 롤을 지니고 있어야함.  
즉 ECS 사용 위해 ECR 데이터 가져올 수 있는 롤을 지니고 있어야 함. 이러한 작업 딱 들어맞는 AmazonECSTask ExecutionRolePolicy 관리형 롤이 미리 정의돼 있다.

때론, 다른 AWS 계정 또는 연합 자격인증 서비스 이용 로그인한 사용자가 정의한 IAM 롤 사용해야 할 때도 있음, (12시간 뒤 자격 인증 만료되도록 설정된) IAM 롤은 바로 이러한 상황 선택할 수 있는 최선 방법

롤은 접근 필요한 리소스 신뢰 개체(trusted entity) 정의하는 방식 생성할 수 있음, 신뢰 개체에는 AWS 서비스, AWS 계정, Amazon, Amazon Cognito, facebook 또는 Google 로그인 접근권한 증명한 웹 식별 객체, SAML(Security Assertion Markup Language) 2.0 연합 자격인증 객체 등 4가지 있음.

신뢰 개체 정의 후 사용자는 정책 문서 생성 및 부착 또는 사전정의된 IAM 정책 할당하는 방식으로 퍼미션 부여할 수 있음. 신뢰 개체에 새 롤이 포함돼 있는 경우 AWS는 AWS Security Token service(STS) 이용해 만료 기한 정해진 보안 토큰 발행

# 접근권한 관리 도구

AWS 사용자 및 리소스 관리 필요한 다양한 도구 제공, 앞서 살펴본 IAM 그 중 작은 일부라고 할 수 있음. 사용자 접근권한 관리 위한 주요 도구 Amazon Cognito, AWs Managed Microsoft AD, AWS Single Sign-On, 키 암호화 및 보안 자격증명 도구로는 AWS Key Management Service(KMS), AWS Secrets Manager, AWS CloudHSM 등 있음

## Amazon Cognito

Cognito 모바일 앱 및 웹 앱 개발자 위한 회원가입 및 로그인 기능 제공

- Congito 유저 풀(user pool)  
애플리케이션 회원가입 및 로그인 기능 추가
- Congito 아이덴티티 풀(identity pool)  
애플리케이션 사용자에게 계정에는 다른 서비스에 대한 임시 접근권한 부여할 수 있다

유저 풀 생성 시 유저 어떤 방식으로 (주소 또는 생년월일 속성 사용) 회원으로 가입, 어떤 방식으로 (유저 네임 또는 이메일 주소 속성 사용) 로그인하도록 할 것인지 정의.  
패스워드 복잡성 대한 최소 요구사항, MFA, 이메일 인증 등 대한 내용 설정

아이덴티티 풀 생성 시(Cognito, AWS 계정, 연합 인증, 기타 미인증 ID 등) 유저 유입 경로 정의.  
풀에 IAM 롤 방식 사용. 풀이 활성화된 뒤 미리 정의해둔 신분 조건 일치하는 유저 나타나면 해당 롤을 이요해 리소스 접근

## AWS Managed Microsoft AD

Managed Microsoft AD는 AWS Directory Service 통한 AD 접근, 즉 액티브 디렉토리 접근 서비스, Amazon Cloud Directory와 Cognito 등 다른 디렉토리 관리 서비스와 유사한 기능 제공.  
Cloud Directory는 기업 사용자 및 HW 자산 목록과 같은 계층적 data 저장, 관리하는 서비스, 이와 같은 디렉토리 서비스 대량의 data 처리 능력 갖춤. AWS 각종 작업 통해 실행할 수 있다는 공통점

관리형 Microsoft AD는 Microsoft Active Directory를 위한 AWS Directory Service라고 함.  
이 서비스의 목적은 AWS VPC 포함된 리소스 Active Directory 통해 Microsoft SharePoint, .NET, SQL 서벗 기반 워크로드와 같은 방식 관리.  
AD Connector를 이용 AWS 서비스와 온프레미스 Microsoft Active Directory 바로 연결

Managed Microsoft AD 도메인 컨트롤러 두 개의 VPC AZ에서 실행, 관리형 서비스인만큼 Microsoft AD 사용하기 위한 data 복제 및 SW 업데이트 중 인프라 관리 업무 자동 수행

## AWS Single Sign-On

AWS Single Sign-On(SSO) 기존 AWS Directory Service 관리 Microsoft Active Directory 신분 확인 및 권한부여 작업 일관되게 수행, AWS Organizations 포함된 다수 AWS 계정 사용

SSO는 Salesforce, Box, Office 365 등 인기있는 애플리케이션 물론 SAML 2.0 지원하는 커스텀 앱에서도 사용할 수 있음

AWS Orgnaizations는 다수 AWS 계정 정책 기반 제어하는 관리 서비스, 하나 이상의 AWS 계정의 보유한 기업 AWS Orgnaizations 이용 자산 분산 방식에 상관 없이 기업 자산 통합적 관리

## AWS Key Mangagement Service

AWS KMS는 AWS 서비스 이용하기 위한 암호화 키 생성 및 관리 서비스. 

KMS 시스템 전반 걸쳐 사용할 수 있는 완전관리형, 중앙제어형 암호화 키라는 특징, 소중한 데이터 보호하기 위한 암호화 키 생성, 추적, 순회, 삭제 기능 제공. 모든 종류 키와 관련된 이벤트 추적하는 AWS CloudTrail과 KMS 통합해 기업 감사 업무 및 준법 감시 업무 사용

콘솔, AWS CLI, 또는 SDK에서 키 생성 및 관리 업무 수행, 키 관리 권한 IAM 유저, 그룹, 또는 롤 단위 부여

## AWS Secrets Mangaer

IAM 롤을 이용한 AWS 서비스 대한 접근권한 관리 방법 알아봄. 롤을 가지고는 인증자격(credential) 정보 안전하게 전달. 인증자격이란 서드파티 서비스 및 DB 등에 접근하기 위한 자격 정보 읨

패스워드 서드파티 API 등 애플리케이션 필요 하는 시크릿 리소스 전문적으로 다룰 수 있는 도구 바로 AWS Secrets Manager. 실행 코드 민감한 시크릿 코드 입력하는 방법 대신, Secrets Manager 이용 변경 사항 정기적 업데이트하는 방식 인증 자격 확인받을 수 있으며, 애플리케이션 요구하는 최신 인증자격 정보 제공. 인증자격 순회 작업 자동으로 이뤄지므로 편리

## AWS CloudHSM

CloudHSM 웹 서버 인프라의 암호화 작업 위해 전용 가상 연산 기기 클러스터 시작.  
CloudHSM에서 HSM은 hardware security module의 약자, 웹 서버 암호화 키 생성, 정렬, 관리 부담 덜어주는 것이 주요 목적 → 웹 서버 사용자 위한 애플리케이션 지원 집중

CloudHSM은 AWS KMS 유사 기능 제공, AWS 다음 같은 특징 및 장점 있다고 설명.

- 키는 높은 수준의 보안성 검증된 전용 서드파티 HSM 저장
- 미 연방정보처리표준(FIPS) 140-2 규정 부합
- Public Key Cryptography Standards(PKCS)#11, Java JCE(Java Cyptograhy), Microsoft CNG(Cryptography API : Next Generation) 인터페이스 이용 애플리케이션 통합된 기능 제공
- VPC 내 고성능 암호화 생성 가속 기능(대량 암호 생성 시 사용)

애플리케이션 데몬으로 CloudHSM 클라이언트 실행해 HSM 클러스터 활성화, 클라이언트는 HSM 완벽하게 암호화된 방식으로만 소통하도록 설정

## AWS Resource Access Manager(AWS RAM)

AWS RAM 리소스 접속 돕는 또 다른 서비스, 단일 조직 내 다수 계정 속한 유저 또는 조직 외부 AWS 계정 유저 안전하게 리소스 공유할 수 있도록 지언

AWS RAM 같은 리소스 접근 기능 사용, 여러 개의 리소스 사본 만들고 관리해야 하는 부담 덜 수 있음, 단일 접근 정책 및 단일 롤 프로필 통해 모든 작업 통제할 수 있다는 장점

특정 리소스 AWS RAM 공유 리소스 포함, 모든 인증 유저 자체 콘솔 또는 AWS CLI 이용해 해당 리소스 접근

## AWS CLI 예제

명령은 네임 속성 Steve인 새 유저 생성, 현재 존재하는 유저 확인

`$ aws iam create-user —user-name steve`

`$ aws iam get-user —user-name steve`

list-policies 명령은 IAM 제공하는 사전 설정된 정책 문서 반환.  
AmazonEC2ReadOnlyAccess 실행 중인 EC2 리소스 대한 읽기 권한만 허용. 특정 유저 Amazon Resource Name(ARN) 기법 정책 추가

`$ aws iam list-policies`

`$ aws iam attach-user-policy \ —policy-arn arn:aws:iam::aws::policy/AmazonEC2ReadOnluyAccess \ —user-name steve`

JSON 포맷 나타낸 AmazonEC2ReadOnlyAccess 정책 내용

```markdown
{
"Version": "2012-10-17",
"Statement": [
	{
	"Effect": "Allow",
	"Action": "ec2:Describe*",
	"Resource": "*"
	},
	{
	"Effect": "Allow",
	"Action": "elasticloadbalancing:Describe*",
	"Resource": "*"
	},
	{
	"Effect": "Allow",
	"Action": [
	"cloudwatch:ListMetrics",
	"cloudwatch:GetMetricStatistics",
	"cloudwatch:Describe*"
	]
	"Resource": "*"
	},
	{
	"Effect": "Allow",
	"Action": "autoscaling:escribe*",
	"Resource": "*"
	}
	]
}
```

list-access-keys 명령은 해당 유저네임과 관련 모든 키 이름 반환함.  
유저네임을 저장하지 않으면, 루트 계정 키가 반환. 아울러 create-access-key 명령은 새 키 생성, delete-access-key 명령 특정 키 삭제

`$ aws iam list-access-keys —user-name steve`

`$ aws iam create-access-key —user-name steve`

`$ aws iam delete-access-key —user-name-steve —access-key-id AKIAJAP<. . .>`

```markdown
위 내용 해석

정책 버전: "2012-10-17"
정책 명세:
a. EC2 관련:
효과: 허용
작업: "ec2:Describe*" (모든 EC2 설명 작업)
리소스: 모든 리소스 ("*")
b. Elastic Load Balancing 관련:
효과: 허용
작업: "elasticloadbalancing:Describe*" (모든 ELB 설명 작업)
리소스: 모든 리소스 ("*")
c. CloudWatch 관련:
효과: 허용
작업:
cloudwatch:ListMetrics
cloudwatch:GetMetricStatistics
cloudwatch:Describe*
리소스: 모든 리소스 ("*")
d. Auto Scaling 관련:
효과: 허용
작업: "autoscaling:Describe*" (모든 Auto Scaling 설명 작업)
리소스: 모든 리소스 ("*")
```
