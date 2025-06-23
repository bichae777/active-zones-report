# Active Zones Report

> “서울시 상권 활성도(상주인구·유동인구·매출)” 퍼센타일 기반 분석 프로젝트

## 📖 프로젝트 개요
- **목적**: 2024년 분기별 데이터를 합산해, 서울시 상권 중 ‘활발한 상권(active zones)’을 퍼센타일(Q3/Q90/Median) 기준으로 선별
- **데이터**:
  - 상주인구 (서울시 상권분석서비스)
  - 길단위 유동인구
  - 추정매출
- **분석 단계**:
  1. 분기 → 연간 집계 (`notebooks/00-aggregate_yearly.ipynb`)
  2. 기본 탐색 (`notebooks/01-explore_data.ipynb`)
  3. 퍼센타일 기반 “활발 상권” 플래그 생성 (`notebooks/02-identify_active_zones.ipynb`)
  4. 결과 시각화 (`notebooks/03-visualize_results.ipynb`)

## 📂 폴더 구조
active-zones-report/
├── data/
│ ├── raw/
│ └── processed/
├── notebooks/
├── src/
├── reports/
└── logs/

bash
복사
편집

## 🚀 시작하기
1. 리포지터리 클론  
   ```bash
   git clone <repo-url>
   cd active-zones-report

의존성 설치
conda env create -f environment.yml
conda activate active-zones
노트북 실행
jupyter lab

👩‍💻 저자
bichae park

곱창집 입지 분석 사이드 프로젝트