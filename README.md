# auto-7z-compresser
간단한 원클릭 압축 시스템

설명
---
지정된 폴더들을 정해진 위치에 7z 으로 압축하여 저장합니다.

설정 파일
---
```py
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
- 설정 파일 파싱하기
- 압축하기
- 멀티프로세싱
