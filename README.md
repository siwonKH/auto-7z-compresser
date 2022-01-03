# auto-7z-compresser
간단한 원클릭 압축 시스템

설명
---
지정된 폴더들을 정해진 위치에 7z 으로 압축하여 저장합니다.

설정 파일
---
```
# config.txt
files {
    "C:\Users\MyProjects\PythonProjects",
    "C:\Users\MyProjects\GoProjects",
}
location {
    "C:\Backup\MyProjects\",
    "",
}
exclude_folder {
    "venv",
    "node_modules",
    ".git",
}
cores {
    8
}
```
- files{}
  - 백업할 폴더들의 경로를 위와 같은 형식으로 안에 작성합니다.
- location{}
  - 백업할 폴더 개수만큼 압축파일이 저장될 경로를 순서대로 안에 작성합니다.
  - 칸을 위와 같이 비워두면 비지 않은 위 경로를 사용합니다.
- exclude_folder{}
  - 제외할 폴더명들을 안에 작성합니다.
  - 제외할 파일은 *.[확장자] 형식으로 작성합니다.
- cores{}
  - 사용할 논리 코어수를 입력합니다.

작동 방식
---
### 설정 파일 파싱함수
files를 예로 든다면..
1. files 라는 글자부터 } 까지의 문자열을 추출  
```
files {\n"C:\Users\MyProjects\PythonProjects",\n"C:\Users\MyProjects\GoProjects",\n}
```
2. 위 문자열에서 { 까지의 문자열을 추출  
```
{\n"C:\Users\MyProjects\PythonProjects",\n"C:\Users\MyProjects\GoProjects",\n}
```
3. " 를 기준으로 split 하여 리스트로 추출  
```py
["{\n", "C:\Users\MyProjects\PythonProjects", ",\n", "C:\Users\MyProjects\GoProjects", ",\n"]
```
4. 리스트의 짝수 주소의 값만 추출하여 그 리스트를 return 함
```py
["C:\Users\MyProjects\PythonProjects", "C:\Users\MyProjects\GoProjects"]
```

### 압축하기
```py
os.system(f'7z a -t7z "{location}{date}\\{name}-{date}" "{folder}" -mmt{cores} -mx=1 {exclude_str}')
```

### 멀티프로세싱
