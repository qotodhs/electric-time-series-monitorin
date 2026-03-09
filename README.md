# Electric Time Series Monitoring

전력 시계열 데이터를 수집하고, 전처리하고, 시각화하며, 간단한 예측까지 수행하는 연습용 프로젝트입니다.  
현재는 샘플 CSV 데이터를 기반으로 동작하며, 이후 실제 API 연동, 시계열 DB 저장, 대시보드 모니터링으로 확장하는 것을 목표로 합니다.

---

## Overview

이 프로젝트는 전력 사용량 데이터를 다루는 기본 파이프라인을 직접 구현해보는 것을 목표로 합니다.

현재 포함된 기능:
- 샘플 전력 데이터 로딩
- 시계열 데이터 전처리
- 전력 사용량 시각화
- baseline 방식의 단순 예측
- 실제값과 예측값 비교 시각화

향후 확장 예정:
- 실제 전력/Open API 데이터 수집
- PostgreSQL / TimescaleDB 저장
- Grafana 대시보드 연동
- Prometheus 기반 모니터링
- FastAPI 서빙
- Kubernetes 환경 배포

---

## Project Structure

```text
electric-time-series-monitoring/
├─ .gitignore
├─ README.md
├─ requirements.txt
├─ docs/
│  └─ 전력_시계열_모니터링_초안.pdf
├─ data/
│  └─ sample_power.csv
└─ src/
   ├─ ingestion/
   │  └─ sample_loader.py
   ├─ preprocessing/
   │  └─ preprocess.py
   ├─ training/
   │  └─ train.py
   └─ visualization/
      ├─ plot.py
      └─ plot_prediction.py