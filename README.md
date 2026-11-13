
# 성적 CSV 검증기

성적 CSV 파일을 읽어 유효한 점수 목록과 제외된 행 및 사유를 반환합니다.
0~100 범위의 정수를 검증하며, 평균·학점 계산은 아직 지원하지 않습니다.

<!-- 예) 성적 CSV 검증기 -->

<!--
  README 여섯 항목 양식입니다. (실습 PPT 28쪽 · 학습지 ⑤와 같은 순서)
  1. 이 파일의 이름을 README.md 로 바꾼 뒤 아래 칸을 채웁니다.
  2. <!-- 로 시작하는 설명은 다 채운 뒤 지웁니다.
  3. 명령은 직접 실행해 보고, 실제로 나온 결과만 적습니다.
  4. 공개 저장소이므로 학번·연락처는 적지 않습니다. (학번은 학습지에만)
  5. 각 칸의 내용은 설명이 끝나는 줄 아래 빈 줄에 적습니다. (설명 안에 쓰면 GitHub에 보이지 않습니다)

  판정 기준: 처음 보는 사람이 이 문서만 보고 실행과 테스트를 할 수 있는가.
  (게시 후 새 폴더에 clone해 이 문서대로 직접 실행해 봅니다)
-->

성적 CSV 검증기

① 무엇을 하나요 (What · 현재 상태)

성적 CSV 파일을 읽어 유효한 점수 목록(kept)과 제외된 행 및 사유(skipped)를 반환합니다.

* 이름과 점수를 읽어 처리합니다.
* 점수는 0~100 범위의 정수만 유효합니다.
* 빈 줄, 빈 이름, 잘못된 점수 및 범위 밖의 점수는 제외합니다.
* 평균 및 학점 계산은 아직 지원하지 않습니다.

② 왜 만들었나요 (Why)

실제 성적 CSV 파일에는 빈 칸, 범위 밖 점수, 잘못된 형식의 데이터 등이 포함될 수 있습니다.

이러한 데이터를 그대로 읽으면 프로그램이 오류를 일으키거나 잘못된 결과를 만들 수 있습니다.

따라서 유효한 데이터와 제외된 데이터의 이유를 구분하여 확인할 수 있도록 만들었습니다.

③ 어떻게 쓰나요 (How)

프로젝트 폴더의 터미널(PowerShell)에서 다음 명령을 실행합니다.

1. Python 버전 확인

python --version

2. 필요한 패키지 설치

python -m pip install --user -U "pytest>=7.0" pytest-cov

3. CSV 파일 실행

python load_scores.py scores.csv

4. pytest 플러그인 설정

$env:PYTEST_DISABLE_PLUGIN_AUTOLOAD="1"

5. 테스트 실행

python -m pytest test_load_scores.py -q

6. Coverage 확인

python -m pytest test_load_scores.py -p pytest_cov --cov=load_scores --cov-report=term-missing

④ 어떻게 테스트하나요 (Testing)

실제 테스트 결과

* 테스트 통과: 12 passed
* Coverage: 80%
* Missing lines: 77-86

테스트 결과 설명

기본 테스트 11개와 weird.csv 보강 테스트 1개를 실행했습니다.

총 12개의 테스트가 모두 통과했습니다.

Coverage는 80%이며, Missing 77-86은 아직 테스트되지 않은 코드 영역입니다.

추가 실험 결과

test_bug3_logic.py 및 test_bug_B.py에서 find_max 함수의 버그를 확인하기 위한 테스트를 진행했습니다.

* 결과: 2 passed / 2 failed
* 실패 원인: 마지막 요소가 가장 큰 경우와 오름차순 점수 목록에서 최대값을 올바르게 찾지 못하는 문제입니다.

⑤ 파일 구성 (File Structure)

파일	하는 일
load_scores.py	CSV 파일을 읽고 유효한 데이터와 제외된 데이터를 반환
scores.csv	기본 성적 데이터
empty.csv	빈 데이터 테스트
weird.csv	특이한 형식의 데이터 테스트
test_load_scores.py	성적 CSV 검증 테스트
bug3_logic.py	find_max 함수
test_bug3_logic.py	find_max 함수 테스트
test_bug_B.py	find_max 함수 추가 테스트

⑥ 만든 사람과 AI 사용

* 만든 사람: YE LWIN
* 사용한 AI 도구: VS Code Copilot Chat
* 모델 이름: 사용한 모델명은 별도 확인 필요
* AI에게 도움받은 부분: pytest 테스트 작성 및 테스트 결과 분석
* 내가 직접 판단·확인한 부분: 테스트 코드 실행, 기대값 확인 및 실패 원인 분석

라이선스

MIT License (LICENSE 파일 참고)
