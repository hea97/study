### 식별자(identifier)
프로그램에서 사용하는 변수, 메서드, 클래스, 상수 등도 이름으로 구별

식별자 작성시 따라야할 규치
- 문자, 언더바(_), $로 시작 한글도 가능하며 영문자 대소문자는 구별해야한다.
- +, -등 연산자를 포함하면도 안된다.
- 자바 키워드를 사용하면 안된다.
- 길이에 제한이 없다
ex. %8, a+b, 5b → 잘못된 식별자
Readme, $a, _code → 올바른 식별자 

### 식별자를 정할때 가독성을 높이는 방법.
1. 변수의 메서드는 모두 소문자로 표기한다.
```java
int thisYear;
String currentPosition;
boolean is Empy;
pulic int getYEar() {}
```

2. 클래스와 인터페이스는 첫 자만 대문자로 표기하고 나머지는 소문자로 표기.
→ 복합 단어일 때는 각 단어의 첫 자만 대문자로 표기.
```java
public class HelloDemo{}
public interface MyRunnable{}
```

3. 상수는 전체를 대문자로 표기.
→ 복합 단어일 때는 단어를 언더바(_)로 연결.
```java
final int NUMBER_ONE = 1;
final double PI = 3.141592;
```
