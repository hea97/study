# Amazon S3 Glacier

Clacier 다른 S3 스토리지 클래스와 비슷한 부분 많음, 다른 S3 클래스처럼 99.999999999%의 내구성 지니고 S3 수명주기 환경설정에 통합해서 사용할 수 있음

bu. Glacier 다른 S3 스토리지 클래스와 다른 부분도 상당히 많다.  
우선 Glacier 아카이브 저장용량은 40TB 제한(S3 용량 제한X), 아카이브 생성 시 기본적 저장 data 암호화(S3 data 암호화 옵션), 아카이브 이름은 기계 생성 ID 형식 지니는 등 다수 차이점 존재.

그 중 가장 큰 차이점으로 data 인출 시간이라 할 수 있음.  
Glacier 아카이브 객체를 인출하는 데는 수 시간이 수요, S3 버킷 거의 즉각적 객체를 인출.   
→ Glacier 특징을 가장 잘 설명하는 속성, Glacier 저장된 data 거의 인출하지 않음, 저렴하게 사용하 수 있는 장기 보관용 스토리지임

---

Glacier 별도의 이용료 지불한 뒤 불과수 분만 data 인출할 수 있는 촉진 인출(Expedited reterievals) 옵션 제공

---

Glacier 아카이브 문서, 비디오, TAR, ZIP 파일 등 저장 객체 가리키는 말, Glacier 볼트(vaults)  저장.  
Glacier 볼트는 S3 버킷에 대응되는 개념, 전역에서 유일무이한 이름 부여

Glacier 스토리지 클래스는 Standard 및 Deep Archive 등 두 가지, Glacier Deep Archive 좀 더 저렴하면서 인출 시간 좀 더 오래 걸림.  
1TB data를 Glacier standard 저장 비용 $4.10 반면, Glacier Deep Archive 저장하는 비용은 $1.02 불과.  
대신 Glacier Deep Archive data 인출에는 12 ~ 48 시간 소요

| 티어 | 인출 용량 | 비용 |
| --- | --- | --- |
| Glacier instant | 100GB | $3.00 |
| Glacier felxible | 100GB | $1.00 |
| Deep Archive | 100GB | $2.00 |

## 스토리지 가격 모델

S3 Glacier 비용 대한 개념 정리 시나리오 구상.  
ex. 매주 5GB 영업 data 생성, → 정기적 백업.  
→ 가장 먼저 사용할 스토리지 클래스 S3 Standard, data 생성 후 첫 30일간 보관, 다음 S3 One Zone-IA로 옮겨 90일간 보관.  → 120일 경과한 후, Glacier 옮겨 730일(2년)간 보관한 뒤, 삭제

이 기간 동안 S3 Standard 20GB, S3 One Zone-IA에 65GB, Glacier 520GB data 누적 및 저장. 

US East 리전 data 용량별 스토리지 가격

| 스토리지 클래스 | 저장 용량 | 월간 GB당 비용 | 월간 총비용 |
| --- | --- | --- | --- |
| Standard | 20GB | $0.023 | $0.46 |
| One Zone-IA | 65GB | $0.01 | $0.65 |
| Glacier Instant | 520GB | $0.004 | $2.08 |
| Total |  |  | $3.19 |

스토리지에 저장만 하지 않음, data 인출 및 활용 위한 PUT, COPY, POST, LIST 명령 실행 및 수명주기 전화 작업 비용 발생.  
스토리지 비용에 대한 최신 자료.

https://aws.amazon.com/ko/s3/pricing/

# 기타 스토리지 관련 서비스

널리 사용되는 AWS 스토리지 클래스 외 다양한 스토리지 서비스 살펴봄 기존 클래스와의 차이점 특징

## Amazon EFS

Amazon Elastic file System(EFS) 리눅스 인스턴스 위한 확장성, 공유성 높은 파일 스토리지, EC2 Linux 인스턴스 마운트된 Network File System(NFS) 통해 VPC 필요 파일 접근하거나 AWS Direct Connect로 연결된 온프레미스 서버의 파일 접근.  
EFS 다수 인스턴스에서 파일 쉽게 접근할 수 있는 안전 전송 지연 문제 적으면 재구성 높은 네트워크 파일 스토리지 서비스

## Amazon FSx

Amazon FSx는 Lustre용 또는 Windows File Server용 가운데 선택 사용, Lustre는 Linux 클러스터 고도 컴퓨팅 작업 수행할 때 고성능 파일 시스템 접속할 수 있게 해주는 오픈소스 분산 파일 시스템, Amazon FSx는 AWS 인프라 Lustre 기능 사용

Windows File Server용 FSx는 Windows 서버 위한 EFS, Server Message Block(SMB), NTFS, Microsoft Active Directory 통합 사용

## AWS Storage Gateway

로컬 스토리지와 클라우드 스토리지 연결 백업 및 아카이브 통합 작업은 꽤 복잡.  
AWS Storage Gateway 문제 해소해 주며, 온프레미스 HW 또는 VMware ESXi, Microsoft Hyper-V, Linux KVM, AWS 기반 VMware Cloud, or EC2 이미지 기반 가상 머신용 SW 게이트웨이로서 다수 가상 연결 인터페이스 제공.

AWS Storage Gateway 기업의 로컬 디바이스 전통적 테이프 드라이브처럼 연결, data S3 or EBS 등 AWS 플랫폼 저장 사용할 수 있고, 로컬 캐시 저장한 뒤 로컬 접속 지연 없이 사용

## AWS Snow Family

대량 data 클라우드 전송할 때 보통 인터넷 연결 방식 이용 지나치게 많은 시간 소모되고 전송 업무 차질 빚어질 수 있음.    
테라바이트급 or 페타바이트급 data 백업 or AWS 내 data 활용 필요한 경우 Snowball 해법

사용자 요청 따라 AWS 물리적인 256비트 암호화 스토리지 디바이스인 Snowball 배송.  
사용자 Snowball 대용량 data 저장, Amazon으로 재배송, 전달된 data S3 버킷 업로드

물리적 data 전송 장치 외, 엣지 로케이션 연결 사용 Snow 패밀리 디바이스 제공.  
저장 장치 일반적인 엔터프라이즈 디바이스 이용 환경, 사막이나 해양 등 불안정적인 기상 환경 문제 없이 사용 있도록 설계

Snow 패밀리 가운데 가장 작은 디바이스 9X6X3인치 크기 Snowcone, HDD 타입 최대 8TB, SSD 타입은 최대 14TB 저장용량, 네 개의 vCPU, 4GB 메모리, RJ45 및 Wi-Fi 통신 환경 지원

좀 더 큰 저장 용량 디바이스 Snowball Edge.  
Snowball Edge Storage Optimized 타입, 80TB 최대 저장 용량, 40개 vCPU, 80GB 메모리 제공, Snowball Edge Compute Optimized 타입, 42TB 최대 저장 용량, 52개의 vCPU, 208GB 메모리 제공.  
두 가지 타입 중 Compute Optimized 타입 엣지 컴퓨팅 최적화 버전

AWS Snowmoblie 방수 및 방진 기능 갖춘 45미트 길이의 컨테이너 차량 패타바이트(petabyte) or 엑사바이트급(exabyte) 저장 용량 제공, 일정 기간 동안 컨테이너 차량 주차 수 년간 쌓인 대용량 data 로컬 네트워크 통해 전송.  
전송 마치면, Snowmoblie 컨테이너 차량 몰고  AWS 리전 이동 계정의 스토리지 리소스 업로드

모든 Snow 패밀리 디바이스 256비트 암호화, 엄격한 HIPAA 규정 충족하도록 만들어짐

AWS data 전송하는 방법 서택하기에 앞서 몇 가지 변수 고려.  
data를 실제 인터넷 통해 전송할 때 속도를 파악할 필요, 전송 진행되는 동안 대역폭 문제 다른 작업 지연 중단 문제도 고려

S3 버킷에 대용량 객체 효율적 저장하는 방법 멀티파트 업로드(Multipart Upload) 및 전송 가속(Transfer Acceleration) 기능 대해 살펴보기, 일부 객체 용량이 커 기존의 인터넷 연결 업로드 어려움.  
ex. 회선이 10MB/초 전송 속도 제공, 1TB의 아카이브 전송 대략 10일 걸림

→ 기업 보유한 data 클라우드 전송 다소 고가인 AWS Direct Connect 이용 좀 더 저렴한 AWS Snowball 이용 실용적.  
엑사바이트급 data 스토리지 컨테이너 운송차인 AWS Snowmoblie 통해 전송

## AWS DataSync

DataSync는 온프레미스 저장 data AWS 계정 옮기는 작업 특화된 도구, 보통 인터넷 연결 이용 Snowball 같은 대규모 data 이전 적합하지 않음, S3 물론 (AWS Database Migration Service) RDS등 다양한 저장소 data 전송할 수 있는 유연성 제공

DataSync 이용 AWS 계성 연결된 어떤 서비스 data 전송

- 고가의 온프레미스 data 센터 저장된 data 신속하고 아전하게 S3 또는 Glacier 이전
- EC2 인스턴스 data 처리 및 분석할 수 있도록 S3, EFS, 또는 FSx 등으로 data 직접 전송
- 설정 쉬운 자동화 시스템으로 어떤 규모의 data 클래스 손쉽게 AWS 서비스 적용 가능

DataSync 최대 10Gbps 수준 data 전송, 암호화 및 data 겁증 기능 제공
