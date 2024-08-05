# AWS 환경에서 작업

각 서비스에 맞는 관리 방식을 채택해야한다.  
브라우저 기반의 관리 콘솔(management console)은  
서비스가 제공하는 각종 기능을 활용할 수 있는 방법, 제공하며 기능 제어를 통해 실제 리소스가 어떻게 변경 되는지 확인 할 수 있다.  
AWS 계정은 각종 서비스를 간단하면서도 체계적으로 관리할 수 있는 다양한 도구를 제공한다.

관리 콘솔을 이용하면 거의 대부분 AWS 관리 업무 처리, 업무 수행에 도움을 주는 각종 시각화 도구 및 지원 문서를 이용.  
관리 콘솔을 이용한 AWS 리소스 관리가 좀 더 편해지는 부분 있음,   
복잡성이 커질수록 일부 콘솔 이용 처리하기 어려운 상황 생길 수 있음.

## AWS Organizations

AWS Organiztions를 이용 다수 AWS 계정을 통합적 관리.  
대규모 조직에서 aWS 기반 실행되는 다수 프로젝트와 리소스 관리할 경우, 관리의 용이성을 위한 통합도 중요. 안정성 등 고려한 리소스 격리(resource isolation)도 중요한 요소.  
다수의 대규모 프로젝트 운영 조직 → 모든 프로젝트를 높은 시점에서 두루 살펴보고 관리 할수 있는 체계 필요, 비용 관리 또한 하나의 계정으로 처리할 수 있으면 편함.

AWS Organizations는 하나의 조직 체계 계정을 새성, 기존의 다른 계정을 초대 관리할 수 있도록함.  
다수의 계정이 연결되면 조직 관리자(organization administration)는 매우 간단한 방식으로 전역 접근 정책(global access policies)을 생성. 다수의 계정과 프로젝트 통합적 관리. 

조직 계정을 안전하게 관리 → 무척 중요.  
서로 분리된 단일 계정으로 관리할 때보다 보안 침해에 따른 파급 효과가 더욱 커짐.  
→ 조직 계정은 다중 인증(MFA), 강력한 암호 그리고 루트 계정 보안 등 기존의 모든 보안 모범 사례를 반영 → 안전하게 관리

**AWS Organizations**

- AWS Single Sign-on 구성을 통해 조직 전체 리소스에 대한 전역 접근 권한을 제공, 관련 리소스를 공유
- 서비스 제어 정책(SCP) 통해 IAM 규칙을 조직 내 모든 리소스 및 서비스에 적용
- 프로그래밍 방식으로 계정, 사용자, 그룹 생성 및 관리
- 조직 내 모든 리소스가 규정에 맞게 사용되는지 여부를 모니터링, 저절한 보호 방식을 적용, 추후 감사 업무 활용.  
단일 계정에 연결된 CloudTrail 서비스를 통해 전체 조직의 모든 이벤트를 추적하도록 설정.

AWS Organizations는 기존 사용되던 통합 과금 도구  
Consolidated Billing 기능을 대신 제공

## AWS Control Tower

AWS Organizations 기능은 Control Tower 생성한 랜딩 존(landing zones) 통해 더욱 넓은 범위로 확장.  
랜딩 존은 새로 생성된 계정에 자동으로 조직의 거버넌스 정책 적용, 클라우드 인프라에 통합 관리 돕는다

랜딩 존은 하나 또는 여러 개의 AWS 리전 사용할 수 있음.  
세부적으로 정의된 관리자 또는 로그 아카이브 계정을 통해 제어  
랜딩 존 생성 후 리소스 관리와 관련된 보안 규칙, 사내 업무 규칙 또는 모법 사례를 선택 및 적용해 관리

거버넌스 관련 정책 생성 기능 외 Control Tower의 랜딩 존은 리소스 모니터링 및 정책 관리 업무를 단순화, 클라우드 인프라를 좀 더 밀접하게 관리.

## AWS Service Catalog

Organizations 사용하다 보면 비즈니스 분석, 마케팅 지원, 리서치 프로젝트 등 조짖ㄱ 단위 계정과 프로젝트 관리 위해 좀 더 효과적 일관된 도구 필요.  
AWS 서비스 전용 도구 AWS Marketplace에서 제공 중 머신 이미지 형태의 각종 도구를 선택해서 활용.  
사용자는 CloudFormation템플릿 등 이용해 → 응용 서비스를 직접 구현하고 수정해서 사용.

AWS Service Catalog는  
→ 각종 템플릿과 도구 구현에 필요한 각종 리소스를 간편하면서도 정확하게 선택, 구성할 수 있도록 돕는다.  
사용자가 자신이 필요로 하는 가용성 수준, 리소스 소모량을 설정, Service Catalog가 보안성 및 범용 모범 사례를 바탕으로 나머지 구현 작업 처리.

## AWS License Manager

AWS License Manager SW 라이선스 관리 전문 도구,  
License Manager 대시보드를 통해 사용량 추적, 모니터링 규칙, 기타 사용 규칙을 근거로 라이선스 약정을 위배하는 일 없도록 관리.  
License Manager 클라우드 기반 SW, 온프레미스 SW 라이선스 관리에도 사용, → 별도의 비용은 부담하지 않아도 됨.

## AWS Artiface

AWS Artifact 고객이 AWS 계정 및 서비스 대한 이용 규칙(compliance) 정보를 다운로드 할 수 있는 저장소(repository) 서비스, 고객은 필요에 따라 이용 현황과 관련 AWS Service Organizations Control 보고서, Payment Card Industry Data Security Standard(PCI DSS) 보고서 그리고 ISO 27001 인증서 이용 규칙 및 감사와 관련된 정보를 좀더 수비게 확인. 

## AWS CLI

AWS CLI(Command Line Interface)  
복잡한 작업을 사용자의 로컬 커맨드 라인으로 처리할 수 있도록 지원하는 도구.  
AWS CLI 익숙해지고 나면 본격적인 AWS 관리 작업을 좀 더 간편하고 효율적으로 처리할 수 있도록 해주는 유용한 도구.  

Linux, Windows, macOS 등 환경에 AWS CLI 설치하고 환경설정하는 일은 그리 어렵지 않음. 기기 따라 세부 과저 약간 다름.

(실습의 경우 금요일에 진행하겠습니다)

## AWS SDK

애플리케이션 코드에 AWS 리소스를 포함시켜야 하는 경우,  
선호하는 언어별 작성된 AWS SDK(software Development Kit) 이용.  
지원하는 언어 https://aws.amazon.com/ko/developer/tools/ 에서 확인할 수 있다 대략 13개이다.

## 기술 지원 및 온라인 자료

AWS는 다양한 유형의 지원을 제공, 아키텍트인 고객이 어떤 지원 서비스를 이용할 수 있는지도 알고 있어야한다.  

AWS 계정을 생성한 뒤 어떤 지원 서비스가 가능한지 알아보는데,  
지원 서비스는 기업의 요구사항 및 예산 규모에 따라 달라짐

## 서포트 플랜

### Basic 플랜

AWS 모든 계정 회원이 사용할 수 있음.  
개발자 문서, 화이트 페이퍼, 서포트 포럼 등 각종 고객 서비스를 제공.  
고객 서비스에는 과금 및 계정 문제 해결 서비스가 포함

### Developer 플랜

월 29$부터 이용 가능.   
하나 이상의 계정을 Cloud Support에 연결해 서비스 이용.  
범용 가이드 및 시스템 이상 응답 서비스를 제공

### Business 플랜

월 100$부터 이용 가능.  
계정 수 상관 없이 시스템 이상, 개별 사용자 가이드, 트러블슈팅, API 지원 등의 문제에 대해 일정 시간 내에 응답할 것을 보장

### Enterprise On-Ramp 플랜

월간 5,500$ or 월간 AWS 요금 10%를 부담하는 조건으로 이용 가능.  
→ Business 플랜 지원 서비스 외 비즈니스에 매우 중요한 시스템의 다운 이벤트 발생시 신속한 대응 서비스를 제공.  
애플리케이션에 대한 선제적 대응 가이드 및 컨설팅 리뷰 등의 서비스 제공.

### Enterprise 플랜

월 15,000$부터 이용 가능.  
위 플랜의 모든 서비스는 물론, 운영 및 설계와 관련되 문제 해결을 위한 AWS 솔루션 아키텍트와의 직접 연결 서비스, 기업 전용 기술 지우너 매니저 등 포함한 → 종합 지원 서비스(support concierge) 제공.  
중요성 매우 큰 애플리케이션 또는 기업 서비스 배포의 경우 저갑한 플랜. 

https://aws.amazon.com/ko/premiumsupport/plans/

# 기존의 리소스를 AWS 이전하기 위한 서비스

AWS 기존의 애플리케이션 및 인프라 구성 리소스를 클라우드로 이전 위한 다양한 도구 제공,  
AWS Migration Hub, AWS Application Migration Service 그리고 AWS Database Migration Service 등이 대표적.  
→ 도구는 각각의 특성과 장점, 기존 리소스를 AWS로 좀 더 신속하고 안전하게 이전하는 방법 제공.

## AWS Migration Hub

AWS Migration Hub는 기존 워크로드 AWS 클라우드로 이전하는 과정을 추적하는 서비스.  
Migration Hub 대시보드는 기존 리소스 인벤토리 정보 및 이전 프로젝트의 진행 상태, 이전 관련된 각종 문제 상황 파악에 도움.  
Migration Hub 이전과 관련 모든 연관 도구의 작업을 조정하는데 도움,  
기존 워크로드를 AWS 이전하기 위한 각종 작업의 발생 가능성 평가 활용.   기존 워크로드를 클라우드 네이티브 애플리케이션으로 변환 및 분할하기위한 각종 도움 제공. 

## AWS Application Migration Service

Application Migration Service(AMS) 과거 제공되던 AWS Server Migration Service 대체 서비스.  
비-클라우드 기반 애플리케이션 서버를 AWS 기반 서버로 이전하기 우히나 검증 및 전환 자동화 도구.  
온프레미스 인프라의 클라우드 전환, 기본적 자동화 기법으로 처리되는 것이 이상적.

AWS 이전 대상인 양측 서버 AWS Replication Agent 설치 시작, 에이전트 서버 실행 영향을 주지 않도록 백그라운드 이전 필요한 복제 작업 진행.    
기존 서버의 애플리케이션 SW 클라우드 모두 복제, 클라우드 기존의 모든 기능 정상적으로 작동하는 확인, 정상작동 여부 확인  
마지막 과정, AWS 애플리케이션 실행.

단, CloudEndure, AWS GovCloud 또는 중국 리전으로의 마이그레이션 활용되는 용도 또는 지역 특화 이전 도구.

## AWS Database Migration Service

 AWS Database Migration Service(AWS DMS) DB를 위한 마이그레이션 서비스, 기존 온프레미스 환경에서만 사용 data를 좀 더 높은 성능 및 가용성을 제공하는 클라우드 환경에서 사용하기 위한 도구.  
AMS보다 좀 더 간단한 편, Replication Agents 설치 없이 기존 DB의 엔드포인트만 연결.

but. data 다양한 속성을 지니고, DB 엔진 또한 Oracle, Microsoft SQL Server 등 다양, 기존 data 어떻게 한 번에 클라우드로 이전?  
DBMS 사용자에게 다양한 선택안 제공.  
Oracle에서 Oracle로, or MariaDB 이전과 같은 동종 이전(homgeneous migration) 옵션 선택, 기존 RDB를 Amazon S3 기반 data 레이크로 이전, Oracle DB AMazon Aurora로 이전.

## AWS Application Discovery Service

AWS Application Discovery Service  
어떤 애플렠이션 온프레미스 data센터 실행 확인,   
→ 애플리케이션 어떻게 서로 연결돼 있으며, 어떤 리소스 사용하는지 파악 도움.  
이전 담당자 이러한 정보를 바탕으로 이전 작업에 좀 더 적합한 기법 및 도구 선택.

Application Discovery Service 기존 data센터 정보 구조를 체계화, 애플리케이션 댛나 정보 수집한 뒤 이전 대상 애플리케이션 및 의존성 요소의 환경설정 모델(configuration model) 생성.

Application Discovery Service 사용 위해, 먼저 온프레미스 서버 Discovery Service Agents 설치.  
설치된 에이전트 애플리케이션에 필요한 리소스 및 각종 의존성 요소 대한 정보 수집.  
→ 수집된 정보는 미리 지정된 data 스토어 저장, 수집된 data 이전 기획 또는 보고서 작성 업무 위해 CSV 파일 저장.

## 정리

클라우드 컴퓨팅 기술 물리적 서버 리소스 유연한 가상의 리소스로 분할해 사용하는 가상화 기술을 기반.  
사용자는 클라우드 사업자로부터 가상의 서버 유닛을 종량제 과금 모델 ‘임대’한 뒤, 사용 용이성, 확장성, 탄력성 등 요구 사하아 충족하는 애플리케이션 또는 워크플로우 구현.

Amazon Web Services 전세계 각지 산재한 리전 및 AZ 통해 신뢰성 및 보안성을 갖춘 클라우드 서비스 제공.  
AWS 오랜 시간 동안 수많은 기업 및 기관에 의해 검증된 베스트 프랙티스 및 글로벌 표준 규정 부합 클라우드 인프라 제공.  
사용자는 공유 책임 모델 기반 AWS 클라우드 인프라 활용, 기업 애플리케이션 및 서비스 제공. 

AWS 서비스 영역은 지속적 확장.  
AWS 핵심 서비스 컴퓨트, 네트워킹, DB, 스토리지, 보안 애플리케이션 관리 및 통합 운영.  
사용자는 AWS 리소스 브라우저 기반 콘솔과 AWS CLI 이용해 관리.  
AWS SDK 이용.  클라우드 리소스 포함된 네이티브 코드 생성.  

기술 지원 및 계정 이용 지원은 기업 요구사항 및 예산에 따라 다양한 서포트 플랜 이용.  
모든 AWS 회원은 개발자 문서 및 커뮤니티 포럼을 무료로 활용.  
AWS 화이트 페이퍼, 개발자 가이드 등 다양한 문서를 웹은 물론, Kindle 버전으로도 제공.

전체 애플리케이션 또는 개별 DB 각종 리소스 AWS로 마이그레이션하는 작업은 AWS Migration Hub 집약.  
앱 서버 이전은 AWS Application Migration Service, DB 이전은 AWS Database Migration Service 그리고 로컬 상 존재하는 애플리케이션 리소스 정보 수집은 AWS Application Discovery Service 이용.  
