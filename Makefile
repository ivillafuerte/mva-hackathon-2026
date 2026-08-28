.PHONY: build shell check inspect qc down clean

build:
	docker compose build

shell:
	docker compose run --rm mva bash

check:
	docker compose run --rm mva bash /workspace/scripts/00_check_environment.sh

inspect:
	docker compose run --rm mva bash /workspace/scripts/01_inspect_vcf.sh

qc:
	docker compose run --rm mva bash /workspace/scripts/02_vcf_qc.sh

python:
	docker compose run --rm mva python3 /workspace/pipeline/main.py

down:
	docker compose down

clean:
	rm -rf results/qc/*
	rm -rf results/annotated/*
	rm -rf results/ranked/*
	rm -rf results/private/*
