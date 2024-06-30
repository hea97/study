# **핵심키워드**

`표현식`  `키워드`  `식별자`  `주석`  `print()` 

---

# **문장**

실행할 수 있는 코드의 최소 단위를 **문장(statement)**.
Python은 ‘한 줄이 하나의 문장이다’라 생각하면된다.
문장들이 모이면 **프로그램(program)**.

```python
# 실행되는 모든 한 줄 코드는 문장.
print("Python Programming") #문장
10 + 20                     #문장
```

현실의 문장처럼 프로그그래밍 언어의 문장도 여러 단어로 구성.

# **표현식**

Python에서는 어떠한 값을 만들어 내는 간단한 코드를 **표현식(expression).
표현식**은 숫자, 수식, 문자열 등과 같은 것을 의미.

<aside>
💡 273
10 + 20 + 30 * 10
”Python Programming”

</aside>

(+, - 는 표현이 아니다.)

# **키워드**

**키워드(keyword)** 특별한 의미가 부여된 단어로 Python이 만들어질 때 이미 사용하겠다고 예약해 놓은 것.
사용자가 키워드인지 아닌지 구분해야 하는 이유는 프로그래밍 언어에서 사용자가 이름을 정할 때 키워드를 사용하면 안되기 때문이다.

### **Python 키워드**

| False | None | True | and | as | assert |
| --- | --- | --- | --- | --- | --- |
| async | await | break  | class | continue | def |
| del | elif | else | except | finally | for |
| from | global  | if  | import | in | is |
| lambda | nonlocal | not | or | pass | raise |
| return | try | while | with | yield |  |

**Python은 대소문자를 구분.**
ex. `True`는 키워드이지만 `true`는 키워드가 아니다.   
즉, `True`로는 이름을 정할 수 없고 `true`로는 이름을 정할 수 있다.  

사용하는 단어가 키워드인지 아닌지 꼭 확인해야 할 경우가 있다.

```python
>>> improt keyword
>>> print(keyword.kwlist)
```

# **식별자**

**식별자(identifier)** 프로그래밍 언어에서 이름을 붙일 때 사용하는 단어.
주로 변수 또는 함수 이름 등으로 사용.

**식별자의 기본적인 규칙.**

- 키워드를 사용하면 안된다.
- 특수 문자는 언더 바(_)만 허용.
- 숫자로 시작하면 안됨.
- 공백을 포함할 수 없음.

규칙에 맞는 단어는 모두 식별자로 사용할 수 있다.

| 사용 가능한 단어 | 사용 불가능한 단어 |
| --- | --- |
| alpha | break |
| alpha10 |  |
| _alpha | 273alpha |
| AlpHa |  |
| ALPHA | has space |

`break` → 키워드라서 안됨.

`273alpha`  → 숫자로 시작하면 안됨.

`has space`  → 공백을 포함해서 안됨.

식별자를 만들 때는 한글, 한자, 일본어와 같은 전 세계의 언어를 모두 사용할 수 있지만, 알파벳을 사용하는 것이 관례이다.   
또한 a, b처럼 의미 없는 단어보다 file, output처럼 의미 있는 단어를 사용하는 것이 좋다.

## 스네이크 케이스와 캐멀 케이스

식별자에는 공백을 사용할 수 없다.

| itemlist | loninstatus | characterhp | rotateangle |
| --- | --- | --- | --- |

이해할 수 있지만, 공백 없이 재빠른 이해는 어렵다.  
개발자들은 다음과 같은 두 가지 방법을 사용해 식별자 쉽게 이해할 수 있도록 했다.

1. **단어 사이에 언더 바(_) 기호를 붙여 식별자로 만든다.**
    
    ex. `itemlist`를 `item_list`로 쓰는 것.
    → **스네이크 케이스(snake_case).**
    
2. **단어들의 첫 글자를 대문자로 만들어 식별자로 만든다.**
    
    ex. `itemlist`를 `ItemList`로 쓰는 것.
    → **캐멀 케이스(CamelCase).**
    

| 식별자에 공백이 없는 경우 | 단어 사이에 _ 기호를 붙인 경우
(스네이크 케이스) | 단어 첫 글자를 대문자로 만든 경우
(캐멀 케이스) |
| --- | --- | --- |
| itemlist | item_list | ItemList |
| loninstatus | longin_status | LonginStatus |
| characterhp | character_hp | CharacterHp |
| rotateangle | rotate_angle | RotateAngle |

<aside>
💡 스네이크 케이스는 글자들이 뱀처럼 연결된다 해서.
캐멀 케이스는 글자들이 낙타 같다고 해서.

</aside>

---

## 식별자 구분하기

캐멀 케이스는 ‘첫 번째 글자를 대문자로 적는다’와 ‘첫 번째 글자를 소문자로 적는다’로 구분.
but. Python ‘첫 번째 글자를 소문자를 적는다’라는 캐멀 케이스는 사용하지 않는다

### **캐멀 케이스 유형 1**

`PrintHello`  → Python 사용.

### **캐멀 케이스 유형 2**

`printHello`  → Python 사용X.

Python에서는 첫 번째 글자가 소문자라면 무조건 스네이크 케이스.

| print | input | list | str | map | filter |
| --- | --- | --- | --- | --- | --- |

반대로 첫 번째 글자가 대문자라면 무조건 캐멀 케이스.

| Animal | Customer |
| --- | --- |

---

                `캐멀 케이스`  → `클래스`

`식별자`        

                                                `뒤에 괄호가 있다`  → `함수`

                `스네이크 케이스`  

                                                `뒤에 괄호가 없다`  → `변수`

---

캐멀 케이스로 작성되면 **클래스,** 
스네이크 케이스로 작성되어 있으면 **함수** 또는 **변수**. 
그리고 뒤에 괄호가 붙어 있으면 **함수.** 괄호가 없다면 **변수.**
단순한 구분이라 약간의 예외가 존재. 대부분 경우에는 이처럼 구분해도 문제가 없다.

클래스, 변수, 함수 구분하기

```python
print()
# 함수
list()
# 함수
soup select()
# 함수
math.pi
# 변수
math.e
# 변수
class Animal:
# 클래스
BeautifulSoup()
# 클래스 -> but. 괄호가 있어 클래스 생성자라고 함.
```

# **주석**

**주석(comment)** 프로그램의 진행에 전혀 영향을 주지 않는 코드, 프로그램을 설명하기 위해 사용함.     
Python 주석은 # 기호를 붙여 주석 처리한다.  
#은 프로그램에 어떠한 영향을 주지 않는다.  

```python
>>> # 간단히 출려하는 예.
>>> print("Hello! Python Programming. . .") # 문자 출력.
# HelloF! Python Programming. . .
```

# **연산자와 자료**

**연산자**는 스스로 값이 되는 것이 아니라 값과 값 사이에 무언가 기능을 적용할 때 사용하는 것을 말한다.  
즉, +, - 와 같이 단독으로 쓰일 때는 아무 의미를 갖지 않지만. 양쪽에 숫자가 있을 때는 +는 더하기, - 는 빼기 기능 수행.

```python
>>> 1 + 1
# 2
>>> 10 - 10
# 0
```

**자료 == 리터럴(literal)**  
자료란 예시 처럼 그게 숫자이든지 문자이든지 어떠한 **값** 자체를 의미.

<aside>
💡 1
10
”Hello”

</aside>

# **출력 : print()**

Python의 가장 기본 적인 출력 방법은 `print()` 함수를 사용.  
**`print()`** 함수, 함수의 괄호 안에 출력하고 싶은 것을 나열해서 사용한다.  

```python
print(출력1, 출력2, . . .)
# 출력하고 싶은 내용이 여러 개면 여러 개를 넣어도 된다.
```

## 하나만 출력하기

`print()` 함수 괄호 안에 출력하고 싶은 내용을 적는다.  

```python
>>> print("Hello Python Programming. . .!")
#Hello Python Programming. . .!
>>> print(52)
# 52
>>> print(273)
# 273
```

## 여러 개 출력하기

`print()` 함수 뒤에 출력하고 싶은 내용을 쉼표로 연결해서 여러 개 적어도 됨. → 숫자와 문자열의 혼합.  

```python
>>> print(52, 273, "Hello")
# 52 273 Hello
>>> print("안녕하세요". "저의", "이름은", "Python")
# 안녕하세요 저의 이름은 Python
```

## 줄바꿈하기

`print()` 함수 괄호 안에 아무것도 입력 하지 않는다면 출력하지 않고 단순하게 **줄바꿈.**   
대화형 셸에 `print()`를 입력하면 아무것도 출력하지 않고 빈 한줄을 만든 후 프롬프트를 표시한다.

```python
>>> print()
# 빈 줄
>>>
```

출력할 때 `print()` 함수는 괄호가 있으므로 **함수(function)**라고 한다.  
함수의 괄호 내부에는 문자열 등의 자료를 입력한다.  
**자료**는 **‘어떤 상태를 가지고 있는 것’** **함수**는 **‘어떤 처리를 하는 것’**이라고 할 수 있다.  

### **기본 출력 (github_code)**

`소스 코드 output.py`
