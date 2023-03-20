# DALL-E2 이미지 생성 프로그램 실행 방법

1. `dalle2_ui.py` 파일을 다운로드하고, Python이 설치된 환경에서 파일을 실행할 수 있도록 합니다.
2. OpenAI API 키를 얻습니다.
3. 환경 변수에 OpenAI API 키를 설정하거나, `config` 파일에 저장합니다.
4. `PyQt5` 모듈을 설치합니다.
5. `dalle2_ui.py` 파일을 실행합니다.

OPENAI_API_KEY를 환경 변수로 설정하려면, 운영 체제에서 다음과 같은 단계를 수행해야 합니다.

## macOS와 Linux에서 환경 변수 설정
1. 터미널을 엽니다.
2. 다음 명령어를 입력하여 홈 디렉토리에서 .bashrc 파일을 엽니다.
```bash
nano ~/.bashrc
```
> 참고: macOS에서는 대신 ~/.bash_profile 파일을 열어야 할 수도 있습니다.

3. 파일의 끝으로 이동하여, 다음 줄을 추가합니다.
```bash
export OPENAI_API_KEY="YOUR_API_KEY_HERE"
```
여기서 YOUR_API_KEY_HERE는 본인의 OpenAI API 키로 바꾸어야 합니다.
4. Ctrl+X를 눌러 파일을 저장하고 나갑니다.
5. 새 터미널 창을 열거나, 다음 명령어를 입력하여 .bashrc 파일을 업데이트합니다.
```bash
source ~/.bashrc
```
> 참고: macOS에서는 대신 source ~/.bash_profile 명령어를 입력해야 할 수도 있습니다.
6. 환경 변수가 성공적으로 설정되었는지 확인하기 위해, 다음 명령어를 입력합니다.
```bash
echo $OPENAI_API_KEY
```
7. 환경 변수가 설정되어 있다면, API 키가 출력됩니다.


## Windows에서 환경 변수 설정

1. 시작 메뉴를 열고 "환경 변수 편집"을 검색합니다.
2. "시스템 환경 변수 편집"을 선택합니다.
3. "환경 변수" 버튼을 클릭합니다.
4. "새로 만들기"를 클릭하고, 변수 이름에 OPENAI_API_KEY를 입력합니다.
5. 변수 값에 본인의 OpenAI API 키를 입력합니다.
6. "확인" 버튼을 클릭하여 변경 사항을 저장합니다.
7. PowerShell 창을 열고, 다음 명령어를 입력하여 환경 변수가 제대로 설정되었는지 확인합니다.
```powershell
echo $env:OPENAI_API_KEY
```
>환경 변수가 설정되어 있다면, API 키가 출력됩니다.

## macOS나 Linux에서의 실행 방법

1. `dalle2_ui.py` 파일을 다운로드하고, 터미널을 엽니다.
2. OpenAI API 키를 얻습니다.
3. 환경 변수에 OpenAI API 키를 설정하거나, `config` 파일을 생성하여 API 키를 저장합니다. 아래는 `config.ini` 파일을 사용하는 예시입니다.

```shell
[openai]
api_key=YOUR_API_KEY_HERE
```


4. `PyQt5` 모듈을 설치합니다. 터미널에서 다음과 같이 입력합니다.
```shell
pip install pyqt5
```


5. `dalle2_ui.py` 파일을 실행합니다. 터미널에서 다음과 같이 입력합니다.
```shell
python dalle2_ui.py
```


이제 프로그램이 실행되고, UI 창이 표시됩니다. "Generate" 버튼을 누르면 DALL-E2 모델을 사용하여 이미지가 생성되고, UI 창에 출력됩니다.


